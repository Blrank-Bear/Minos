# Issue / PR bounty and "paid contribution" platforms launched 2025–2026

Research date: 2026-10-28. Budget: 30 tool calls. Coverage is partial: the search tool surfaced few 2025–26 launches with press coverage. Most new entrants are small indie or hackathon projects with self-reported claims only. Nothing below is independently verified unless marked **verified**.

## Q1: Which issue/PR bounty platforms are NEW in 2025–2026 (Web2 and Web3)?

### Takeaway
No large new Web2 issue-bounty marketplace launched in 2025–26. The funded 2025 entrant, Merit Systems' "Terminal" (a16z crypto, $10M seed), shows no sign of activity on Merit's current homepage, which lists only AI-agent payment products. The 2025–26 launches that do exist are small: indie Show HN products (IssuePay, HitCommit, a BountyHub relaunch) and many crypto escrow-on-merge projects (MergePay on Arc, PullPay on Optimism, Kudoz on Solana, claudelance on Celo). The only large-scale 2025–26 paid-contribution program found is Drips Wave itself, which runs on points and pools. Live bounty volume on these boards also looks very thin.

### Cited Findings

**Merit Systems – Terminal (merit.systems)** – Web2/Web3 hybrid. Launched 2025.
- Raised a $10M seed co-led by a16z crypto and Blockchain Capital, January 2025 — [SiliconANGLE](https://siliconangle.com/2025/01/16/merit-systems-raises-10m-create-new-economic-model-called-open-source-capitalism/); [The Block](https://theblock.co/post/335347/merit-systems-raises-10-million-in-round-co-led-by-a16z-crypto-and-blockchain-capital)
- Launch post "Launching the Terminal and a new financial stack for open-source software", dated July 2, 2025 — [Merit blog](https://www.merit.systems/blog/launch)
- Mechanism (from a search summary of Merit pages): a GitHub-based interface where owners choose contributors to pay based on merged PRs, with PR insights. Payouts are in stablecoins, and Merit says it handles tax compliance, including for unincorporated projects. Contributors withdraw to a bank account or in stablecoins — [Merit blog](https://www.merit.systems/blog/launch), [Merit docs](https://www.merit.systems/docs). These claims come from a search summary. The fetched launch page was only a teaser and did not show these details.
- **Status change (verified on the homepage, 2026-10-28):** the homepage now lists only x402scan, MPPscan, AgentCash, Poncho, OpenInstinct and Theo, which are AI-agent payment and discovery products. The Terminal for paying GitHub contributors is not listed — [merit.systems](https://www.merit.systems/)
- Fees, KYC/geo limits and payout volumes: not found.

**BountyHub (bountyhub.dev)** – Web2. First launched Oct 2024; Show HN Jan 2025; relaunched on Product Hunt June 8, 2025.
- Product Hunt launches: Oct 29, 2024 ("Monetizing GitHub issue resolution through bounties", #4 of the day) and June 8, 2025 ("Crowdfunding GitHub issues made easy", #5 of the day). Features listed: secure payments and dispute resolution, plus a GitHub app — [Product Hunt](https://www.producthunt.com/products/bountyhub?launch=bountyhub-2); [GitHub Marketplace](https://github.com/marketplace/bountyhub-app)
- Show HN "What if you could directly pay GitHub contributors?" on Jan 5, 2025, 2 points. It works on repos where no bot is installed and uses a dedicated UI instead of comment commands. Non-maintainer bounty creators must get maintainer approval for feature requests — [HN](https://news.ycombinator.com/item?id=42602127)
- Fees and currency: not stated. Strictly a 2024 launch, but its public relaunch was in 2025.

**IssuePay (issuepay.app)** – Web2. Show HN June 27, 2025.
- Maintainers post bounties on GitHub/GitLab issues. Contributors merge code, get paid automatically and withdraw to a bank account. Companies can fund "sponsor issues". A premium plan gives priority placement in "Job Offers" — [HN](https://news.ycombinator.com/item?id=44399096)
- **Red flags:** 8 points. A commenter cited a 50% platform fee, and the founder said pricing was being reevaluated. A "Trusted by leading tech companies" claim was challenged and then removed. Footer, Terms and Privacy links did not work at launch — [HN](https://news.ycombinator.com/item?id=44399096)

**HitCommit (hitcommit.com)** – Web2/Web3 rails. Show HN about 11 months before Oct 2026, so roughly late 2025 (exact date not shown).
- Maintainers attach rewards to GitHub issues. Contributors are paid via PayPal or Stellar, with "no tokens, no marketplace complexity". 3 points, no traction signals — [HN](https://news.ycombinator.com/item?id=46085012)

**MergePay (mergepay.fun)** – Web3. Launch date not stated (2025–26 likely, unverified).
- Anyone escrows USDC on a public GitHub issue. The contract pays whoever's merged PR fixes it, after verifying GitHub's signed merge proof on-chain. It runs on the Arc network (the site shows "live on arc mainnet"), with no bot, backend or trusted key. No platform fee; about $0.016 gas per award, covered by a funder-set relayer fee (default $0.03). Solo builder Rohit Purkait (@codeswithroh); not affiliated with GitHub or Circle. No payout figures were visible — [mergepay.fun](https://mergepay.fun/)

**PullPay** – Web3 (Optimism). Date not stated.
- USDC escrow per issue, auto-paid when the linked PR merges. Uses the UMA Optimistic Oracle for disputes and EAS attestations for reputation. Repo has 47 commits, 1 star and 0 forks, with a demo at pullpay-sigma.vercel.app. Looks like a hackathon or early project — [GitHub](https://github.com/irham3/pullpay)

**Other crypto "pay-on-merge" prototypes (hackathon-grade, mostly unverified as live):**
- MergeReward (Chainlink hackathon): a GitHub webhook is verified by Chainlink CRE, then escrow pays 95% to the developer and 5% to the protocol — [Chainlink hack-26](https://chain.link/hack-26/projects/mrewards)
- vGrant (ETHGlobal): a vault pays the first valid merged PR, with a refund after the deadline — [GitHub](https://github.com/b3ww/ethglobal)
- Kudoz (Solana): sponsors fund campaigns, and eligible merged PRs (gated by AI review and CI) pay to a GitHub-linked wallet managed by Privy — [GitHub](https://github.com/token2049-decentralizing/core)
- Code Bounty (codebounty.org): bounties on GitHub issues, released by smart contract on merge, in ETH or ERC-20. Date and status unknown, and the site gave no content when fetched — [codebounty.org](https://www.codebounty.org/); a design-agency case study also exists — [Contra](https://contra.com/community/yYklUKoV-code-bounty-streamlined-open-source-funding-for)
- claudelance: describes itself as an onchain marketplace on Celo mainnet where Claude Code subscriptions earn cUSD/CELO/USDC solving GitHub bounties (agent-oriented) — via [GitHub topic bounty-marketplace](https://github.com/topics/bounty-marketplace)
- agent-bounties: an open-source bounty network where AI agents post, claim, solve and get paid — [GitHub](https://github.com/zhumeiyan/agent-bounties)
- TON Society GitHub Action: awards soulbound tokens (not money) after a merged PR — [GitHub](https://github.com/ton-society/gh-ton-contribution-reward)

**Ecosystem "builder rewards" programs (paid contribution, not per-issue):**
- Talent Protocol Builder Rewards (Base): weekly rewards to builders, with GitHub activity as one scoring input. Eligibility requires a Builder Score of 40+, a Human Checkmark and a Basename. Described as 2 ETH to 100 developers per week. The WalletConnect variant paid 75,000 WCT per week to the top 100 builders, Sep 30–Nov 11, 2025 — [Talent guide](https://talentprotocol.notion.site/builder-rewards-guide?pvs=4); [Talent FAQ](https://docs.talent.app/docs/legal/builder-rewards-faq-walletconnect); [Base docs](https://docs.base.org/get-started/get-funded)
- Stacks Builder Challenges: weekly STX for building — [Stacks blog](https://www.stacks.co/blog/stacks-builder-challenges-stx-rewards)

**Drips Wave (the comparator, launched 2026):**
- Stellar Wave 1 ran Jan 21–31, 2026. Contributors resolve curated issues for Points and get a pro-rata share of a reward pool per Wave — [Drips Stellar Wave](https://www.drips.network/wave/stellar); [Docs](https://docs.drips.network/wave)
- In Wave 2, almost 600 participants merged over 3,000 PRs across 200+ repos in 10 days. Drips added application limits and captchas against spam and self-dealing — [Wave 2 changelog](https://www.drips.network/blog/posts/wave-2-changelog)
- Q1 2026 update: over 1,000 new developers onboarded and 3 Waves completed — [RadWorks forum](https://community.radworks.org/t/drips-org-q1-2026-update/3721); [Q1 roundup](https://www.drips.network/blog/posts/q1-2026-roundup)

**Market thinness and red flags:**
- The BountyOS aggregator tracks Algora, Opire, IssueHunt, BountyHub and TaskBounty. Its snapshot on 2026-10-28 showed **only 2 open bounties worth $101 in total** (Opire 1/$10, BountyHub 1/$91, the others 0). It says it filters out honeypots, dead repos, bot-farmed listings, self-proposed amounts and brand-new low-trust repos — [BountyOS](https://bountyos.rovidev.com/en/github-bounty-board/). A search snippet for the same page dated 2026-09-30 showed 155 bounties worth $68,771. This conflicts, possibly because filters changed or a scraper broke. Treat both numbers cautiously.
- A dev.to author running an AI bounty-hunting agent reported 240+ PRs, 72 merged and $500–800 earned in 96 hours (self-reported). The author warned that most bounty listings are scam repos that create fake bounty issues to attract automated PRs. Another author found mostly ecosystem credits rather than cash — [dev.to](https://dev.to/zeroknowledge0x/i-let-an-ai-agent-hunt-open-source-bounties-for-96-hours-heres-the-brutal-truth-about-what-42p3); [dev.to](https://dev.to/hermesxclawctrl/i-let-my-ai-agent-hunt-bounties-for-48-hours-heres-what-it-actually-found-4c5p)
- An Apify scraper aggregates USDC bounties from GitHub, Algora, Collaborators.build and Dework — [Apify](https://apify.com/theaurora/bounty-aggregator)

### Inferences
- The AI-agent PR flood of 2025–26 seems to have hurt open issue bounties. Maintainers get swamped with low-quality claims, and honeypot "bounty" repos target agents. That would explain both the thin live volume and why Drips Wave added captchas and application limits. Curated, points-and-pool programs (Drips Wave, Talent Builder Rewards) look like the surviving model.
- Merit's move from paying OSS contributors to x402/agent payments suggests the best-funded 2025 OSS-pay startup did not find enough demand. The pivot itself is inferred from the homepage. No announcement was found.
- Crypto escrow-on-merge is now a common hackathon template (Optimism, Arc, Solana, Celo, Chainlink). None shows verified payout volume.

### Gaps
- Not checked within budget: Boss.dev, Gitpay, Bounty.new (search returned nothing), devs.fun, TaskBounty (no URL found), Gib.work, Bountycaster, Collaborators.build, Superteam Earn, Ubiquity DevPool, Layer3-for-devs, Coinbase/Base PR rewards.
- No fees, KYC/geo rules or verified payout totals for any 2025–26 entrant. The Merit Terminal's fee and KYC details and its real payout volume are unknown.
- Exact launch dates are unknown for MergePay, PullPay, Code Bounty, HitCommit and Kudoz.

## Q2: 2025–26 status of older platforms (Algora, Opire, IssueHunt, Polar, Gitcoin, OnlyDust)

### Takeaway
Algora and Opire are still running but have very little open bounty volume as of Oct 2026. IssueHunt seems to have gone quiet as an OSS bounty board. Gitcoin wound down its software arm in 2025 and runs only grant rounds. No shutdown notice was found for Polar issue funding or OnlyDust.

### Cited Findings
- **Algora:** still live. Pricing shows an 11% fee on bounties and tips (19% tier for community organizations), with contributor payouts in 3–8 days on average — [Algora pricing](https://console.algora.io/pricing). Still used in 2025, e.g. the GeoStats.jl/Arpeggeo funding in May 2025 — [Julia Discourse](https://discourse.julialang.org/tag/bounty). No 2025–26 funding news found. BountyOS showed 0 open Algora bounties on 2026-10-28 — [BountyOS](https://bountyos.rovidev.com/en/github-bounty-board/)
- **Opire:** still listed. It uses a GitHub bot plus a web app, and developers get 100% of the reward. A listing from 2024 gives a fee of 4% plus Stripe fees — [Opire GitHub](https://github.com/opire); [ossfund](https://ossfund.onrender.com/opire). A TrustMRR listing was updated in June 2026 — [TrustMRR](https://trustmrr.com/startup/opire-llc?metric=mrr)
- **IssueHunt:** AlternativeTo lists it as discontinued, with no social media activity since 2019 — [AlternativeTo](https://alternativeto.net/software/issuehunt/about). Dealroom describes the company as a bug-bounty (security) platform — [Dealroom](https://ai-startups.dealroom.co/companies/issuehunt). In other words, it moved away from OSS issue bounties.
- **Polar.sh:** the docs still describe issue funding and rewarding contributors. Fees changed from a 5% revenue share to 4% plus 40¢ — [Polar docs](https://docs.polar.sh/issue-funding); [Polar FAQ](https://docs.polar.sh/support/faq). No deprecation notice was found, but Polar's focus is now merchant-of-record billing (inference; not verified).
- **Gitcoin:** Gitcoin Labs wound down in April 2025, and Grants Stack has not been maintained since May 31, 2025 — [The Block](https://www.theblock.co/post/352055/ethereum-public-goods-funding-protocol-gitcoin-winding-down-its-software-division); [Gitcoin gov](https://gov.gitcoin.co/t/focusing-gitcoins-future-sunsetting-grants-stack-eol-may-2025/20333/2). GG24 (Oct 2025) distributed about $1.8M across several mechanisms — [Gitcoin](https://gitcoin.co/campaigns/gitcoin-grants-24-gg24). Gitcoin runs grants only; its old issue-bounty product was retired before 2025.
- **OnlyDust:** no shutdown or pivot news found. It still appears as the reward channel for Starknet contributor programs (undated pages) — [Troves docs](https://docs.troves.fi/p/developers/contribute-onlydust); [Trustless Work](https://docs.trustlesswork.com/trustless-work/readme/our-journey-so-far/current-programs/od-hack-campaigns)

### Inferences
- Among older platforms, the per-issue cash bounty model looks stagnant to declining. Drips Wave's 2026 traction (thousands of PRs per Wave) runs on curated issues plus pooled ecosystem money, not on individual bounty posters.

### Gaps
- OnlyDust's 2025–26 status and volume are unconfirmed. Algora's 2025–26 GMV is unknown, and the stats found date from 2023–24. IssueHunt's OSS side has no explicit shutdown date.
