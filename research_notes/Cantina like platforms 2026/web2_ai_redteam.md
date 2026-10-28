# Web2 Bug Bounty and AI Red-Teaming / AI Safety Bounty Platforms: New or Changed in 2026

Research date: 2026-10-28. About 17 tool calls. Several primary pages (openai.com, securityweek.com) returned HTTP 403, so some figures come from search-result summaries of those pages and are marked as such. "Verified" means a primary or first-hand source was read. "Reported" means secondary or aggregator coverage only.

## Q1: New Web2 bug bounty / crowdsourced security / PTaaS platforms launched or opened publicly in 2026 (incl. regional and government)

### Takeaway
I found no clearly sourced new general-purpose Web2 bug bounty platform, and no new national government bug bounty platform, that launched in 2026. Most of the 2026 activity was programs moving between existing platforms (Adobe to Intigriti) and small regional programs launching on existing regional platforms (Bugv, Nepal). The one notable new "platform" I found, CertiK Hunt, is Web3 and invite-only.

### Cited Findings
- **CertiK Hunt** (Web3 firm CertiK): announced July 1, 2026 as an **invite-only** platform where blockchain projects run bug bounties, audit competitions and "AI-powered security challenges", with researchers vetted before joining. This is a Web3 platform, so it overlaps another researcher's scope. I saw only press-release coverage and no verified payouts. — [HackerNoon](https://hackernoon.com/certik-launches-invite-only-hunt-platform-for-elite-security-researchers)
- **Adobe moves its bug bounty program to Intigriti** from **September 1, 2026**. All new reports go through Intigriti from that date. This is a migration, not a new platform, but it is a notable gain for Intigriti. — [Adobe Security blog](https://blog.adobe.com/security/a-new-home-for-the-adobe-bug-bounty-program) (seen via search snippet, page not fetched)
- **Bugv (Nepal regional platform)** posted several small 2026 program launches: RedVault Security (Jul 5, 2026), Dealkhana (Jul 12), ZoZo Hub (Jul 12), Programiz (Aug 23), UG Bazaar (Aug 24). The search summary put rewards at roughly $10–$800 per bug. Bugv is not new in 2026, and some post dates look inconsistent. — [Bugv blog: Programiz](https://blog.bugv.io/programiz-launched-a-bug-bounty-program/), [Bugv blog: RedVault](https://blog.bugv.io/redvault-security-launched-a-bug-bounty-program/), [Bugv blog: UG Bazaar](https://blog.bugv.io/ug-bazaar-launched-bug-bounty-program/)
- **Government programs:** a search for 2026 national or government bug bounty platform launches found only older programs. Examples are Azerbaijan's GOV.AZ bounty (Apr 15–Jul 31, **2025**), Hack DHS (FY2022), and the GSA/TTS program on HackerOne (**2017**). — [SCIS Azerbaijan](https://scis.gov.az/en/news/view/266), [SecurityWeek: Hack DHS](https://www.securityweek.com/us-government-launches-hack-dhs-bug-bounty-program/amp/), [ExecutiveGov: GSA](https://www.executivegov.com/2017/05/gsas-tech-transformation-service-launches-bug-bounty-program/)
- **Immunefi** IMU token launch on Jan 22, 2026 (Web3, listed for completeness only). — [MEXC news](https://www.mexc.com/news/438949)

### Inferences
- In 2026 the Web2 platform market looks consolidated, with incumbents (HackerOne, Bugcrowd, Intigriti, YesWeHack) gaining programs instead of new entrants appearing. A new "platform" in 2026 is more likely to be an AI-agent pentest product from an incumbent (see Q3) than a new crowdsourced marketplace.
- Regional platforms such as Bugv offer low payouts (tens to hundreds of USD). They are a way to build reputation, not a meaningful source of income.

### Gaps
- My searches did not cover regional newcomers in the Middle East (e.g., Saudi or UAE national platforms), Africa, LATAM, India, Japan or Korea for 2026. I have no confirmed 2026 launches there, and targeted per-country searches would be needed.
- I did not search for new PTaaS startups that opened public researcher signups in 2026.

## Q2: AI red-teaming / jailbreak / AI safety bounty platforms and programs new in 2026

### Takeaway
The two largest verified 2026 AI items are the **OpenAI Safety Bug Bounty** (public, on Bugcrowd, launched March 25, 2026) and **Gray Swan's Arena 2.0 relaunch with the $300K "IPI Black" indirect-prompt-injection competition** (October 20, 2026, sponsored by Anthropic, Meta, Google DeepMind and Reflection AI). Anthropic's model-safety bounty is ongoing from 2024 and remains application/invite-gated on HackerOne.

### Cited Findings
**OpenAI Safety Bug Bounty (new in 2026)**
- Launched **March 25, 2026** as a **public** program for AI abuse and safety risks. It sits alongside the existing Security Bug Bounty and takes reports that are not classic security vulnerabilities. — [OpenAI](https://openai.com/index/safety-bug-bounty) (403 when fetched; date from search summary), [StartupHub.ai](https://www.startuphub.ai/ai-news/artificial-intelligence/2026/openai-launches-safety-bug-bounty.md)
- Scope: prompt injection and data exfiltration, agentic products taking disallowed actions at scale, and vulnerabilities in connectors and MCP integrations. Generic content-policy bypasses without demonstrable impact are excluded. — [SecurityWeek](https://www.securityweek.com/openai-launches-bug-bounty-program-for-abuse-and-safety-risks/amp/), [ThreatCluster](https://threatcluster.io/cluster/openai-launches-safety-bug-bounty-program-to-address-ai-abus-12f4b80b)
- Platform: **Bugcrowd**. OpenAI's Safety and Security bounty teams triage reports and may reroute them between the two programs. — [SecurityWeek](https://www.securityweek.com/openai-launches-bug-bounty-program-for-abuse-and-safety-risks/amp/), [ThreatCluster](https://threatcluster.io/cluster/openai-launches-safety-bug-bounty-program-to-address-ai-abus-12f4b80b)
- **Sources conflict on rewards.** SecurityWeek reports up to **$7,500** for consistently reproducible, high-severity reports with clear mitigations, at OpenAI's discretion. Storyboard18 reports "up to **$100,000**" for critical issues. The $100K figure is probably the Security Bug Bounty maximum (raised to $100K in 2025) and may have been conflated. Treat **$7,500** as the more credible safety-bounty ceiling until it is checked on openai.com. — [SecurityWeek](https://www.securityweek.com/openai-launches-bug-bounty-program-for-abuse-and-safety-risks/amp/); contradicted by [Storyboard18](https://storyboard18.com/digital/openai-launches-safety-bug-bounty-program-with-payouts-up-to-100000-93422.htm)
- Storyboard18 reports safe-harbour protections for good-faith researchers. — [Storyboard18](https://storyboard18.com/digital/openai-launches-safety-bug-bounty-program-with-payouts-up-to-100000-93422.htm)

**Gray Swan Arena (Arena 2.0 and IPI Black, 2026), verified via Fortune**
- On **Oct 20, 2026** Gray Swan launched a redesigned "Arena 2.0" alongside **IPI Black**, its largest competition so far: **$300,000** in prizes, sponsored by **Anthropic, Meta, Google DeepMind and Reflection AI**. New attack scenarios release weekly through **Nov 2, 2026**. The target is indirect prompt injection against AI agents. — [Fortune](https://fortune.com/2026/10/20/exclusive-ai-security-company-gray-swan-red-team-arena-contest-to-jailbreak-ai-agents/)
- The public Arena uses guardrailed models and requires a human to drive each agent. Gray Swan also runs **private, NDA-bound arenas** for frontier labs, sometimes with unguardrailed models and vetted participants. — [Fortune](https://fortune.com/2026/10/20/exclusive-ai-security-company-gray-swan-red-team-arena-contest-to-jailbreak-ai-agents/)
- Credibility: the original Arena launched in Sept **2024**, and its community is about 15,000 people (Discord). Gray Swan raised a **$40M Series A** in May (co-led by Wing VC and Madrona), spun out of CMU, and grew from about 15 to 66 staff. Cofounder Zico Kolter chairs OpenAI's Safety and Security Committee. Fortune does not state the total paid out to date. — [Fortune](https://fortune.com/2026/10/20/exclusive-ai-security-company-gray-swan-red-team-arena-contest-to-jailbreak-ai-agents/)
- An earlier 2026 Indirect Prompt Injection Arena reportedly drew 464 participants and about 272,000 attempts across 13 frontier models and 41 scenarios. These figures come from a secondary guide and are **reported, not verified**. — [CASRAI guide](https://casrai.org/guides/gray-swan-arena-crowdsourced-red-teaming)
- **Proving Ground**: a weekly recurring challenge series (chat, image, agent and indirect-injection attacks) that feeds into the larger competitions. — [Gray Swan news](https://www.grayswan.ai/news/introducing-the-gray-swan-ai-proving-ground), [Arena blog](https://app.grayswan.ai/arena/blog/proving-ground-your-weekly-arena-for-ai-red-teaming-mastery)

**Anthropic Model Safety Bug Bounty (from 2024, ongoing)**
- Ongoing program on **HackerOne**. Participants submit "once accepted to the Program", so access is application/invite-gated. Scope is universal jailbreaks that bypass Constitutional Classifiers. — [Claude support](https://support.claude.com/en/articles/12119250-model-safety-bug-bounty-program)
- Launched **August 2024**, with rewards up to **$15,000** and invite-only at launch. — [Maginative](https://www.maginative.com/article/anthropic-will-pay-you-up-to-15-000-to-jailbreak-its-next-gen-ai-safety-system/), [HackerOne blog](https://www.hackerone.com/blog/anthropic-expands-their-model-safety-bug-bounty-program)
- An aggregator reports a **May 10–18, 2026** Anthropic program with rewards up to **$25,000**. This is **unverified** and I found no primary confirmation. — [ThreatCluster](https://threatcluster.io/cluster/anthropic-launches-bug-bounty-for-ai-safety-defenses-2de609cc)

**HackerOne Good Faith AI Research Safe Harbor (Jan 2026)**
- HackerOne reportedly unveiled a "Good Faith AI Research Safe Harbor" in January 2026, giving testers clearer authorisation to probe AI systems. Aggregator only, and I did not read a primary HackerOne page. — [SecurityBrief tag page](https://securitybrief.co.uk/tag/hackerone)

### Inferences
- In 2026 the money for individual AI red-teamers is concentrated in (a) time-boxed competitions with sponsored prize pools (Gray Swan, $300K for IPI Black) and (b) lab bounties that pay modest per-finding amounts (OpenAI safety at about $7.5K max per SecurityWeek; Anthropic at $15K+). Indirect prompt injection and agent/MCP abuse are the 2026 focus areas, not plain chat jailbreaks.
- Gray Swan is the most credible AI red-team marketplace: it has a VC raise, frontier-lab sponsors and a long track record. Its best-paid work (private arenas) needs vetting and an NDA.

### Gaps
- I found no 2026 sources for Google (AI VRP changes), xAI, Meta, HackAPrompt, Haize Labs or Lakera/Gandalf. These need targeted searches. Google's AI VRP is from 2023–2025, and HackAPrompt 2.0 is from 2025 and may have had 2026 tracks.
- I could not read openai.com directly to resolve the $7,500 vs $100,000 conflict.
- I found no data on total amounts actually paid by Gray Swan or the OpenAI safety bounty.

## Q3: Notable 2026 changes at HackerOne, Bugcrowd, Intigriti, YesWeHack, Synack, Open Bug Bounty

### Takeaway
The main 2026 theme is the **flood of AI-generated reports**. HackerOne reportedly paused Internet Bug Bounty submissions (April 2026), GitHub cut public payouts and added an invite-only VIP tier on HackerOne (from July 27, 2026), and curl and Google pulled back too. Incumbents also launched AI-agent pentest products: YesWeHack Agentic Pentest (June 25, 2026, verified) and Bugcrowd "Savant Pathseeker" (early access). I found no 2026 acquisition by any of the major platforms.

### Cited Findings
**HackerOne**
- **Internet Bug Bounty paused (around April 2026):** HackerOne is reportedly "pausing submissions" to the IBB because AI-generated reports overwhelm maintainers. It is unclear whether the cause is spam or the cost of fixing a higher volume of valid bugs. — [Privacy Guides, Apr 17 2026](https://www.privacyguides.org/news/2026/04/17/hackerone-pauses-internet-bug-bounty.md)
- Context from the same article: **curl stopped participating in its bug bounty in Jan 2026**, and **Google stopped accepting AI-generated reports in March 2026**. Both are secondary reports. — [Privacy Guides](https://www.privacyguides.org/news/2026/04/17/hackerone-pauses-internet-bug-bounty.md)
- HackerOne reportedly updated its program policy templates so programs can require disclosure of AI tool use or ban fully autonomous AI submissions. The same blog says neither HackerOne nor Bugcrowd had a comprehensive AI policy as of mid-2026. This comes from a single blog and is unverified. — [Decryption Digest](https://www.decryptiondigest.com/blog/bug-bounty-programs-ai-era-hackerone-bugcrowd-2026)
- HackerOne reported submissions up 92% year over year around its 2026 platform launch. Aggregator only. — [SecurityBrief tag page](https://securitybrief.co.uk/tag/hackerone)

**GitHub program on HackerOne (a major program change)**
- For reports from **July 27, 2026**, the public tier pays fixed amounts: **$250 / $2,000 / $5,000 / $10,000** (low/medium/high/critical). One outlet says the previous maximums were about $20K for high and $30K for critical. A new **invite-only VIP tier** pays about 3–4x, with critical starting around $30K. New researchers face a HackerOne signal requirement or initial-submission cap. GitHub cites low-quality and AI-generated reports. — [TechRadar](https://techradar.com/pro/security/github-restructures-bug-bounty-program-following-flood-of-ai-generated-reports), [SC World](https://www.scworld.com/brief/github-to-implement-two-tier-bug-bounty-program-amid-ai-generated-report-surge), [Neowin](https://www.neowin.net/amp/github-adjusts-bounty-program-adds-vip-program-to-filter-ai-submissions/)

**YesWeHack: verified**
- **Agentic Pentest launched June 25, 2026.** It is an on-demand autonomous AI-agent pentest with same-day findings covering web, mobile, API and other internet-facing assets in black, grey or white box. It uses frontier and open-weight models, with an EU or APAC hosting choice and optional human triage that YesWeHack says gives "zero false positives". It is a customer product, not a hacker earning program. — [YesWeHack news](https://www.yeswehack.com/news/yeswehack-agentic-pentest), [Business Wire](https://www.businesswire.com/news/home/20260625181000/en)
- Dealroom reports deployments at Dassault Systèmes and Sanofi plus other CAC 40 firms. This is a third-party claim. — [Dealroom](https://app.dealroom.co/news/feed/yeswehack-launches-agentic-pentest-for-same-day-ai-powered-security-testing)

**Bugcrowd**
- No 2026 acquisition found. Its recent deals are **Mayhem Security (2025)**, an AI offensive security firm, and **Informer (May 2024)**, an ASM and continuous pentest provider. Bugcrowd's site currently promotes "**Savant Pathseeker**, agentic pentesting on the Bugcrowd Platform", with early access open. I did not confirm a launch date. — [Wikipedia](https://en.wikipedia.org/wiki/Bugcrowd), [Fenwick: Mayhem](https://www.fenwick.com/insights/experience/fenwick-represents-bugcrowd-in-acquisition-of-mayhem-security), [Bugcrowd press release (Informer, banner shows Pathseeker)](https://www.bugcrowd.com/press-release/bugcrowd-acquires-informer/)
- Bugcrowd hosts the new OpenAI Safety Bug Bounty (see Q2). — [SecurityWeek](https://www.securityweek.com/openai-launches-bug-bounty-program-for-abuse-and-safety-risks/amp/)

**Intigriti**
- Won Adobe's bug bounty program, effective Sept 1, 2026. — [Adobe Security blog](https://blog.adobe.com/security/a-new-home-for-the-adobe-bug-bounty-program)

### Inferences
- For individual hunters, 2026 is worse on public programs: fixed and lower public payouts (GitHub), paused open-source bounties (IBB, curl), and anti-AI-spam gates (signal requirements, AI-disclosure rules). More of the money now sits in invite-only and VIP tiers that need a track record.
- The agentic pentest products (YesWeHack, Bugcrowd Pathseeker) compete with human hunters for the routine findings. Pressure on low-hanging-fruit income is likely to keep growing.

### Gaps
- I found no 2026 information on **Synack** or **Open Bug Bounty**, and none on Intigriti's AI report policy.
- I found no primary HackerOne statement on the IBB pause or on AI-report rules, so both rest on secondary coverage.
- My searches found no 2026 acquisition at HackerOne, Bugcrowd, Intigriti or YesWeHack, but I did not search exhaustively.
