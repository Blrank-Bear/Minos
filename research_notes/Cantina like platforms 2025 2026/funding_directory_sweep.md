# Funding / directory / launch-site sweep: Cantina-like security earning platforms unveiled 2025-2026

Method: funding/fundraise searches (seed rounds, CryptoRank, YC directory), launch sites (Product Hunt, BetaList, Show HN), directories and comparison lists (The Grid, SourceForge, CloudSEK, GBHackers, xhack.io, bug-bounties.as93.net, GitHub lists), plus community searches. Sweep date 2026-10-28. About 33 tool calls. **The shared web-search budget ran out partway through**, so the Product Hunt / HN / RootData domain-restricted searches and Reddit thread searches never ran. Several directory pages (smartcontractshacking.com, Trend Hunter, Wellfound, CryptoRank article, X) returned 403/402 and could not be read.

## Q1. Which 2025-2026 platforms not in the known list did this discovery method surface?

### Takeaway
The funding, directory and launch-site route turned up very few new platforms. The only good-quality new find is **Bugbop**, a small bootstrapped Web2 bug bounty SaaS (alpha April 2025, public on BetaList/Product Hunt about January 2026). Weaker finds are **HackAPrompt 2.0**, a one-off AI red-team contest announced January 2025, and **DualGuard**, an unverified new audit-contest brand whose first contest was announced for November 2025. Every directory and comparison list checked contains only pre-2025 platforms.

### Cited Findings

