# AI-agent task networks and coding/open-source bounty platforms new in 2026

Research date: 2026-10-28. About 18 tool calls. Coverage is broad but shallow: for most items the only sources are press releases or the project's own pages. Each item is marked **[VERIFIED-ish]** (independent or primary evidence), **[PR-ONLY]** (only press releases or self-reported numbers) or **[OLDER]** (platform started before 2026).

## Q1: AI-agent task networks, agent marketplaces and agent competitions new in 2026

### Takeaway
2026 brought a lot of "agents earn money" platforms. Three have some substance beyond their own claims: Bounty (trybounty.ai), backed by a16z; Execution Market, an x402/USDC marketplace where agents post tasks for humans, shown as an ETHGlobal 2026 showcase project; and Agentic.market, a Coinbase x402 service marketplace (not a bounty board). The three leads named in the brief are weaker. AgentOn and Bot Games are known only from press releases. agentbounty.org shows implausible self-reported numbers and names no operator, so treat it as low-credibility.

### Cited Findings

**AgentOn (agenton.me) [PR-ONLY]**
- GlobeNewswire release datelined Hong Kong, June 8, 2026. Describes itself as an "AI-native task network" for the AI agent economy. Launched with a $100,000 bounty campaign from June 8 to July 8, 2026 with "more than 30" participating projects. Users can do tasks by hand or have their own AI agents do them. Task types are user growth, content creation, data research and marketing, which suggests crypto-style quest/campaign work rather than technical tasks. Campaign organizers publish tasks and distribute rewards on the platform. — [TechDogs/GlobeNewswire repost](https://www.techdogs.com/tech-news/globe-newswire/agenton-officially-launches-kicking-off-a-100000-bounty-campaign-for-ai-agents-and-users)
- The release names no backers or incubator. The media contact is bd@me.news, so the domain hints at a link to ME / ME Group, but the release does not confirm one. — [TechDogs](https://www.techdogs.com/tech-news/globe-newswire/agenton-officially-launches-kicking-off-a-100000-bounty-campaign-for-ai-agents-and-users)
- A ".agent community" profile page for "ME Group" turned up in search alongside AgentOn. I did not fetch it, so the claim that ME Group incubated AgentOn is unverified. — [agentcommunity.org/m/me-group](https://agentcommunity.org/m/me-group)
- The release mentions no token. I found no independent coverage of traction or payouts. X handle: @AgentON_. — [search summary / TechDogs](https://www.techdogs.com/tech-news/globe-newswire/agenton-officially-launches-kicking-off-a-100000-bounty-campaign-for-ai-agents-and-users)

**Bot Games (botgames.io) [PR-ONLY]**
- PR.com release dated Feb 8, 2026. The organizer is AI Implemented of Palm Bay, FL; Christopher Thomas is quoted as founder. Prizes: 1st 1 BTC, 2nd 1 ETH, 3rd Mac Mini M4. Open-source models only (Llama, Mistral and others); commercial APIs such as GPT-4, Claude and Gemini are banned. Head-to-head real-time challenges in reasoning, coding, creativity and problem-solving, run in isolated sandboxes, with no pre-computation and no human intervention. First round was set for March 1, 2026. Entry fee is not stated, and the release offers no proof that the prize funds exist. — [PR.com release 960264](https://www.pr.com/press-release/960264); [PR.com company profile](https://www.pr.com/company-profile/press-releases/580548)
- Search found no independent coverage, results or winner announcements. — [search, Feb 2026 release only]

**Agent Bounty (agentbounty.org) [LOW CREDIBILITY]**
- Site tagline: "The bounty platform for AI agent developers." Categories are agent frameworks, benchmarks, open source, research, integrations and security. Rewards are paid "via crypto or bank." Featured bounties run $8.5k–$15k and active ones $2.5k–$7.2k. The site claims an "average $4,200," "$2.4M total paid," "342 active bounties," "8,900+ hunters" and a top hunter at $128,500. No operator is named; the only contact is team@agentbounty.org, with a "© 2026" footer. — [agentbounty.org](https://agentbounty.org)
- An independent search summary notes that listings carry early-2026 due dates and that it found no independent confirmation of the payout claims. — [search summary referencing agentbounty.org](https://agentbounty.org/)
- Several unrelated projects use the "AgentBounty" name: a DEV Community guide to a Base Sepolia USDC pay-per-task agent marketplace, a Solana devnet "forge agent bounty" escrow project, a BOUNTY token on Base listed on DexScreener, and Hedera's "AI Agent Bounty." This makes attribution confusing. — [DEV guide](https://dev.to/prema_ananda/agentbounty-user-guide-454o); [DeepWiki forge-agent-bounty](https://deepwiki.com/0xNyk/forge-agent-bounty); [DexScreener](https://dexscreener.com/base/0xc4b46bec73e149f82d4b051a32f9527032f1b40386851ca816a397b27610f7e4); [Hedera AI Agent Bounty](https://ai-bounties.hedera.com/)

**Bounty (trybounty.ai) [VERIFIED-ish: media coverage and a16z funding]**
- New York startup co-founded in early 2026 by Rayan Dabbagh, Aashna Doshi (ex-Google) and Shivam Patel (ex-Barclays algo trading). It is a marketplace where AI agents compete for and complete paid tasks: clients post a task, a price and requirements, and the highest-rated suitable agent claims it. Payment is held in escrow until the client approves, and the platform takes a 10% commission. — [MENA Startup Digest, updated Jul 26, 2026](https://menastartupdigest.com/?p=46086)
- Funding is over $1M in total, of which a16z invested $1M and is the only institutional investor. Selected for the a16z Speedrun summer cohort. Launched a few weeks before early July 2026 with 1,300+ tasks posted. The founder says some agents earn "up to $500/month" for their owners; that figure is unverified. — [MENA Startup Digest](https://menastartupdigest.com/?p=46086)

**Execution Market (execution.market), by Ultravioleta DAO [hackathon showcase, claims production use]**
- Here AI agents post USDC bounties for humans to complete physical or real-world tasks: checking that a store is open, photos, deliveries, market research, translations. Agents post via MCP, REST or A2A. Workers are paid through gasless x402 escrow on 9 EVM chains, including Base. Humanity is proved with World ID, at Orb level for tasks over $5. Reputation runs on ERC-8004. Listed at ETHGlobal Cannes 2026; the listing says it is "live in production." — [ETHGlobal showcase](https://ethglobal.com/showcase/execution-market-xc51v); [apis.io provider listing](https://apis.io/providers/execution-market/)
- Related x402 bounty rails found in the same search: Vangrid's bounty API, where agents pay bounties via x402 on Base or Arc ([Forkast](https://forkast.news/?p=131862)), and BountyBook.ai, a USDC x402 escrow bounty marketplace on Base ([browserless skill listing](https://cloud.browserless.io/skills/bountybook.ai)). Neither has been verified.

**Agentic.market (x402 / Coinbase ecosystem, April 2026)**
- Forklog reports that the developers of the Coinbase-backed x402 standard launched a marketplace of apps and services for AI agents. It is a service-discovery marketplace (agents paying for services), not a bounty board. — [Forklog](https://forklog.com/en/news/x402-launches-marketplace-for-ai-agent-services)

**Other agent-earning venues mentioned (low verification)**
- Claw Earn: promoted on AI Agent Store news pages as an on-chain jobs layer on Base with USDC escrow. — [AI Agent Store news, Feb 2026](https://aiagentstore.ai/ai-agent-news/topic/human-ai-synergy/2026-02-17)
- AIGEN "Open Bounty Protocol for AI Agents": hosted on a duckdns subdomain and pitches a 0.5% fee against Superteam's 5–15%. Promotional, with a hobby-grade domain. — [AIGEN_PROTOCOL.md](https://cryptogenesis.duckdns.org/AIGEN_PROTOCOL.md)
- "Agents University Bounty Board": appears only as an ERC-8004 registry entry on Base mainnet. — [QuickNode ERC-8004 explorer](https://erc-8004.quicknode.com/agents/base-mainnet/19383)
- A DEV guide claims cumulative x402 agent-to-agent volume above $50M. This is unverified. — [DEV Community](https://dev.to/neilvolner/how-ai-agents-are-earning-real-money-in-2026-a-practical-guide-3ei6)

**Practitioner evidence on agent bounty-hunting (credibility signals)**
- Real-money GitHub bounties get claimed within minutes to hours. On Algora there are about 10–20 hunters per bounty, and the first valid PR wins. — [DEV: 48h agent test](https://dev.to/hermesxclawctrl/i-let-my-ai-agent-hunt-bounties-for-48-hours-heres-what-it-actually-found-4c5p); [DEV: 24/7 bounty agent](https://dev.to/zeroknowledge0x/i-built-an-ai-agent-that-hunts-github-bounties-247-architecture-code-and-brutal-lessons-after-2kma)
- Reported outcomes range from $345 in one week (4 merged PRs at $50–100) to $10 across 17 PRs, and $0 from 8 PRs. Writers warn about fake bounty repos and about token-denominated payouts (MergeOS, RustChain, Roxonn) that may be worthless. — [DEV $345](https://dev.to/hummern/how-ai-agents-earn-345-real-world-bounty-hunting-results-3b3m); [DEV $10](https://dev.to/ydd039/how-i-earned-10-on-github-using-ai-agents-without-writing-a-single-line-of-complex-code-575b); [HackerNoon $0](https://hackernoon.com/i-sent-an-ai-agent-to-hunt-open-source-bounties-for-three-days-it-earned-$0)
- The "awesome-agent-bounties" list (github.com/Scottcjn) returned 404 when fetched, so it may have been deleted or renamed. — [GitHub link (404)](https://github.com/Scottcjn/awesome-agent-bounties)

### Inferences
- Of the brief's three leads, none has independently verified payouts. AgentOn looks like a Web2.5 quest/campaign network: its tasks are growth and marketing, not technical work. Bot Games depends entirely on one small company's press release, with no visible results. agentbounty.org's numbers ($2.4M paid, 8,900 hunters) with no named operator and stale due dates fit a template or placeholder site, or possibly a scam. Do not recommend it without proof of payouts.
- The most credible new agent marketplace is Bounty (trybounty.ai). It has named founders and a disclosed a16z investment, but its payout scale is small (about $500/month per agent at best, by the founder's own claim).
- The x402 ecosystem (Execution Market, BountyBook, Vangrid) is building agent-to-human and agent-to-agent bounty rails. These are early and hackathon-grade, and the rewards are mostly micro-tasks.

### Gaps
- I could not confirm ME Group's role in AgentOn or whether its campaign paid out; there are no post-campaign reports.
- No Bot Games results, winners or prize escrow found. Did the March 1 round happen?
- agentbounty.org's operator, domain registration date and any third-party payout confirmation are unknown.
- I did not check other 2026 agent competitions, such as Kaggle-style agent arenas, Bittensor agent subnets or Virtuals/ACP job markets, for lack of budget.

## Q2: Coding / open-source issue bounty platforms (new in 2026 or with major 2026 changes) and AI-training expert platforms

### Takeaway
The established GitHub-issue bounty platforms (Algora, Polar, Opire, IssueHunt, Gitcoin) are all **[OLDER]**, and I found no 2026 launches or shutdowns for them. Gitcoin's Grants Lab was dissolved in 2025, and the Grants program continues under "Gitcoin 3.0." The main 2026 change in paid technical work is expert AI-training platforms. Toptal ExpertCrowd launched in Oct 2026, and micro1 has scaled sharply. Both pay vetted engineers rather than open bounty hunters.

### Cited Findings

**Algora (algora.io) [OLDER, active]**
- Bounties on GitHub issues: maintainers post with `/bounty` and contributors use `/claim`; payment comes when the PR is merged. Contributors keep 100% and are paid via Stripe/Alipay in 3–8 days on average. Maintainers pay an 11% fee (individuals); org tiers cost $1k / $2.5k / $7k. Algora also offers contract work. — [Algora pricing](https://console.algora.io/pricing); [docs.algora.io](https://docs.algora.io)
- Scale figures, all undated: "$335k+ to 559 devs in 68 countries" (Algora), 2,177 bounties worth $267,962 to 497 contributors ([Tembo blog](https://tembo.io/blog/algora-code-bounties)), and 652 contributors from 71 countries ([Algora community](https://algora.io/community)). I found no 2026-specific change.
- Competition is intense (about 10–20 hunters per bounty, first valid PR wins). — [DEV](https://dev.to/zeroknowledge0x/i-built-an-ai-agent-that-hunts-github-bounties-247-architecture-code-and-brutal-lessons-after-2kma)

**Polar.sh [OLDER]**
- Its docs still describe "Issue Funding" and "Rewards" (bounty-like). I found no announcement of a 2026 shutdown, but current status is unconfirmed. Polar has shifted toward monetization and billing for developers. — [Polar docs: issue funding](https://docs.polar.sh/issue-funding); [Introducing Rewards](https://polar.sh/polarsource/posts/introducing-rewards)

**Opire [OLDER, possibly stagnant]**
- The latest third-party snapshot shows "Live" with a last update in Sep 2024. One 2026 agent experiment found every Opire reward it checked was closed or its repo unavailable. — [ossfund listing](https://ossfund.onrender.com/opire); [HackerNoon](https://hackernoon.com/i-sent-an-ai-agent-to-hunt-open-source-bounties-for-three-days-it-earned-$0)

**IssueHunt [OLDER]**: no 2026 results found.

**Gitcoin [OLDER; restructured]**
- April 2025: Gitcoin wound down Gitcoin Labs and Grants Lab for lack of profitability. Grants Stack and Allo Protocol were sunset, with Grants Stack unmaintained from May 31, 2025. Passport (now human.tech), KERNEL, Public Works and Allo Capital were not affected. — [The Block](https://www.theblock.co/news/markets/2025-04-25-ethereum-public-goods-funding-protocol-gitcoin-winding-down-its-software-division-352055); [Gitcoin gov forum](https://gov.gitcoin.co/t/focusing-gitcoins-future-sunsetting-grants-stack-eol-may-2025/20333)
- A governance proposal (quorum not reached) says Grants Lab was dissolved mid-2025, that the DAO entered "Gitcoin 3.0" in H2 2025, and that 2026 plans build on it. Gitcoin Grants rounds continue. — [Tally proposal](https://www.tally.xyz/gov/gitcoin/proposal/2798837891353020055)

**Superteam Earn [OLDER, Solana; agent-eligible listings in 2026]**
- A 2026 guide reports $66k+ in active bounties, some explicitly open to agents. — [DEV guide](https://dev.to/neilvolner/how-ai-agents-are-earning-real-money-in-2026-a-practical-guide-3ei6)
- An AI agent's own Feb 2026 account says about 80% of bounties block AI or require KYC. It also reports 479 submissions for one $3.1k bounty (a win rate under 1%), winners announced weeks late, and agent API endpoints returning 404. This is a single anecdote. — [DEV: AI agent given $50](https://dev.to/neilvolner/i-am-an-ai-agent-given-50-to-make-money-here-is-what-actually-happened-3gjg)

**AI-training / expert coding-task platforms (2026)**
- **Toptal ExpertCrowd [NEW, Oct 2026]:** a platform for RLHF, RL data generation, labeling and evaluation that uses vetted Toptal experts. Toptal says it booked more than $5M in recurring revenue before launch, with clients including Scale AI. It also released the ExpertCrowd-SWE benchmark (87 codebases, 11 languages), whose tasks and rubrics were written by Toptal engineers. Pay rates were not disclosed. — [Toptal press center](https://www.toptal.com/press-center/toptal-launches-expertcrowd-to-advance-ai-with-world-class-domain-expertise)
- **micro1 [OLDER, scaled in 2026]:** links AI labs with vetted experts (about the top 1% of applicants, mostly PhDs and senior SWEs) for RLHF and labeling. Sacra estimates about $500M annualized revenue by Aug 2026; this is an estimate. — [Sacra micro1](https://sacra.com/c/micro1/)
- Sacra's competitor profiles note that Scale AI launched RL environments in early 2026, and they cover AfterQuery. — [Sacra AfterQuery](https://sacra.com/c/afterquery)

### Inferences
- I found no genuinely new 2026 GitHub-issue bounty platform with credible traction. The category is dominated by Algora, and the others are stagnant or have pivoted. The newest "bounty" products target AI agents rather than humans (see Q1).
- For technical contributors who want reliable pay in 2026, expert AI-training platforms (ExpertCrowd, micro1 and peers) are probably more lucrative and steady than open bounties. They are invite or vetting-gated, though, not open.
- Open GitHub bounties are now saturated by AI-agent hunters, which lowers the expected value per human hunter.

### Gaps
- No 2026 primary-source updates for Algora, IssueHunt or Polar's bounty features. Their status comes from older or undated pages.
- Pay rates for ExpertCrowd and micro1 were not found.
- I did not cover other 2026 AI-coding bounty or annotation entrants (e.g., new Mercor/Outlier/Handshake AI coding programs, GitHub-native agent bounty bots).
