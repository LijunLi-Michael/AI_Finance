# OpenClaw · The Agent That Never Sleeps

Required Pre-Reading for Our Next Class · MB/CSE 599 AI Finance

**A program that keeps working after you close the laptop**

Every AI tool you have used so far waits for you. You type, it answers, it stops. OpenClaw breaks that deal. You install it on your own machine, and it keeps running: it wakes itself up on a timer, reads your messages, runs commands, and texts you on Telegram when it thinks something needs your attention. In ten months it went from one developer's weekend project to one of the most-starred repositories on GitHub — and in September 2026 Meta shipped a product that openly copies it.

This reading tells that story — no verdicts, no lectures. It opens each door and hands you the entry point. You go in and dig yourself.

**How to use it:** read each section's story first (a minute or two). If it grabs you, open the Further reading links. Each section ends with a question worth chasing. The Resource Library at the end is for when you want to go deep.

**One throughline:** a chatbot has a human in the loop by definition — you are the one who hits Enter. An always-on agent does not. The moment software can act while you are asleep, one question stops having an easy answer: who approves what it does? Keep that question in your pocket for the whole reading. Next class, we deploy one and give it a wallet.

**Start with these three**

- [★ TechCrunch — OpenClaw's creator joins OpenAI (Feb 2026)](https://techcrunch.com/2026/02/15/openclaw-creator-peter-steinberger-joins-openai/)

- [★ The Hacker News — 341 malicious skills found on ClawHub (Feb 2026)](https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html)

- [★ TechCrunch — Meta admits Muse's likeness to OpenClaw isn't a coincidence (Sep 2026)](https://techcrunch.com/2026/09/22/meta-admits-muses-likeness-to-openclaw-isnt-a-coincidence/)

*The founder, the fall, the copy — about twenty minutes in that order.*

**I. A weekend project, renamed four times**

**Five names in ten weeks.** The GitHub repository was created on November 24, 2025, under the name Warelay. It became CLAWDIS in December and Clawdbot in January — a lobster-claw pun on "Claude." Anthropic raised a trademark concern ("Clawd" sounds a lot like "Claude"), so on January 27, 2026 it became Moltbot, after the way a lobster sheds its shell. Three days later it was renamed again, to OpenClaw: its creator admitted Moltbot "never quite rolled off the tongue." During one of the switches, scammers reportedly grabbed the abandoned social handles within seconds.

**Why the names matter.** Nobody plans a hit. The project was built fast and in public, and the branding caught up afterward. That speed is the story of the whole project: features shipped in days, a new release every few days even today (version numbers are dates — the one we install is v2026.9.6).

**🔍 Worth digging into:** what does it cost a project to rename itself four times while it is going viral — in trust, in search results, in security?

**Further reading:**

- [Wikipedia · OpenClaw (full timeline)](https://en.wikipedia.org/wiki/OpenClaw)

- [Laravel News · Clawdbot renamed after Anthropic's request](https://laravel-news.com/clawdbot-rebrands-to-moltbot-after-trademark-request-from-anthropic)

- [Forbes · the viral sidekick that shed its old skin](https://www.forbes.com/sites/ronschmelzer/2026/01/27/viral-ai-sidekick-clawdbot-changes-name-to-moltbot-and-sheds-its-old-skin/)

**II. The founder — from PDF software to OpenAI**

**Peter Steinberger.** An Austrian developer who, while still a student in Vienna, built PSPDFKit — a toolkit for showing and editing PDFs that ended up inside many well-known apps. In 2021 his company took a strategic investment of more than €100 million from Insight Partners, and he stepped back. After a break, he came back to programming through AI coding assistants — and OpenClaw started as a "playground project" on the side.

**Then the big labs came calling.** In February 2026 Sam Altman announced that Steinberger was joining OpenAI "to drive the next generation of personal agents" (reports say he turned Meta down first). OpenClaw did not go with him: it moved into an independent non-profit, the OpenClaw Foundation, with OpenAI as a sponsor. Open the repository's LICENSE file today and the copyright line names the Foundation.

**🔍 Worth digging into:** one experienced developer plus AI coding tools produced one of the fastest-growing projects in GitHub history. What does that say about how software will be built — and who captures the value?

**Further reading:**

- [Wikipedia · Peter Steinberger](https://en.wikipedia.org/wiki/Peter_Steinberger_(programmer))

- [Insight Partners · the PSPDFKit investment (2021)](https://www.insightpartners.com/ideas/pspdfkit-announces-e100-million-strategic-investment-from-insight-partners-to-fuel-growth/)

- [Steinberger's own post on the Foundation](https://steipete.me/posts/2026/openclaw)

**III. Going viral — agents with their own social network**

**Moltbook.** In late January 2026 someone launched a social network where the users were OpenClaw agents — posting, replying and arguing with each other while their owners watched. The press ran headlines about agents "building their own social network." Within days, the site's database was found exposed, and humans were caught sneaking in to pose as agents.

**The numbers.** As of September 25, 2026 the GitHub repository shows about 390,000 stars and 82,000 forks (it had about 247,000 stars in March), with thousands of contributors. You will also see claims like "3.2 million monthly users" or "50,000 skills" — those come from aggregator blogs, not from the project. A number with no primary source is a rumor with a decimal point.

**🔍 Worth digging into:** stars measure attention, not usage. If you were an investor, what number would you actually want — and where would you get it?

**Further reading:**

- [GitHub · openclaw/openclaw (check the live numbers yourself)](https://github.com/openclaw/openclaw)

- [Wikipedia · Moltbook and the viral period (with press citations)](https://en.wikipedia.org/wiki/OpenClaw)

**IV. What it actually is — a chatbot that got a heartbeat**

Strip away the hype and OpenClaw is five parts. You will meet every one of them in the lab:

**The Gateway.** One program that runs in the background 24/7 on your machine. Everything — the web dashboard, your phone, Telegram — talks to it. By default it only listens to the machine itself; to reach it from your laptop you tunnel in.

**The personality files.** Plain-text files the agent reads every time it starts: SOUL.md (character and principles), IDENTITY.md (name and role), USER.md (who you are), MEMORY.md (what it has learned). Edit a text file, change the agent.

**Skills.** A folder with a SKILL.md: a written manual telling the agent when and how to use a tool. Anyone can publish skills on a marketplace called ClawHub — remember that for section V.

**The heartbeat.** A timer that wakes the agent with nobody asking — every 30 minutes by default, plus any scheduled jobs you add. This is the line between a chatbot and an agent.

**Memory.** Daily notes, plus a nightly "dreaming" job that promotes the things it keeps coming back to into long-term memory. Yes, it really is called dreaming.

**🔍 Worth digging into:** the heartbeat turns a tool you use into something that acts on its own schedule. In a trading context, what should run on the heartbeat, and what should never wait for an LLM to wake up?

**Further reading:**

- [OpenClaw docs · architecture](https://docs.openclaw.ai/concepts/architecture)

- [OpenClaw docs · skills](https://docs.openclaw.ai/tools/skills)

- [OpenClaw docs · heartbeat](https://docs.openclaw.ai/gateway/heartbeat)

**V. When nobody is watching — the incidents**

**ClawHavoc — poisoning the skill store (February 2026).** Security firm Koi audited 2,857 skills on ClawHub and found 341 malicious ones. Most were dressed up as exactly what a crypto user wants: wallet tools, Polymarket bots, trading helpers. Installed, they dropped a macOS password-and-wallet stealer. The project's fix: let users report skills, and auto-hide any skill reported by more than three people.

**The skill that read your data (January 2026).** Cisco researchers found a third-party skill quietly exfiltrating data and injecting instructions into the agent — prompt injection delivered as a plugin.

**The dating profile nobody asked for.** In one widely reported case, an agent created a dating profile for its owner without being explicitly told to. It was trying to be helpful.

**"Secure by default?" (August 2026).** When OpenClaw 2.0 shipped, The Register pointed out that stored secrets were not encrypted at rest and that the sandbox — the thing that stops commands from touching your real machine — was off by default.

Put these together and a pattern appears. An agent's personality file might say "I always ask before moving money." That is a promise, and a clever enough message can talk a model out of a promise. What actually protects you is either code the model cannot change (spending caps, allow-lists, approval rules) or a hard physical limit (the wallet only holds what you can afford to lose).

**🔍 Worth digging into:** why were the malicious skills disguised as crypto tools specifically? And if your agent can read your email, what one-line email would an attacker send it?

**Further reading:**

- [The Hacker News · 341 malicious ClawHub skills](https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html)

- [Cybersecurity News · how ClawHavoc grew](https://cybersecuritynews.com/clawhavoc-poisoned-openclaws-clawhub/)

- [OpenClaw docs · exec approvals (the code-level guard)](https://docs.openclaw.ai/tools/exec-approvals)

**VI. The copy — Meta Muse**

**A turnkey OpenClaw for the masses (September 2026).** On September 8, Meta launched Muse: a personal agent that answers email, books travel and buys things for you — no servers, no config files, one-minute setup. Meta reported more than half a million users in the first week. Two weeks later, asked why Muse even ships a SOUL.md nearly identical to OpenClaw's, Meta's Nat Friedman said Muse was "definitely heavily inspired as a product by OpenClaw" and that its creator "got those things exactly right." Friedman had bought hundreds of Mac minis so his team could run OpenClaw back in January.

**Hosted vs. self-hosted.** Muse runs on Meta's cloud, Meta writes the rules, and payments go through Stripe Link. OpenClaw runs on your machine and you write the rules — which is both the freedom and the problem. Elsewhere, Tencent and Z.ai launched services built on OpenClaw, while China restricted its use in state agencies and banks.

**🔍 Worth digging into:** which one would you give a private key to — and under what rules? Bring your answer to class.

**Further reading:**

- [TechCrunch · Meta admits Muse's likeness to OpenClaw](https://techcrunch.com/2026/09/22/meta-admits-muses-likeness-to-openclaw-isnt-a-coincidence/)

- [The Next Web · Muse, OpenClaw and SOUL.md](https://thenextweb.com/news/meta-muse-openclaw-friedman-soul-md)

**VII. Try it yourself (optional, before class)**

You need a machine you control (Mac, Linux, or Windows with WSL2), Node.js 24.16 or newer, and a model account. Installing is one line — the official installer — then a guided setup:

curl -fsSL https://openclaw.ai/install.sh \| bash

openclaw onboard --install-daemon

**Who pays for the thinking.** Signing in with a ChatGPT subscription uses that plan's quota (no extra bill, but there is a 5-hour window and a weekly cap — an agent that writes its own code can burn through the window in an afternoon). An API key is billed per token, separately.

**Do not connect your real email, real wallet or real accounts.** Use a throwaway setup. That is not paranoia — it is section V.

**Further reading:**

- [OpenClaw docs · getting started](https://docs.openclaw.ai/start/getting-started)

**Resource Library — go dig on your own**

**🎓 Getting started**

- [OpenClaw docs — install and first run](https://docs.openclaw.ai/install)

- [GitHub — openclaw/openclaw (code, releases, issues)](https://github.com/openclaw/openclaw)

- [Wikipedia — OpenClaw (timeline with citations)](https://en.wikipedia.org/wiki/OpenClaw)

**🧠 How it works**

- [Architecture — Gateway, clients, nodes](https://docs.openclaw.ai/concepts/architecture)

- [Skills — the SKILL.md format](https://docs.openclaw.ai/tools/skills)

- [Heartbeat — how the agent wakes itself](https://docs.openclaw.ai/gateway/heartbeat)

- [OAuth — using a ChatGPT subscription as the model](https://docs.openclaw.ai/concepts/oauth)

**🛡️ Security**

- [Exec approvals — the code-level approval policy](https://docs.openclaw.ai/tools/exec-approvals)

- [The Hacker News — ClawHavoc](https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html)

**💸 Agents that pay (crypto)**

- [AWS — OpenClaw agents that transact with Bedrock AgentCore payments](https://aws.amazon.com/blogs/machine-learning/build-openclaw-agents-that-transact-with-amazon-bedrock-agentcore-payments/)

*Community wallet and x402 payment skills exist on ClawHub and GitHub. They are not part of OpenClaw itself — read the code before you install one (see section V).*

**Three things to take away**

1.  **A heartbeat changes everything.** Once software acts on its own schedule, "a human approves each step" is no longer true by default.

2.  **A promise is not a guard.** Rules written in a personality file can be talked around; caps in code and limits in the wallet cannot.

3.  **The plugin store is the attack surface.** The fastest way into an agent is a skill it trusts — and attackers dress malware as the tools you most want.

**Before class**

This is required reading before our next class. Sections I–VI take about 30 minutes; section VII and the Further reading links are optional. Come ready to answer the question at the end of section VI: which agent would you give a private key to, and under what rules? In class we deploy one together and give it a testnet wallet.

*Snapshot: facts and numbers as of September 25, 2026. OpenClaw changes weekly — check the live sources.*
