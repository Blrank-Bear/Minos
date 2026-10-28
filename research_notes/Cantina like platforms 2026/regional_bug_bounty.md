# Regional and lesser-known bug bounty platforms: 2026 launches (global sweep)

Scope note: Midway through, the user narrowed the scope to platforms or programs launched or unveiled in 2026, searched equally across all regions. Platforms founded earlier are listed in one line each at the end of section 2, labelled "pre-2026". Bittensor/decentralized AI and Web3-only platforms are excluded.

Method: about 17 searches and fetches (searches in English only). Sources were general news and government searches, regional searches (MENA, South/Southeast Asia, Korea/Japan, Africa/Turkey/Ukraine/Central Asia, LATAM), the disclose.io GitHub platform list (about 122 platforms), and the Kensai "100+ platforms" directory (last updated March 2026). I also searched for AI-bounty marketplaces and exploit-acquisition programs.

## 1. Which crowdsourced-security platforms or programs were launched or opened publicly in 2026, region by region?

### Takeaway
I found no new standalone, commercial, publicly joinable bug bounty platform with a confirmed 2026 launch date in any region. The 2026 items that do exist fall into four groups:
- government programs or competitions: Pakistan NADRA, the Swiss e-ID bounty opening publicly, US GSA TTS, India UIDAI
- an existing platform expanding into new regions: BugHunt in LATAM
- one platform that looks pre-launch: bug.sa in Saudi Arabia
- new programs hosted on the big platforms (for example OpenAI on Bugcrowd)

### Cited Findings

