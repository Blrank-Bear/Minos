# Blockchain-ecosystem OSS contributor reward platforms/programs launched or opened 2025-2026

Scope note: 29 tool calls (about 24 searches and fetches). Today is 2026-10-28. Most sources are first-party: foundation blogs, program docs, governance forums. Search coverage for Aptos, Sui, Cosmos, Mina, Hedera, Cardano, ICP, Gnosis, Scroll, zkSync, Monad, Berachain and the Ethereum Foundation turned up nothing usable (see Gaps). "Verified" below means a primary source reports realised payouts or results. "Claimed" means only announcements or self-reported figures.

## Q1: Which ecosystems ran a NEW public platform or recurring program in 2025-2026 where individual devs earn per contribution, per month or retroactively?

### Takeaway
The closest match to the target model (pay per merged issue/PR, recurring, open to anyone) is **Drips Wave on Stellar** (launched Jan 2026). Stellar also has **GrantFox**, which filled the gap OnlyDust left when it pivoted away from Web3 in 2025. Talent Protocol "Builder Rewards" is the second family: automated weekly or monthly payouts based on scored GitHub and on-chain activity, run for Base, Celo (Proof of Ship), Stacks and WalletConnect. A third family pays projects rather than individual PRs, retroactively or in rounds: Optimism Retro Funding (Dev Tooling), Avalanche Retro9000, Algorand xGov retroactive, Filecoin ProPGF, Gitcoin GG24 OSS. The NEAR "Protocol Rewards" SDK also pays weekly tiered rewards from GitHub metrics.

### Cited Findings

