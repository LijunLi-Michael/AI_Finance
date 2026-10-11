# Farcaster — speak in public (the "speak" verb)

The agent gets a voice: it posts, in public, what it did today — behind a human gate. Trading in silence is a script; reporting its own work in the open is an actor you can watch.

## Setup

Copy `.env.example` to `.env` and fill `NEYNAR_API_KEY` and `SIGNER_UUID` (a signer you approved for **your own** Farcaster account, from neynar.com). Keys stay in `.env`, which is gitignored.

    pip install requests python-dotenv

## Post

Write your draft to a text file, then:

    python cast.py example-post.txt          # preview only — nothing leaves the machine
    python cast.py example-post.txt --yes     # actually posts

Every post waits for `--yes`. Share the strategy and the result — **never a wallet address or a key**. The signer is never written to the log.