**Pakistan: NADRA Bug Bounty Challenge 2026 (government competition, January 2026)**
- NADRA (the national ID authority) launched its "first national Bug Bounty Challenge" on about 27 January 2026. It runs with the Higher Education Commission and the national CERT, and it offers prizes. — [ProPakistani](https://propakistani.pk/2026/01/27/nadra-launches-first-national-bug-bounty-challenge/); [Biometric Update](https://www.biometricupdate.com/202601/nadra-launches-bug-bounty-challenge-to-fortify-pakistans-digital-id-infrastructure); [ARY News](https://arynews.tv/nadra-bug-bounty-challenge-2026); [ID Tech](https://idtechwire.com/nadra-launches-bug-bounty-challenge-2026-to-strengthen-pakistans-digital-identity-systems/)
- It is team-based and reportedly open only to leading universities and partner organisations. Ordinary individual researchers cannot take part. It is a time-boxed challenge, not a standing platform. — [ID Tech / Biometric Update, via search summary](https://idtechwire.com/nadra-launches-bug-bounty-challenge-2026-to-strengthen-pakistans-digital-identity-systems/)

**Switzerland: federal e-ID bug bounty opened to the public (April 2026)**
- The Federal Administration's e-ID bug bounty launched privately in July 2025 and has been open to the public since April 2026. The AGOV government-login bounty has been public since December 2025. The Swiss programmes run on the Bug Bounty Switzerland platform (founded before 2026). — [BACS (Swiss Federal Office for Cybersecurity)](https://www.bacs.admin.ch/en/bug-bounty-programme-to-increase-cyber-resilience-in-the-federal-administration)

**USA: GSA Technology Transformation Service bug bounty (reported July 2026)**
- GSA TTS launched a bug bounty, with HackerOne as the contracted platform. Rewards range from $300 to $5,000. This is a new program on an existing platform, not a new platform. — [ExecutiveGov](https://www.executivegov.com/articles/gsas-tech-transformation-service-launches-bug-bounty-program)

**India: UIDAI (Aadhaar) researcher cohort (April 2026)**
- UIDAI selected 20 bug bounty hunters and white-hat hackers to test Aadhaar systems, working with a private partner. It is a closed, selected cohort, not open signup. — [Biometric Update](https://www.biometricupdate.com/202604/uidai-selects-20-bug-bounty-hunters-to-bolster-indias-digital-id-security)

**Saudi Arabia: bug.sa (looks pre-launch, 2026 status unclear)**
- The site calls itself "Saudi Arabia's bug bounty platform" for organisations and researchers. Search snippets mention CVE registration and payouts in SAR, and the headline reads "Coming soon". When fetched, the page gave no operator, date, eligibility or KYC details. — [bug.sa](https://bug.sa/)
- Not to be confused with the government bugbounty.sa (CST with Tuwaiq Academy, launched at LEAP 2023). That platform's September 2026 figures: more than 30 programs, more than 980 researchers, more than 1,700 reports, and more than SAR 1 million paid. — [SPA](https://www.spa.gov.sa/en/N2668278)
- A 2026 event on bugbounty.sa: the live "Bug Bounty SA Cup" at Black Hat MEA in Riyadh, 1–3 December 2026. Only the top 100 on the bugbounty.sa leaderboard are eligible. — [Black Hat MEA](https://blackhatmea.com/bug-bounty)

**LATAM: BugHunt (Brazil) expands into Spanish-speaking markets (announced April 2026)**
- After six years in Brazil, BugHunt said it is expanding to Mexico, Chile, Peru and Colombia, with projects "underway or in launch phase". It claims more than 25,000 hackers and more than 40 clients (OLX, WebMotors, TIM Brasil). This is a regional expansion of a 2020-era platform, not a new platform. I found no independent confirmation of a launch in Mexico. — [Startups.com.br](https://startups.com.br/negocios/bughunt-avanca-na-america-latina-para-levar-bug-bounty-a-novos-mercados/); [bughunt.com.br](https://bughunt.com.br/)

**Korea: LG Uplus global bug bounty (about August 2026)**
- LG Uplus is the first Korean mobile carrier to run a global bug bounty, hosted on HackerOne. This is a new program, not a new platform. — [BigGo Finance](https://finance.biggo.com/news/5da45715-45aa-433c-8d08-3799ece1aac2)

**Regions with no 2026 platform launch found:** UAE, Turkey, Israel, Africa (Kenya, Nigeria, Egypt), Indonesia, Vietnam, Japan, China, Singapore, Germany, France, Netherlands, Poland, the Nordics, Ukraine, Kazakhstan, Uzbekistan and Nepal. Searches turned up only platforms founded earlier (see section 2). — [Search across disclose.io list](https://github.com/disclose/bug-bounty-platforms); [Kensai directory](https://gokensai.com/blog/bugbountysystems/)

### Inferences
- In 2026, governments acted mainly by adding programs on existing platforms (HackerOne, Bug Bounty Switzerland, bugbounty.sa) or by running closed competitions. None of them created new open platforms.
- For an individual researcher, the most joinable 2026 additions are the Swiss e-ID programme (public since April 2026) and the GSA TTS programme on HackerOne. NADRA and UIDAI are closed.
- Running new programs on established platforms seems to be the norm, which suggests the market for new general bug bounty platforms is consolidated.

### Gaps
- I could not confirm bug.sa's operator, launch date or whether it is live. Check it again directly.
- NADRA's prize amounts, and whether any prizes have been paid, were not verified.
- My searches were in English. Local-language media (Arabic, Turkish, Bahasa, Vietnamese, Korean, Japanese, Chinese, Polish, Ukrainian, Spanish, Portuguese) may report small 2026 launches I did not find.
- Neither directory I used dates its entries, so a 2026 addition to either list could not be confirmed as a 2026 founding.

## 2. Which other crowdsourced-security models were new in 2026 (AI-system bounties, pay-per-vuln pentest marketplaces, VDPs that started paying, exploit acquisition), and which older regional platforms came up?

### Takeaway
In 2026, AI-safety bounties grew a lot, but as vendor programs hosted on Bugcrowd or HackerOne, not as new marketplaces. I found no new legitimate exploit-acquisition program or pay-per-vuln pentest marketplace that launched in 2026.

### Cited Findings
- **OpenAI Safety Bug Bounty** (public, announced 25–26 March 2026, on Bugcrowd). It covers AI abuse and safety issues such as prompt injection, data exfiltration and agent abuse. A third-party guide says the top critical payout is $100,000, which I did not verify with OpenAI. — [OpenAI](https://openai.com/index/safety-bug-bounty/); [Infosecurity Magazine](https://www.infosecurity-magazine.com/news/openai-bug-bounty-ai-abuse-safety/); [Digital Applied, unverified payout figure](https://www.digitalapplied.com/blog/openai-safety-bug-bounty-ai-agent-security-guide)
- **OpenAI Bio Bug Bounty** became an ongoing private program on 9 July 2026. It pays $50,000 for a universal jailbreak (up from $25,000), and requires an application and an NDA. — [TechRepublic](https://www.techrepublic.com/article/news-openai-bio-bounty-jailbreak/); [OpenAI](https://openai.com/index/bio-bug-bounty/)
- **GitHub** moved its bounty to two tiers, public and private, for reports submitted from 27 July 2026, because of a flood of AI-generated reports. — [TechRadar](https://www.techradar.com/pro/security/github-restructures-bug-bounty-program-following-flood-of-ai-generated-reports)
- **Microsoft Zero Day Quest 2026**: nearly 700 cases submitted and $2.3 million awarded. This is a vendor bounty event, not exploit acquisition. — [MSRC blog](https://www.microsoft.com/en-us/msrc/blog/2026/04/zero-day-quest-2026-over-2-million-awarded-vulnerability-research)
- **Exploit brokers**: I found no new legitimate acquisition program in 2026. On 24 February 2026 the US Treasury sanctioned the Russian broker Operation Zero, which shows the risk of the grey market. — [TechCrunch](https://techcrunch.com/2026/02/24/treasury-sanctions-russian-zero-day-broker-accused-of-buying-exploits-stolen-from-u-s-defense-contractor/)
- **Existing legitimate acquisition channels** (pre-2026): ZDI, plus SSD Secure Disclosure (Israel). — [disclose.io list](https://github.com/disclose/bug-bounty-platforms)

**Pre-2026 regional platforms found (one line each, for completeness; none launched in 2026):**
- Bugloud (UAE). Founder Mohammed Tareq Alawadhi, ex-MOI-CERT, already described it as the UAE's first public bounty platform in 2024. Researcher tiers are free, AED 49 and AED 99 per month, and in late 2026 it was still showing 0 of 100 "founding member" spots claimed and placeholder stats. Red flags: paid tiers for researchers and no visible activity. — [bugloud.com](https://bugloud.com/); [HITB 2024 bio](https://conference.hitb.org/hitbsecconf2024auh/speaker/mohammed-tareq-alawadhi/)
- UAE National Bug Bounty: phase one launched in 2021. One source dates a phase or event to January 2025. — [Khaleej Times](https://www.khaleejtimes.com/business/local/uae-cybersecurity-council-launches-national-bug-bounty-programme?web_view=true); [Wattle Corp](https://www.wattlecorp.com/?p=35134)
- Others in the disclose.io and Kensai directories, all founded before 2026:
  - Middle East and Caucasus: Catchify, TrustLine (Saudi Arabia); Crowdswarm (UAE); bugbounty.qa (Qatar); CyberTalents (MENA/Africa); BugBounter (Turkey/Estonia); Ravro, Kolahsefid (Iran); BugBounty.am (Armenia)
  - Africa: Bug Bounty Box (Kenya); Teklabspace (Nigeria)
  - South Asia: Bugbase, Com Olho, Safehats, BugRakshak, Cyber3ra, Pentabug (India); Bugv (Nepal); Bug Zero (Sri Lanka); ZeroDay Test (Bangladesh); NCSA bounty (Maldives)
  - Southeast Asia: Cyber Army Indonesia, RedStorm, Gerobug (Indonesia); WhiteHub, Safevuln (Vietnam); Secuna (Philippines); Swarmnetics (Singapore); thebugbounty (Malaysia)
  - East Asia: Find The Gap, PatchDay (Korea); BBHunt, bugbounty.jp (Japan); Butian, Vulbox, Huoxian, BugBank, BountyTeam (China); Cyberbay (Hong Kong); HITCON ZeroDay (Taiwan)
  - Central Asia: TumarOne (Kazakhstan); UzHunter (Uzbekistan)
  - Europe: BugStream (Ukraine); Hackrate (Hungary); HACKTIFY (CEE); Findbug (Kosovo); Hackr.fi (Finland); Nordic Defender (Sweden); Zerocopter (Netherlands); Yogosha (France); Bug Bounty Switzerland, GObugfree (Switzerland); Genbounty, Bugsbounty.io (UK)
  - LATAM: Bug Hunt, HuntersPay (Brazil); Vulnscope (Chile); Cyscope, Secur0 (LATAM/Europe)
  - Oceania: Capture The Bug (NZ); Bugbop, Dvuln (Australia)
  - AI bounties: 0din (Mozilla), Huntr, Gray Swan Arena, HackAPrompt
  - Sources: [disclose.io](https://github.com/disclose/bug-bounty-platforms); [Kensai](https://gokensai.com/blog/bugbountysystems/)
- PatchDay (Korea, by Theori): one listing gives its program period as 2021-10-05 to 2026-10-05, so it may be ending or stale. — [ooosec](https://ooosec.com/programs/patchday); [bbradar](https://bbradar.io/program/PatchDay:patchday)

### Inferences
- In 2026 the growth area is AI-safety and jailbreak bounties. The money comes from model vendors (OpenAI, Anthropic), and the programs sit on incumbent platforms. That is not a new opportunity in the style of a new regional platform.
- Because of the flood of AI-generated reports (GitHub's two tiers, HackerOne's agentic triage), platforms are moving toward invite-only or tiered access. That trend works against new open platforms appearing.

### Gaps
- I found no verified evidence of any pay-per-vulnerability pentest marketplace, or any VDP that switched to paid rewards, launching in 2026.
- I verified no payout record for any of the regional platforms.
- Kazakhstan and Uzbekistan national programs, and Ukraine government bounties in 2026: searches returned nothing.
