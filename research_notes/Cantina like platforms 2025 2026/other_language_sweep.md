# Cantina-like security earning platforms launched 2025-2026: non-English language sweep

Scope: bug bounty / audit-contest / crowdsourced-testing / AI red-team platforms unveiled or launched in 2025-2026, found through searches in Spanish, Portuguese, French, German, Italian, Polish, Turkish, Russian, Ukrainian, Kazakh/Uzbek (via Russian/English), Arabic, Persian and Hebrew, plus English searches for Africa (Nigeria, Kenya). About 38 tool calls. Search date: 2026-10-28.

Bottom line: these languages turn up very few new platforms. There are two real 2025-2026 platform launches: **VulneraPro** (Brazil, June 2025) and **BugSecure Africa** (Senegal, soft launch around Sept/Oct 2026, official launch planned for Dec 2026). The other 2025-2026 activity is one of three things: new government programs or rules placed on existing platforms, a market expansion (BugHunt into LatAm), or a merger (IPv7 acquiring HuntersPay). I found no new Web3 audit-contest platforms and no AI red-team contest platforms marketed mainly in these languages.

## Q1. Which new platforms launched in 2025-2026, marketed mainly in non-English languages?

### Takeaway
Only two verifiable new platforms: VulneraPro (Oi Soluções + IPV7, Brazil, B2B and aimed at banks, June 2025) and BugSecure Africa (Senegal/France founders, payouts in FCFA, early stage in Oct 2026). Both are small and regional. Neither is a public, global earning venue like Cantina.

### Cited Findings

