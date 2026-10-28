# Drips Wave stands almost alone in 2025–26

*Research date: 2026-10-28. Built from five research notes. Scope: platforms where developers earn money for open-source (OSS) work. Security bug bounties, Bittensor and ML competitions are excluded.*

**Short answer:** only one large new platform in 2025–26 pays individual developers per open-source contribution, in public and on a repeating schedule: **Drips Wave on Stellar**. It started in January 2026. Its 10 monthly Waves posted **about $705K in budgets**, it pays in **USDC on Stellar**, and it **requires KYC** ([Stellar Wave page](https://www.drips.network/wave/stellar)). The rest of the new activity falls into five weaker groups:

- **Small issue-bounty start-ups:** BountyHub, IssuePay, HitCommit. Little traction and no checked payout data.
- **Short crypto campaigns:** Talent Protocol, Celo Proof of Ship, NEAR, AKINDO. They score your GitHub and on-chain activity and pay in tokens.
- **Funding for projects, not people:** ecosyste.ms Funds, Deep Funding and the Optimism, Algorand, Filecoin, Avalanche and Gitcoin rounds.
- **Grants and fellowships for maintainers:** Sovereign Tech Fellowship, HeroDevs, Rust Foundation, Open Source Endowment, GNOME.
- **Many hackathon prototypes.**

The best-funded new start-up, **Merit Systems' Terminal** ($10M seed, launched July 2025), no longer appears on Merit's homepage. The homepage now lists only payment products for AI agents ([merit.systems](https://www.merit.systems/)). The open bounty market is very thin. On the research date, one aggregator showed **only 2 open bounties worth $101 in total** ([BountyOS](https://bountyos.rovidev.com/en/github-bounty-board/)). One writer also warns that most bounty listings are fake repos built to attract automated AI pull requests ([dev.to](https://dev.to/zeroknowledge0x/i-let-an-ai-agent-hunt-open-source-bounties-for-96-hours-heres-the-brutal-truth-about-what-42p3)). Almost all money figures below come from the operators themselves. An individual who wants paid OSS work today has a few real options: Drips Wave (wait for the next Wave), GitHub Sponsors, FLOSS/fund, Algora and Opire (both thin), and the maintainer grants if you already own a widely used project.

**How to read this report:** *Verified* means a primary or independent source reports something that already happened (for example, a published results post). *Claimed* means marketing copy, a plan, a proposal or a figure the operator reports about itself. **[unsure URL]** means the domain came from the notes but nobody opened it, or it is a common URL that the notes do not cite.

---

## The reference point: Drips moved from streams to paid sprints

**Drips Network** ([drips.network](https://www.drips.network/)) is run by the Public Goods Association / Radworks. It started as a tool for **funding streams, splits and "Drip Lists"**: money flows continuously to a list of projects or their dependencies. In 2025 it went live on Optimism and Metis ([Drips Q1 2025 roundup](https://www.drips.network/blog/posts/q1-2025-roundup)). It also added end-to-end **RetroPGF tooling** (nomination, voting, payouts), which Filecoin used for a **580k+ FIL** round ([Radworks forum Q3 2025](https://community.radworks.org/t/drips-org-q3-2025-update/3687)). These tools mostly fund **projects**, not single contributors.

**Drips Wave** ([solution page](https://www.drips.network/solutions/wave)) is the new product for individual contributors. It was announced on 23 Dec 2025 ([Drips blog](https://www.drips.network/blog/posts/drips-wave-whats-launching-in-january)). Drips calls it "a one-week bounty sprint that repeats each month" ([Drips on X](https://x.com/dripsnetwork/status/2005985553557406038)). It works like this:

1. Maintainers choose GitHub issues and give each one a size.
2. Contributors solve the issues and earn **Points**: Trivial 100, Medium 150, High 200 ([Drips docs](http://docs.drips.network/wave/contributors/solving-issues-and-earning-rewards/)).
3. At the end of the Wave, the pool is split by each person's share of all Points.

Limits: at most 15 pending applications per person, and at most 4 assigned issues per organisation per Wave. The **Stellar Development Foundation** pays for the pools.

| Stellar Wave | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Dates (2026) | Jan 21–31 | Feb 19–26 | Mar 23–30 | Apr 22–29 | May 26–Jun 2 | Jun 23–30 | Jul 23–30 | Aug 24–31 | Sep 23–30 | Oct 15–22 |
| Budget (USD) | 60K | 60K | 60K | 75K | 75K | 75K | 75K | 75K | 75K | 75K |

*Source: [Stellar Wave page](https://www.drips.network/wave/stellar). The total of $705K is our own sum. No Wave 11 was listed on 2026-10-28.*

Scale reported by Drips itself:

| What | Figure | Source |
|---|---|---|
| Wave 2 activity | Almost **600 participants** merged **3,000+ PRs** across 200+ repos | [Wave 2 changelog](https://www.drips.network/blog/posts/wave-2-changelog) |
| Q1 2026 activity | **1,000+ new developers** and **30,000+ merged PRs** | [Radworks Q1 2026](https://community.radworks.org/t/drips-org-q1-2026-update/3721) |
| Business | Wave revenue roughly covers Drips' monthly staff costs | [Radworks Q1 2026](https://community.radworks.org/t/drips-org-q1-2026-update/3721) |
| Other partners | None besides Stellar. An Optimism-branded Wave page exists, but no Optimism Wave was found | [optimism.drips.network](https://optimism.drips.network/solutions/wave) |

The rules matter for earners ([Terms & Rules](http://docs.drips.network/wave/terms-and-rules/)):

- You must be **18 or older**.
- People in sanctioned countries are excluded.
- **One account per person.**
- **Points have no fixed money value.** The Association decides the Points-to-money rate.
- There may be a cap per person.
- Part of the pool can go to maintainers.
- Low-quality AI output is banned. Using AI is not banned.

Payouts are "Reward Grants" in USDC on Stellar. You need approved KYC and a Stellar wallet that holds USDC ([withdrawing docs](https://docs.drips.network/wave/withdrawing-rewards/)). One contributor doc says identity checks run through **Sumsub before you can apply to any issue** ([Drips docs](http://docs.drips.network/wave/contributors/solving-issues-and-earning-rewards/)).

**What a typical person earns (estimate):** a $75K pool shared by about 800 contributors gives **about $95 per person per Wave on average**. A third-party guide says the top of the leaderboard earns a few thousand USDC and most people get under $100 ([gigs.sh](https://gigs.sh/p/drips-wave)). Wave is real money, but for most people it pays little per hour.

---

## Group 1: per-contribution platforms for individuals (closest to Drips Wave)

Only Drips Wave and GrantFox (both on Stellar) pay for specific issues out of curated pools. The Talent, Celo, NEAR and AKINDO programs score **your general activity** (GitHub commits plus on-chain use) or **your own app**. They do not pay for fixing someone else's issue. The Web2 bounty start-ups are small and do not show payout data.

### 1a. Basic facts

| Platform | Site link | Launch / public date | Mechanism | Who earns | KYC / eligibility | Reward scale & currency |
|---|---|---|---|---|---|---|
| **Drips Wave (Stellar)** | https://www.drips.network/wave/stellar | Announced 23 Dec 2025; Wave 1 ran 21–31 Jan 2026 | Monthly 7–11-day sprint; curated issues; Points; pro-rata pool | Individuals | Sumsub KYC; 18+; no sanctioned countries; one account | $60K–$75K per Wave; USDC on Stellar |
| **GrantFox (Stellar)** | No own-site URL found. Stellar Community Fund (SCF) listing: https://communityfund.stellar.org/project/grantfox-4zq | 2025 | GitHub-synced issue marketplace and campaigns; escrow through Trustless Work | Individuals | Not found | First two campaigns >$75K; Stellar Summit São Paulo 2026 pool of 10,000 USDC ([SCF](https://communityfund.stellar.org/project/grantfox-4zq), [dev.to](https://dev.to/stellar_nigeria/over-400000-went-to-stellar-contributors-this-year-33jd), [LinkedIn](https://cr.linkedin.com/in/joelvr)) |
| **Merit Systems Terminal** | https://www.merit.systems/ (the Terminal is no longer listed there) | 2 Jul 2025 ([launch post](https://www.merit.systems/blog/launch)) | Repo owners pay chosen contributors for merged PRs; Merit says it handles tax | Individuals (picked by the repo owner) | Not found | Stablecoins; no volume published |
| **BountyHub** | https://bountyhub.dev **[unsure URL]** | First Product Hunt launch 29 Oct 2024; Show HN 5 Jan 2025; **relaunch 8 Jun 2025** | Anyone attaches a bounty to a public GitHub issue (several people can pool money); the poster accepts the claim; unclaimed money is refunded | Individuals | Not found | Currency not stated; 10% fee paid by the bounty creator (2024 listing) ([ossfund](https://ossfund.onrender.com/bountyhub)) |
| **IssuePay** | https://issuepay.app **[unsure URL]** | Show HN 27 Jun 2025 ([HN](https://news.ycombinator.com/item?id=44399096)) | Maintainers or sponsors post bounties on GitHub/GitLab issues; withdraw to a bank account | Individuals | Not found | Fee unclear (a commenter said 50%) |
| **HitCommit** | https://hitcommit.com **[unsure URL]** | Show HN about late 2025 ([HN](https://news.ycombinator.com/item?id=46085012)) | Rewards on GitHub issues | Individuals | Not found | Paid by PayPal or on Stellar |
| **Talent Protocol Builder Rewards** | https://talent.app | 2025 campaigns: Base; WalletConnect 30 Sep–11 Nov 2025; Stacks Dec 2025 and Jan 2026 | Weekly leaderboard based on a "Builder Score" from GitHub and on-chain data | Individuals ("builders") | Builder Score ≥40, Human Checkmark, Basename (Base); compliance checks at payout (Stacks) | Base: 2 ETH/week to the top ~100; WalletConnect: 75K WCT/week to the top 100; Stacks: 5,000 STX (week 1, Dec 2025), 15,300 STX (Jan 2026) ([Talent guide](https://talentprotocol.notion.site/builder-rewards-guide?pvs=4), [WC FAQ](https://docs.talent.app/docs/legal/builder-rewards-faq-walletconnect), [Stacks](https://docs.talent.app/docs/legal/stacks-builder-challenges)) |
| **Celo Proof of Ship** | https://celoplatform.notion.site/Build-With-Celo-Proof-of-Ship-17cd5cb803de8060ba10d22a72b549f8 (program page); docs: https://docs.gap.karmahq.xyz/how-to-guides/partners/celo-proof-of-ship | About early 2025 (round #4 in May 2025) | Monthly contest: judges and AI agents score **your own app** (users, transactions, commits) | App builders / small teams | Talent Human Checkmark, Builder Score, Karma GAP profile | 5K cUSD at first, later 15K cUSD, then 15K CELO + 5K cUSD (round 7), then 20K CELO (round 9) ([PoS 7](https://celo-devs.beehiiv.com/p/proof-of-ship-7-2nd-milestone-checkin), [PoS 9](https://celo-devs.beehiiv.com/p/proof-of-ship-9-2nd-milestone-checkin)) |
| **AKINDO WaveHack** | https://builderboard.notion.site/What-is-AKINDO-1844c0f2a0728042884bef4149887997 (Notion page; main site not found in the notes) | Original launch date not confirmed (probably before 2025); 0G WaveHack announced 12 Aug 2025 | Grants paid out in "waves" to the builders who contribute most | Builders / teams | Not found | 0G WaveHack: $50K pool ([HackerNoon](https://hackernoon.com/lang/ja/0g-launches-wavehack-buildathon-for-ai-developers-on-akindo-with-$50000-grant)) |
| **NEAR Protocol Rewards** | https://github.com/near-horizon/near-protocol-rewards | 2025 (exact date not verified) | Software kit scores GitHub activity (50%) and on-chain activity (50%) each week | Teams | Not found | Weekly tiers from $500 to $2,500 ([docs](https://unpkg.com/near-protocol-rewards@1.1.2/docs/rewards.md)) |

### 1b. Verified facts vs self-reported claims and red flags

| Platform | Verified | Self-reported / red flags |
|---|---|---|
| Drips Wave | Budgets on the primary page; Wave 2 and Q1 2026 activity in Drips' own posts | Points-to-money rate is at Drips' discretion; very high PR counts suggest farming (Drips added captchas and application limits in Wave 2); only Stellar so far; no Wave after 22 Oct listed |
| GrantFox | Listed in the Stellar Community Fund (SCF) | Every figure comes from GrantFox's own team; it calls itself the successor to OnlyDust on Stellar |
| Merit Terminal | $10M seed, Jan 2025, co-led by a16z crypto and Blockchain Capital ([SiliconANGLE](https://siliconangle.com/2025/01/16/merit-systems-raises-10m-create-new-economic-model-called-open-source-capitalism/), [The Block](https://theblock.co/post/335347/merit-systems-raises-10-million-in-round-co-led-by-a16z-crypto-and-blockchain-capital)) | No payout data; homepage now shows only AI-agent payment products; a "legacy2" domain exists ([legacy2](https://legacy2.merit.systems/blog/fundraise)); a critic said companies have "no incentive … to pay for something that's free" ([Garden Research](https://gardenresearch.substack.com/p/garden-research-weekly-recap-9)) |
| BountyHub | Product Hunt #5 of the day, 196 upvotes ([hunted.space](https://webmail.hunted.space/product/bountyhub/launches/bountyhub-2)); app on [GitHub Marketplace](https://github.com/marketplace/bountyhub-app) | No backers, no payout totals; a question about how claims are checked went unanswered; BountyOS showed 1 open bounty ($91) |
| IssuePay | Show HN thread exists | 50% fee mentioned; a "trusted by leading tech companies" claim was removed after users challenged it; Terms links were broken; later pivoted to hiring and "GitHub as CV" ([HN threads](https://news.ycombinator.com/threads?id=Mario10)) |
| HitCommit | Show HN thread exists | 3 points, no traction signal |
| Talent Protocol | Terms published in Talent's docs; Talent's Stacks page showed 508 builders tracked and 318 active (Feb 2026) ([talent.app/stacks](https://talent.app/~/ecosystems/stacks)) | Base pilot "200 builders, 8 ETH, 72% retention" comes from the founder's own post ([paragraph](https://paragraph.xyz/@macedo/my-q1-journey)); scores can be gamed with many commits; pays in tokens; Base campaign may have ended (see conflicts) |
| Celo Proof of Ship | Round pools published in the Celo devs newsletter | Marketed as "earn up to $15k monthly", but that is the whole pool, not one person's pay; rewards your own app, not work on others' OSS; 2026 status unclear |
| AKINDO WaveHack | None independent | ">$250K total grants" in Season 1 is self-reported ([AKINDO](https://akindo.substack.com/p/recapwavehack-global-1st-season)); rewards product building, not always OSS |
| NEAR Protocol Rewards | Nansen reports $200K+ paid to 30+ teams in Q2 2025 ([Nansen](https://research.nansen.ai/articles/near-quarterly-report-q2-2025)) | No current status page; the scoring formula rewards burst activity, which can be gamed (it triggers extra checks) |

Two more ecosystem programs fit only partly. The **Stellar Build Challenge (7th edition)** rewards new contributions to Stellar OSS projects ([Stellar blog](https://stellar.org/blog/announcing-the-7th-stellar-build-challenge)). **Polkadot Bounty 59** pays up to **$30K each** to about 15 individuals or small teams for milestone-based OSS work, with **KYC/KYB required** ([Polkadot forum](https://forum.polkadot.network/t/open-source-developer-grants/11427)). Both work more like grants than pay per PR.

---

## Group 2: dependency and ecosystem funding pays packages, not people

These are the closest match to the original Drips idea of "stream money to your dependency tree". All three pay **projects or package maintainers**, not drive-by contributors.

| Platform | Site link | Launch / public date | Mechanism | Who earns | KYC / eligibility | Reward scale & currency | Verified vs claimed / red flags |
|---|---|---|---|---|---|---|---|
| **ecosyste.ms Funds** (with Open Source Collective) | https://funds.ecosyste.ms | Announced Dec 2024; **generally available 4 Apr 2025**, covering 291 ecosystems ([blog](https://blog.ecosyste.ms/2025/04/04/ecosystem-funds-ga.html)) | A donor picks an ecosystem (a language or framework). Money goes to its critical packages through each project's funding channel (GitHub Sponsors, Open Collective, thanks.dev, etc.) | Projects / maintainers | The project needs a funding channel; 10% fee ([FAQ](https://funds.ecosyste.ms/faq)) | USD. Sentry seed of $67,500; $165,000 from the Linux Foundation, dated Sep 2025 ([OC page](https://opencollective.ecosyste.ms/funders/the-linux-foundation)) | **Reported by the operator:** 375 payments to 136 projects at launch. This is the most "real" new dependency fund found |
| **Deep Funding** | https://deepfunding.org **[unsure URL]**; mechanism page: https://gitcoin.co/mechanisms/deep-funding | 2025 pilot (results due 27 Feb 2025); used in GG24, Oct 2025 | AI models plus a human jury set weights on the Ethereum dependency graph (40K+ edges); GG24 also used Seer prediction markets | Projects / repos | Not stated | Pilot: $170K to projects (the $80K model prizes are an ML competition and out of scope); GG24: ~$350K ([GG24 case study](https://gitcoin.co/case-studies/gg24-first-funding-round-of-gitcoin-3-0)) | Run by Gitcoin and Vitalik Buterin; the final pilot payout list was not found |
| **tea protocol mainnet** | https://tea.xyz/ | Mainnet **scheduled 4 Jun 2026** ([Whale Alert](https://whale-alert.io/stories/f5b301bbd524d6/Tea-protocol-to-launch-mainnet-June-4-and-hold-TEA-token-listing-on-Aerodrome-after-Aerodrome-vote-on-May-28)) | "Proof of Contribution": a teaRank score from 0 to 100 for package maintainers (npm, Homebrew) | Package maintainers | Not found | TEA token; 28% of supply goes to contributor incentives and airdrops ([Bitget](https://www.bitget.com/academy/what-is-tea-protocol-tea-token-presale-september-25-2025)) | Only an AI-written secondary summary says the mainnet launched ([CMC AI](https://coinmarketcap.com/cmc-ai/tea-protocol/latest-updates/)); the **2024 testnet was flooded with spam repos** ([devclass](https://devclass.com/2024/03/04/test-launch-of-tea-open-source-reward-project-clouded-by-repository-spam-attack)); the reward token's price can change a lot |

---

## Group 3: retro and round funding rewards projects you already own

These programs launched or changed in 2025–26. They reward **projects** for impact they already had, or for proposals, using rounds. An individual gains only by owning or maintaining a funded tool.

| Program | Site link | Launch / change date | Mechanism | Who earns | KYC / eligibility | Reward scale & currency | Verified vs claimed |
|---|---|---|---|---|---|---|---|
| **Optimism Retro Funding: Dev Tooling** | https://www.optimism.io/blog/retro-funding-2025 ; mission rules: https://gov.optimism.io/t/retro-funding-dev-tooling-mission-details/9598 | 2025: changed from yearly rounds to monthly algorithmic rewards. Season 7 ran 5 Feb–31 Jul 2025; Season 8 runs from Aug 2025 | Open Source Observer (OSO) metrics from GitHub, npm, crates and on-chain data; a package must be imported by at least 3 verified Superchain builder projects | Projects | Application | S7: up to 8M OP; S8: see conflicts table | **Verified (foundation-reported):** 6.6M OP to 97 of 242 applicants by Jul 2025; top recipients include Ethers, Hardhat, OpenZeppelin and Viem ([gov forum](https://gov.optimism.io/t/season-7-retro-funding-early-evidence-on-developer-tooling-impact/10162)) |
| **Algorand xGov retroactive proposals** | https://algorand.co/blog/algorand-xgov-update-now-accepting-retroactive-proposals | xGov mainnet Aug 2025; retro proposals accepted from **1 Oct 2025** | Proposals for work already delivered, voted on by xGovs | Projects or individual proposers | **Open-source licence only** ([guide](https://forum.algorand.co/t/xgov-beta-xgov-guide-2025/14703/1)) | 2026 budget of 3M ALGO ([announcement](https://forum.algorand.co/t/xgov-mainnet-announcement/14812)); a 500K ALGO cap was discussed | Outcomes not found |
| **Filecoin ProPGF** | https://filecoin.io/blog/announcing-filecoin-propgf-batch-2-general-track | Batch 1 in 2025; Batch 2 applications 12 Nov–23 Dec 2025, payouts Feb 2026 | Committee-reviewed grants paid by milestone | Teams | Application | Batch 1: **$3.68M to 14 teams** (**verified** results post: [Filecoin blog](https://filecoin.io/blog/filecoin-propgf-batch-1-36m-awarded-to-ecosystem-builders)); Batch 2: $4M | Filecoin's separate RetroPGF (580k+ FIL) ran on Drips; RPGF-4 is planned on Drips |
| **Avalanche Retro9000** | https://www.avax.network/about/blog/the-avalanche-foundation-announces-third-cohort-for-retro9000-l1-and **[unsure URL, may be cut short]** | Launched Nov 2024; first snapshot 15 Apr 2025; third cohort 2 Dec 2025; C-Chain round early 2026 (sources disagree on the date) | Retroactive grants based on impact snapshots | Teams | **KYC/KYB required** | 3rd cohort: 4 grantees, >$140K; >$1.25M in total (press) ([AOL](https://www.aol.com/finance/avalanche-kicks-off-c-chain-193554725.html)) | Foundation blog reports cohorts; the total comes from press only |
| **Gitcoin GG24** | https://gitcoin.co/campaigns/gitcoin-grants-24-gg24 | 14–28 Oct 2025, the first "Gitcoin 3.0" round | Several mechanisms across 6 "domains": quadratic funding (QF) on Giveth, Deep Funding, and others | Projects | Curated projects; anti-Sybil checks | ~$1.8M in total; OSS QF: $300K matching to 64 projects from 1,286 donors ([Giveth retro](https://gitcoin.co/case-studies/gg24-oss-qf-giveth-retrospective)) | A 2026 proposal to turn Grants into a single "d/acc" campaign is **unconfirmed** ([forum](https://gov.gitcoin.co/t/proposal-gitcoin-d-acc-2026-funding-initiative-restructuring-the-grants-program/25157)) |

---

## Group 4: maintainer funds and fellowships are the Web2 growth area

In 2025–26 no new Web2 copy of Drips appeared. New Web2 money went into **curated grants and salaried "fellow / maintainer-in-residence" roles**. These suit people who already maintain important software.

| Program | Site link | Launch / public date | Mechanism | Who earns | Eligibility | Scale & currency | Verified vs claimed / red flags |
|---|---|---|---|---|---|---|---|
| **Sovereign Tech Fellowship** (Germany) | https://www.sovereign.tech/news/2026-fellowship-applications-open | 2025 pilot; 2026 round closed **6 Apr 2026** | Paid one-year fellowship | **Individuals**: maintainers; from 2026 also community managers and technical writers | Competitive; work must be on critical technology | Stipend amount not found; **6 fellows in 2025, 14 in 2026** ([2026 fellows](https://www.sovereign.tech/news/meet-the-2026-sovereign-tech-fellows)); the agency's separate maintenance contracts start at €50,000 ([Help Net Security](https://www.helpnetsecurity.com/2026/07/16/open-source-projects-funding-impact/)) | **Verified:** fellows were paid. Public money, high credibility |
| **HeroDevs Open Source Sustainability Fund** | https://www.herodevs.com/sustainability-fund | 23 Jun 2025 ([press release](https://www.herodevs.com/blog-posts/herodevs-launches-20-million-sustainability-fund-for-open-source-creators-to-secure-end-of-life-software)) | Grants to maintainers of widely used projects | Maintainers / projects | Must follow end-of-life (EOL) best practices | **$20M fund; $2,500–$250,000 per grant**; USD | **Claimed only**, no independent payout tally. Conflict of interest: the EOL rules feed HeroDevs' paid support business |
| **Rust Foundation Maintainers Fund** | https://blog.rust-lang.org/2026/06/02/launching-the-rust-foundation-maintainers-fund/ | Announced Nov 2025 ([The Register](https://www.theregister.com/2025/11/05/rust_foundation_announces_maintainers_fund/)); launched 2 Jun 2026 | New Funding team plus a "Maintainer in Residence" program | Individual Rust maintainers | Through the Rust project's own process | Size not stated; still fundraising | First hire still pending in June 2026 |
| **Open Source Endowment** | https://endowment.dev | Founded 14 Feb 2025; launched publicly late Feb 2026 ([TechCrunch](https://techcrunch.com/?p=3096506)) | Donations are invested; only the returns (~5%/yr) are given out as grants | Projects (widely used, nonprofit or independent) | "Value–Risk" selection framework | Site shows **$765K and 120 donors**. That gives only about **$38K a year** to grant (our estimate) | Backers include Thomas Dohmke and Mitchell Hashimoto. **No grants confirmed paid**, although the first round was due in Q2 2026. FOSS Force asks whether an endowment helps projects that need cash now ([FOSS Force](https://fossforce.com/2026/03/can-the-open-source-endowment-fix-what-years-of-neglect-broke/)) |
| **GNOME Foundation Fellowship** | https://blogs.gnome.org/foundation/?p=20106 | 2026; first two fellows start Jul 2026 ([OSS Funded #12](https://buttondown.com/ossfunded/archive/2026-06-15/)) | Paid fellowship | Individuals | Selected by the foundation | Amount not stated | Named recipients are public |
| **Linux Foundation grant pool** (Alpha-Omega / OpenSSF) | https://linuxfoundation.org/press/linux-foundation-announces-12.5-million-in-grant-funding-from-leading-organizations-to-advance-open-source-security | 17 Mar 2026 | Grants to give maintainers more capacity against floods of AI-generated vulnerability reports (not bug bounties) | Projects / organisations | Chosen by the grant program | **$12.5M**, funded by Anthropic, AWS, GitHub, Google, Microsoft and OpenAI | Greg Kroah-Hartman said money alone won't fix the problem ([Help Net Security](https://www.helpnetsecurity.com/2026/03/17/linux-foundation-12-5-million-grants/)) |

**Credit-only programs (not cash).** Several AI labs and cloud companies launched maintainer programs that give **subscriptions or credits, not money**:

| Program | Site link | Date | What you get | Eligibility |
|---|---|---|---|---|
| Anthropic "Claude for Open Source" | No official URL in the notes (reported by [The New Stack](https://thenewstack.io/openai-anthropic-open-source/)) | 27 Feb 2026 | 6 months of Claude Max, capped at 10,000 people | Reportedly about 5K+ GitHub stars or 1M+ npm downloads |
| OpenAI "Codex for Open Source" | https://openai.com/form/codex-for-oss/ | Mar 2026 | 6 months of ChatGPT Pro, Codex Security access and API credits from a $1M fund; up to $25K per project according to a third-party guide | Maintainers (application form) |
| Vercel Open Source Program | https://vercel.com/open-source-program | Apr 2025; quarterly groups of projects | $3,600 in Vercel credits | Selected projects |
| UK Open-Source AI Builder Fund | https://www.gov.uk/government/news/new-backing-for-open-source-ai-builders-data-centre-design-challenge-and-robotics-partnership | 2026 | More than £500K in compute plus mentoring | Organisations |

---

## Group 5: prototypes and unverified "pay-on-merge" projects

In 2025–26, a crypto escrow contract that pays when a PR is merged became a common **hackathon template**. **None of the projects below shows verified payout volume.** Treat them as experiments, not income sources.

| Name | Site link | Chain / status | What it claims |
|---|---|---|---|
| MergePay | https://mergepay.fun/ | Arc; the site says "live on Arc mainnet"; built by one developer | Anyone can lock USDC on a GitHub issue; a contract checks GitHub's signed merge proof and pays the author of the merged PR; no platform fee, about $0.016 gas per award |
| PullPay | https://github.com/irham3/pullpay (demo: https://pullpay-sigma.vercel.app **[unsure URL]**) | Optimism; 1 star, looks like a hackathon project | USDC escrow per issue; UMA oracle settles disputes |
| MergeReward | https://chain.link/hack-26/projects/mrewards | Chainlink hackathon | Pays on a verified merge: 95% to the developer, 5% to the protocol |
| Kudoz | https://github.com/token2049-decentralizing/core | Solana; hackathon project | Sponsor campaigns; merged PRs checked by AI and CI get paid |
| vGrant | https://github.com/b3ww/ethglobal | ETHGlobal hackathon | A vault pays the first valid merged PR |
| claudelance | No public URL found (seen under https://github.com/topics/bounty-marketplace) | Celo | AI coding agents solve GitHub bounties for cUSD/CELO/USDC |
| Githoney (TxPipe) | https://lidonation.com/en/proposals/githoney-by-txpipe-good-first-issue-program-f13 | Cardano test network; a 2026 work plan exists ([Intersect](https://committees.docs.intersectmbo.org/intersect-open-source-committee/about/paid-open-source-model-posm/bug-bounty-program/tx-pipe-contract-githoney)) | GitHub bot plus on-chain bounties; its F13 funding request got ₳0 of ₳199,943 |
| GitCash | https://ethglobal.com/showcase/gitcash-2avdg | ETHOnline 2025 hackathon | Repo vaults in PYUSD that pay out on merged PRs |
| OpenWave | https://ethglobal.com/showcase/openwave-a8rs5 | ETHGlobal hackathon | Smart-contract bounty extension |
| GITHUNDER | https://ethglobal.com/showcase/githunder-7rn9f | ETHGlobal hackathon | Smart-contract bounty extension |
| Aigen Protocol | No public URL found | Token | 50 AIGEN per PR (anecdote only, [dev.to](https://dev.to/zeroknowledge0x/the-open-source-money-map-every-way-developers-are-actually-making-money-in-2026-with-real-45ba)) |
| MergeOS | No public URL found | Token | 300 MRG per PR verification; the token's price later fell (same dev.to source) |

Similar items: Code Bounty (https://www.codebounty.org/, the site showed no content when fetched) and agent-bounties (https://github.com/zhumeiyan/agent-bounties, a bounty network for AI agents). Paying per PR in a project's own token is a **red flag**: the token's price can collapse, and these schemes attract farmed PRs.

---

## Group 6: what changed for older platforms in 2025–26

| Platform | Site link | 2025–26 status change |
|---|---|---|
| OnlyDust | https://app.onlydust.com/my-dashboard/rewards | Its dashboard says it is "transitioning to our new platform for all open source projects" and asks users to **withdraw pending rewards** ([OnlyDust](https://app.onlydust.com/my-dashboard/rewards)). In 2025 it opened up to non-Web3 OSS. The new platform's name was not found. It used to claim $11M+ paid to 10K developers (self-reported) |
| Gitcoin Grants Stack | https://gitcoin.co | Gitcoin Labs wound down in Apr 2025, and **Grants Stack has not been maintained since 31 May 2025** ([The Block](https://www.theblock.co/post/352055/ethereum-public-goods-funding-protocol-gitcoin-winding-down-its-software-division)). Gitcoin now runs "Gitcoin 3.0" rounds (GG24) |
| IssueHunt | https://issuehunt.io **[unsure URL]** | Listed as discontinued for OSS, with no social activity since 2019 ([AlternativeTo](https://alternativeto.net/software/issuehunt/about)). The company is now described as a security bug-bounty platform ([Dealroom](https://ai-startups.dealroom.co/companies/issuehunt)) |
| Algora | https://algora.io | Still live. **11% fee** (19% for community organisations); payouts take 3–8 days ([pricing](https://console.algora.io/pricing)). BountyOS showed 0 open bounties on 2026-10-28 |
| Polar.sh | https://docs.polar.sh/issue-funding | Issue funding is still in the docs; fee is now 4% + 40¢ ([FAQ](https://docs.polar.sh/support/faq)). The focus has moved to merchant-of-record billing (our inference) |
| Opire | https://github.com/opire | Still listed; developers get 100% of the reward; a 2024 listing gives a 4% fee plus Stripe fees ([ossfund](https://ossfund.onrender.com/opire)) |
| FLOSS/fund (Zerodha, India) | https://floss.fund/ | Launched Oct 2024; $1M/yr. Tranche 1 (May 2025): $325K to 9 projects. Tranche 2 (Oct 2025): $675K to about 30 projects. **Only about $195K had been paid by Oct 2025 because of cross-border payment problems** ([The DropTimes](https://www.thedroptimes.com/node/55345)) |
| GitHub Secure Open Source Fund | https://github.blog/open-source/maintainers/what-50-open-source-projects-taught-us-about-security-in-the-ai-era/ | $10K per project; **$1.88M paid to 188 projects** by Aug 2026; Session 5 closed 24 Aug 2026. Maintainers must be in regions GitHub Sponsors supports |
| GitHub Sponsors | https://github.com/sponsors **[common URL, not cited in notes]** | **Passed $100M paid out** (Jul 2026), about 70K maintainers, 103 regions; self-reported ([Help Net Security](https://www.helpnetsecurity.com/2026/07/21/open-source-github-sponsors-100-million/)) |
| Open Source Pledge | https://opensourcepledge.com | Companies pay $2,000 per developer per year; **$7.42M paid by 37 members** in total (self-reported) ([Sentry](https://blog.sentry.io/another-year-another-1-000-000-to-open-source-maintainers/)) |
| thanks.dev | https://thanks.dev **[common URL, not cited in notes]** | Canonical gave $10K/month for 12 months, reaching 350+ projects ([Canonical](https://canonical.com/blog/canonical-thanks-dev-giving-back-to-open-source-developers)); Sentry routed $495K through it. Fee reports conflict (5% commission vs a voluntary tip) |
| NLnet / NGI Zero | https://nlnet.nl/news/2026/20260612-NGIZero-stocktaking.html | **Paused most open calls on 12 Jun 2026** after funding 1,215 projects. Three new "Open Internet Stack" programmes (Restack, CodeSupply, ELFA) are planned after summer 2026 |
| Outreachy | https://www.outreachy.org | Less money. Since Dec 2025 the communities themselves pay for the internships, and the May 2026 group ran with reduced funding ([Outreachy](https://www.outreachy.org/blog/2026-02-06/may-2026-call-for-mentoring-organizations/)) |

Smaller notes: Tidelift (bought by Sonar) still pays "lifters" ([Sonar](https://www.sonarsource.com/open-source-maintainers)). The Stellar Community Fund v7 now pays team awards of up to $150K in XLM ([SCF v7](https://stellar.org/blog/ecosystem/introducing-scf-v7)). Open Collective is being turned into a general fiscal host ([update](https://opencollective.com/commonunity/updates/open-collective-refresh)).

---

## Where the notes disagree, and how we resolved it

| Topic | Conflict | Resolution |
|---|---|---|
| **Drips Wave totals** | $705K (sum of budgets on the page) vs **$255K** "disbursed Jan–Apr" (gigs.sh) vs **"$400K+ distributed"** (Drips) | The figures fit together. Waves 1–4 budgets add up to exactly $255K. Waves 1–6 add up to $405K, which matches "$400K+" around July 2026. $705K is all 10 posted budgets, a plan rather than confirmed payouts. One note said pool sizes were "not published"; in fact the Stellar page lists them |
| **Drips Wave issues / repos** | "50K+ issues resolved, 200+ repos" vs page counters of 372,399 issues and 842 repos | Probably different things: the counters seem to count indexed issues, not solved ones. Different dates explain the rest. Use the smaller "resolved" figure |
| **Drips Wave points** | 100/150/200 from a third-party guide only | Confirmed: Drips' own contributor docs give Trivial 100 / Medium 150 / High 200. The conversion to money is still at Drips' discretion |
| **Drips Wave KYC timing** | KYC "to withdraw" vs Sumsub "before applying to any issue" vs "may be required" (Terms) | Plan to finish KYC **before you start**. The contributor docs, the strictest source, require it |
| **Drips Wave length** | "One week" vs "~10 days" | The page shows 11 days for Wave 1 and 7–8 days for later Waves |
| **Optimism Season 8 budget** | Budget Board proposal: up to 20M OP (8M for dev tooling) vs vote page: Dev Tooling "up to 3.65M OP", Onchain Builders up to 1.35M OP | The 20M figure was a **proposed ceiling**. The vote page comes later in the process, so **3.65M OP for Dev Tooling is the more likely real budget**. We did not confirm the final adopted figure |
| **Merit Systems status** | Launch post (Jul 2025) and docs describe paying GitHub contributors vs the Oct 2026 homepage, which lists only AI-agent payment products | Treat the Terminal as **no longer a main product** (probably a pivot). We found no announcement, so this is our inference from the homepage. Do not plan income around it |
| **BountyHub launch date** | Oct 2024 vs Jan 2025 vs Jun 2025 | **First launch: Oct 29, 2024** (Product Hunt). Show HN: Jan 5, 2025. **Public relaunch: Jun 8, 2025.** It counts only as a 2025 relaunch |
| **Talent / Base status** | Base docs still advertise 2 ETH/week vs a third-party issue (Jul 2026) saying the Base campaign ended on 31 Jan 2026 | Unresolved. **Assume it is not running** until Talent's own page shows a live campaign |
| **OnlyDust** | "No pivot news found" (one note) vs its dashboard saying it is "transitioning" and an SCF listing saying it is leaving Web3 | Primary evidence wins: OnlyDust is **in transition**, and users are asked to withdraw rewards |
| **GG24 OSS project count** | 64 vs 55 projects | 64 = Dev Tooling plus Interop QF rounds together; 55 = Dev Tooling only |
| **Open Source Endowment size** | ~$700K / 60+ donors (launch) vs $765K / 120 donors (site) | The fund grew between those dates; this is not a real conflict |
| **BountyOS snapshot** | 155 bounties / $68,771 (30 Sep 2026) vs **2 bounties / $101** (28 Oct 2026) | Probably a filter change or a broken scraper. Both say the same thing: open bounty money is small and spread thin |

---

## Warning: fake bounty repos and a thin bounty market

The open issue-bounty market became **less attractive** in 2025–26.

- **Very few open bounties.** On 28 Oct 2026, BountyOS covered Algora, Opire, IssueHunt, BountyHub and TaskBounty. It counted **2 open bounties worth $101**. It says it filters out honeypots, dead repos and bot-farmed listings ([BountyOS](https://bountyos.rovidev.com/en/github-bounty-board/)).
- **Fake bounty repos.** One developer ran an AI bounty-hunting agent for 96 hours: 240+ PRs, 72 merged, and **$500–800 earned** (self-reported). He warned that **most bounty listings are scam repos** that create fake bounty issues to attract automated PRs ([dev.to](https://dev.to/zeroknowledge0x/i-let-an-ai-agent-hunt-open-source-bounties-for-96-hours-heres-the-brutal-truth-about-what-42p3)). Another writer found mostly ecosystem credits, not cash ([dev.to](https://dev.to/hermesxclawctrl/i-let-my-ai-agent-hunt-bounties-for-48-hours-heres-what-it-actually-found-4c5p)).
- **Unpaid crypto bounties.** An undated review of 23 crypto bounty programs said **4 were scams**: PRs were merged but never paid ([dev.to](https://dev.to/hopkins_jesse_cdb68cfa22c/i-reviewed-23-crypto-bounty-programs-so-you-dont-have-to-261f)).

Our reading: floods of AI-written PRs pushed money towards **curated pools with identity checks** (Drips Wave, Talent). That is why the programs that still work ask for KYC, human checks, captchas and application limits.

**Before you work on any bounty, check four things:**

1. Is the repo old, with real users?
2. Has the maintainer paid bounties before?
3. Is the money already locked in escrow?
4. Does the bounty pay in a stable currency, not a new token?

---

## Coverage gaps: what this research could not see

- **Little independent checking.** Almost every money figure here comes from the operator: Drips, GrantFox, Talent, AKINDO, HeroDevs, Open Source Pledge, GitHub Sponsors. Independently checked payouts are rare. The best are Optimism's results post, Filecoin's Batch 1 post, the Sovereign Tech Fellowship and GitHub SOSF.
- **Missing details:**
  - No fees, KYC rules or payout totals were found for any 2025–26 Web2 bounty start-up.
  - Unknown: whether Drips Wave continues after Wave 10, or adds a non-Stellar partner.
  - Unknown: whether the tea mainnet launched and pays.
  - Not found: the name of OnlyDust's new platform.
  - Not found: grant results from the Open Source Endowment and HeroDevs.
- **Not searched:**
  - Crypto ecosystems: Aptos, Sui, Cosmos, Cardano Catalyst, ICP, zkSync, Scroll, Monad, Arbitrum, Ethereum Foundation and Solana OSS programs.
  - Other platforms: Superteam Earn, Gitpay, Bountycaster, Ubiquity DevPool, DoraHacks, Gitee GVP and OpenAtom.
  - Government OSS funds in France, Japan, India and Switzerland.
  - Searches in Korean and Spanish found very little.
- **Not finding something is not proof it does not exist.** Product Hunt cannot be searched by date, so some 2026 launches may be missing.

---

## Practical guidance: what an individual developer can join today

| Option | Can you join today (28 Oct 2026)? | How |
|---|---|---|
| **Drips Wave (Stellar)** | Account: yes. Earning: only when a Wave is open; none is listed after Wave 10 (15–22 Oct) | Sign up at https://www.drips.network/wave/stellar, finish Sumsub KYC, connect GitHub, set up a Stellar wallet that holds USDC, and watch for Wave 11. Pick fewer, harder issues (200 points) rather than many trivial ones, and never send untested AI code |
| **GrantFox (Stellar)** | Probably, through campaigns | Look for its campaigns through the Stellar Community Fund listing and Stellar community channels; check that funds are in escrow |
| **GitHub Sponsors** | Yes, if your region is supported | Turn on Sponsors for your profile or project. It is also needed for the GitHub Secure Open Source Fund (Session 5 closed in Aug 2026; watch for the next one) and helps ecosyste.ms Funds pay you |
| **ecosyste.ms Funds / thanks.dev** | Yes, passively, if you maintain a used package | Add a funding channel (Sponsors, Open Collective) to your package so dependency money can reach you |
| **FLOSS/fund** | Yes, if you own a project | Add a `funding.json` file to your project and apply at https://floss.fund/. Expect slow international payments |
| **Algora / Opire / BountyHub / Polar** | Yes, but there is very little work | Use them only on known repos with escrowed money; Algora takes an 11% fee |
| **Talent Protocol campaigns** | Only when a campaign is live | Build a talent.app profile, reach Builder Score ≥40 and get the Human Checkmark. Rewards are in tokens (ETH, WCT, STX) |
| **Celo Proof of Ship / NEAR / AKINDO** | Only if you build an app on that chain | They reward your own product, not fixes to other people's issues |
| **HeroDevs fund** | Yes, if your project is widely used | Publish an end-of-life policy and apply at https://www.herodevs.com/sustainability-fund |
| **Optimism Retro / Algorand xGov / Filecoin ProPGF** | Yes, if you own a dev tool used in that ecosystem | Apply as a project; payouts go to the project, usually in tokens |
| **Sovereign Tech Fellowship / GNOME / Rust fund** | No open call right now (2026 rounds closed) | Watch for the 2027 calls; these are paid roles with few places |
| **NLnet / NGI Zero** | Mostly paused | Wait for the new Open Internet Stack programmes |
| **AI-lab credits** (Anthropic, OpenAI, Vercel) | Yes, if eligible | Free tools, **not money** |

**Avoid** programs that pay per PR in their own new token (Aigen, MergeOS), and repos with no history that post large bounties.

---

## Conclusion

In 2025–26 the "get paid per contribution" model did not grow as an open market. It moved into **funded, gated pools**. Drips Wave works because one sponsor (Stellar) pays for each Wave up front, and because KYC and curated issues keep out the AI spam that is hurting open bounty boards. This makes income depend on one ecosystem's marketing budget, which can stop at any time. Wave already has no announced Wave 11, and Talent's Base campaign may have ended. Merit's apparent pivot, which is the strongest negative signal, suggests that even well-funded start-ups could not get companies to pay contributors directly.

For a developer, the long-term money is now on the **maintainer side**: GitHub Sponsors passed $100M, there are new fellowships and funds, and dependency routing pays package owners. Contributor-side income stays small and campaign-based. The best plan is to treat Wave-style sprints and bounties as **small, irregular extra income**. Steady earnings come from owning or maintaining a package that others depend on, because that is where grants, dependency funds and retro rounds now send their money.
