"""RES07/RES09/RES10 synthetic hourly service and microgrid prototype. No live actuation."""
from dataclasses import dataclass, field

@dataclass
class Service:
    name:str
    kw:float
    priority:int=0
    requires:list=field(default_factory=list)
    minimum:float=0.5

@dataclass
class Resource:
    name:str
    kwh:float
    max_kw:float
    solar_kw:float=0
    soc:float=0
    down:set=field(default_factory=set)
    eta_in:float=0.95
    eta_out:float=0.95

def strongly_connected(services):
    graph={s.name:s.requires for s in services}
    for v, deps in graph.items():
        for d in deps:
            if d not in graph: raise ValueError(f"unknown dependency {d} of {v}")
    idx={}; low={}; stack=[]; on=set(); output=[]
    def visit(v):
        idx[v]=low[v]=len(idx); stack.append(v); on.add(v)
        for w in graph[v]:
            if w not in idx:
                visit(w);low[v]=min(low[v],low[w])
            elif w in on: low[v]=min(low[v],idx[w])
        if low[v]==idx[v]:
            group=[]
            while True:
                w=stack.pop();on.remove(w);group.append(w)
                if w==v: break
            output.append(sorted(group))
    for v in graph:
        if v not in idx: visit(v)
    return [c for c in output if len(c)>1 or c[0] in graph[c[0]]]

def simulate(name,services,resources,sun,hours=168,down_services=None):
    """Read-only demo: no AC power flow, intertie isolation or restart scheduler.
    Any cyclic SCC without an externally modeled restart seed cannot start.
    """
    if len(sun)<hours:raise ValueError("insufficient solar profile")
    names={s.name for s in services}
    if len(names)!=len(services):raise ValueError("duplicate services")
    cycles=strongly_connected(services)
    graph={s.name:s for s in services}
    for s in services:
        if s.kw<0 or not 0<=s.minimum<=1:raise ValueError("invalid service")
    for r in resources:
        if min(r.kwh,r.max_kw,r.solar_kw,r.soc)<0 or r.soc>r.kwh:raise ValueError("invalid resource")
    down_services=down_services or {}
    full={s.name:0 for s in services};minimum={s.name:0 for s in services};trace=[]
    for t in range(hours):
        active=[r for r in resources if t not in r.down]
        pv=sum(r.solar_kw*max(0,min(1,sun[t])) for r in active)
        available=pv+sum(min(r.max_kw,r.soc*r.eta_out) for r in active)
        fractions={s.name:0 for s in services};allocation={}
        for s in sorted(services,key=lambda s:(s.priority,s.name)):
            if t in down_services.get(s.name,set()):continue
            if any(fractions[d]<graph[d].minimum for d in s.requires):continue
            # Capacity gate: no partial below viable threshold.
            grant=min(s.kw,available)
            if s.kw and grant/s.kw+1e-9<s.minimum:continue
            allocation[s.name]=grant;fractions[s.name]=grant/s.kw if s.kw else 1
            available-=grant
        served=sum(allocation.values());draw=max(0,served-pv);rest=draw
        for r in active:
            g=min(rest,r.max_kw,r.soc*r.eta_out)
            r.soc-=g/r.eta_out;rest-=g
        if rest>1e-6:raise AssertionError("battery conservation violation")
        surplus=max(0,pv-served)
        for r in active:
            charge=min(surplus,r.max_kw,(r.kwh-r.soc)/r.eta_in)
            r.soc+=charge*r.eta_in;surplus-=charge
        for s in services:
            full[s.name]+=int(fractions[s.name]>=1-1e-9)
            minimum[s.name]+=int(fractions[s.name]+1e-9>=s.minimum)
        trace.append({"hour":t,"served_kw":round(served,3),"soc_kwh":round(sum(r.soc for r in resources),3),
                      "solar_kw":round(pv,3),"service_fraction":{k:round(v,3) for k,v in fractions.items()}})
    return {"case":name,"hours":hours,"cyclic_components":cycles,"minimum_service_hours":minimum,
            "full_service_hours":full,"served_kwh":round(sum(x["served_kw"] for x in trace),3),
            "final_soc_kwh":round(sum(r.soc for r in resources),3),
            "status":"SYNTHETIC_NONCANON","trace":trace}

def example_case(case,hours=168):
    services=[Service("comms",2,0),Service("refrigeration",3,1,["comms"]),Service("water",5,2,["comms"])]
    sun=[0.65 if 7<=i%24<=17 else 0 for i in range(hours)]
    if case=="baseline":
        resources=[Resource("legacy",120,10,0,120,set(range(12,hours)))]
    elif case=="distributed":
        resources=[Resource("A",180,6,8,160),Resource("B",180,6,8,160)]
    elif case=="networked":
        resources=[Resource("A",180,6,8,160),Resource("B",180,6,8,160),Resource("regional",240,10,10,220)]
    elif case=="degraded":
        resources=[Resource("A",180,6,8,160,set(range(36,120))),Resource("B",180,6,8,160),
                   Resource("regional",240,10,10,220,set(range(36,96)))]
    else:raise ValueError(case)
    return simulate(case,services,resources,sun,hours)

if __name__=="__main__":
    import json
    for case in ("baseline","distributed","networked","degraded"):
        r=example_case(case)
        print(json.dumps({k:v for k,v in r.items() if k!="trace"},sort_keys=True))