**VulneraPro (Brazil, Portuguese). Launched June 2025 (verified announcement)**
- Oi Soluções announced VulneraPro, a bug bounty platform for the Brazilian corporate sector, at Febraban Tech. It is operated with IPV7, which already runs bug bounty programs. Researchers are paid by the severity of what they find. — [IT Forum](https://itforum.com.br/?p=9604430) (403 on fetch; details via search snippet); [Convergência Digital](https://convergenciadigital.com.br/mercado/oi-solucoes-busca-hackers-do-bem-para-combater-ataques-ciberneticos/)
- Pricing for client companies comes in three modes: by time, by budget, or per vulnerability. At first it was offered only to existing Oi Soluções cybersecurity clients. Banking is the main target. — [Convergência Digital](https://convergenciadigital.com.br/mercado/oi-solucoes-busca-hackers-do-bem-para-combater-ataques-ciberneticos/); [IT Forum tag page](https://itforum.com.br/tag/bug-bounty/)
- Background: in Feb 2025 IPv7.security (the security arm of Brazil's IPv7 group) acquired the bug bounty platform HuntersPay. In Mar 2025 Oi Soluções partnered to resell HuntersPay services. — [Teletime, 28 Feb 2025](https://teletime.com.br/28/02/2025/ipv7-security-anuncia-aquisicao-da-hunterspay/); [Teletime, 20 Mar 2025](https://teletime.com.br/20/03/2025/oi-solucoes-e-hunterspay-firmam-parceria-para-bug-bounty-no-brasil/)
- The launch date is inferred: the article says "terça-feira (10)", which matches Tuesday 10 June 2025 during Febraban Tech. I did not see the full article (403).
- Not found: public URL, hunter count, reward ranges, payout evidence, nationality/KYC rules.

**BugSecure Africa (Senegal, French). Soft-launched around Sept/Oct 2026; official launch planned for December 2026 (claimed)**
- Co-founded by Mbaye Sankhe (founder of Kulinda Security; based in France; 12+ years in offensive security at BNP Paribas, Thales, RATP, Orano) and Bilal Ndao. It is pitched as a "sovereign" African platform, with data hosted in Senegal. — [OSIRIS / Le Techobservateur, 19 Oct 2026](https://www.osiris.sn/payer-pour-les-failles-trouvees-le-pari-souverain-de-bugsecure-africa.html)
- At publication it had been running for about 3 weeks. It reported 50 registered researchers, 30 reports processed, one active program (KLDS's internal program), and more than 500,000 FCFA paid out (about USD 800-900; my conversion). — [OSIRIS](https://www.osiris.sn/payer-pour-les-failles-trouvees-le-pari-souverain-de-bugsecure-africa.html)
- Model: companies pay a subscription starting at 85,000 FCFA/month and the platform takes no commission on rewards. Rewards follow each company's severity grid and are paid in FCFA. Severity disputes go to an independent third-party evaluator, with appeal. Researchers are identity-verified (KYC). Sensitive programs can be invite-only. — [OSIRIS](https://www.osiris.sn/payer-pour-les-failles-trouvees-le-pari-souverain-de-bugsecure-africa.html)
- Not found: the platform's own URL; the article does not give one and a search found none.

### Inferences
- VulneraPro is a white-label channel for IPV7/HuntersPay, not a new hunter pool. For hunters, the platform underneath is HuntersPay.
- BugSecure Africa is very early (one in-house program, tiny payouts). It is a regional opportunity for West African/francophone researchers paid in FCFA, not a meaningful earning venue yet.

### Gaps
- VulneraPro URL, public status and payout evidence could not be confirmed (IT Forum and Convergência pages blocked or only partly visible).
- BugSecure Africa URL and whether the December 2026 public launch happened (it is still in the future as of this search).

## Q2. Expansions, government programs and new rules in 2025-2026 (existing platforms)

### Takeaway
In Spanish, Portuguese, Russian, Ukrainian, Azerbaijani and Arabic sources, most 2025-2026 news is new government programs or legal frameworks on existing platforms, not new platforms.

### Cited Findings
- **BugHunt (Brazil) LatAm expansion, 2026.** After 6 years in Brazil it is taking its model to Mexico, Chile, Peru and Colombia. It has 25k+ hackers, aims to add 5-7k by end of 2026, and has no outside investment. Not a new platform (it is already on the known list). — [Startups.com.br](https://startups.com.br/negocios/bughunt-avanca-na-america-latina-para-levar-bug-bounty-a-novos-mercados/) (fetch 403; via search snippet)
- **Russia, Mintsifry (July 2025).** New stage of the e-government vulnerability program covering 9 state services. Open to anyone, up to RUB 1M per bug, runs until 20 Dec 2026. Hosted on existing platforms (Standoff 365). — [ComNews, 9 Jul 2025](https://www.comnews.ru/content/240081/2025-07-09/2025-w28/1008/mincifry-poruchilo-belym-khakeram-proverit-devyat-gosservisov)
- **Russia, market stats (existing platforms only).** In 2025 Standoff Bug Bounty had about 32,000 researchers (+74%), 233 programs, more than RUB 160M paid, and a top reward of RUB 4.97M. — [Habr / Positive Technologies, Jan 2026](https://habr.com/ru/articles/988296). BI.ZONE Bug Bounty: about RUB 100M paid in 2025 for 2.5k reports, about 150 programs. — [ComNews, 19 Jan 2026](https://www.comnews.ru/content/243314/2026-01-19/2026-w04/1008/rossiyskie-kompanii-2025-g-vyplatili-belym-khakeram-100-mln-rub)
- **Russia, Positive Technologies (Dec 2025)** launched bug bounty programs for 15 of its own products, with scenario rewards up to RUB 60M. — [Anti-Malware, 26 Dec 2025](https://www.anti-malware.ru/news/2025-12-26-111332/48577)
- **Russia, Web3 Tech** (blockchain infrastructure provider) opened a private program on Standoff Bug Bounty on 22 Apr 2026. This is the only Web3 item found in Russian sources. It is a program, not a platform. — [via search of cnews/Habr PT news](https://habr.com/ru/companies/pt/news)
- **Ukraine, legal framework (Dec 2025).** Cabinet Resolution No. 1580 of 3 Dec 2025 sets rules for involving ethical hackers in vulnerability searches of state systems and critical infrastructure (via CERT-UA/CSIRTs, State Cyber Protection Centre, and external researchers). No new dedicated platform was named. — [KMU / Mintsyfra](https://www.kmu.gov.ua/news/mintsyfry-bug-bounty-dlia-derzhavnykh-system); [DOU](https://dou.ua/lenta/news/bug-bounty-in-ukraine/)
- **Azerbaijan.** A GOV.AZ bug bounty program ran 15 Apr to 31 Jul 2025 (state SCIS). The national platform Qarabug (qarabug.az) has operated since 2023, so it is older. — [SCIS](https://scis.gov.az/en/news/view/266/xususi-rabite-ve-informasiya-tehlukesizliyi-dovlet-xidmeti-bug-bounty-proqramina-start-verir); [Report.az](https://report.az/ikt/azerbaycanda-bug-bounty-proqrami-basa-catib)
- **EU.** YesWeHack won the European Commission's bug bounty tender (4-year framework, up to about EUR 7.68M), Oct 2025. Existing platform. — [BusinessWire IT](https://www.businesswire.com/news/home/20251001559762/it)
- **Porsche** started its 3rd bug bounty program on 18 Aug 2025, with an AI element (on an existing platform). — [Porsche Newsroom PDF](https://newsroom.porsche.com/pdf/5ffddf2f-4b1e-4507-9660-50e353a3bbd0)

### Inferences
- The CIS/Russian market is consolidated around Standoff 365, BI.ZONE and BugBounty.ru. New 2025-2026 money there flows through these incumbents, which in practice need Russian payment rails or residency (not verified in this sweep).

### Gaps
- Exact hosting platform and eligibility for Ukraine's new framework (still being implemented).

## Q3. Countries/languages with no 2025-2026 launches found (negative results)

### Takeaway
No new 2025-2026 platforms were found in Spain, Mexico, Chile, Colombia, Argentina, France, Morocco, Germany, Italy, Poland, Turkey, Kazakhstan, Uzbekistan, UAE, Egypt, Iran, Israel, Nigeria or Kenya. Older local platforms found are listed in one line each.

### Cited Findings (older platforms, status only)
- Spain, **Secur0** (secur0.com): Spanish bug bounty company and hacker community. Claims 3,500+ vulns reported to 130+ companies and 500+ professionals. Model: annual platform fee plus a percentage per vuln. Founders Javier Juárez and Daniel Ximénez. Founding date not confirmed. — [El Referente](https://elreferente.es/startups/secur0-la-mayor-red-de-hackers-eticos-espanoles/); [Discord](https://discord.com/servers/secur0-bug-bounty-1307703020288741509). Spain also has **CazHack** (older broker). — [Escudo Digital](https://www.escudodigital.com/ciberseguridad/cazar-los-errores-ciberneticos-nos-convierte-en-el-control-de-calidad-de-vulnerabilidades-de-las-empresas.html)
- Oman, "مكافئة صائد الثغرات" (Bug Hunter Reward): private Omani platform that went into official operation in **2024** (interview Jan 2025), so out of scope. — [Oman Daily](https://www.omandaily.om/ampArticle/1171714)
- Iran, **Bugdasht** (باگدشت): launched around 2018-2020, public and private programs, about 300 hunters in 2020. Old. — [Donya-e-Eqtesad](https://donya-e-eqtesad.com/fa/tiny/news-3689031). Iran's Bazaar raised its bounty cap to 1B toman in 2024 (a company program). — [Digiato](https://digiato.com/iran-technology-news/increasing-the-ceiling-of-bug-bounty-bazar)
- Kazakhstan, **BugBounty.kz** / **Tumar.One**: national program from about 2021-2022. Old. — [vc.ru](https://vc.ru/423358-tumarone-pervaya-polnocenno-rabotayushaya-bugbounty-ploshadka-v-sng); [Forbes.kz](https://forbes.kz/news/newsid_261946)
- Uzbekistan: no platform found. Only a 2022 memorandum with Kazakhstan's BugBounty on adoption. — [Trend.az](https://www.trend.az/casia/kazakhstan/3635400.html)
- Turkey, **BugBounter**: from about 2020-2022. No 2025-2026 launches, and no Cybersecurity Presidency bounty program found. — [Para Dergi 2022](https://www.paradergi.com.tr/girisimcilik/2022/01/05/bugbounter-77-milyon-tl-degerlemeye-ulasti)
- Saudi Arabia, the national "منصة مكافآت الثغرات" (bugbounty.sa) launched in 2019 per Saudipedia; the coordinator listed it as 2023. — [Saudipedia](https://saudipedia.com/%D9%85%D9%86%D8%B5%D8%A9-%D9%85%D9%83%D8%A7%D9%81%D8%A2%D8%AA-%D8%A7%D9%84%D8%AB%D8%BA%D8%B1%D8%A7%D8%AA)
- Lebanon, **Bugreader**: 2019. — [Annahar](https://www.annahar.com/arabic/article/981103-bugreader-أول-منصة-لبنانية-لصائدي-الثغر-الأمنية-في-العالم)
- Morocco: DGSSI ran CTFs (2024) and internal audits (2025), but no bounty platform. — [Le360](https://fr.le360.ma/politique/defense-abdellatif-loudiyi-met-en-garde-contre-la-recrudescence-des-cyberattaques_5DG7QFDMJRC7TAH5IXJACO67FM/); [Medias24](https://medias24.com/2024/03/13/la-dgssi-et-secdojo-organisent-le-premier-concours-capture-the-flag-pour-renforcer-la-cybersecurite/)
- Kenya: Safaricom's program runs on HackerOne. No local platform. — [Business Chief](https://businesschief.eu/technology/safaricom-launch-programme-support-ethical-hackers)
- Nepal (seen incidentally), **Bugv** (bugv.io): active program launches in 2026, but founding date not established and outside the requested regions. — [Bugv blog](https://blog.bugv.io/edusanjal-launched-bug-bounty-program/)
- Germany/DACH: demand for EU-hosted platforms is rising under NIS2 (2026), but no new German platform was found. — [shattered.io](https://shattered.io/de/?p=1552)

### Inferences
- In these regions, 2025-2026 growth in demand is being captured by incumbents (YesWeHack, Intigriti, Standoff, BI.ZONE, BugHunt) and by government programs, not by new entrants.
- Web3 audit contests and AI red-team contests stay overwhelmingly English-language and global. I found no native-language Code4rena/Cantina/Sherlock-style entrant in any of the languages searched.

### Gaps
- **Russia, Kiberbastion**: the founder teased a "digital platform" reveal for 3 Aug 2026, and the company publishes bug bounty statistics. Whether it is a bug bounty platform is **unconfirmed**. — [TenChat](https://tenchat.ru/media/5789918-zanaves-priotkryvayetsya); [TenChat stats](https://tenchat.ru/media/4844094-statistika-ot-kiberbastion-bug-bounty--ekonomika-uyazvimostey)
- **Secur0** founding date: its Discord server ID decodes (my calculation from the Discord snowflake) to roughly Nov 2024, which suggests a late-2024/2025 community launch. The company itself may be older. Unverified.
- Searches for Dutch, Swahili, Hebrew (only irrelevant results), Persian 1404 launches, and Arabic UAE/Qatar/Egypt/Jordan all returned nothing relevant. Absence in search is not proof of absence. Local platforms marketed only through Telegram/LinkedIn would be missed.
- Several primary pages (IT Forum, Startups.com.br, El Referente) returned 403, so their details rest on search-engine snippets.
