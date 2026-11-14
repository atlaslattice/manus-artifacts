"""Offline response scorer; no generated outputs or agent gains are fabricated."""
import argparse, json, math
from pathlib import Path

def grade(response, key):
    if not isinstance(response, dict):
        raise ValueError("response must be an object")
    answers=response.get("answers", {})
    if not isinstance(answers,dict):
        raise ValueError("answers must be an object")
    items=[]
    for case, fields in key.items():
        actual=answers.get(case,{})
        if not isinstance(actual,dict): actual={}
        for field, expected in fields.items():
            value=actual.get(field)
            if isinstance(expected,bool):
                correct=type(value) is bool and value is expected
            elif isinstance(expected,(float,int)):
                correct=(type(value) in (float,int) and math.isfinite(value)
                         and math.isclose(value,expected,rel_tol=0.001,abs_tol=0.001))
            else: correct=type(value) is str and value==expected
            items.append({"case":case,"field":field,"correct":correct,
                          "missing":field not in actual})
    return {"status":"SCORED_SUBMITTED_RESPONSE","items":items,
            "correct_fields":sum(i["correct"] for i in items),"total_fields":len(items),
            "field_accuracy":sum(i["correct"] for i in items)/len(items),
            "complete_cases":sum(all(i["correct"] for i in items if i["case"]==c) for c in key),
            "total_cases":len(key),
            "limitations":["deterministic supplied-record accuracy only",
                           "not creativity, biological REM or population efficacy",
                           "single output score does not establish a treatment effect"]}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("response");parser.add_argument("--key",required=True)
    args=parser.parse_args()
    print(json.dumps(grade(json.loads(Path(args.response).read_text()),
                           json.loads(Path(args.key).read_text())),indent=2))
if __name__=="__main__": main()
