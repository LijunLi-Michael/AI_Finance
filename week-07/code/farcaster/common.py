"""Tiny Neynar helper for the Farcaster demos.
Reads NEYNAR_API_KEY and SIGNER_UUID from a .env in this folder (gitignored)."""
import os, sys, requests
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
API = "https://api.neynar.com/v2/farcaster"


def env(k):
    v = os.getenv(k)
    if not v:
        sys.exit(f"Missing {k} — set it in .env (see .env.example)")
    return v


def call(method, path, **kw):
    r = requests.request(
        method, API + path,
        headers={"x-api-key": env("NEYNAR_API_KEY"), "content-type": "application/json"},
        timeout=30, **kw,
    )
    if r.status_code >= 400:
        sys.exit(f"{r.status_code} {r.text[:500]}")
    return r.json()
