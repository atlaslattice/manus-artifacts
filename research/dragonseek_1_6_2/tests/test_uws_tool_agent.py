import json,sys,unittest
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from uws_tool_agent import run_agent,UWS_TOOL

class AgentIntegrationTests(unittest.TestCase):
    def test_preview_has_real_tool_schema_but_no_execution(self):
        r=run_agent("Search files",model="gpt-compatible-model",
                    endpoint="http://127.0.0.1:11434/v1/chat/completions",
                    tools=True,execute=False)
        self.assertEqual(r["state"],"PREVIEW_ONLY")
        self.assertEqual(r["tool_definition"]["function"]["name"],"uws_call")
    def test_remote_inference_needs_explicit_optin(self):
        r=run_agent("test",model="model",endpoint="https://example.com/v1/chat/completions",
                    tools=True,execute=True)
        self.assertEqual(r["state"],"DENIED_ENDPOINT")
    def test_real_model_tool_loop_calls_uws_gateway(self):
        messages=[
            {"role":"assistant","content":None,"tool_calls":[
                {"id":"call_1","type":"function","function":{
                    "name":"uws_call","arguments":json.dumps(
                        {"command":["drive","files","list"],"params":{"pageSize":2}})}}]},
            {"role":"assistant","content":"I found two files."}
        ]
        captures=[]
        def model(url,payload,key):
            captures.append(payload.copy())
            return messages.pop(0)
        with patch("uws_tool_agent.run_uws",return_value={
                "state":"EXECUTED","executed":True,"data":{"files":["a","b"]}}) as uws:
            r=run_agent("Find files",model="test",endpoint="http://127.0.0.1:11434/v1/chat/completions",
                        tools=True,execute=True,transport=model)
        self.assertEqual(r["state"],"ANSWER")
        self.assertEqual(r["tool_events"][0]["state"],"EXECUTED")
        self.assertEqual(r["answer"],"I found two files.")
        self.assertEqual(uws.call_count,1)
        self.assertEqual(uws.call_args.kwargs["params"],{"pageSize":2})
        self.assertTrue(uws.call_args.kwargs["execute"])
        self.assertTrue(any(m.get("role")=="tool" for m in captures[-1]["messages"]))
    def test_no_tools_means_no_model_tool_execution(self):
        msg={"role":"assistant","content":None,"tool_calls":[{"id":"x","function":{"name":"uws_call","arguments":"{}"}}]}
        with patch("uws_tool_agent.run_uws") as gateway:
            r=run_agent("test",model="model",endpoint="http://localhost:11434/v1/chat/completions",
                        tools=False,execute=True,transport=lambda *a:msg)
        self.assertEqual(r["state"],"UNEXPECTED_TOOL_REQUEST")
        gateway.assert_not_called()
if __name__=="__main__":unittest.main()
