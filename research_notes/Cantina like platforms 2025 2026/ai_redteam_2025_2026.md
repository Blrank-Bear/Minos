# AI red-teaming / AI safety / AI security bounty and contest platforms launched 2025–2026

Scope: platforms (not single vendor programs) where individuals earn money by jailbreaking, prompt-injecting or finding vulnerabilities in AI models, agents, MCP servers and AI apps, launched/unveiled in 2025 or 2026. Research date: 2026-10-28. About 36 tool calls. Gray Swan's own arena pages returned HTTP 429, so some Gray Swan figures come from search snippets of those pages and secondary sources.

**Bottom line:** No brand-new, standalone, Cantina-style AI-jailbreak bounty marketplace launched in 2025–2026 turned up in any search. What did happen:
- Existing arenas relaunched or expanded: Gray Swan Arena (Proving Ground, then Arena 2.0 in Oct 2026) and HackAPrompt 2.0 (May 2025).
- Existing gamified red-team games added new modes: Lakera Gandalf: Agent Breaker.
- One-off cash contests ran on existing platforms: Kaggle/OpenAI ($500K), CrowdStrike/AWS ($100K), Alibaba (CN¥300K pool), Singapore AI CTF.
- Lab programs became public or semi-public: the OpenAI Safety Bug Bounty and the OpenAI and Anthropic bio/jailbreak bounties.
- General bug-bounty platforms took on AI scope: HackerOne, Bugcrowd.

## 1. Platforms and arenas launched or relaunched in 2025–2026 (name, URL, launch, format, access, rewards, backers, payouts, red flags)

### Takeaway
Gray Swan Arena is the dominant platform with prize money, with about $370K paid by mid-2025 and a $300K challenge running now. HackAPrompt 2.0 (May 2025) is the only other recurring arena-style platform with a large pool, and its announced pool size is disputed. Everything else is either a one-off contest, a vendor game without cash, or a lab bounty run on HackerOne or Bugcrowd.

### Cited Findings

