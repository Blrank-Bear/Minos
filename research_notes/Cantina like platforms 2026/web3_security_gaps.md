# Web3 / Smart-Contract Security Platforms Launched in 2026: Gap Pass

Research date: 2026-10-28. This is the second pass. It follows `web3_security.md` and does not repeat its findings: CertiK Hunt, CODESPECT SpecSiege, the Code4rena wind-down, the Hats shutdown, and the status of Immunefi, Cantina, Sherlock, HackenProof and CodeHawks.

Partway through, the scope changed. It now covers global search and **only platforms unveiled or launched in 2026**. Older platforms get one line each at most.

This pass used about 20 tool calls, mostly search-engine summaries plus a few fetched pages. "Verified" means an official page or two independent outlets. "Claim" means the vendor's own statement or a sponsored press release.

**Headline result:** this pass found only **two** additional 2026-launched earning venues that could be confirmed. They are **Sherlock Audit Engine**, launched publicly on 18 Aug 2026 as an invite-based venue where AI auditors participate, and **Cyfrin's BattleChain**, whose testnet launched in March 2026 as a "legal attack" L2 paying whitehat bounties. There is one notable 2026 format change: **Immunefi restarted audit competitions with a per-report submission fee**. Targeted searches for regional (Asian, Turkish, European, LATAM) platforms, chain-owned contest platforms and new auditor marketplaces turned up **no 2026 launches**.

## Q1. Regional platforms (global search) launched in 2026

### Takeaway
I found no regional Web3 audit-contest or bug-bounty *platform* launched in 2026 in any region: Korea, Japan, China, Vietnam, India, Turkey, Europe or LATAM. The only regional 2026 item is a government-run Korean financial-sector bug bounty that adds crypto-asset businesses. That is a public program, not a Cantina-like platform.

