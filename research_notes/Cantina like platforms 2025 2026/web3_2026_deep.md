# Web3 / smart-contract security earning platforms launched in 2026 (deep pass, third sweep)

Scope: Jan 1 – Oct 28, 2026. Already-known items (CertiK Hunt, CODESPECT SpecSiege, Sherlock Audit Engine, BattleChain, Immunefi audit-competition restart with submission fees) are not re-researched; corrections only. About 40 tool calls were used. The shared web-search budget ran out before the last two queries (a broad "launches audit competitions Sept 2026" sweep and a Hyperliquid/Sui/Sonic sweep), so those angles are only partly covered.

## 1. New 2026 platforms that earlier passes missed

### Takeaway
This pass found only one new, verified 2026 launch that pays researchers directly: **Jump Crypto's self-hosted Firedancer Bug Bounty Platform** (bounty.firedancer.io, live 16 Oct 2026, 1 SOL burn per report). It is a single-program, protocol-run platform, not a multi-client marketplace. Searches in English, Chinese and Korean for new startup audit-contest marketplaces, AI-agent audit arenas, chain-specific contest platforms or security DAOs found nothing else that both launched in 2026 and pays per finding.

### Cited Findings
**Firedancer Bug Bounty Platform (Jump Crypto) – VERIFIED 2026 launch**
- URL bounty.firedancer.io. It went live on 16 October 2026 and is run by Jump Crypto's Firedancer team directly, "rather than through Immunefi as its earlier programs did." Researchers sign in with GitHub and accept the terms. The coverage does not mention KYC. — [Solana Compass](https://solanacompass.com/news/firedancer-bug-bounty-platform-goes-live-with-3x-rewards-for-alpenglow-findings-after-jumps-1m-audit-contest)
- Each report requires a non-refundable 1 SOL burn to an incinerator address. This applies even to duplicate, invalid and out-of-scope reports, and the terms take effect 18 Oct. It is meant to deter AI-generated spam. — [CryptoSlate (headline/snippet)](https://cryptoslate.com/firedancer-makes-bounty-hunters-burn-1-sol-even-for-duplicate-bug-reports/); [PrimeXBT](https://primexbt.com/news/firedancer-requires-researchers-to-burn-1-sol-to-qualify-for-bug-bounty-duplicat/); [CoinDesk 27 Oct 2026 (headline/snippet; page 403)](https://www.coindesk.com/tech/2026/10/27/solana-bug-reports-now-cost-1-sol-as-ai-floods-security-teams-with-spam)
- Launch promotion: valid reports earn 2x the normal reward and Alpenglow-related findings earn 3x, until 20 Nov 2026. The base reward schedule is not published in the coverage. — [Solana Compass](https://solanacompass.com/news/firedancer-bug-bounty-platform-goes-live-with-3x-rewards-for-alpenglow-findings-after-jumps-1m-audit-contest)
- Background: the earlier $1M Firedancer audit contest ran on Immunefi from 9 Apr to 9 May 2026. It drew 809 reports from 162 researchers, yielding 127 unique findings, and nearly half of valid submissions were duplicates. The pool was tiered at $100k minimum, $250k with at least one Medium, $500k with a High, and $1M only for a Critical. The worst bug was rated High, and the total paid out was not disclosed. — [Solana Compass](https://solanacompass.com/news/firedancer-bug-bounty-platform-goes-live-with-3x-rewards-for-alpenglow-findings-after-jumps-1m-audit-contest); [Immunefi contest page](https://immunefi.com/audit-competition/firedancer-v1-audit-comp/scope)
- Red flag for researchers: paying about $100 per report, with no refund for duplicates, is a negative-expected-value trap for low-confidence submissions.

**Adjacent 2026 items (not Cantina-style per-finding marketplaces)**
- **TheDAO Security Fund** was announced in January 2026. It is an endowment built on about 69,420 staked ETH (about 75k ETH of unclaimed 2016 DAO funds) that pays grants to security researchers, tooling developers and rapid-response teams, with an estimated $8M/yr in yield. Seven curators, including Vitalik Buterin and pcaversaccio (SEAL 911), oversee it. It funds grants, not bounties per finding. — [The Block](https://www.theblock.co/post/387697/the-dao-back-ethereum-dev-griff-green-use-unclaimed-hack-funds-new-ethereum-security/); [Unchained](https://unchainedcrypto.beehiiv.com/p/exclusive-thedao-to-become-new-220-million-ethereum-security-fund)
- ETHSecurity Initiatives Round Two (TheDAO fund) opened with a board of 10 projects needing about $1.77M. Decisions are expected by mid-Nov 2026, and submissions stay open to late Jan 2027. Round one moved over $1.6M from 20+ funders and 3,934 donors. — [Crypto Briefing](https://cryptobriefing.com/ethsecurity-round-two-onchain-security/)
- **Immunefi IMU token** launched on 22 Jan 2026. This is a token launch on an existing platform, not a new platform. — [BlockEden](https://blockeden.xyz/blog/2026/01/25/immunefi-imu-token-web3-security-bug-bounty-platform/) (secondary blog)
- **BountyHunt.xyz** (June 2026) monitors the GitHub repos of bounty programs across seven platforms. It is a tool and does not pay researchers. — [Cointelegraph press release](https://cointelegraph.com/press-releases/bountyhuntxyz-launches-to-speed-up-web3-bug-hunting)
- **OpenAI Safety Bug Bounty** (March 2026) is not Web3 and is out of scope. EVMbench (OpenAI + Paradigm, Feb 2026) is a benchmark with no prize pool. — [OpenAI EVMbench](https://openai.com/index/introducing-evmbench/); [arXiv](https://arxiv.org/html/2603.04915v1)

**Checked and ruled out (not 2026 launches)**
- **MixBytes Camp**: an audit-contest platform staffed by MixBytes Farm graduates, with a soulbound-token record of each auditor. No launch date was found, and evidence points to before 2026. — [camp.mixbytes.io](https://camp.mixbytes.io/); [MixBytes blog](https://mixbytes.io/blog/an-overview-of-the-mixbytes-camp-soulbound-token)
- **Remedy (Hexens)**: bug bounty and CTF platform with claimed ZK-based duplicate protection. Its CTF dates to 2025 and no 2026 launch was found. — [The Grid](https://thegrid.id/profiles/Remedy); [Web3SecNews 2025](https://web3secnews.substack.com/p/are-you-ready-for-the-biggest-web3)
- **HackenProof DualDefense**: a Hacken audit followed by a month of crowdsourced review that pays for Criticals only. Contests were already running in Nov 2025, so it is not new in 2026. A third-party tracker says 67 of 78 settled DualDefense audits paid $0. — [HackenProof blog](https://hackenproof.com/blog/what-is-dual-defense-audit); [Soda Labs Nov 2025](https://hackenproof.com/blog/soda-labs-protocol-dualdefense-audit); [munimtechnologies tracker](https://github.com/munimtechnologies/audit-contest-ai-rules)
- **Immunefi Magnus** (unified security ops platform) predates 2026. **Secure3** (2022) and **Hats Finance** have no 2026 launch. **Octane** (AI auditor, $6.75M seed in Apr 2025) showed no 2026 researcher-contest launch. — [The Grid list](https://thegrid.id/discovery/productType/bug-bounty-competitions); [Dealroom Secure3](https://app.dealroom.co/companies/secure3); [Decrypt Octane](https://decrypt.co/314038/winklevoss-backed-startup-octane-raises-millions-blockchain-hacks-ai?amp=1)
- **Savant Chat**: an AI agent that its vendor's press release (2 Sep 2025) says placed 6th in a Sherlock contest. It is from 2025 and unverified. — [Bitcoin.com PR](https://news.bitcoin.com/savant-chat-achieves-a-historic-top-6-ranking-in-the-sherlock-defi-audit-contest/)
- Korean search: the only 2026 Korean-language hit was CertiK Hunt (already known). Exchanges such as Bithumb and Upbit run their own bug bounties, and Upbit's ran with Theori on its PatchDay platform. These are not 2026 Web3 contest platforms. — [fnnews](https://www.fnnews.com/news/202607021028271024); [Blockmedia](https://www.blockmedia.co.kr/archives/276422)
- Chinese search: no 2026 Chinese audit-contest platform launch surfaced. — [Bitget news (zh)](https://www.bitget.com/zh-CN/news/detail/12560605470496)

### Inferences
- The 2026 trend is consolidation plus protocols bringing programs in-house: Code4rena exited, Firedancer left Immunefi for its own platform, and Ethereum Core is listed as self-hosted. Fees per submission are spreading (Firedancer burn, Immunefi fees) because AI-generated report spam is overwhelming triage. New multi-client startup marketplaces did not appear in indexed sources.
- If an AI-agent paid audit arena launched in 2026 outside Bittensor, it has no indexed press coverage. The nearest are Sherlock Audit Engine, which accepts "AI auditors", and CertiK Hunt's "AI security challenges", both already known.

### Gaps
- The Firedancer base reward schedule and payout evidence for the new platform are not public in the coverage. The primary Jump terms page was not fetched.
- Searches of X/Twitter, Product Hunt, RootData and Crunchbase could not be run directly, and the search budget ran out before the dedicated Hyperliquid/Sui/Sonic/TON/Starknet ecosystem sweep. Smaller chain-native contest launches may be missed.

## 2. Code4rena wind-down: successors and spin-offs

### Takeaway
Code4rena announced its wind-down on 13 May 2026, and Immunefi absorbed its bounty customers and wardens. No platform started by ex-Code4rena staff or wardens was found in indexed sources.

### Cited Findings
- C4 announced the wind-down on 13 May 2026 and said "all open contests and bounties will be completed." — [Code4rena on X](https://x.com/code4rena/status/2054492081876324458); [Crypto Times](https://www.cryptotimes.io/2026/05/13/immunefi-moves-to-rescue-bug-bounty-programs-after-code4rena-exit/)
- Immunefi invited wardens to its platform and offered migration support for scope, rules and reward structures. — [AMBCrypto](https://ambcrypto.com/immunefi-takes-over-code4renas-wardens-can-defi-survive-2026-exploit-surge/); [usethebitcoin](https://usethebitcoin.com/news/immunefi-to-absorb-code4rena-customers/)
- One third-party blog gives 12 July 2026 as the shutdown date. This is unverified against C4's own materials. — [Paragraph](https://paragraph.com/@cmaluractu/code4rena-is-shutting-down-heres-where-beginners-should-go-next)
- As of 15 Oct 2026, a tracker reports C4 closed, with K2 ($135k) still in judging. — [munimtechnologies tracker](https://github.com/munimtechnologies/audit-contest-ai-rules)
- One of C4's last big contests was Monad: a $500k pool with 4 High and 7 Medium findings, report published Feb 2026. — [Code4rena on X](https://x.com/code4rena/status/2027126526492524881)
- Beginner guides point C4 refugees to CodeHawks First Flights, Sherlock, Cantina and Immunefi, none of them new. — [Paragraph](https://paragraph.com/@cmaluractu/code4rena-is-shutting-down-heres-where-beginners-should-go-next)

### Inferences
- The C4 user base appears to have been absorbed by existing platforms, mainly Immunefi, rather than spawning a successor.

### Gaps
- No evidence found either way of a warden-led spin-off. X/Discord announcements were not searchable.

## 3. Zellic's plans

### Takeaway
No Zellic-branded contest platform launched in 2026. Zellic's visible 2026 move was running validators and returning half of validator profits as audit credits.

### Cited Findings
- In Feb 2026 Zellic said it operates validators and infrastructure for partner chains and returns half its validator profits as audit credits. — [Security Boulevard](https://securityboulevard.com/2026/02/zellic-runs-validators/)
- Zellic acquired Code4rena in Aug 2024. The tracker says that from Sep 2025, findings from Zellic's AI auditor V12 counted as known issues in C4 contests. — [The Block](https://www.theblock.co/post/312583/zellic-code4rena); [munimtechnologies tracker](https://github.com/munimtechnologies/audit-contest-ai-rules)

### Inferences
- Zellic seems to be moving toward AI auditing (V12) and infrastructure rather than running crowdsourced contests.

### Gaps
- No Zellic statement on the reasons for C4's closure or future contest plans was found.

## 4. Corrections and updates to already-known items

### Takeaway
There are small updates to known items: BattleChain mainnet is now live, the Immunefi fee amount is still unpublished, CertiK Hunt has no payout evidence, and the Sherlock Audit Engine has had no open engagements.

### Cited Findings
- **BattleChain**: the official docs now list Mainnet (chain ID 626) and Testnet (chain ID 627) as live. It is a ZKsync-based L2 where audited contracts with real funds sit in "Attack Mode" under Safe Harbor, and promotion to production goes through a DAO. The mainnet launch date was not found. — [BattleChain docs](https://docs.battlechain.com/overview); [deployments.json](https://docs.battlechain.com/deployments.json)
- CodeHawks' BattleChain Confidence Pools contest (9–16 Jul 2026) was its first audit in 15 months. CodeHawks penalises "relying excessively on AI." — [munimtechnologies tracker](https://github.com/munimtechnologies/audit-contest-ai-rules)
- **Immunefi**: its three most recent competitions state a per-report submission fee, but the amount is not shown. As of 15 Oct 2026, no competitions were live and AI-generated reports were banned by its terms. Recent pools: Base Azul up to $250k, ending 4 May 2026, and ENS $70k, 18 Aug–14 Sep 2026. — [tracker](https://github.com/munimtechnologies/audit-contest-ai-rules); [Base blog](https://immunefi.com/blog/all/base-immunefi-audit-competition/); [ENS blog](https://ens.domains/blog/post/ens-immunefi-audit-competition)
- **Sherlock Audit Engine**: publicly launched 18 Aug 2026. It is invite-based, requires KYC plus an NDA for each engagement, and pays in USDC on Polygon or RLUSD on XRPL. It accepts fully autonomous "AI auditors." Payout needs at least 2 valid findings and a 20% valid ratio. As of 15 Oct it showed 0 engagements taking applications. — [tracker](https://github.com/munimtechnologies/audit-contest-ai-rules)
- **CertiK Hunt**: launched 1 Jul 2026 (confirmed). No public payout totals or named first programs were found. — [CertiK blog](https://www.certik.com/blog/introducing-certik-hunt); [Crypto Briefing](https://cryptobriefing.com/certik-debuts-invite-only-bug-bounty-platform-for-web3-researchers/)
- Context: Cantina's live Revert v4lend competition ($50k USDC, 6 Oct–3 Nov 2026), and BitGo's bounty on Cantina (up to $75k, April 2026). These are new programs on Cantina, not new platforms. — [tracker](https://github.com/munimtechnologies/audit-contest-ai-rules); [BitGo](https://www.bitgo.com/resources/blog/bitgo-launches-bug-bounty-program-on-cantina/)

### Inferences
- The tracker (a single unofficial compilation dated 15 Oct 2026) is the main source for live-status data. Treat its numbers as a snapshot that has not been verified independently.

### Gaps
- The Immunefi fee amount, the BattleChain mainnet date and CertiK Hunt payout evidence remain unverified.