**Bugbop (bugbop.com): new, verified to exist, small**
- Australian (Melbourne) bug bounty platform founded by John "Ponny" Sherwood. He says he ran Gleam's bug bounty for 7 years and paid about $45k in bounties. The company describes itself as bootstrapped, with him as a 50% owner. — [Bugbop About](https://bugbop.com/about)
- Alpha release "to a small group of bounty programs and bug hunters." The post sits under a /posts/2025/04/11/ URL and claims "Bounties already paid out too!" In one early program it says 3 bugs (low/medium/high) were found despite two professional pentests the year before. — [Bugbop alpha post](https://bugbop.com/posts/2025/04/11/bugbop-in-alpha-release)
- BetaList "Featured" date is January 24, 2026. A company funds a $575 "bounty wallet" to launch a program and gets a refund if no bugs are found. Private programs are free. AI sets severity, filters duplicates and removes low-quality reports. — [BetaList](https://betalist.com/startups/bugbop)
- Product Hunt listing by @ponny, tagline "Run Security Bug Bounties with less noise and fair pricing." It has very low traction (about 4 upvotes, 3 comments, 8 followers, 0 reviews). — [Product Hunt](https://www.producthunt.com/p/bugbop)
- SourceForge lists pricing as "$0 monthly + 15% on bounties." — [SourceForge startup bug bounty list](https://sourceforge.net/software/bug-bounty/for-startup/)
- Type: public, self-serve Web2 bug bounty platform for SMBs. Reward scale: small (program wallets start at $575). Backers: none (bootstrapped). Payout evidence: only the company's own claim. Red flags: no researcher count, no program list, no payout stats published.

**HackAPrompt 2.0 (hackaprompt.com): AI red-team contest from Learn Prompting**
- Announced January 10, 2025 with $100,000 in prizes over about 2 months. Tracks: Classic, Agents, Future Attacks, with 2 more marked "coming soon." It is time-limited, not an ongoing platform. — [Learn Prompting announcement](https://learnprompting.org/blog/announce-hackaprompt-2)
- A later newsletter calls it a $100k competition "in partnership with OpenAI," with a CBRNE track ($50k) and an Agents track ($60k). — [Learn Prompting newsletter](https://newsletter.learnprompting.org/p/openai-x-learn-prompting-our-100-000-ai-red-teaming-competition-hackaprompt-2-0-7144)
- Decrypt reported the contest "returns with $500,000 in prizes," including $50k bounties for the most dangerous exploits. The size of the total is therefore inconsistent across sources. — [Decrypt](https://decrypt.co/323351/how-to-trick-chatgpt-and-get-paid-50000/)
- Caveat: HackAPrompt 1.0 ran in 2023 (on AIcrowd), so the brand is not new. Only the 2.0 edition and its own site date to 2025. — [AIcrowd HackAPrompt 2023](https://www.aicrowd.com/challenges/hackaprompt-2023)

**DualGuard (@dualguardaudits on X): claimed, unverified**
- A search snippet of an X post says "Our first audit contest will start soon": dates 17/11 to 23/11 (2025 implied by the status ID), protocol @Alignerz_ (a token launchpad, Solidity, about 1,500 nSLOC), prize pool 45,000 USDT (H/M 20k, L 3k, two "LSG" pools of 6k each, winner bonus 7.5k, judge 2.5k). — [X post (snippet only, page returned 402)](https://x.com/dualguardaudits/status/1989357921314996606)
- I could not open the post or find a website, so whether the contest happened and whether it paid out is unknown. A search for "DualGuard" returned only HackenProof's similarly named "DualDefense" product, so it may be easy to confuse the two.

**Peripheral / out of scope**
- SevHunt is an *internal* bug bounty platform where employees earn points for reporting bugs. Product Hunt shows #74 for the day, 6 upvotes and no launch date. It does not pay outside researchers. — [hunted.space](https://hunted.space/product/sevhunt)
- PlugBounty and Com Olho appear in SourceForge's list (PlugBounty: open-source and WordPress plugin auditing with "monthly payouts"; Com Olho: AI-assisted bug bounty with KYC-verified researchers), but no launch dates were found. — [SourceForge](https://sourceforge.net/software/bug-bounty/for-startup/)

### Inferences
- Platforms in this space that are new and lack press coverage tend to be tiny Web2 SaaS tools like Bugbop, not Cantina-scale researcher marketplaces. If the goal is earning money, Bugbop is unlikely to matter until it publishes programs or payout data.
- No new Web3 audit-contest platform with funding appeared in any funding database or directory. This fits the market contraction described in Q3: new entrants have little reason to launch contest platforms in 2025-2026.

### Gaps
- Bugbop's researcher count, live programs and fees for hunters are unknown, and its exact public launch date is unclear (somewhere between April 2025 and January 2026).
- DualGuard's website, team and payout record are unverified.
- Product Hunt / Show HN / RootData domain-restricted searches, Reddit r/bugbounty and r/ethdev threads, and DefiLlama/Solodit filters were **not done** because the web-search budget ran out. smartcontractshacking.com's platform tracker returned 403. These are the most promising follow-ups.

## Q2. What did funding databases, YC and directories show? (negative results matter)

### Takeaway
Funding in 2025-2026 went to AI-automated offensive security and AI red-team *vendors* (V12, Beacon, Mindgard, Armadin, YC's Veria Labs, Casco, MindFort), not to crowdsourced researcher platforms. Directory and comparison lists dated 2026 still list only incumbents. The one new listing in a "bug bounty competitions" directory is Bittensor-based and therefore excluded.

### Cited Findings
- Searching YC for 2025 bug bounty startups found none. Federacy (YC S18) is the only YC bug bounty platform that came up. — [YC Federacy](https://www.ycombinator.com/companies/federacy); [Launch HN Federacy](https://news.ycombinator.com/item?id=17673461)
- 2025 YC security companies are autonomous AI hacking tools, not crowds: Veria Labs (F25), Casco (2025), MindFort (2025). — [YC cybersecurity directory](https://www.ycombinator.com/companies/industry/cybersecurity)
- 2026 security seed rounds are AI- and agent-focused: Beacon Security $13M (July 2026), Furl $10M, and Crunchbase-cited figures of $855M across 150+ AI-security seed rounds in 2026. None is crowdsourced. — [Dealroom Beacon](https://dealroom.co/news/139379-beacon-security-lands-13m-seed-topping-97-of-security-rounds/); [AIWeekly](https://aiweekly.co/alerts/ai-security-startups-pull-855m-across-150-seed-rounds-in-2026); [Axios Furl](https://www.axios.com/pro/enterprise-software-deals/2026/01/21/cyber-agentic-furl-seed-ten-eleven)
- V12, an AI security startup, reportedly raised a $10M seed after its AI agent won a $2.5M blockchain bug bounty (July 2026). This is AI-agent hunting, not a platform. The article returned 403, so only the headline is confirmed. — [CryptoRank headline](https://cryptorank.io/news/feed/v-12-security-seed-2026-07-30)
- AI red-team vendors raising money: Mindgard $30M Series A; Armadin $189.9M Series A ("elite red teamers... combined with agentic AI"). Neither is an open researcher marketplace. — [Dealroom Mindgard](https://dealroom.co/news/144657-mindgard-raises-30m-series-a-to-red-team-ai-systems/); [TAMradar Armadin](https://www.tamradar.com/funding-rounds/armadin-series-a-189-9m)
- The Grid "bug bounty competitions" directory (updated 2026-10-28) lists only Immunefi, MixBytes Camp, Remedy, Cantina, HackenProof and Innerworks/RedTeam. Innerworks is on Bittensor, so it is excluded. — [The Grid](https://thegrid.id/discovery/productType/bug-bounty-competitions)
- Remedy (Hexens) is **not** a 2025 launch. A review dates it to 2023 (beta), and Hexens' 2023 year-in-review already describes it. — [JohnnyTime Medium](https://medium.com/@JohnnyTime/a-revolutionary-bug-bounty-platform-zero-knowledge-proofs-in-web3-5e9aaa536084); [Hexens 2023 review](https://hexens.io/blog/2023-year-in-review)
- 2026 comparison lists (CloudSEK 9, GBHackers 12, SourceForge 23, xhack.io 4) contain only established platforms. xhack.io is a Pakistani pentest company that "does not run a bug bounty platform." — [CloudSEK](https://www.cloudsek.com/knowledge-base/best-bug-bounty-platforms); [GBHackers](https://gbhackers.com/best-bug-bounty-compared/); [xhack.io](https://xhack.io/blog/bug-bounty-platforms-compared)
- GitHub awesome lists (Anugrahsr/Awesome-web3-Security, JeffCX/collection-web3-bug-bounty) list programs and resources and add no 2025-2026 platforms. — [ecosyste.ms list](https://awesome.ecosyste.ms/lists/7100); [JeffCX repo](https://github.com/JeffCX/collection-web3-bug-bounty)

### Inferences
- Investors in 2025-2026 are betting on AI replacing crowds, so a "funding database" sweep is structurally unlikely to find new crowdsourced platforms. The money is in autonomous hunting, such as V12 and Veria.

### Gaps
- RootData and CryptoRank fundraising tables could not be queried directly, and the CryptoRank article returned 403.
- I did not get YC W26/S26/F26 batch-specific listings.

## Q3. Market context that affects any new entrant (2025-2026)

### Takeaway
The Web3 audit-contest market contracted sharply. Code4rena shut down in May 2026, and contest counts and prize money fell about 80%. The new "launches" are mostly existing players adding invite-only or AI-hybrid products (Sherlock Audit Engine, CertiK Hunt, HackenProof DualDefense). On the AI side, the labs run their own bounties.

### Cited Findings
- Code4rena announced its wind-down; Immunefi is absorbing its bug-bounty customers and wardens. — [The Block](https://www.theblock.co/post/401179/immufefi-absorb-code4rena-bug-bounty-customers-shutdown-decision)
- A dated snapshot (as of 15 Oct 2026) reports: Code4rena wind-down announced 13 May 2026. Sherlock + Cantina public contests fell from 76 (2024 H1) to 13 (2026 H1), down 83%, while submissions rose 24%. Prize per submission fell from $451 to $85. Total prize money fell from $7.12M to $1.56M. Immunefi audit competitions fell from 20 (2024 H2) to 3 (2026 H1). CodeHawks started no competitive audit between 3 Apr 2025 and 9 Jul 2026. Sherlock Audit Engine went public 18 Aug 2026 and is invite-based. — [munimtechnologies/audit-contest-ai-rules](https://github.com/munimtechnologies/audit-contest-ai-rules) (single third-party source with self-reported figures)
- HackenProof DualDefense (crowd review after an audit, criticals paid from a staker-funded "Flash Pool") ran contests from November 2025 to January 2026 with headline caps of $4k-$75k. — [HackenProof Soda Labs](https://hackenproof.com/blog/soda-labs-protocol-dualdefense-audit); [HackenProof ZIGChain](https://hackenproof.com/blog/zigchain-smart-contract-dualdefense-audit). The same snapshot says DualDefense paid 11% of headline maximums, and 67 of 78 paid nothing. — [munimtechnologies](https://github.com/munimtechnologies/audit-contest-ai-rules)
- CertiK Hunt (already known) was announced July 1, 2026 as invite-only. — [HackerNoon](https://hackernoon.com/certik-launches-invite-only-hunt-platform-for-elite-security-researchers)
- AI-lab programs (not platforms): OpenAI Safety Bug Bounty (March 2026); OpenAI GPT-5 Bio Bug Bounty ($25k, raised to $50k for GPT-5.5/5.6, now private); Anthropic classifier bounty (up to $25k, May 2025, via HackerOne). — [OpenAI Safety Bug Bounty](https://openai.com/index/safety-bug-bounty/); [OpenAI GPT-5 bio bounty](https://openai.com/gpt-5-bio-bug-bounty/); [Anthropic](https://www.anthropic.com/news/testing-our-safety-defenses-with-a-new-bug-bounty-program)

### Inferences
- A brand-new Web3 contest platform launching into this market (for example DualGuard) carries high counterparty and payout risk. Any 2025-2026 entrant should be judged on a verified payout record, not on headline pools.
- HackenProof DualDefense is a 2025 product from a known platform, not a new platform. Headline prizes overstate what it actually pays.

### Gaps
- No independent verification of the munimtechnologies statistics.
- Not checked: whether any ex-Code4rena warden collective launched a successor platform after May 2026 (searches found only Immunefi absorbing the community).
