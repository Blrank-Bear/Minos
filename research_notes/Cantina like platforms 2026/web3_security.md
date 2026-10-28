# Web3 / Smart-Contract Security Earning Platforms: 2026 Launches and Status Changes

Research date: 2026-10-28. Note on source quality: most of what follows comes from search-result summaries and a few fetched pages (16 tool calls in total). "Verified" means an official page or at least two independent outlets. "Claim" means a press release or the company's own statement.

## Q1. New platforms launched or opened publicly in 2026

### Takeaway
I could confirm only two genuinely new contest/bounty platforms in 2026: **CertiK Hunt** (1 July 2026, invite-only bounties, audit competitions and AI security challenges) and **CODESPECT SpecSiege** (about July 2026, a curated re-audit contest capped at 50 researchers). The other 2026 launches I found are AI audit products, not earning platforms: Sherlock Audit Engine, CertiK AI Auditor and Cyberscope's Cyberscan AI. I found no new decentralized on-chain bounty protocol and no chain-specific contest platform launched in 2026. The Solana Alpenglow bounty was a one-off competition run by Anza.

### Cited Findings
**CertiK Hunt** (certik.com; blog "Introducing CertiK Hunt")
- Announced and launched **1 July 2026**. Three program types: bug bounty programs, audit competitions (time-bound, competitive) and "AI security challenges" focused on AI-driven vulnerability discovery — [CertiK blog (official)](https://www-cn.certik.com/blog/introducing-certik-hunt)
- **Invite-only on both sides.** Researchers are selected on technical expertise, past findings, community contributions and reputation ("Unlike open platforms that allow anyone to submit reports, CertiK Hunt is intentionally invite-only"). Projects are also reviewed before they can launch programs — [CertiK blog](https://www-cn.certik.com/blog/introducing-certik-hunt)
- The blog does **not** state KYC rules, reward amounts, fees or payout terms, and names no launch partners. It mentions only a leaderboard, "exclusive rewards" and "flexible triaging tiers" for projects — [CertiK blog](https://www-cn.certik.com/blog/introducing-certik-hunt)
- Secondary coverage says CertiK justifies the vetting by pointing to disputes and delayed payouts on open platforms, and lists Sherlock, Cantina and HackenProof as rivals with invite-only tracks — [HackerNoon](https://hackernoon.com/certik-launches-invite-only-hunt-platform-for-elite-security-researchers?source=rss); [ThreatCluster (aggregator)](https://threatcluster.io/cluster/certik-launches-invite-only-bug-bounty-platform-for-web3-sec-d1a0794c)
- First named program I found: on **14 Oct 2026** WEMIX relaunched its joint bug bounty with CertiK on CertiK Hunt, paying **up to $10,000 per finding** by severity — [Webull/news wire](https://www.webull.com/news/15744748814672896)
- Note: CertiK ran a bounty product called "CertiK Hunt" before 2026; WEMIX's 2026 program is described as an "upgraded" one. The July 2026 launch looks like a relaunch or rebrand as an invite-only platform rather than a brand-new name — [Webull headline "Upgraded CertiK Hunt Bug Bounty Program"](https://www.webull.com/news/15744748814672896) (inference from the wording; not confirmed)

**CODESPECT SpecSiege**
- Reported on **27 July 2026** as just launched. It is a closed "re-audit" contest: after CODESPECT's own audit, the fixed codebase goes to a vetted group of **up to 50 researchers**, half from CODESPECT's leaderboard and half new applicants, who compete for a preset, fixed-budget pool. Payouts are severity-weighted points — [Mpost](https://mpost.io/codespect-rolls-out-specsiege-a-curated-audit-contest-platform-for-web3-security/)
- It explicitly **excludes AI-generated or automated submissions** — [Mpost](https://mpost.io/codespect-rolls-out-specsiege-a-curated-audit-contest-platform-for-web3-security/); [EdgeX news](https://pro.edgex.exchange/en-US/news/article/codespect-launches-specsiege-web3-audit-contest-platform)
- First contest: an ERC-6909 bond platform. Top payouts were only about **€118 to €3,902**, so the scale is small. KYC and backers are not stated — [Mpost](https://mpost.io/codespect-rolls-out-specsiege-a-curated-audit-contest-platform-for-web3-security/)

**AI audit products launched in 2026 (not earning platforms, context only)**
- **Sherlock Audit Engine**, unveiled 18 Aug 2026 (sponsored press release). It is an "orchestration layer for AI-native security review" that combines frontier LLMs, purpose-built AI auditors and AI-enabled human researchers, then judges, validates and deduplicates their findings into one report. No pricing or named customers. Sherlock claims 200+ engagements in H1 2026 — [Decrypt (sponsored PR)](https://decrypt.co/375876/sherlock-unveils-audit-engine-as-ai-security-race-accelerates)
- **CertiK AI Auditor**, April 2026 (secondary summary only) — [search summary; source list in Decrypt/Mpost results](https://decrypt.co/375876/sherlock-unveils-audit-engine-as-ai-security-race-accelerates)
- **Cyberscan AI** (Cyberscope / TAC InfoSec), May 2026. A free AI smart-contract scanner — [NSE filing PR](https://nsearchives.nseindia.com/corporate/TAC_13052026214546_Cyberscan_PR_India.pdf)
- **Nethermind AgentArena**: parallel AI audit agents with an arbiter/triage layer. Known only from a job listing, so the launch date is unverified — [CryptoJobsList](https://cryptojobslist.com/jobs/web3-security-triager-auditagent-at-nethermind)

**Notable chain-specific 2026 competition (one-off, not a platform)**
- **Solana Alpenglow bounty**, run by **Anza** (Agave client team), **not Cantina**. Pool up to **50,000 SOL**. Ran **5 to 19 Aug 2026**, with submissions only via Anza's portal and a **non-refundable 0.5 SOL fee per finding** (a controversial anti-spam measure). Adjudication ran to 2 Sep 2026 — [anza-xyz/alpenglow GitHub](https://github.com/anza-xyz/alpenglow); [CryptoSlate](https://cryptoslate.com/solanas-alpenglow-bug-hunt-charges-researchers-0-5-sol-to-report-flaws/); [Solana Compass](https://solanacompass.com/news/anza-announces-alpenglow-bug-bounty-competition-before-solana-consensus-mainnet)
- It drew **300+ submissions**. Payout results were not found — [Crypto Briefing](https://cryptobriefing.com/solana-alpenglow-bug-bounty-closes/)
- I found no source tying Alpenglow to Cantina, so the brief's lead ("Solana Alpenglow on Cantina, Aug 2026") **appears incorrect** — [Cantina competitions docs (no mention)](https://docs.cantina.xyz/for-organizations/security-solutions/competitions)

### Inferences
- The 2026 trend runs toward **curation and invite-only access** (CertiK Hunt, SpecSiege, Sherlock and Cantina private tracks) and toward **AI-orchestrated review**, not new open platforms. For a newcomer, open entry points are shrinking.
- SpecSiege's no-AI rule and CertiK Hunt's "AI security challenges" point in opposite directions on AI-assisted hunting.
- Red flags: CertiK Hunt publishes no reward or fee terms. SpecSiege pays at a small scale. Alpenglow charged researchers a submission fee.

### Gaps
- KYC policy, fees and verified payout totals for CertiK Hunt: not published.
- I could not check Sui, Aptos, TON, Starknet or Base for new 2026 security programs within my tool budget. No results surfaced.
- I found no new decentralized or on-chain bounty protocol launched in 2026.
- I did not search whether any established platform formally "left beta" in 2026.

## Q2. 2026 status of established platforms

### Takeaway
The biggest 2026 event is the **Code4rena wind-down (announced 13 May 2026)**, with **Immunefi onboarding its bug-bounty customers and researchers**. **Hats Finance** shut down its hosted service at the end of **2025**. Immunefi, Cantina, Sherlock, HackenProof and CodeHawks remain active. Cantina won large 2026 bounties (OKX DEX, Paxos). I found **no evidence of a Cantina move to cantina.security**: all results point to cantina.xyz.

### Cited Findings
**Code4rena: winding down (verified, The Block plus multiple outlets)**
- **13 May 2026**: Code4rena posted on X, "After careful consideration, we've made the decision to wind down Code4rena." Open contests and bounties were to be completed and active engagements "seen through to a proper close" — [The Block](https://www.theblock.co/post/401179)
- Background: Paradigm-backed ($6M raise, 2023); acquired by Zellic in 2024 with a promise to stay independent — [The Block](https://www.theblock.co/post/401179)
- Context cited: more than 20 crypto exploits in April 2026, a monthly record per DefiLlama; DeFi TVL down from about $160B (Oct 2025) to about $83B — [The Block](https://www.theblock.co/post/401179)

**Immunefi**
- Absorbing Code4rena's **bug-bounty** customers and researchers and helping move scopes, rules and reward structures over. Immunefi said "Code4rena played a huge role in shaping crypto security." **Verified** — [The Block](https://www.theblock.co/post/401179); also [ChainCatcher](https://www.chaincatcher.com/en/article/2264611), [AMBCrypto](https://ambcrypto.com/?p=598300)
- Stats: 45,000+ researchers, 650+ programs, $110M+ paid out. Median confirmed payout about $2,000, average about $52,800. Largest listed bounty: Uniswap v4 at $15.5M. These are reported by competitor Sherlock with figures "as of March 2026" — [Sherlock blog, 31 Aug 2026](https://sherlock.xyz/post/best-web3-bug-bounties-in-2026-the-highest-paying-programs-on-every-platform)
- **IMU token** reportedly launched **22 Jan 2026** (single secondary blog, unverified) — [BlockEden](https://blockeden.xyz/de/blog/2026/01/25/immunefi-imu-token-web3-security-bug-bounty-platform/)
- Magnus (AI SecOps command center) dates from **Feb 2025**, not 2026 — [The Block, 2025](https://www.theblock.co/post/343177/immunefi-rolls-out-magnus-an-ai-powered-command-center-to-streamline-onchain-security)

**Cantina (Spearbit network)**
- Still at **cantina.xyz**. I found no evidence of a cantina.security domain. Its docs now describe it as an "agentic security platform" covering audits, bounties, competitions and pentesting. A third-party directory lists products Clarion and Apex (unverified) — [Cantina docs](https://docs.cantina.xyz/about-cantina/about-cantina); [cybersectools (third-party)](https://cybersectools.com/companies/cantina)
- **30 Jan 2026**: $1M OKX DEX on-chain bug bounty with OKX Labs — [MEXC news](https://www.mexc.com/news/597030)
- **March 2026**: Paxos bounty up to $1M (in USDG) covering PYUSD, PAXG and USDG — [MEXC news](https://www.mexc.com/news/594955)
- BitGo multisig bounty (critical tier $75k); Cantina Bug Bounty Cover with Nexus Mutual (protocol pays at most 20% of a critical, Nexus covers the rest; launch date not confirmed as 2026); Cantina claims 5,000+ researchers — [BitGo](https://www.bitgo.com/resources/blog/bitgo-launches-bug-bounty-program-on-cantina.md); [Nexus Mutual](https://nexusmutual.io/blog/cantina-partners-with-nexus-mutual-to-launch-bug-bounty-and-native-protocol-cover)
- Largest listed Cantina bounty: Coinbase/Base at $5M — [Sherlock blog](https://sherlock.xyz/post/best-web3-bug-bounties-in-2026-the-highest-paying-programs-on-every-platform)

**Sherlock**
- New in 2026: Audit Engine (Aug 2026) and "Institutional Security." **Usual bounty, $16M** (launched March 2026, per Sherlock itself; no independent confirmation). An Aave V4 bounty on Sherlock was proposed and still in governance — [Sherlock blog](https://sherlock.xyz/post/best-web3-bug-bounties-in-2026-the-highest-paying-programs-on-every-platform); [Decrypt PR](https://decrypt.co/375876/sherlock-unveils-audit-engine-as-ai-security-race-accelerates)
- Ethereum Foundation **Fusaka** contest ($2M, 15 Sep to 13 Oct **2025**, 4 highs found) was run on Sherlock. **That was 2025.** I found no 2026 EF contest (e.g., Glamsterdam) — [The Block 2025](https://www.theblock.co/post/370846/ethereum-devs-open-fusaka-upgrade-to-2-million-security-audit-contest); [Sherlock case study](https://sherlock.xyz/case-studies/ethereumfoundation)

**HackenProof / Hacken**
- Active. In **May 2026**: six contests, $603,760 in bug bounty payouts, 7,785 reports — [HackenProof payouts May 2026](https://hackenproof.com/blog/bug-bounty-payouts-may-2026)
- **DualDefense** product (audit plus a 30-day contest/coverage pool). 2026 contests include ZIGChain (up to $75k, Jan) and Dexalot (up to $7k, Apr) — [HackenProof DualDefense](https://hackenproof.com/blog/dualdefense)
- 200+ programs; NEAR Intents Bridges (Mar 2026) and Citrea (Feb 2026) — [Sherlock blog](https://sherlock.xyz/post/best-web3-bug-bounties-in-2026-the-highest-paying-programs-on-every-platform)

**CodeHawks (Cyfrin)**
- Active, with First Flights running in Jan 2026. The last major change I found was CodeHawks v2 in **Aug 2024** (USDC payouts on ZKsync). No 2026 change found — [Cyfrin blog](https://www.cyfrin.io/blog/introducing-the-new-cyfrin-codehawks-update); [CodeHawks docs](https://docs.codehawks.com/)

**Hats Finance: shut down (2025)**
- Announced **1 Dec 2025**: hosted UI and back-end offline **31 Dec 2025**, custodial withdrawals before 17 Dec. The on-chain protocol remains under the DAO, but there is no active team — [Coinotag](https://en.coinotag.com/breakingnews/hats-token-faces-wind-down-as-hats-finance-phases-out-custodial-services-by-december-31-2025); [ChainCatcher](https://www.chaincatcher.com/en/article/2225329)
- Sherlock's Aug 2026 article still lists Hats as "active," which looks stale — [Sherlock blog](https://sherlock.xyz/post/best-web3-bug-bounties-in-2026-the-highest-paying-programs-on-every-platform)

**Secure3, Remedy, Spearbit, Zellic**
- Secure3: no 2026 news found. Directory funding data is from 2022 — [Dealroom](https://app.dealroom.co/companies/secure3)
- Remedy: only a 2025 CTF ($50k+, Hexens-sponsored) found; nothing from 2026 — [Web3SecNews](https://web3secnews.substack.com/p/are-you-ready-for-the-biggest-web3)
- Zellic: as Code4rena's owner it oversaw the wind-down. I found no other 2026 news about Zellic itself — [The Block](https://www.theblock.co/post/401179)
- Spearbit operates as Cantina's researcher network; nothing separate found for 2026 — [Cantina docs](https://docs.cantina.xyz/about-cantina/about-cantina)

### Inferences
- With Code4rena gone in 2026 and Hats gone at end of 2025, the main **open** competitive-audit venues left are Sherlock, Cantina, CodeHawks, and HackenProof's contests. Immunefi dominates bounties. An open-contest researcher has fewer venues than in 2025.
- Immunefi took over Code4rena's **bounty** customers. Coverage does not say who inherits Code4rena's **competitive-audit** business. Sherlock and Cantina are the natural beneficiaries, but I found no source confirming this.

### Gaps
- Exact final date of the last Code4rena contest, and whether code4rena.com and its leaderboard remain archived: not found.
- No independent confirmation of Sherlock's $16M Usual bounty or of Immunefi's IMU token.
- Cantina domain move to cantina.security: **no evidence found**. Treat it as unconfirmed or false.
- No 2026 funding rounds or acquisitions found for any platform (I did not check Crunchbase or Dealroom directly).
- Not researched for lack of budget: Hacken corporate news, Secure3 activity, Zellic's own 2026 products, Sui/Aptos/TON/Starknet/Base programs.
