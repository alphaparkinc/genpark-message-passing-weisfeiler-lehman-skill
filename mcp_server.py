import sys
import json
from client import WeisfeilerLehmanGraph

def handle_call(name, arguments):
    if name == "refine":
        adj = {int(k): v for k, v in arguments["adj"].items()}
        wl = WeisfeilerLehmanGraph(adj)
        return {"colors": wl.iterate()}
    return {"error": f"Unknown tool: {name}"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_call(req.get("name"), req.get("arguments", {}))
            print(json.dumps({"id": req.get("id"), "result": res}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()

if __name__ == "__main__":
    main()
