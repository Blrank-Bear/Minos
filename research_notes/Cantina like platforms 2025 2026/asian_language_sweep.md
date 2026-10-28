# Asian-language sweep: Cantina-like security earning platforms launched 2025–2026

Scope: searches run in Chinese (simplified and traditional), Japanese, Korean, Vietnamese, Thai, Indonesian and India-focused English. About 36 tool calls. **Caveat:** the session-wide WebSearch budget (200 calls per turn, shared with other agents) ran out partway through, so the follow-ups on Cyberbay, Korean exchanges, Theori, SlowMist and ScaleBit/MoveBit, and Thai and Hindi sources were never run. The search engine is US-based and indexes Asian-language news poorly. Many native-language queries returned only pre-2025 or English pages. Treat "not found" here as weak evidence of absence.

## Q1. Which NEW (2025–2026) third-party platforms marketed mainly in Asian languages exist?

### Takeaway
The sweep found very few genuinely new platforms. Inside the window, the confirmed new third-party platforms are CertiK Hunt (Web3, invite-only, July 2026) and SpecSiege (curated Web3 audit contests, July 2026; it surfaced through Chinese-language coverage, but its operator's country is unknown). Two more items are relaunches or rebrands, not new marketplaces: Japan's IssueHunt One (a merger and rebrand, Jan 2026) and China's state-run AI-model crowdtesting campaigns (2025 and 2026). Every other Asian platform found predates 2025.

### Cited Findings

**CertiK Hunt (Web3; bug bounties, audit contests, and AI security challenges planned) — VERIFIED launch 2026-07-01**
- Announced July 1, 2026 as launching "today". It is an invite-only platform for bug bounty programs and audit competitions. AI security challenges are "to be hosted later". Researchers are picked on expertise, past findings, community contributions and reputation, and can apply for an invitation. Projects are vetted before they launch a program. The launch post gives no fees, reward scale, KYC rules or nationality rules — [CertiK blog](https://www.certik.com/blog/introducing-certik-hunt); a Chinese mirror exists — [CertiK CN blog](https://www-cn.certik.com/blog/introducing-certik-hunt)
- Docs: once accepted, a researcher can join every program on the platform without per-program invites — [CertiK Hunt docs](https://hunt.certik.com/docs/getting-started). Rules of conduct are at [hunt.certik.com/legal](https://hunt.certik.com/legal/rules-of-conduct)
- Stated rationale from CertiK's communications head: many researchers face disputes or delayed payments elsewhere, and a curated pool targets that trust problem — [Hackernoon](https://hackernoon.com/certik-launches-invite-only-hunt-platform-for-elite-security-researchers?source=rss); [CryptoBriefing](https://cryptobriefing.com/certik-debuts-invite-only-bug-bounty-platform-for-web3-researchers/)
- First visible Asian client: Korea's WEMIX Foundation moved its bug bounty to CertiK Hunt (announced 2026-10-14 KST). It has three severity tiers, with Critical paying up to $10,000. Rewards are priced in USD and paid in USDT on Ethereum. KYC is required before payout. Only top-tier "Vanguard" researchers can submit formal reports — [Digital Today (KR, CN edition)](https://www.digitaltoday.co.kr/cn/view/114346/wemix-upgrades-bug-bounty-with-certik-hack-threat-detection)
- One search summary said CertiK Hunt replaces the earlier "Skyshield" researcher program. The fetched CertiK blog does not mention this — unverified.
- Red flags and notes: no public payout statistics yet. The project-side reward cap is small ($10k Critical for WEMIX). The platform belongs to an auditor, so a vendor sells audits and also judges bounty severity. CertiK claims it independently reproduces and rates severity — [CertiK Hunt docs](https://hunt.certik.com/docs/getting-started).

**SpecSiege by CODESPECT (Web3 curated audit contests) — VERIFIED launch late July 2026 (via Chinese-language crypto press)**
- Launch tweet dated 2026-07-27; Chinese article dated 2026-07-28. It runs a fixed reward pool as a second review layer after a standard audit. Up to 50 vetted researchers per contest: half from an internal leaderboard, half new applicants. Submissions must be manual and AI-generated ones are rejected. Findings stay confidential unless the protocol chooses to disclose. First contest: an ERC-6909 bond platform, with payouts of about €118–€3,902 per winner — [Bitget News (zh-CN), republishing Mpost](https://www.bitget.com/zh-CN/news/detail/12560605553472); original at [mpost.io zh-CN](https://mpost.io/zh-CN/codespect-rolls-out-specsiege-a-curated-audit-contest-platform-for-web3-security/); company site [codespect.net](https://codespect.net/)
- The articles do not state CODESPECT's country, the SpecSiege URL, KYC rules or nationality rules. Euro-denominated payouts suggest a European operator (an inference). It is small: the first contest's prizes were only in the low thousands of euros.

**IssueHunt One (Japan; Web2 bug bounty plus code-to-cloud security) — VERIFIED 2026-01-20, but a merger and rebrand, not a new marketplace**
- Press release of 2026-01-20: it merges the IssueHunt bug bounty platform with "Baseline" (code-to-cloud), adds AI vulnerability intelligence and an AI diagnosis model, and keeps fully pay-for-results white-hacker testing. The release gives no hacker counts or payout totals — [PR TIMES](https://prtimes.jp/main/html/rd/p/000000238.000039740.html)
- The original IssueHunt bug bounty platform launched in July 2022 — [PR TIMES 2022](https://prtimes.jp/main/html/rd/p/000000006.000039740.html). Old platform, so it does not count as a 2025–26 launch.

**China state "网络安全众测平台" AI large-model crowdtesting (AI red-team bounty campaigns) — VERIFIED 2025 and 2026 campaigns; the platform itself is not new**
- 2025-07-03: CNCERT's 网络安全众测平台 (technical provider 北京数字观星) opened a vulnerability crowdtest of mainstream foundation LLMs and LLM applications. Testers must pass platform review. Rewards go up to RMB 150,000 per vulnerability — [CNVD 众测 notice](https://zc.cnvd.org.cn/news/info?id=173)
- 2026 campaign announced 2026-04-20. Organisers: CNCERT plus the 众测平台, guided by the Central Cyberspace Affairs Commission's office and the NDRC. Technical support: 斗象 (Vulbox) and 补天. Registration closed April 30, testing ran from early May to June 30, in three tracks: open-source LLMs, domestic LLM apps, and agent apps. Over 20 vendors were invited. Vendors fund rewards of up to RMB 100,000 per bug. Results are published as rankings, including "AI安全众测•白帽先锋榜". No nationality rule is stated, but registration runs through Chinese mobile-phone contacts — [CNCERT notice](https://www.cert.org.cn/publish/main/12/2026/20260420085512582844908/20260420085512582844908_.html)
- 360's white paper reports that China's first live-network AI-model crowdtest (2025) found 281 vulnerabilities, over 60% of them LLM-specific — [36Kr](https://36kr.com/p/3556948076575618)

**Hong Kong — Cyberbay "BugHunting Campaign 2025" (program on an existing platform)**
- Co-run by the HK Police Force, the Privacy Commissioner (PCPD) and Cyberbay, "a local crowdsourced cybersecurity company". SME registration opened 2025-06-09 and the campaign ran July–August 2025. "Bounty hunters" must pass technical assessments and background checks, using what the release calls bank-standard ID verification. AI applications are also audited. The campaign series started in 2023, and over 210 SMEs joined in the previous two years. The release names no cash prize amounts — [HK Gov press release](https://www.info.gov.hk/gia/general/202506/09/P2025060900289.htm); details at cyberdefender.hk and cyberbay.tech/events/protectHK2025
- Cyberbay's own launch date was not established, because search ran out. The campaign began in 2023, so Cyberbay likely predates 2025 (an inference).

### Inferences
- English-only sweeps are not missing many new Asian marketplaces. In China, Japan, Korea, Vietnam and Indonesia, 2025–26 activity is mostly new programs on existing platforms, state campaigns, or rebrands.
- The real new Asian-language opportunity type is state-run AI-model crowdtesting in China (RMB 100k–150k caps). It is effectively limited to vetted, China-reachable testers, and probably closed to foreigners in practice (inferred: Chinese phone registration, CNCERT-run).
- CertiK Hunt is the only new platform with clear Asian distribution: CertiK has a Chinese-language site and a Korean client, WEMIX. Its invite-only, KYC, Vanguard-tier model makes it hard to enter.

### Gaps
- The SpecSiege URL, CODESPECT's jurisdiction, and SpecSiege's KYC rules were not found.
- No payout totals for CertiK Hunt.
- No platform URL for the China 网络安全众测平台 (only zc.cnvd.org.cn appears), and no explicit rule on foreign participants.

## Q2. Country-by-country: what was checked and what predates 2025 (one line each)

### Takeaway
Searches in each country's language turned up no other 2025–26 platform launches. The only additions are government or corporate programs, listed here so they are not mistaken for platforms.

### Cited Findings
**China (Web2 众测):** The established third-party platforms are all pre-2025: 漏洞盒子 Vulbox, 补天 Butian, 火线 Huoxian, 雷神众测 BountyTeam, 腾讯众测, 360众测, 漏洞银行, CNVD众测, 微步 ThreatBook 通用漏洞奖励, 先知 (Alibaba Cloud). A May 2026 list of them gives no launch dates and labels none as new — [hilangdev blog, 2026-05-13](https://hilangdev.xyz/%E5%9B%BD%E5%86%85src%E4%B8%8E%E6%BC%8F%E6%B4%9E%E8%B5%8F%E9%87%91%E5%B9%B3%E5%8F%B0%E6%B1%87%E6%80%BB/)
- 斗象 (Vulbox's parent, founded via FreeBuf in 2014) is repositioning as an "AI security cloud platform". That is a pivot, not a new bounty platform — [上海证券报 2025-10](https://paper.cnstock.com/html/2025-10/10/content_2129479.htm)
- 腾讯安全众测平台: an April 2026 talk describes AI-driven pentest contests (AI渗透赛, 大模型安全赛). The talk gives no launch date and does not present the platform as new — [Tencent Cloud Dev, 2026-04-04](https://cloud.tencent.com/developer/article/2650328)
- Web3 China firms: searches for new bounty platforms from SlowMist, Beosin or ExVul returned nothing. SlowMist's co-founder earlier built Seebug (old) — [36Kr pitchhub](https://pitchhub.36kr.com/project/2090264771707783). BitsLab ran a "Web3护航计划" campaign (date and payout details not retrieved, page empty) — [learnblockchain.cn](https://learnblockchain.cn/article/14409)

**Japan:** IssueHunt (2022), IssueHunt VDP (Jan 2023), Bugty (3-shake, operations agency with Intigriti, 2021), ZONE ZERO (Vector Digital, 2024-05-15) — [PR TIMES search results: IssueHunt 2022](https://prtimes.jp/main/html/rd/p/000000006.000039740.html), [Bugty](https://prtimes.jp/main/html/rd/p/000000040.000024873.html), [IssueHunt VDP](https://prtimes.jp/main/html/rd/p/000000009.000039740.html). The only 2025–26 item is IssueHunt One (see Q1).

**Korea:** FindTheGap 파인더갭 (formerly HackingZone; about 7,000 ethical hackers, KYC plus VDI/VPN private model), Enki BugCamp 버그캠프 (2021-07). Both pre-2025 — [Boannews rename](http://www.boannews.com/media/view.asp?idx=107664), [DailySecu BugCamp](https://www.dailysecu.com/news/articleView.html?idxno=126743), [VentureSquare](https://www.venturesquare.net/944300)
- 2025–26 programs, not platforms: LG U+ ran Korea's first telecom global bug bounty on HackerOne (2026) — [LG release](https://www.lg.co.kr/media/release/30487), [FN News](https://en.fnnews.com/news/202608240857099469). UnetSystems is HackerOne's Korean reseller — [etnews 2025-12](https://www.etnews.com/20251217000093). The FSS/FSI 2026 financial-sector bug bounty grew from 32 to 70 firms, now including crypto firms, with a top reward of KRW 10M and submissions through FSI's platform — [Bloomingbit JP](https://jp.bloomingbit.io/feed/news/112287). Genians widened its bounty to all products in Feb 2026 — [Digital Today](https://www.digitaltoday.co.kr/jp/view/75922/genians-shares-bug-bounty-results-reports-up-129-percent-in-first-half)
- AI red team: MSIT/TTA "생성형 AI 레드팀 챌린지" ran in April 2024 with no prize reported; Selectstar co-ran a "Global AI Red Team Challenge" with GSMA at MWC 2025. These are events, not platforms — [NewsSeoul](https://newsseoul.co.kr/news/view/1065601204005979), [VentureSquare](https://www.venturesquare.net/958992/)

**Vietnam:** WhiteHub (CyStack, launched April 2019, about 4,000 researchers claimed) and Vietnam Bug Bounty (VSEC with the national cyber monitoring centre, 2019). Both are old, and no 2025–26 launch was found — [vjst.vn](https://vjst.vn/whitehub-nen-tang-phat-hien-va-quan-ly-lo-hong-dau-tien-tai-viet-nam-67934.html), [VietnamNet](https://vietnamnet.vn/ra-mat-nen-tang-ho-tro-ket-noi-doanh-nghiep-voi-cac-chuyen-gia-bao-mat-whitehub-i30657.html)

**Indonesia:** CyberArmyID (founded 2018; bug bounty platform listed in its 2022 deck), old — [ITB-hosted deck](https://isg.stei.itb.ac.id/wp-content/uploads/2022/10/CyberArmyID-Deck-2022-1.pdf). New in 2026: the Ministry of Primary and Secondary Education (Kemendikdasmen) bug bounty opened 2026-04-06. It is a government program run in a sandbox by the ministry's Pusdatin, not a platform — [RRI](https://rri.co.id/voice-of-indonesia/technology/2320740/indonesia-advances-cyber-resilience-in-education-through-bug-bounty-program), [gebrak.id](https://www.gebrak.id/2026/04/bug-bounty-2026-resmi-dibuka.html)

**India:** BugBase (2022 seed funding), Cyber3ra (Nagpur; launch year not confirmed, Daily Swig coverage suggests it is older) — [Entrepreneur India](https://india.entrepreneur.com/news-and-trends/bugbase-raises-500000-in-funding-led-by-2am-vc/431669), [Daily Swig](https://portswigger.net/daily-swig/new-bug-bounty-platform-launches-for-indian-ethical-hackers). New program: UIDAI's first structured Aadhaar bug bounty (March 2026), invite-only panel of 20 researchers — [News on AIR](https://www.newsonair.gov.in/uidai-launches-first-structured-bug-bounty-programme-to-strengthen-aadhaar-system-security)

**Taiwan:** HITCON ZeroDay is a non-profit matching platform that does not handle money; an invite-only bounty feature was in beta at an undated time. No 2025–26 change was found — [iThome](https://www.ithome.com.tw/news/124844)

**Thailand / Southeast Asia:** No new Thai platform was found. Regional 2025–26 activity is programs on Western platforms: Agoda went public on HackerOne (June 2026, up to $6,000), and Grab marked 10 years on HackerOne — [TechNode Global](https://technode.global/2026/06/23/tourism-platform-agoda-launches-public-bug-bounty-program-on-hackerone-rewards-up-to-6000/), [HackerOne](https://www.hackerone.com/blog/grab-10-years-bug-bounty-anniversary)

### Inferences
- Asian markets are served mostly by established local platforms (Vulbox, Butian, FindTheGap, WhiteHub, IssueHunt) and by Western ones through resellers (UnetSystems for HackerOne in Korea; Takachiho selling XBOW in Japan). New entrants in 2025–26 have gone after Web3 (CertiK) or AI, not general Web2.
- Most Chinese, Korean and Indonesian platforms and government programs require local identity or real-name verification (FindTheGap uses KYC; China's 众测 needs platform review; Kemendikdasmen targets students and lecturers). They are poor targets for a foreign earner (inference; nationality rules are mostly not stated).

### Gaps
- Searches not run because the budget ran out: Hindi-language and Thai-native follow-ups; Korean exchanges (Upbit and Bithumb platforms); Theori; Chinese Web3 auditors ScaleBit, MoveBit, Salus, Secbit, Hacken Asia; Cyberbay's founding date; 补天 and 漏洞盒子 2025–26 product launches.
- Whether 腾讯众测 (zc.tencent.com) or ThreatBook's 通用漏洞奖励 page launched in 2025–26 could not be confirmed. No dated launch announcement was found.

## Q3. Red flags and quality signals across findings

### Takeaway
None of the new entrants shows payout evidence yet. The best-documented money in this sweep is in state-run Chinese AI crowdtests, and those are effectively closed to outsiders.

### Cited Findings
- CertiK Hunt: invite-only, KYC, and Vanguard-only submission for WEMIX. The visible reward cap is $10k, paid in USDT. No payout stats — [Digital Today](https://www.digitaltoday.co.kr/cn/view/114346/wemix-upgrades-bug-bounty-with-certik-hack-threat-detection), [CertiK blog](https://www.certik.com/blog/introducing-certik-hunt)
- SpecSiege: small pools (€118–€3,902 per winner in contest one), and AI-assisted submissions are banned — [Bitget/Mpost](https://www.bitget.com/zh-CN/news/detail/12560605553472)
- China AI crowdtests: large caps (RMB 150k in 2025, RMB 100k in 2026). Vendors pay, not the platform, and payout realisation is not documented — [CNVD](https://zc.cnvd.org.cn/news/info?id=173), [CNCERT](https://www.cert.org.cn/publish/main/12/2026/20260420085512582844908/20260420085512582844908_.html)
- Industry-wide: AI-generated junk reports are pushing platforms toward curation and stake-to-submit. For example, Solana's Firedancer requires burning 1 SOL per report — [TechFlow](https://www.techflowpost.com/en-US/article/34902); [PANews](https://www.panewslab.com/zh-hant/articles/019db412-c18d-7464-a0cf-1b06672dfb32)

### Inferences
- The 2026 trend is toward curated, invite-only, KYC-gated models (CertiK Hunt, SpecSiege), partly as a reaction to AI-slop reports. New entrants will be harder to join than open platforms like Cantina or Immunefi.

### Gaps
- No independent researcher testimonials or payout disputes were found for CertiK Hunt or SpecSiege. Both are too new, and search was cut short.
