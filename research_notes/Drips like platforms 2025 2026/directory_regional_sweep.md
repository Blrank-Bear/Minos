# Drips-like OSS contributor-earning platforms launched 2025-2026: directory, launch-site and non-English sweep

Scope: Product Hunt, Show HN, awesome lists, accelerators/fundraises, plus Chinese, Japanese, Korean, Portuguese/Spanish and Indian sources. Already-known platforms are skipped (Drips, Gitcoin, OnlyDust, Algora, Opire, IssueHunt, Polar, thanks.dev, Tidelift, GitHub Sponsors, Open Collective, tea.xyz). About 30 tool calls were used. Searches ran 2026-10-28.

## Q1: New launches found on launch sites and directories (Product Hunt, Show HN, awesome lists)

### Takeaway
Product Hunt and Show HN produced two small new issue-bounty marketplaces: BountyHub (Product Hunt, June 2025) and IssuePay (Show HN, June 2025). Both are thin, self-reported products with no verified payout data, and IssuePay drew significant red flags. The awesome/funding lists are stale and list nothing from 2025-2026.

### Cited Findings
**BountyHub (bountyhub.dev)**
- Launched on Product Hunt on June 8, 2025: 196 upvotes, 14 comments, #5 Product of the Day. Tagline: "Crowdfunding GitHub issues made easy." — [Product Hunt mirror (hunted.space)](https://webmail.hunted.space/product/bountyhub/launches/bountyhub-2)
- How it works: users attach bounties to public GitHub issues and a bot comments to alert developers. A solver submits a PR and claims the bounty, and the poster accepts or rejects the claim in a dashboard. Unclaimed bounties can be retracted for a refund. — [ossfund directory](https://ossfund.onrender.com/bountyhub); [maker's dev.to post](https://dev.to/omarsoufiane/monetizing-github-issue-resolutions-with-bountyhub-3517)
- Several users can pool funds on one issue, and the solver gets the full pot. — [dev.to](https://dev.to/omarsoufiane/crowdfunding-open-source-projects-with-bountyhub-2hp1)
- Fee (claimed, directory listing last updated Sep 2024): 10% platform fee plus processing, paid by the bounty creator on top of the bounty. — [ossfund directory](https://ossfund.onrender.com/bountyhub)
- The launch date is disputed. One aggregator lists an earlier campaign on Oct 29, 2024, so June 2025 may be a relaunch. — [Innolope PULSE](https://innolope.com/pulse/startups/6915ab49f915b3ab4c71cbdd)
- A Product Hunt commenter asked how claims are validated. The page has no answer, and it lists no backers and no payout totals. — [hunted.space](https://webmail.hunted.space/product/bountyhub/launches/bountyhub-2)

**IssuePay (issuepay.app)**
- "Show HN: IssuePay – Get paid for open-source contributions," posted June 27, 2025 by user Mario10. — [HN 44399096](https://news.ycombinator.com/item?id=44399096)
- How it works: maintainers or "sponsors" (companies, users) post bounties on GitHub/GitLab issues. Contributors merge code, get paid and withdraw to a bank account. A premium tier gives priority in a "Job Offers" section. — [HN 44399096](https://news.ycombinator.com/item?id=44399096)
- Red flags: a commenter called out a 50% platform fee, and the founder said pricing was being "reevaluated." A "Trusted by leading tech companies" claim was removed after a challenge ("Name one."). Footer, Terms and Privacy links were broken, and a question about payout reliability went unanswered. — [HN 44399096](https://news.ycombinator.com/item?id=44399096)
- It later pivoted toward hiring. Follow-up Show HN posts: "Make Your GitHub Account Your CV" (~Sep 12, 2025), "Helping Companies Turn Open Source Contributions into Hiring," and a "Job Score" browser extension. — [Mario10 HN threads](https://news.ycombinator.com/threads?id=Mario10)

**Directories and awesome lists**
- nayafia/lemonade-stand has no dated or recently added entries. Its newest references date from 2019. — [lemonade-stand](https://github.com/nayafia/lemonade-stand)
- BRUNOSolutions/awesome-oss-funding lists only established platforms (Gitcoin, Bountysource, IssueHunt, Sponsors, Open Collective). Its last-update date was not checked. — [awesome-oss-funding](https://github.com/BRUNOSolutions/awesome-oss-funding)
- ralphtheninja/open-funding was last pushed 2021-12-26. — [search summary referencing repo](https://github.com/topics/funding)
- bounty-radar (2026) is an open-source CLI, not a marketplace. It aggregates Algora bounties plus GitHub bounty labels and title keywords. Its sample output shows a $10k bounty issue created 2026-03-30, and it does not index any newer bounty platform. — [bounty-radar](https://github.com/JuanM94/bounty-radar)
- PayDevs ("Spotify for OSS libraries," on Product Hunt) is about four years old, so it is out of scope. — [Product Hunt](https://www.producthunt.com/p/paydevs/paydevs)

### Inferences
- Launch sites show a long tail of small issue-bounty clones (BountyHub, IssuePay) with no backers and no verified payouts. None comes close to the stream or wave model of Drips.
- That bounty-radar indexes only Algora plus generic labels suggests no new bounty marketplace gained traction in 2025-2026.

### Gaps
- No Product Hunt or Show HN launch in 2026 matching "fund maintainers" or "pay contributors" was found. Product Hunt cannot be searched by date through this tooling.
- No verified payout totals for BountyHub or IssuePay. IssuePay's current fee and whether it still runs are unknown.

## Q2: Accelerator- and VC-backed OSS-funding startups and mechanisms (2025-2026)

### Takeaway
The strongest new entries found this way are Merit Systems (a16z crypto, $10M seed, Jan 2025), Ecosystem Funds by ecosyste.ms and Open Source Collective (generally available Apr 2025, dependency-graph funding with verified payouts), and the Open Source Endowment (launched early 2026, first grants planned Q2 2026). No YC-batch company focused on OSS funding turned up.

### Cited Findings
**Merit Systems (merit.systems)**
- $10M seed in January 2025, co-led by a16z crypto and Blockchain Capital. Founders: Sam Ragsdale, Ryan Sproule, Mason Hall. — [The Block](https://www.theblock.co/post/335347/merit-systems-raises-10-million-in-round-co-led-by-a16z-crypto-and-blockchain-capital); [Merit blog](https://www.merit.systems/blog/fundraise)
- Pitch: an attribution protocol that rewards contributors in proportion to the value they create. Product: a "Terminal" that lets repo owners pay contributors straight from a repo, with no tax-form paperwork (claimed). — [Blockchain Capital](https://blockchaincapital.com/blog/merit-a-new-economy-for-open-source); [Merit docs](https://www.merit.systems/docs)
- Skeptical commentary: "no incentive for companies to pay for something that's free by design." — [Garden Research](https://gardenresearch.substack.com/p/garden-research-weekly-recap-9)
- A `legacy2.merit.systems` domain exists, which suggests the product or site was reworked. — [legacy2.merit.systems](https://legacy2.merit.systems/blog/fundraise)

**Ecosystem Funds (funds.ecosyste.ms), from ecosyste.ms and Open Source Collective**
- Generally available April 4, 2025, covering 291 open-source ecosystems (announced late 2024). Seed commitment: $67,500 from Sentry to the Rust, Python, Django and JS ecosystems. — [ecosyste.ms blog](https://blog.ecosyste.ms/2025/04/04/ecosystem-funds-ga.html)
- Verified (self-reported) payouts: more than 80% of funds went out in 375 payments to 136 projects at GA. Payouts route through GitHub Sponsors, thanks.dev, StackAid, LF Community Bridge or Open Collective. Management fee is 10%. — [ecosyste.ms blog](https://blog.ecosyste.ms/2025/04/04/ecosystem-funds-ga.html)
- An Open Collective funder page shows $165,000 from The Linux Foundation to Ecosyste.ms dated Sep 26, 2025. — [opencollective.ecosyste.ms](https://opencollective.ecosyste.ms/funders/the-linux-foundation)
- Mechanism: dependency-graph funding, closest in spirit to Drips dependency splits. Payments go to projects, not individual contributors.

**Open Source Endowment (OSE)**
- Launched early 2026 as a US 501(c)(3). It invests donations and pays out only the returns, about 5%/yr. About $700K from more than 60 founding donors, including leaders from HashiCorp, Nginx, curl and Vue.js. — [OpenSourceForU (Feb 2026)](https://www.opensourceforu.com/2026/02/worlds-first-oss-endowment-backs-maintainers-with-investment-income/); [Linuxiac](https://linuxiac.com/open-source-endowment-launches-to-fund-critical-foss-infrastructure/)
- Grants go to widely used nonprofit or independent projects, selected through a "Value–Risk" framework. The first grant round was planned for Q2 2026, and no funded projects were confirmed in the sources found. — [Linuxiac](https://linuxiac.com/open-source-endowment-launches-to-fund-critical-foss-infrastructure/); [Open Source Pledge blog](https://opensourcepledge.com/blog/welcoming-the-open-source-endowment)

**YC**
- No YC 2025-2026 company with OSS contributor funding as its core product was found. The search only surfaced YC companies that use Algora bounties (Keep W23, Trigger.dev W23). — [Algora testimonials](https://algora.io/testimonials)

### Inferences
- Ecosystem Funds is the most Drips-like new mechanism found here (dependency-weighted, multi-channel payouts, real disbursements). Its recipients are projects, not individual developers.
- Merit Systems is the best-funded new startup, but the sources show no traction data. Its current product direction needs a check (the legacy domain hints at a pivot).

### Gaps
- Merit Systems traction, payout volume and current product could not be found (a search for a pivot returned nothing relevant).
- No RootData or Crunchbase scan for other 2025-2026 OSS-funding raises fit the budget.
- OSE first-round grant results (planned Q2 2026) were not found.

## Q3: Crypto-ecosystem contributor rewards, waves and retro funding (2025-2026)

### Takeaway
The closest analogues to Drips "Waves" in 2025 are ecosystem builder-reward programs: Optimism Dev Tooling Retro Funding (monthly, metric-based, 6.6M OP paid by July 2025), Ethereum Deep Funding (AI plus jury dependency weights, ~$170K to deps), Talent Protocol Builder Rewards (weekly, sponsor-funded, partly GitHub-scored), Celo Proof of Ship (monthly), and AKINDO WaveHack (a Japanese company, wave-based grants). Hackathon prototypes (GitCash, OpenWave, GITHUNDER) and TxPipe Githoney (Cardano) are pre-launch or unfunded.

### Cited Findings
**Optimism Retro Funding, Dev Tooling (Season 7, 2025)**
- Budget of up to 8M OP. Ran Feb 5 – Jul 31, 2025, with monthly rewards from March. Impact was measured algorithmically from GitHub, npm, Crates and onchain data. Packages had to be imported by at least 3 verified Superchain builder projects. — [Optimism gov forum](https://gov.optimism.io/t/retro-funding-dev-tooling-mission-details/9598); [Optimism blog](https://www.optimism.io/blog/retro-funding-2025)
- Verified (foundation-reported): 6.6M OP awarded by July 2025. 97 of 242 applicants were rewarded, with top recipients Ethers, Hardhat, OpenZeppelin, Solidity and Viem. — [Optimism gov forum (early evidence)](https://gov.optimism.io/t/season-7-retro-funding-early-evidence-on-developer-tooling-impact/10162)

**Ethereum Deep Funding (deepfunding.org / Gitcoin)**
- Pilot sponsored by Vitalik Buterin: ~$170K to Ethereum dependency-graph projects weighted by AI models. The graph is seeded from client repos and extends two hops (more than 40,000 edges). Model prizes were $40K + $40K, or "$80k" in a later guide. Models were scored against human jurors (via Kaggle). Sources disagree on the amounts. — [Gitcoin Deep Funding](https://gitcoin.co/mechanisms/deep-funding); [Gitcoin visual guide](https://gitcoin.co/research/deep-funding-visual-guide); [Ethereum Magicians](https://ethereum-magicians.org/t/model-submissions-for-ethereum-deep-funding/24200)
- Note: the model-competition side borders on an "ML competition" (out of scope). The dependency payouts are in scope.

**Talent Protocol Builder Rewards (talent.app)**
- Weekly distributions to builders with Builder Score of 40 or more. The score blends GitHub, onchain and other signals, and a Human Checkmark plus a Basename are required. — [Talent guide](https://talentprotocol.notion.site/builder-rewards-guide?pvs=4)
- Example campaign: WalletConnect, 75,000 WCT/week to the top 100 builders, Sep 30 – Nov 11, 2025, scored on GitHub activity, WCT usage and Base activity. — [Talent docs](https://docs.talent.app/docs/legal/builder-rewards-faq-walletconnect)
- Stacks Builder Challenges: weekly STX, tiered, ranked by Talent scores. — [Stacks blog](https://www.stacks.co/blog/stacks-builder-challenges-stx-rewards)

**Celo Proof of Ship**
- Monthly program. A GitHub repo is required, and AI agents review the README, code and commits alongside judges and DevRel. Rewards varied: early pools of 5k cUSD/month, PoS 7 at 15,000 CELO + 5,000 cUSD, PoS 9 at 20,000 CELO. — [Celo forum](https://forum.celo.org/t/celo-season-1-program-overview/12484); [Karma GAP docs](https://docs.gap.karmahq.xyz/how-to-guides/partners/celo-proof-of-ship); [Celo devs newsletter](https://celo-devs.beehiiv.com/p/proof-of-ship-9-2nd-milestone-checkin)

**AKINDO WaveHack (Japan-origin)**
- A "grant allocation protocol" that distributes grants onchain, continuously and in waves, to the builders who contribute most. — [AKINDO Notion](https://builderboard.notion.site/What-is-AKINDO-1844c0f2a0728042884bef4149887997)
- WaveHack Global Season 1 reported more than $250K in total grants. The 0G WaveHack (announced Aug 12, 2025) had a $50K pool with allocations rising each wave. — [AKINDO Substack recap](https://akindo.substack.com/p/recapwavehack-global-1st-season); [HackerNoon/Chainwire](https://hackernoon.com/lang/ja/0g-launches-wavehack-buildathon-for-ai-developers-on-akindo-with-$50000-grant)
- Caveat: it rewards product builders on ecosystem projects, not necessarily OSS contributions. The original WaveHack launch date (likely before 2025) was not confirmed.

**Pre-launch / prototype**
- TxPipe Githoney (Cardano): a GitHub bot plus onchain bounty contracts, with a prototype on preprod testnet. The F13 "good first issue" bounty proposal was listed as unfunded (₳199,943 requested, ₳0 received). A 2026 Intersect statement of work suggests development continues. — [Lido Nation F13](https://lidonation.com/en/proposals/githoney-by-txpipe-good-first-issue-program-f13); [Intersect](https://committees.docs.intersectmbo.org/intersect-open-source-committee/about/paid-open-source-model-posm/bug-bounty-program/tx-pipe-contract-githoney)
- GitCash (ETHOnline 2025): repo vaults in PYUSD pay out on merged PRs. OpenWave and GITHUNDER are smart-contract bounty extensions. All are hackathon projects, not launched products. — [GitCash](https://ethglobal.com/showcase/gitcash-2avdg); [OpenWave](https://ethglobal.com/showcase/openwave-a8rs5); [GITHUNDER](https://ethglobal.com/showcase/githunder-7rn9f)

### Inferences
- The "wave" format in Drips is converging with Celo Proof of Ship, Talent weekly rewards and AKINDO WaveHack: recurring rounds with algorithm- or AI-scored GitHub activity. These are ecosystem-locked and often reward building apps rather than contributing to OSS.
- Talent, Celo and Optimism use GitHub-activity scoring, which invites farming. Talent requires human verification for this reason.

### Gaps
- No final Deep Funding payout list was found. Optimism Season 7's final total after Aug 1, 2025 was not confirmed.
- No independent verification of AKINDO's $250K figure was found.

## Q4: Non-English and regional discovery (China, Japan, Korea, Brazil/LatAm, India)

### Takeaway
Non-English searches found no new 2025-2026 Drips-like platform. Results in Chinese, Japanese, Korean and Portuguese returned only older platforms or localized coverage of Western ones. Regional activity is grant-based (FOSS United, FLOSS/fund) or a long-standing forge feature (Gitee 悬赏), and all of it predates 2025.

### Cited Findings
- **China:** Gitee's bounty feature (悬赏) is described as fully live: maintainers enable it and anyone can post funded issues. No launch date or volume was found, and the linked page is just a user profile. — [Gitee](https://gitee.com/gitee_reward)
- **China:** OpenBuild, a Chinese Web3 dev community, pays USDT bounties within 3 days of a PR on partner repos (e.g. Amphitheatre) and gives an SBT to contributors with 40+ hours. It is not a dated 2025 launch. — [Amphitheatre contributing guide](https://github.com/amphitheatre-app/playground/blob/master/docs/how_to_contribute.md)
- **China (research):** OpenI/PCL hosts an OSS incentive-mechanism research repo. It is research, not a platform. — [OpenI](https://openi.pcl.ac.cn/zhangxunhui/OSS_incentive_mechanism/src/branch/master)
- **Japan:** Japanese results returned only BountyHub, Bountysource, GitHub Sponsors (2019) and OpenFare (2022). No Japan-origin 2025 OSS reward platform was found apart from AKINDO WaveHack (Q3). — [huntscreens JP](https://huntscreens.com/ja/products/bountyhub); [Gigazine OpenFare](https://www.gigazine.net/news/20220114-openfare-distribute-funds-software-contributors/)
- **Korea:** The only Korean issue-bounty site found was featured on GeekNews in January 2021 (10% fee), and it is unclear whether it still runs. — [news.hada.io](https://news.hada.io/topic?id=3626)
- **Brazil/LatAm:** Portuguese and Spanish results covered only GitHub Sponsors in Brazil (2022), Gitcoin and Bountysource. — [Tecnoblog](https://tecnoblog.net/noticias/2022/06/02/programa-do-github-para-apoio-financeiro-a-desenvolvedores-chega-ao-brasil/); [desdelinux](https://blog.desdelinux.net/bountysource-plataforma-financiacion-software-codigo-abierto/)
- **India, FOSS United:** more than INR 2.5 crore (~$110K) disbursed to date. Annual budget is ₹25 lakh, and about 200 grant requests came in during 2025 (~20% for direct FOSS work). It predates 2025. — [FOSS United 2025 recap](https://fossunited.org/blog/grants/2025-grants-recap)
- **India, FLOSS/fund (Zerodha):** Zerodha's 2025 report lists $205,000 in completed FLOSS/fund payments and about $100K to FOSS United, with more than $823K in total 2025 OSS contributions. FLOSS/fund launched in late 2024, so it falls just outside the window. — [Zerodha 2025 report](https://zerodha.com/open-source/2025-report/)

### Inferences
- In 2025-2026, new "earn from OSS" activity in China, Japan and Korea appears to flow through Web3 dev communities (OpenBuild, AKINDO) rather than standalone OSS-funding platforms.
- Regional programs are grants for projects and maintainers, not continuous streams for contributors.

### Gaps
- No search covered Gitee GVP or the OpenAtom (开放原子) incentive programs, or Chinese Web3 platforms (e.g. DoraHacks BUIDL grants), because of budget. These are worth a follow-up.
- Korean and Spanish-language coverage was thin. Absence of results is weak evidence that nothing exists.
- RootData and Crunchbase were not queried directly.