**Gray Swan Arena (app.grayswan.ai/arena). Original launch Sept 2024; 2025 expansion; "Arena 2.0" relaunch Oct 2026**
- The original Arena launched in September 2024. On Oct 20, 2026 Gray Swan relaunched a redesigned Arena aimed at AI agents, with sandboxes. A human must drive each tested agent, and contestants who ignore an agent that goes off-task are barred. The relaunch adds beginner challenges that run between major competitions, training certificates, and invitations for top performers into its paid red-teaming community — [Fortune](https://fortune.com/2026/10/20/exclusive-ai-security-company-gray-swan-red-team-arena-contest-to-jailbreak-ai-agents/)
- Current flagship: the Indirect Prompt Injection (IPI) "Black" challenge with a $300,000 pool, sponsored by Anthropic, Meta, Google DeepMind and Reflection AI. Fortune says weekly scenarios run through Nov 2; a second outlet says Oct 15 to Nov 5, 2026 — [Fortune](https://fortune.com/2026/10/20/exclusive-ai-security-company-gray-swan-red-team-arena-contest-to-jailbreak-ai-agents/); [The Data Tech Times](https://thedatatechtimes.com/ai-ml/gray-swan-relaunches-arena-300k-prompt-injection-challenge); [Gray Swan on X](https://x.com/GraySwanAI/status/2110746350983737460)
- Community size: about 15,000 (Discord) per Fortune; "more than 15,000 registered participants" per The Data Tech Times — [Fortune](https://fortune.com/2026/10/20/exclusive-ai-security-company-gray-swan-red-team-arena-contest-to-jailbreak-ai-agents/); [Data Tech Times](https://thedatatechtimes.com/ai-ml/gray-swan-relaunches-arena-300k-prompt-injection-challenge)
- 2025 challenges (advertised pools; the arena listings mark them "awarded"):
  - UK AISI Agent Red-Teaming, Mar 8 to Apr 6, 2025: $171,800, sponsored by UK AISI, OpenAI, Anthropic and Google DeepMind. Logged about 1.8M attacks on 22 models and about 62K successful breaks.
  - Visual Vulnerabilities: $60K.
  - Dangerous Reasoning: $20K.
  - Harmful AI Assistant: $40K.
  - Machine-in-the-Middle, Nov 1 to Dec 14, 2025: $100K in cash and prizes from Hack The Box.
  - Sources: [Gray Swan agent-red-teaming page](https://app.grayswan.ai/arena/challenge/agent-red-teaming); [CASRAI guide](https://casrai.org/guides/gray-swan-arena-crowdsourced-red-teaming); [Visual Vulnerabilities](https://app.grayswan.ai/arena/challenge/visual-vulnerabilities); [Dangerous Reasoning blog](https://www.grayswan.ai/blog/gray-swan-introduces-the-dangerous-reasoning-arena-competition); [Machine-in-the-Middle](https://app.grayswan.ai/arena/challenge/machine-in-the-middle)
- "Proving Ground": a weekly recurring Arena track introduced in 2025 (exact month unverified; the page was rate-limited) — [Gray Swan news](https://www.grayswan.ai/news/introducing-the-gray-swan-ai-proving-ground); [Arena blog](https://app.grayswan.ai/arena/blog/proving-ground-your-weekly-arena-for-ai-red-teaming-mastery)
- 2026: IPI Q1 2026 ran Feb 25 to Mar 11, 2026 with a $40,000 pool. Sponsors were UK AISI, OpenAI, Anthropic, Amazon, Meta and Google DeepMind (from the search snippet of the rules page) — [Gray Swan IPI Q1 2026](https://app.grayswan.ai/arena/challenge/indirect-prompt-injection-q1-2026?panel=rules)
- Cumulative payouts: Gray Swan's own June 2025 post claims "over $370K paid out." Another Gray Swan page says "$350K+ distributed" — [Gray Swan search snippet via grayswan.ai](https://www.grayswan.ai/news/introducing-the-gray-swan-ai-proving-ground); [app.grayswan.ai](https://app.grayswan.ai)
- Independent validation: NIST CAISI (Mar 23, 2026) analysed a Gray Swan public agent-hijacking competition: 400+ participants, 250K+ attempts, 13 frontier models, at least one successful attack against every model — [NIST CAISI blog](https://www.nist.gov/blogs/caisi-research-blog/insights-ai-agent-security-large-scale-red-teaming-competition)

**HackAPrompt 2.0 (hackaprompt.com, by Learn Prompting). Launched May 2025**
- Launched May 2025 with OpenAI as sponsor and "$100,000+ in prizes." Tracks: CBRNE ($50K, later raised to $65K and extended to June 19) and "Agents and More" (June, $60K pool). Prize categories included per-jailbreak pools, a fewest-tokens prize and wild cards — [Learn Prompting newsletter (launch)](https://newsletter.learnprompting.org/p/new-hackaprompt-2-0-x-openai-largest-ai-red-teaming-competition-with-100-000-in-prizes-d426); [newsletter (OpenAI)](https://newsletter.learnprompting.org/p/openai-x-learn-prompting-our-100-000-ai-red-teaming-competition-hackaprompt-2-0-7144); [CBRNE $65K update](https://newsletter.learnprompting.org/p/4-new-cbrne-challenges-a-65-000-prize-pool)
- Decrypt (June 3, 2025) reported "$500,000 in prize money" with $50K jackpots for CBRNE. It also reported a Pliny track from June 4 running two weeks, after which top performers could be invited to Pliny's "Strike Team" and data would be open-sourced. Decrypt and Learn Prompting disagree: $500K vs $100K+ — [Decrypt](https://decrypt.co/323351/how-to-trick-chatgpt-and-get-paid-50000/)
- Format: public, season-style multi-track platform — [Decrypt](https://decrypt.co/323351/how-to-trick-chatgpt-and-get-paid-50000/)
- Payouts: no verified final payout total found. AICrowd says results are at paper.hackaprompt.com (not retrieved) — [AICrowd](https://www.aicrowd.com/challenges/hackaprompt-2023)

**Lakera "Gandalf: Agent Breaker" (gandalf.lakera.ai). New agent mode 2025; Gandalf itself dates to 2023**
- A browser game with 10 simulated agent apps (tools, memory, files). It collected 19,433 crowdsourced attacks used in the open-source "b3" benchmark released Oct 27–28, 2025 by Check Point/Lakera with UK AISI. Lakera is now part of Check Point — [press release via FinancialContent](https://markets.financialcontent.com/observerreporter/article/bizwire-2025-10-28-lakera-launches-open-source-security-benchmark-for-llm-backends-in-ai-agents); [KBI.media](https://kbi.media/?p=25560651)
- No cash prizes found. This is a free game and data source, not a paid platform.

**Hack The Box AI Range (hackthebox.com). Launched Dec 3, 2025; Enterprise Edition Oct 6–7, 2026**
- A controlled cyber range that benchmarks autonomous AI security agents side by side with humans. HTB also announced an AI Red Teamer certification for Q1 2026. The Enterprise Edition, released October 2026, is enterprise-facing. It is not a public bounty — [Business Wire](https://www.businesswire.com/news/home/20251203955741/en/Hack-The-Box-Launches-the-World%E2%80%99s-First-AI-Cyber-Range-to-Benchmark-AI-Agents-and-Accelerate-Human-AI-Teaming-Across-Offensive-and-Defensive-Cyber-Operations); [HTB blog](https://www.hackthebox.com/blog/htb-ai-range-launch); [Bernama](https://bernama.com/en/press/news.php?id=2616455)
- HTB's money flows into AI red-teaming mostly through sponsorship: it funded the $100K Gray Swan Machine-in-the-Middle prizes. It also ran an "AI vs Human" CTF in March 2025 with a $7,500 pool — [Machine-in-the-Middle](https://app.grayswan.ai/arena/challenge/machine-in-the-middle); [CTFtime](https://ctftime.org/event/2723)

**RedTeam Arena (redarena.ai, Arena.ai/LMSYS with Pliny/BASI). Launched 2024**
- An open-source community jailbreak game ("Bad Words") with a leaderboard. Its creators explicitly say "not a bug bounty program," and it has no cash — [Arena.ai blog](https://arena.ai/blog/redteam-arena)

**Bugcrowd Red Team as a Service. Launched Apr 28, 2025**
- A crowdsourced red-teaming offering. It is general security, not AI-specific, but it is a 2025 platform-level launch — [Bugcrowd press release](https://www.bugcrowd.com/press-release/bugcrowd-launches-the-industrys-first-crowdsourced-red-team-as-a-service/)

**HackerOne AI Red Teaming (product; date not verified)**
- Vetted pool of 750+ AI security researchers per a 2026 listing; engagements are invite-only — [HackerOne](https://www.hackerone.com/product/ai-red-teaming)
- HackerOne 2025 report: $81M in total payouts, valid AI vulnerability reports up about 210% YoY, prompt-injection reports up 540%, and 1,121 programs with AI in scope (up 270%). AI-vulnerability rewards rose 339%; secondary coverage puts the figure at about $2.1M — [HackerOne report](https://www.hackerone.com/report/hacker-powered-security); [SecurityBrief](https://securitybrief.co.nz/story/ai-vulnerability-reports-surge-as-hackbots-reshape-cyber-risks); [Expert Insights](https://expertinsights.com/news/hackerone-540-rise-in-prompt-injection)

**Crypto-native AI jailbreak games**
- Freysa (Base) was a Nov 2024 one-off, not 2025. The winner extracted about 13.19 ETH (about $47K) after 482 attempts by 195 players. Message fees started at $10 and rose 0.78% per message, with 70% going to the pool — [Cointelegraph](https://cointelegraph.com/news/crypto-user-convinced-ai-bot-transfer-47k); [The Block](https://www.theblock.co/post/328747/human-player-outwits-freysa-ai-agent-in-47000-crypto-challenge)
- JailbreakMe (Solana): a gamified on-chain jailbreak platform with token-linked prize pools. Its launch date and pool sizes are not verified; only aggregator listings and a Medium piece claiming a ">$10M market cap" were found — [MadeOnSol](https://madeonsol.com/compare/jailbreakme-vs-zerebro); [Medium](https://medium.com/@OpenAlpha/jailbreaking-llms-how-crypto-projects-turn-ai-vulnerabilities-into-high-stakes-games-and-what-8c9d427326bf)
- Hacken DevOps AI-Agent CTF (2025): a crypto-auditor-run agent CTF with a 500 USDC winner prize, running until Nov 10, 2025 — [Hacken](https://hacken.io/hacken-news/ai-ctf/)

**Older platforms (one line each)**
- Mozilla 0DIN (0din.ai): GenAI bug bounty launched in 2024. Abstract-first submission with a scope and bounty-range decision within 3 business days. Third parties report $500 to $15K tiers; no 2025 payout totals were found — [0din policy](https://0din.ai/policy); [SecurityWeek](https://www.securityweek.com/mozilla-launches-0din-gen-ai-bug-bounty-program/); [CO/AI](https://getcoai.com/?p=32762)
- huntr (Protect AI, now part of Palo Alto Networks per a deal tracker): OSS AI/ML bounty dating to 2023. A model-file-format bounty pays up to $1,500 for pickle and $3,000 for other formats (beta), with 200+ reports — [huntr](https://huntr.com/bounties/disclose/models); [Hugging Face blog](https://huggingface.co/blog/pai-6-month); [PrivSource](https://www.privsource.com/acquisitions/deal/D8Sg27)
- Lakera Gandalf (2023): free game with 80M+ data points — [press release](https://markets.financialcontent.com/observerreporter/article/bizwire-2025-10-28-lakera-launches-open-source-security-benchmark-for-llm-backends-in-ai-agents)
- Microsoft LLMail-Inject (late 2024 to 2025): $10K pool — [Microsoft](https://microsoft.github.io/llmail-inject/)

### Inferences
- In 2025–26, "Cantina-like for AI" in practice means Gray Swan Arena. It runs recurring public, lab-sponsored prize pools ($20K to $300K per challenge), pays out at scale, and is backed by frontier labs and UK AISI. Arena 2.0 (Oct 2026) is the clearest 2026 "unveiling."
- HackAPrompt 2.0 is the second real 2025 platform-level launch. It should be described as "$100K+ (organizer) / $500K (Decrypt, likely all tracks)," with unverified final payouts.
- Lakera Agent Breaker, HTB AI Range and RedTeam Arena are skill or benchmark platforms without public cash bounties. They are on-ramps, not income sources.

### Gaps
- No verified total for HackAPrompt 2.0 payouts. Proving Ground launch month and prize scale are unverified (pages rate-limited).
- No independent audit of Gray Swan payouts beyond its own claims and CASRAI.
- JailbreakMe launch date, pool sizes and legitimacy are unverified.
- Dreadnode Crucible: no evidence of 2025–26 cash competitions. Haize Labs, Invariant Labs, Lasso, Pillar, Mindgard, Repello and Promptfoo turned up only as vendor tools or blogs; none was found running a public paid bounty platform.
- "BT6" (Pliny-associated group): no sources found.

## 2. One-off cash contests and lab programs, 2025–2026 (listed briefly; these are programs, not platforms)

### Takeaway
The largest 2025–26 money came from one-off contests: OpenAI's $500K Kaggle gpt-oss challenge, CrowdStrike/AWS's $100K Agents of Chaos and Alibaba's CN¥300K challenge. Lab bounties (OpenAI and Anthropic bio/jailbreak) are mostly invite-only and under NDA.

### Cited Findings
- **OpenAI gpt-oss-20b Red-Teaming Challenge (Kaggle):** launched Aug 5, 2025 with a $500K pool. Holistic AI/UCL say they were a Top-10 team from 600+ submissions and received $50K (self-reported). The challenge ended with a workshop — [Infosecurity Magazine](https://www.infosecurity-magazine.com/news/openai-launches-red-teaming/); [Kaggle](https://www.kaggle.com/competitions/openai-gpt-oss-20b-red-teaming); [TechDogs/Holistic AI](https://www.techdogs.com/tech-news/access-newswire/holistic-ai-named-top-10-winner-in-openais-gpt-oss-20b-red-teaming-hackathon); [ndurner](https://ndurner.substack.com/p/kaggle-red-teaming-challenge-openai-gpt-oss-concluded)
- **CrowdStrike "AI Unlocked: Agents of Chaos":** announced Aug 5, 2026 with AWS. A public virtual prompt-injection game against agents running Aug 31 to Sep 29, 2026. Prizes totalled $100K: Act 1 $10K, Act 2 $20K, Act 3 $70K — [CrowdStrike press release](https://www.crowdstrike.com/en-us/press-releases/crowdstrike-announces-international-ai-security-challenge/); [CrowdStrike blog](https://www.crowdstrike.com/en-us/blog/agents-of-chaos-immersive-ai-security-challenge/)
- **OpenAI Safety Bug Bounty:** launched Mar 25, 2026 as a public program covering abuse and safety risks, including agentic vulnerabilities, prompt injection and data exfiltration. A secondary source says it runs on Bugcrowd with MCP in scope — [OpenAI](https://openai.com/index/safety-bug-bounty/); [Practical DevSecOps](https://www.practical-devsecops.com/mcp-security-statistics-2026-report/)
- **OpenAI bio bounties:**
  - ChatGPT Agent bio bounty (Jul 2025) and GPT-5 bio bounty (Sep 2025): $25K and $10K tiers; apply, invite and NDA required.
  - GPT-5.5 bio bounty (Apr 23, 2026): $25K top prize.
  - Raised to $50K and extended to GPT-5.6 (Jul 2026).
  - Sources: [OpenAI GPT-5 bio bounty](https://openai.com/zh-Hans-CN/gpt-5-bio-bug-bounty/); [OpenAI smapply](https://openai.smapply.org/prog/gpt-5-5-safety-bio-bounty-program/); [TechRepublic](https://www.techrepublic.com/article/news-openai-bio-bounty-jailbreak/)
- **Anthropic Model Safety Bug Bounty (HackerOne):** began in Aug 2024, invite-only, up to $15K. It was expanded later and requires an NDA. A May 10–18, 2026 round was invite-only.
  - Conflicting claims: one jobs guide says it is "open, no NDA, up to $35K," and a secondary stats page says it went public in May 2026. Anthropic's support page still requires an NDA.
  - Sources: [Anthropic](https://www.anthropic.com/news/model-safety-bug-bounty); [Anthropic support](https://support.claude.com/en/articles/12119250-model-safety-bug-bounty-program); [HackerOne](https://www.hackerone.com/blog/anthropic-expands-their-model-safety-bug-bounty-program); [threatcluster](https://threatcluster.io/cluster/anthropic-launches-bug-bounty-for-ai-safety-defenses-2de609cc); contradicted by [aitraining.jobs](https://aitraining.jobs/roles/red-teaming)
- **Alibaba × Alibaba Cloud first AI Security Global Challenge (2025, China):** CN¥300K total pool. The preliminary round is attack (eliciting harmful output) and the final round is defence, with a CN¥260K final pool. Low confidence: this comes from a Chinese search summary and the source page was not fetched — [ITHome](https://www.ithome.com/0/986/234.htm); [secrss](https://www.secrss.com/articles/54509)
- **CCF large-model security challenge (2024, China):** CN¥300K, with goal-hijacking and red-teaming tracks (older) — [BAAI hub](https://hub.baai.ac.cn/view/40441)
- **Singapore AI CTF 2025 (GovTech/CSA):** Oct 11–21, 2025. SGD 19K pool; the Open category paid 10K, 6K and 3K — [Snyk roundup](https://snyk.io/articles/usd800k-up-for-grabs-12-ai-hacking-competitions-that-could-launch-your/)
- **Global AI Red Team Challenge at MWC 2025 (SelectStar × GSMA, Korea-led):** Mar 5, 2025, about 80 to 100 challengers; no prize info found — [LG U+](https://www.lguplus.com/biz/insight/trend/858)
- **Other 2025 AI CTFs:**
  - PHDays AI CTF, May 2025: mostly merchandise prizes.
  - CSAW Agentic Automated CTF 2025: autonomous agents only.
  - Neurogrid CTF: $50K, reportedly won by an AI agent (CAI).
  - Sources: [CTFtime](https://ctftime.org/event/2778); [CSAW](https://csaw.io/node/58); [arXiv CAI](https://arxiv.org/abs/2512.02654v1)
- **Snyk's Sept 30, 2025 roundup** of "12 AI hacking competitions, $800K+" mostly lists events, not platforms; the OpenAI Kaggle contest is the bulk of the total — [Snyk](https://snyk.io/articles/usd800k-up-for-grabs-12-ai-hacking-competitions-that-could-launch-your/)

### Inferences
- Money in this space is concentrated in lab-funded pools routed through Gray Swan, Kaggle or HackerOne/Bugcrowd. No independent "jailbreak marketplace" with its own budget surfaced.
- A real 2026 shift: OpenAI's public Safety Bug Bounty (Mar 2026) makes prompt-injection and agent-safety findings payable outside contests.

### Gaps
- No dedicated MCP-security bounty platform found. MCP appears only as scope in the OpenAI and Anthropic programs (per a secondary source).
- No Korean or Japanese crowdsourced paid platforms found. Chinese coverage is limited to contests (Alibaba, CCF), not standing platforms.
- Kaggle gpt-oss final prize distribution is not fully verified.

## 3. Red flags and verification status

### Takeaway
Most prize figures are organizer-advertised. Independent verification exists for Gray Swan (NIST CAISI, CASRAI, UK AISI co-sponsorship) and partly for Kaggle/OpenAI. The highest-risk category is token-linked crypto jailbreak games.

### Cited Findings
- HackAPrompt 2.0 pool discrepancy: $100K+ (organizer) vs $500K (Decrypt) — [Learn Prompting](https://newsletter.learnprompting.org/p/new-hackaprompt-2-0-x-openai-largest-ai-red-teaming-competition-with-100-000-in-prizes-d426); [Decrypt](https://decrypt.co/323351/how-to-trick-chatgpt-and-get-paid-50000/)
- Gray Swan payouts are self-reported ($350K to $370K+ by mid-2025). CASRAI independently describes $171,800 paid for the UK AISI agent challenge — [CASRAI](https://casrai.org/guides/gray-swan-arena-crowdsourced-red-teaming)
- Gray Swan Arena 2.0 rules: a contestant who ignores an agent going off-task is banned from current and future competitions. Compliance risk for participants — [Fortune](https://fortune.com/2026/10/20/exclusive-ai-security-company-gray-swan-red-team-arena-contest-to-jailbreak-ai-agents/)
- Crypto games: Freysa used escalating pay-to-message fees, with 70% going to the pool. JailbreakMe is token-linked, and only aggregator and Medium sources were found — [Cointelegraph](https://cointelegraph.com/news/crypto-user-convinced-ai-bot-transfer-47k); [Medium](https://medium.com/@OpenAlpha/jailbreaking-llms-how-crypto-projects-turn-ai-vulnerabilities-into-high-stakes-games-and-what-8c9d427326bf)
- The lab bio bounties are invite-only and NDA-bound, so payouts cannot be publicly verified — [OpenAI GPT-5 bio bounty](https://openai.com/zh-Hans-CN/gpt-5-bio-bug-bounty/); [Anthropic support](https://support.claude.com/en/articles/12119250-model-safety-bug-bounty-program)
- Dark-web "jailbreak-as-a-service" tools sell for $50 to $200 a month. This is not a legitimate platform; avoid confusing it with bounty platforms — [Group-IB](https://www.group-ib.com/resources/knowledge-hub/jailbreak-detection/)

### Inferences
- For someone seeking Cantina-style income, the safest and most verifiable venues in 2026 are:
  1. Gray Swan Arena (live $300K IPI Black).
  2. The OpenAI Safety Bug Bounty (public).
  3. Periodic contests (CrowdStrike, Kaggle, HackAPrompt seasons).
  4. Invite-only lab bounties after building a track record.

### Gaps
- No verified payout records for HackAPrompt 2.0, JailbreakMe, the Alibaba challenge or CrowdStrike Agents of Chaos (which ended Sep 29, 2026; no winners announcement found).
