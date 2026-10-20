#!/usr/bin/env python3
"""Read-only NO FREE READS skill-tree explorer."""
import argparse, json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
def read(file): return json.loads((ROOT/file).read_text(encoding="utf-8"))
def validate(tree,tracks,ledger):
    errors=[]
    nodes=tree["nodes"]; ids=[n["id"] for n in nodes]; known=set(ids)
    if len(ids)!=len(known): errors.append("duplicate skill id")
    if len(nodes)!=26 or len(tree["branches"])!=6: errors.append("unexpected skill or branch count")
    groups={x["id"] for x in tree["branches"]}; graph={}
    for n in nodes:
        graph[n["id"]]=n["requires"]
        if n["branch"] not in groups: errors.append("unknown branch")
        if set(n["requires"])-known: errors.append("unknown prerequisite")
        if n["status"]!="SEED" or n["audio_evidence"]!="NONE": errors.append("unexpected adopted skill")
    active=set(); finished=set()
    def walk(id):
        if id in active: errors.append("cycle at "+id); return
        if id in finished or id not in graph: return
        active.add(id)
        for dep in graph[id]: walk(dep)
        active.remove(id); finished.add(id)
    for id in graph: walk(id)
    if len(tracks)!=12: errors.append("expected twelve tracks")
    if len({t["id"] for t in tracks})!=len(tracks): errors.append("duplicate track")
    for t in tracks:
        if set(t["focus"])-known: errors.append("invalid track focus")
        if t["canon_status"]!="UNAPPROVED" or t["audio_status"]!="UNTESTED": errors.append("unexpected canon/audio promotion")
    byid={e["record_id"]:e for e in ledger}
    if byid["HEARD-001"]["verbatim"]!="What did the other team concede for?": errors.append("changed listener quote")
    if byid["LIT-001"]["verbatim"]!="What the other team can see for.": errors.append("changed draft quote")
    if byid["SCENE-001"]["protected_fragments"]!=["They done handled they biz.","The aura has been farmed."]: errors.append("changed user scene")
    return errors
def main():
    ap=argparse.ArgumentParser(description=__doc__); sp=ap.add_subparsers(dest="cmd",required=True)
    for x in ["branches","tracks","validate"]: sp.add_parser(x)
    for x in ["skill","track"]: sp.add_parser(x).add_argument("id")
    args=ap.parse_args(); tree=read("skills.json"); tracks=read("track-development-matrix.json"); ledger=read("learning-ledger.json")
    issues=validate(tree,tracks,ledger)
    if issues: raise SystemExit("Validation failed: "+"; ".join(issues))
    if args.cmd=="validate": print("PASS: 26 nodes, 6 branches, 12 tracks, DAG, unapproved status and provenance")
    if args.cmd=="branches":
        for b in tree["branches"]: print(b["id"],b["name"],len([x for x in tree["nodes"] if x["branch"]==b["id"]]),b["goal"])
    if args.cmd=="tracks":
        for t in tracks: print(t["id"],t["title"],"focus:",",".join(t["focus"]))
    if args.cmd=="skill":
        n=next((x for x in tree["nodes"] if x["id"]==args.id.upper()),None)
        if not n: raise SystemExit("Unknown skill")
        print(n["id"],n["name"],"tier",n["tier"],"requires",",".join(n["requires"]) or "none")
        print("DRILL:",n["exercise"]); print("PROOF:",n["evidence_test"]); print("STATUS:",n["status"])
    if args.cmd=="track":
        t=next((x for x in tracks if x["id"]==args.id.zfill(2)),None)
        if not t: raise SystemExit("Unknown track")
        print(t["id"],t["title"],"\nSTORY:",t["story_problem"],"\nMUSIC:",t["sonic_test"])
        for code in t["focus"]:
            n=next(x for x in tree["nodes"] if x["id"]==code)
            print("\n",code,n["name"],"\nDRILL:",n["exercise"],"\nPROOF:",n["evidence_test"])
if __name__=="__main__": main()
