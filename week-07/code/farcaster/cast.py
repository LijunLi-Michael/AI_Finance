"""Post a cast — the agent's 'speak' verb.
Preview only by default; add --yes to actually send. Every post waits for a human.

    python cast.py post.txt [--reply-to <hash>] [--channel <id>] [--yes]

Share the strategy and the result — never a wallet address or a key.
"""
import sys, json, datetime
from common import env, call

text = open(sys.argv[1]).read().strip()
arg = lambda k: sys.argv[sys.argv.index(k) + 1] if k in sys.argv else None

body = {"signer_uuid": env("SIGNER_UUID"), "text": text}
if arg("--reply-to"):
    body["parent"] = arg("--reply-to")
if arg("--channel"):
    body["channel_id"] = arg("--channel")

meta = {k: v for k, v in body.items() if k not in ("text", "signer_uuid")}
print(f"--- preview ({len(text.encode())} bytes) ---\n{text}\n---", meta)

if "--yes" not in sys.argv:
    sys.exit("(preview only — nothing sent. Add --yes to post.)")

r = call("POST", "/cast", json=body)
h = (r.get("cast") or {}).get("hash", "")
print("posted:", h[:10])
with open("actions.log", "a") as f:
    f.write(json.dumps({
        "t": datetime.datetime.now().isoformat(), "op": "cast",
        "body": {k: v for k, v in body.items() if k != "signer_uuid"},  # never log the signer
    }) + "\n")