### Cited Findings
- Korea's Financial Supervisory Service is extending its 2026 financial-industry vulnerability reward program to **crypto-asset businesses**. The program grew to 70 companies (from 32) and 306 services in scope, announced around 18 May 2026. This is a government program, not an open Web3 platform. The source is a Japanese-language news page summarised by search; I did not read it in full — [Bloomingbit JP](https://jp.bloomingbit.io/feed/news/112287)
- A Korean blog post from May 2026 surveys 15 bug-bounty platforms in managed, self-hosted, Web3 and AI categories. Its search summary named no new Korean or Japanese Web3 platform — [youngju.dev](https://www.youngju.dev/transcribe/culture/2026-05-16-bug-bounty-vdp-platforms-2026-hackerone-bugcrowd-intigriti-synack-yeswehack-immunefi-code4rena-deep-dive)
- An English-language search for Vietnam, China, India or Turkey audit-contest platforms in 2026 returned only Western platforms. That search did turn up **MixBytes Camp**, an **older** contest platform (MixBytes, a European firm) for graduates of the MixBytes Farm course. Contestants carry a Polygon SBT track record. **No launch date found and no evidence it is new in 2026** — [camp.mixbytes.io](https://camp.mixbytes.io/); [MixBytes SBT blog](https://mixbytes.io/blog/an-overview-of-the-mixbytes-camp-soulbound-token); [The Grid directory](https://thegrid.id/discovery/productType/bug-bounty-competitions)
- The Grid's "bug bounty competitions" directory (2026) lists six names: Immunefi, MixBytes Camp, Remedy (ZK-proof dedup, Hexens triage, plus Remedy CTF), Cantina, HackenProof, and Innerworks RedTeam (a Bittensor subnet, out of scope). None are tagged with a 2026 launch — [The Grid](https://thegrid.id/discovery/productType/bug-bounty-competitions)

### Inferences
- The 2026 market for Cantina-like platforms looks consolidated around incumbents. Regional entrants either never appeared or are invisible to English-language search.
- Older one-liners: MixBytes Camp (European, curated, older) and Remedy (older, ZK dedup).

### Gaps
- I ran no searches in Korean, Japanese, Chinese, Vietnamese, Turkish or Portuguese/Spanish. A regional platform marketed only in a local language could have been missed. This is the biggest remaining blind spot.
- Asian security firms such as SlowMist, Verichains, ExVul, Beosin and Salus were not checked for 2026 crowdsourced products.

## Q2. Chain-ecosystem security programs that act as platforms in 2026

### Takeaway
The one genuinely new 2026 "chain as platform" is **BattleChain** (Cyfrin). It is a ZKsync-based pre-mainnet L2 where protocols deploy audited contracts with real funds and whitehats legally attack them for bounties. Its **testnet launched in March 2026**. The major L1/L2 ecosystems (Sui, Aptos, Starknet, Berachain, Hyperliquid, Base) still run their bounties and contests on existing platforms (HackenProof, Immunefi) or in-house. I found no new chain-owned contest platform in 2026.

### Cited Findings
**BattleChain (Cyfrin), new in 2026**
- **Testnet launched March 2026**: "a pre-mainnet blockchain allowing whitehat hackers to legally attack smart contracts." Mainnet is listed as a future goal — [RootData Cyfrin profile](https://www.rootdata.com/projects/detail/Cyfrin?k=ODA4Nw%3D%3D)
- The official docs (search summary) say **BattleChain Mainnet (chain ID 626) and Testnet (chain ID 627) are both live**. The flow: protocols deploy post-audit contracts with seed liquidity, a DAO approves "attack mode," and whitehats exploit the contracts under Safe Harbor agreements for bounties before the contracts move to "production mode." The chain is a ZKsync-based L2 — [docs.battlechain.com overview](https://docs.battlechain.com/overview); [Attack a Contract quickstart](https://docs.battlechain.com/battlechain/quickstart/execute-first-attack)
- The best-practices doc suggests a **10% bounty, capped at $5M**, as the industry standard. Plans include prediction markets and private transactions ("Prividium") — [BattleChain best practices](https://docs.battlechain.com/battlechain/explanation/best-practices)
- **Conflict:** as of 28 Oct 2026 the homepage says it is "currently under construction" and lists no launch dates. It says "Protocols set their own bounty terms" and that "ethical hackers, AI bots, and security researchers" can attack contracts. It does not mention KYC, backers or payout mechanics. The docs URL now redirects to the homepage — [battlechain.com (fetched)](https://www.battlechain.com/)
- CodeHawks' **BattleChain Confidence Pools** contest (9–16 Jul 2026) was CodeHawks' first audit in 15 months — [Munim snapshot, GitHub, 15 Oct 2026](https://github.com/munimtechnologies/audit-contest-ai-rules)

**Chain programs on existing platforms (not new platforms)**
- **Sui**: bounty on HackenProof, up to $500k per critical. **Aptos**: on HackenProof (listing dated 13 Nov 2025; the two listings conflict at $100k vs $1M). **Starknet**: HackenProof, up to $250k — [HackenProof programs](https://hackenproof.com/programs)
- **Berachain**: bounty on Immunefi, max $100k, at 10% of funds affected, updated 24 Jul 2026 — [Immunefi Berachain](https://immunefi.com/bug-bounty/berachain/information/)
- **Hyperliquid**: in-house bounty announced with HyperEVM, rewards from under 10k to about 1M USDC. The article date is unclear and likely predates 2026 — [Cointelegraph](https://cointelegraph.com/news/hyperliquid-hyperevm-bug-bounty-launch-layer1)
- **Base**: an Immunefi audit competition for the "Base Azul" upgrade, up to $250k, ran 21 Apr – 4 May 2026 — [Immunefi blog](https://immunefi.com/blog/all/base-immunefi-audit-competition/)
- **TON, Monad, Polkadot, Cosmos, NEAR**: no 2026 contest platform found. NEAR Intents is on HackenProof, per the first pass.

### Inferences
- BattleChain is the most novel 2026 venue structurally. It replaces "submit a report, get triaged" with "exploit for real under Safe Harbor and keep a bounty cut," and it explicitly invites AI bots. Its real launch state is unclear (docs vs homepage), so treat it as early-stage, with no verified payouts.

### Gaps
- No verified BattleChain payouts, TVL in attack mode, participant counts or funding. Whether its mainnet is truly live is unresolved because the sources conflict.
- I found no Solana-, TON- or Move-specific new contest platform. The search budget did not allow per-chain deep dives.

## Q3. AI-assisted / AI-agent audit competition platforms launched in 2026

### Takeaway
**Sherlock Audit Engine** (public 18 Aug 2026) is the clearest 2026 venue where **AI auditors and humans compete in the same paid engagement**. It is invite-based and KYC'd. Elsewhere 2026 brought benchmarks (EVMbench) and AI products, not open AI-agent bounty platforms. Platform policy on AI submissions split sharply in 2026: Sherlock Audit Engine welcomes them, Cantina allows them if validated, HackenProof and CodeHawks penalise them, and Immunefi bans them.

### Cited Findings
**Sherlock Audit Engine (new 2026, claim plus third-party snapshot)**
- It went public **18 Aug 2026** after "months of quiet testing." It is an orchestration platform that puts frontier LLMs, purpose-built AI auditors (e.g., V12, ZeroCool) and AI-enabled researchers into one engagement, then dedups and validates the findings — [BeInCrypto](https://beincrypto.com/sherlock-launches-public-audit-engine/); [Sherlock product page](https://sherlock.xyz/solutions/audit-engine); [Decrypt (sponsored PR)](https://decrypt.co/375876/sherlock-unveils-audit-engine-as-ai-security-race-accelerates)
- First large engagement: **Polygon Heimdall V2**, with **200+ participants and systems** and a **$100K+ guaranteed reward pool**. Sherlock says AI auditors were among the strongest performers on coverage (claim) — [Sherlock: Why We Built Audit Engine](https://sherlock.xyz/post/why-we-built-sherlock-audit-engine); [Sherlock product page](https://sherlock.xyz/solutions/audit-engine)
- Participant terms per the 15 Oct 2026 snapshot: **invite-based**, "AI auditors" are an explicit participant type, **KYC required before accepting an invite plus a per-engagement NDA**, payout in USDC on Polygon (or RLUSD on XRPL), and a minimum of **2 valid findings and a 20% valid ratio** to be paid. **No engagements were open to applications on 15 Oct.** Aerodrome's contest on Audit Engine has no public findings or payouts — [Munim snapshot (third party)](https://github.com/munimtechnologies/audit-contest-ai-rules) (cites docs.sherlock.xyz/audit-engine/for-participants)

**AI-submission policy across platforms, per the Oct 2026 snapshot**
- Cantina: AI findings allowed if validated; unvalidated AI findings can mean a "permanent ban." HackenProof: all 43 programs that started in 2026 carry AI rules (e.g., no AI reports without a runnable PoC). CodeHawks: "relying excessively on AI" risks disqualification. Immunefi: its terms ban "AI-generated/automated scanner bug reports." Code4rena treated V12 findings as known issues from Sep 2025 — [Munim snapshot](https://github.com/munimtechnologies/audit-contest-ai-rules)

**Context, not platforms**
- **EVMbench** (OpenAI + Paradigm, about 18 Feb 2026) benchmarks AI agents on Code4rena-derived vulnerabilities. Vendor pages report leaderboard scores (Cecuro 91.45%, Nethermind AuditAgent 67%, and others), but these are vendor claims, and an independent re-test reshuffled the rankings — [Cecuro comparison (vendor)](https://cecuro.ai/compare/best-smart-contract-audit-companies/); [yajin.org re-test](https://yajin.org/blog/2026-03-18-ai-smart-contract-audit-reevmbench/)
- **BountyHunt.xyz** (17 Jun 2026) is a $9/month Telegram alert tool that watches bounty programs across seven platforms. It is a tool, not a platform — [Cointelegraph PR](https://cointelegraph.com/press-releases/bountyhuntxyz-launches-to-speed-up-web3-bug-hunting)
- Cyfrin **Cygent**, an AI security engineer built on its internal CARA engine, is a product, not an earning venue. Its date is unclear — [RootData](https://www.rootdata.com/projects/detail/Cyfrin?k=ODA4Nw%3D%3D)

### Inferences
- A 2026 newcomer who wants to compete with an AI agent for pay has realistically two routes: Sherlock Audit Engine (invite plus KYC) and BattleChain (AI bots named as attackers). CertiK Hunt's "AI security challenges" (first pass) is a third, invite-only route.
- Red flags: Audit Engine had zero open engagements in mid-October, and its payouts are not public. Thresholds such as 2 valid findings and a 20% valid ratio penalise low-precision AI output.

### Gaps
- No open, permissionless AI-agent audit-competition platform launched in 2026 could be confirmed.
- Nethermind AgentArena's launch status is still unverified (first pass).

## Q4. Auditor marketplaces / freelance audit networks: new public ones in 2026

### Takeaway
I found **no new auditor marketplace or freelance network launched in 2026**. The existing collectives (Pashov, Zenith) recruit freelancers publicly, and AuditOne runs a curated marketplace, but all three are older. The one 2026 format change in the bounty and contest space is **Immunefi restarting audit competitions with a per-report submission fee**.

### Cited Findings
- **Immunefi audit competitions, restarted in 2026 with a fee.** The ENS competition (18 Aug – 14 Sep 2026) states that "a submission fee, set and managed by Immunefi, applies to each report," plus a fee to start mediation. The amount is not published. The snapshot says the fee applies to the three competitions since the restart (Firelight, Quantus, ENS), and none were live on 15 Oct — [ENS blog](https://ens.domains/blog/post/ens-immunefi-audit-competition); [Munim snapshot](https://github.com/munimtechnologies/audit-contest-ai-rules)
- HackenProof track record (snapshot): settled programs paid **22% of headline maximums**, and **67 of 78 settled DualDefense audits paid $0** — [Munim snapshot](https://github.com/munimtechnologies/audit-contest-ai-rules)
- **Pashov Audit Group** (older) is hiring remote, freelance security researchers (portfolio or contest profiles; listing valid to 31 Dec 2026) — [pashov.com/jobs](https://www.pashov.com/jobs)
- **Zenith** (older) invites applicants to "the network of independent auditors with proven track records" — [zenith.security/team](https://www.zenith.security/team)
- **AuditOne** (older, Cologne) runs a curated auditor-pooling marketplace that matches projects with 3–4 vetted reviewers. The source is a single third-party review — [m3dython review 2026](https://m3dython.com/blog/auditone-review-2026)
- Octane, Guardian, Bailsec, Sec3 and Dedaub: no new public 2026 marketplace or application programme found.

### Inferences
- In 2026 the freelance audit route still means applying to an established collective (Pashov, Zenith, Spearbit via Cantina), not a new marketplace.
- Submission fees are spreading. Immunefi's competitions charge them in 2026, as did the Anza Alpenglow bounty (0.5 SOL, first pass). Fees push down the expected value for low-hit-rate hunters, AI-assisted ones included.

### Gaps
- Immunefi's fee amount is not published.
- I found no Solodit-linked job marketplace and no new 2026 freelance audit board.
- No 2026 funding announcements found for any new security platform.