**1. Drips Wave (Stellar). The primary Drips-Wave model, launched Jan 2026**
- URL: https://www.drips.network/wave/stellar. Announced late 2025. Stellar Wave 1 ran Jan 21-31, 2026 — [Drips Wave Stellar page](https://www.drips.network/wave/stellar); [What's launching in January](https://www.drips.network/blog/posts/drips-wave-whats-launching-in-january)
- Mechanism: maintainers curate issues. Contributors earn Points by complexity (Trivial 100, Medium 150, High 200). After each Wave, a Reward Budget is split pro rata by share of total Points. Limits: max 15 pending applications, max 4 assigned issues per org per Wave, optional per-contributor reward cap per program. Organizers can deduct points or withhold rewards for misbehaviour. Two-way reviews happen within 14 days — [Drips docs: solving issues and earning rewards](http://docs.drips.network/wave/contributors/solving-issues-and-earning-rewards/)
- KYC: mandatory Sumsub identity verification before applying to any issue — [Drips docs](http://docs.drips.network/wave/contributors/solving-issues-and-earning-rewards/)
- Cadence: described as a monthly Wave (~10 days per month in one source, "one week every month" in docs). Wave 3 launched Mar 23 and Wave 4 on Apr 22, 2026. Wave 4 had a "significantly larger" budget than earlier Waves (amount not disclosed) — [RadWorks: Drips Org Q1 2026 Update](https://community.radworks.org/t/drips-org-q1-2026-update/3721); [Drips blog](https://drips.network/blog)
- Scale (claimed by Drips): >1,000 new developers into Stellar OSS in Q1 2026, and >30,000 PRs merged in the Stellar Wave Program. "Thousands of contributors" per Wave — [RadWorks Q1 2026 update](https://community.radworks.org/t/drips-org-q1-2026-update/3721); [Drips Q1 2026 roundup](https://www.drips.network/blog/posts/q1-2026-roundup)
- Business: Wave generates "significant revenue" that roughly covers Drips' monthly personnel costs. It needs heavy monthly ops. Q1 ran over budget. No other Wave partner had been named as of Q1 2026, only "multiple promising leads". UNICEF Office of Innovation is a separate DPG-funding pilot, not a Wave — [RadWorks Q1 2026 update](https://community.radworks.org/t/drips-org-q1-2026-update/3721)
- Launch bonus: 100 Points for early sign-ups, plus a social-share bonus with a deadline of Jan 22, 2026 — [Drips campaign page](https://drips.network/campaigns/wave-launch-points-bonus); [socials campaign](https://www.drips.network/campaigns/wave-launch-socials)
- Red flags: per-Wave pool sizes are not published. 30k PRs from ~1k+ devs in one quarter is a very high rate, which suggests many trivial or farmed PRs. The sources do not mention spam or AI-PR policy.

**2. GrantFox (Stellar). Issue/bounty marketplace, 2025**
- Positioned in its Stellar Community Fund listing as the Stellar-only successor hub after "OnlyDust shifts away from Web3". Features: maintainer workspace synced with GitHub, contributor app to apply to issues, campaigns, smart-escrow funding (Trustless Work). This is a competitor's self-description — [SCF project: GrantFox](https://communityfund.stellar.org/project/grantfox-4zq); [SCF submission](https://communityfund.stellar.org/submissions/rechsG6zSfsxxGqxw)
- Payouts in USDC after work is accepted. The first two campaigns put up >$75,000 (claimed) — [Stellar Nigeria, DEV.to](https://dev.to/stellar_nigeria/over-400000-went-to-stellar-contributors-this-year-33jd)
- Ran the bounty platform for Stellar Summit São Paulo 2026 with a USDC 10,000 pool escrowed upfront (LinkedIn claim from a team member) — [LinkedIn](https://cr.linkedin.com/in/joelvr)

**3. OnlyDust (Starknet, Stellar and others). Older (2022-24), pivoted in 2025**
- One line: a GitHub-overlay marketplace that claims $11M+ in rewards to 10,000 devs in its first two years. Backed by StarkWare, Starknet Foundation, OP Foundation, Aptos, Zama, EF. In 2025 it announced it was opening to the wider (non-Web3) OSS world, citing a May 2025 hackathon with ~1,000 devs — [OnlyDust Notion: Call for Contributions](https://onlydust.notion.site/Only-Dust-Call-for-Contributions-2190bfb1fcbd48a7ab01c2e08d2a03da); [paragraph.xyz](https://paragraph.xyz/@papajams.eth/onlydust-connecting-developers-to-build-the-future-of-starknet). It also ran "OD Hack" campaigns used by Stellar projects such as Trustless Work — [Trustless Work docs](https://docs.trustlesswork.com/trustless-work/about-trustless-work/our-journey-so-far/current-programs/od-hack-campaigns)

**4. Talent Protocol Builder Rewards (Base, Celo, Stacks, WalletConnect). Automated scored payouts, 2025**
- Base: "2 ETH to 100 developers each week", automated and merit-based (founder post) — [paragraph.xyz/@macedo](https://paragraph.xyz/@macedo/my-q1-journey). Base docs list "2 ETH in weekly rewards ... through Talent Protocol" — [Base docs: Get Funded](https://docs.base.org/get-started/get-funded)
- Eligibility: Builder Score >= 40 (combines GitHub, on-chain and credentials), Human Checkmark (anti-Sybil) and a Basename — [Talent builder rewards guide](https://talentprotocol.notion.site/builder-rewards-guide?pvs=4)
- Status conflict: a third-party GitHub issue (Jul 14, 2026) says Talent's Base page shows "Base Campaign Has Ended". It says the last campaign ("Top Base Builders: January") ended Jan 31, 2026 and the 2 ETH/week format ended Jul 2025. This is unverified, and Base docs still advertise it — [issue mirror](https://mymirror.duckdns.org/base/docs/issues/1723) vs [Base docs](https://docs.base.org/get-started/get-funded)
- WalletConnect x Base Builder Rewards: weekly distributions Sep 30 – Nov 11, 2025 (campaign end Dec 2, 2025). 75,000 WCT per week to the top 100 builders, scored on GitHub activity, WalletConnect usage and Base on-chain activity — [Talent docs: WalletConnect FAQ](https://docs.talent.app/docs/legal/builder-rewards-faq-walletconnect)
- Stacks Builder Challenges: Dec 10–30, 2025, three weekly challenges (Clarity 4, Chainhooks, WalletConnect) with STX pools. The first week was 5,000 STX (KuCoin flash). Ranked by Talent score ("verified onchain activity and open-source contributions"). Paid automatically to the linked STX address, with "standard compliance checks at payout" — [Stacks blog, Dec 9, 2025](https://www.stacks.co/blog/stacks-builder-challenges-stx-rewards); [KuCoin news](https://www.kucoin.com/news/flash/stacks-partners-with-talent-protocol-for-weekly-builder-challenge-focused-on-clarity-4-bitcoin-apps). Talent's Stacks page reported 508 builders tracked and 318 active in Feb 2026 — [talent.app/stacks](https://talent.app/~/ecosystems/stacks)
- Red flags: rewards go to "builders" by score, not to specific merged contributions, so they can be gamed with commit volume. Campaigns are short and stop and start.

**5. Celo Proof of Ship. Monthly builder rewards, launched ~early 2025**
- Monthly contest. By PoS #4 (newsletter May 7, 2025) it offered "up to $15k monthly", plus partner tracks (Divvi up to $5k, Self $250 per integration) — [Celo devs newsletter](https://celo-devs.beehiiv.com/p/prove-your-impact-on-celo-earn-up-to-15k-monthly). The earliest Notion page lists a 5k cUSD monthly pool — [Celo Notion](https://celoplatform.notion.site/Build-With-Celo-Proof-of-Ship-17cd5cb803de8060ba10d22a72b549f8)
- Later rounds: PoS 6 was 15k cUSD, PoS 7 was 15,000 CELO + 5k cUSD, PoS 9 was 20,000 CELO in Builder Rewards plus sponsor bounties — [PoS 6](https://celo-devs.beehiiv.com/p/proof-of-ship-6-2nd-milestone-checkin-ed40); [PoS 7](https://celo-devs.beehiiv.com/p/proof-of-ship-7-2nd-milestone-checkin); [PoS 9](https://celo-devs.beehiiv.com/p/proof-of-ship-9-2nd-milestone-checkin)
- Mechanism: register each month, connect a GitHub repo, and submit a demo video and deck. Scored by judges and AI agents on live deployment, transactions, users, GitHub README and commits, and milestones. Impact metrics in the Karma GAP profile feed builder rewards, which are claimed monthly via Talent's Builder Score. Talent's human checkmark is required — [Karma GAP docs: Celo Proof of Ship](https://docs.gap.karmahq.xyz/how-to-guides/partners/celo-proof-of-ship); [Talent T&C Celo](https://docs.talent.app/docs/legal/builder-rewards-terms-conditions-celo)
- Rewards go to projects or apps, not contributions to someone else's OSS.

**6. NEAR "Protocol Rewards" (near-horizon). GitHub-metric weekly tiers**
- An npm SDK/GitHub Action collects commits, PRs, reviews and issues, plus on-chain metrics. Caps include 100 commits = 17.5 pts and 20 merged PRs = 12.5 pts. Weekly tiers: Diamond $2,500 (90+), Platinum $2,000, Gold $1,500, Silver $1,000, Bronze $500. Burst activity triggers validation — [near-protocol-rewards docs (unpkg)](https://unpkg.com/near-protocol-rewards@1.1.2/docs/rewards.md); [GitHub repo](https://github.com/near-horizon/near-protocol-rewards)
- Launch date, cohort status and realised payouts were not verified. These are project docs only.

**7. Optimism Retro Funding: Dev Tooling (Season 7, 2025, and Season 8). Retroactive, monthly-measured**
- 2025 changed Retro Funding from annual rounds to ongoing monthly impact evaluation. Season 7 allowed up to 8M OP for dev tooling — [Optimism blog: Retro Funding 2025](https://www.optimism.io/blog/retro-funding-2025); [Dev Tooling Mission details](https://gov.optimism.io/t/retro-funding-dev-tooling-mission-details/9598)
- Verified: 6.6M OP awarded to dev tools after 5 of 6 monthly periods (Jul 2025), with the final allocation on Aug 1, 2025 — [gov.optimism.io early evidence](https://gov.optimism.io/t/season-7-retro-funding-early-evidence-on-developer-tooling-impact/10162)
- Season 8: Budget Board proposed a max of 20M OP (8M Onchain Builders, 8M Dev Tooling, 4M OP Stack deps), monthly from Aug, measured by OSO algorithms — [Budget Board proposal](https://gov.optimism.io/t/budget-board-proposal-for-retro-funding-for-season-8/10097); [L2BEAT governance review](https://l2beat.com/publications/governance-review-61). Conflict: a vote page lists Dev Tooling "up to 3.65M OP" — [vote.optimism.io](https://vote.optimism.io/proposals/104254402796183118613790552174556993080165650973960750641671478192868760878324)
- Paid per project (repo-level impact), not per individual PR.

**8. Avalanche Retro9000. Retroactive, launched Nov 2024 (snapshots through 2025-26)**
- First grant snapshot Apr 15, 2025 — [Snow Report Mar 2025](https://info.avax.network/snow-report-march-25). Third cohort of the L1 and Infrastructure Tooling round (Dec 2, 2025): 4 grantees got >$140k. KYC/KYB is required — [Avalanche Foundation blog](https://www.avax.network/about/blog/the-avalanche-foundation-announces-third-cohort-for-retro9000-l1-and)
- >$1.25M granted cumulatively (press). The C-Chain round started in early 2026, but sources conflict on the date — [AOL](https://www.aol.com/finance/avalanche-kicks-off-c-chain-193554725.html)

**9. Algorand xGov: retroactive proposals (Oct 2025)**
- xGov mainnet was announced Aug 2025 with an initial 2026 budget of 3,000,000 ALGO — [xGov Mainnet Announcement](https://forum.algorand.co/t/xgov-mainnet-announcement/14812). Retroactive proposals (funding for already-delivered work) were accepted from Oct 1, 2025 — [Algorand blog](https://algorand.co/blog/algorand-xgov-update-now-accepting-retroactive-proposals)
- Only open-source licences are accepted. The aim is SDKs, libraries and tools — [xGov Guide 2025](https://forum.algorand.co/t/xgov-beta-xgov-guide-2025/14703/1). The Council discussed a 500k ALGO cap and a non-OSS maintenance bucket, outcome unknown — [Council meeting #4](https://forum.algorand.co/t/xgov-council-meeting-4/15050)

**10. Filecoin ProPGF. Batch rounds, 2025-26**
- Batch 1 (2025): $3.68M to 14 teams (infra, dev tooling) from 38 applications, via a 12-member committee on Questbook. Verified results post — [Filecoin blog](https://filecoin.io/blog/filecoin-propgf-batch-1-36m-awarded-to-ecosystem-builders)
- Batch 2 General Track: $4M milestone-based for OSS infra and tooling. Applications on Karma Nov 12 – Dec 23, 2025, decisions ~Jan 30, 2026, payouts Feb 2026 — [Filecoin blog](https://filecoin.io/blog/announcing-filecoin-propgf-batch-2-general-track). Filecoin is also preparing an RPGF round on Drips — [RadWorks Q1 2026](https://community.radworks.org/t/drips-org-q1-2026-update/3721)
- Teams apply with proposals, so this is a grant round rather than per-contribution pay.

**11. Gitcoin GG24 OSS rounds (Oct 2025)**
- Dev Tooling and Interop QF rounds ran Oct 14–28, 2025 on Giveth. $300k matching to 64 curated projects from 1,286 donors. Another summary says 55 projects in Dev Tooling, so counts are inconsistent. Payouts ~Nov 13, 2025 — [GG24 OSS QF results](https://gov.gitcoin.co/t/gg24-oss-quadratic-funding-results/24782); [Giveth retrospective](https://gitcoin.co/case-studies/gg24-oss-qf-giveth-retrospective). There was also a GG24 Public Goods Tooling Development Round — [retrospective](https://gov.gitcoin.co/t/gg24-public-goods-tooling-development-round-full-retrospective/25276)

**12. Polkadot: Open Source Developer Grants Bounty (Bounty 59, 2025)**
- Treasury bounty (Ref 1080) for ~15 individuals or small teams, up to $30k each. Milestone-based, OSS only, KYC/KYB required. As of Apr 2025: 11 applications, 2 approved, 2 rejected. Moved to rolling intake — [Polkadot forum](https://forum.polkadot.network/t/open-source-developer-grants/11427); [Subsquare Ref 1080](https://polkadot.subsquare.io/referenda/1080). Grant-style, not per-PR.

**Older or ongoing programs (pre-2025, one line each)**
- Superteam Earn (Solana): open bounties and projects, typically ~1,500 USDC. No 2025 GitHub-specific change found — [SolanaCompass](https://solanacompass.com/projects/Superteam)
- Starknet Seed Grants: up to $25k (STRK or USDC conflict), for early-stage teams, not per-contribution — [starknet.io](https://www.starknet.io/grants/seed-grants/)
- Stellar Community Fund v6: Build Award up to $150k XLM. SCF #41 deadline Feb 2026 — [SCF awards](https://communityfund.stellar.org/awards). Stellar Build Challenge 7 rewards "new contributions to meaningful Stellar-related open-source projects" — [Stellar blog](https://stellar.org/blog/announcing-the-7th-stellar-build-challenge)
- TON Footsteps / TON Society bounties: community bounty programs, paid on completion. No 2025 launch date found — [GitHub ton-footsteps](https://github.com/Gusarich/ton-footsteps)

### Inferences
- Only Stellar has a true Drips-Wave-style per-issue program open to anyone: Drips Wave, with GrantFox alongside it. Stellar also funds it heavily. For an individual dev seeking recurring per-contribution pay, Stellar Wave is the main 2026 venue.
- The Talent Protocol family looks like a run of short, rotating campaigns, not durable programs. Base's weekly ETH may have ended, though that is unconfirmed.
- Retro programs (OP, Avalanche, Algorand, Filecoin, Gitcoin) reward projects or maintainers, not drive-by PRs, so they suit people who own a tool.
- Common requirements: KYC (Drips Sumsub, Avalanche, Polkadot), human or Sybil checks (Talent Human Checkmark, Gitcoin Passport).
- Generic risk: a third-party review of 23 crypto bounty programs said 4 were scams (merged PRs, no payment), and some use CLAs to take code without merging. This is anecdotal and undated — [DEV Community](https://dev.to/hopkins_jesse_cdb68cfa22c/i-reviewed-23-crypto-bounty-programs-so-you-dont-have-to-261f)

### Gaps
- Searches returned nothing on new 2025-26 per-contribution OSS programs from Aptos, Sui, Cosmos, Mina, Hedera, Cardano (Catalyst changes), Internet Computer, Gnosis, Scroll, zkSync, Monad, Berachain, Arbitrum (only a 2024 non-code "Arbiter" proposal) or the Ethereum Foundation. This could be a search-coverage gap. It does not prove the programs don't exist.
- Drips Wave per-Wave budgets, payout currency and verified payout totals are undisclosed. Status after Wave 4 (Apr 2026) and any new Wave partners after Q1 2026 were not found.
- Celo Proof of Ship current round, and whether it continued into 2026 (PoS 9's year is unclear).
- Talent/Base: whether the 2 ETH/week format really ended (Jul 2025 vs Jan 2026).
- NEAR Protocol Rewards: whether the program is live and actually pays out.
- Final Optimism S7 Dev Tooling allocation and the adopted S8 budget (8M vs 3.65M OP).
- OnlyDust's current status in 2026 (fully left Web3 or not).
- Solana Foundation OSS-specific programs, Polkadot OpenGov contributor programs beyond Bounty 59, and Kusama were not covered due to budget.
