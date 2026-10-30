# Security signal: last 7 days

🔴 act now · 🟠 worth knowing

## 2026-10-30

### 🔴 Attacker Tried to Exploit Alpine Linux’s GitLab via CVSS 10.0 Flaw Its Ruby Left Open
`CVE-2026-76418, CVE-2026-97229, CVE-2026-98432 · EPSS 0.18 · CISA KEV`

An attacker tried to exploit a critical GitLab vulnerability on the Alpine Linux project's own GitLab server a week after GitLab released a fix, Alpine Linux said on 28 October. The flaw, CVE-2026-97229 (CVSS score: 10.0), can let an attacker run code on a GitLab server through a crafted regular expression in a CI configuration.

**Do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

[The Hacker News](https://thehackernews.com/2026/10/attacker-tried-to-exploit-alpine-linuxs.html) · [The Hacker News](https://thehackernews.com/2026/10/cisco-patches-actively-exploited-asa.html) · [CISA Advisories](https://www.cisa.gov/news-events/alerts/2026/10/29/cisa-adds-two-known-exploited-vulnerabilities-catalog) · [The Hacker News](https://thehackernews.com/2026/10/linux-kernel-tcp-flaw-with-98-cvss.html) · [The Hacker News](https://thehackernews.com/2026/10/cisa-adds-actively-exploited-gitlab-rce.html) · [SecurityWeek](https://www.securityweek.com/max-severity-gitlab-vulnerability-exploited-against-alpine-linux/) · [CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-97229) · [CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-76418)

### 🔴 Hackers Exploited Cisco SD-WAN Flaw to Plant Malware Built to Steal Encryption Keys
`CVE-2026-20127 · EPSS 0.89 · CISA KEV`

Hackers exploited a critical Cisco Catalyst SD-WAN flaw, fixed in February, to plant custom malware inside the systems that control an organization's SD-WAN network. The malware, called KeyDrift, is designed to copy the keys that encrypt traffic between sites and store them for later use, Cisco Talos said on October 28.

[The Hacker News](https://thehackernews.com/2026/10/hackers-exploited-cisco-sd-wan-flaw-to.html) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/hackers-exploit-cisco-sd-wan-flaw-to-deploy-custom-keydrift-malware/)

### 🔴 China-Linked Hackers Exploited VMware ESX Zero-Day to Reduce Audit Trail Visibility
`CVE-2026-41709 · EPSS 0.01 · CISA KEV`

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Wednesday added a security flaw impacting Broadcom VMware ESX to its Known Exploited Vulnerabilities (KEV) catalog, after CrowdStrike revealed that it had been weaponized by a China-nexus threat actor known as Warp Panda in attacks targeting the U.S.

**Do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

[The Hacker News](https://thehackernews.com/2026/10/china-linked-hackers-exploited-vmware.html) · [CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-41709)

### 🔴 CVE-2026-46300: Linux Kernel Missing Initialization of a Variable Vulnerability
`CVE-2026-46300 · EPSS 0.16 · CISA KEV`

Linux Kernel contains a missing initialization of a variable vulnerability that could allow for unintended modification of page-cache-backed data via failure to preserve the shared-fragment marker during socket buffer coalescing, causing ESP input processing to decrypt shared fragments in place. This vulnerability can be chained with CVE-2026-109618 and CVE-2026-109619 to implant PHP webshells and

**Do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

[CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-46300)

### 🔴 Hackers Actively Exploit Highly Critical Drupal Commerce Core Authorization Bypass Flaw
`CVE-2026-118539 · exploited`

Drupal has warned that threat actors are exploiting a "highly critical" security flaw in its Commerce Core component. The vulnerability, tracked as CVE-2026-118539 (CVSS score: N/A), is a case of missing authorization affecting Commerce Core versions from 0.0.0 to 2.41 and from 3.0.0 to 3.3.13.

[The Hacker News](https://thehackernews.com/2026/10/hackers-actively-exploit-highly.html) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/drupal-warns-of-critical-commerce-core-flaw-exploited-in-attacks/) · [SecurityWeek](https://www.securityweek.com/drupal-commerce-core-vulnerability-exploited-against-online-stores/)

### 🟠 Fake ChatGPT and Claude Apps Abuse Signed Executables to Deploy Crypto Miners

Threat actors are delivering malicious loaders and cryptocurrency miners under the guise of artificial intelligence (AI) desktop applications for Anthropic Claude and OpenAI ChatGPT as part of a campaign dubbed Yoba. The activity involves creating fake GitHub projects that claim to be desktop applications like GPT-5.6 Sol, GPT-6 Astra, and Claude Opus, only to deliver a malware family called

[The Hacker News](https://thehackernews.com/2026/10/fake-chatgpt-and-claude-apps-abuse.html) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/fake-crypto-app-on-apple-app-store-linked-to-23k-wallet-theft/) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/binance-probes-potential-58-billion-crypto-theft-hack/) · [The Record](https://therecord.media/binance-hit-by-record-6-billion-crypto-hack) · [The Hacker News](https://thehackernews.com/2026/10/binance-suffers-security-breach.html) · [SecurityWeek](https://www.securityweek.com/6-billion-binance-hack-bears-hallmarks-of-north-koreas-tradertraitor/) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/binance-links-63-billion-crypto-theft-to-compromised-devops-laptop/)

### 🟠 CVE-2026-103409: A Missing authentication for critical function vulnerability in Juniper Networks Session Smart Router a
`CVE-2026-103409 · CVSS 9.8 · EPSS 0.00 · exploited`

A Missing authentication for critical function vulnerability in Juniper Networks Session Smart Router allows an unauthenticated network-based attacker to obtain administrative privileges by passing crafted URL parameters to an insecure endpoint running as root. Note that this vulnerability can only be exploited prior to the device being onboarded to Mist/Conductor.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103409)

### 🟠 Hitachi Energy CoreTec Product
`CVE-2026-106087, CVE-2026-10756, CVE-2026-13162, CVE-2026-43284 · EPSS 0.94 · exploited`

View CSAF Summary Hitachi Energy is aware of OS command injection and Dirty Frag vulnerabilities that affect CoreTec product versions listed in this document. Successful exploitation of these vulnerabilities could result in impact on confidentiality, integrity and availability of the product.

[CISA Advisories](https://www.cisa.gov/news-events/ics-advisories/icsa-26-302-03) · [CISA Advisories](https://www.cisa.gov/news-events/ics-advisories/icsa-26-302-02)

### 🟠 CVE-2026-103406: An Improper Neutralization of Special Elements used in an OS Command vulnerability in the AutomatedProv
`CVE-2026-103406 · CVSS 9.8 · EPSS 0.01`

An Improper Neutralization of Special Elements used in an OS Command vulnerability in the AutomatedProvisioner in Juniper Networks Session Smart Conductor allows a remote attacker to execute arbitrary commands as root via a specially crafted salt minion ID.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103406)

### 🟠 Volt Typhoon Used Covert Silent Train Network in Four Zero-Day Exploitation Campaigns
`exploited`

The China-nexus cyber espionage group known as Volt Typhoon has been attributed to a now-disrupted covert access network dubbed Silent Train that has been put to use for zero-day exploitation and strategic access. "First identified in late 2023, Silent Train uses rotating chains of compromised SOHO, IoT, and enterprise infrastructure," Lumen Technologies Black Lotus Labs said in a report shared

[The Hacker News](https://thehackernews.com/2026/10/volt-typhoon-used-covert-silent-train.html)

### 🟠 rust:zip: zip: Critical Parser Differential & Security Control Bypass via Dual-Header Inconsistencies (Zip Cloaking) Lea
`CVE-2026-115905 · CVSS 10.0 · EPSS 0.00`

Affected packages: rust:zip. ## Summary A critical architectural parser differential exists in the `zip` crate (`<= 9.0.4`) between random-access archive readers (`ZipArchive`) and streaming readers (`ZipStreamReader`).

[GitHub Advisory](https://github.com/advisories/GHSA-m665-v7pm-7grj)

### 🟠 Hugging Face malware campaign returns to hijack GPUs for crypto mining

A crypto-mining campaign abusing Hugging Face models returned days after takedown, hijacking GPU servers and planting backdoors, with one model downloaded over 28,000 times. Separately, a fake Solana starter kit on GitHub is positioned to trick AI coding agents into installing a NetSupport RAT.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/hugging-face-malware-campaign-returns-to-hijack-gpus-for-crypto-mining/)

### 🟠 Japan Airlines suffers third-party data breach exposing passenger info

Japan Airlines (JAL) has announced that a data breach at Amadeus's Passenger Service System exposed the data of about 92,000 customers. [...]

[BleepingComputer](https://www.bleepingcomputer.com/news/security/japan-airlines-suffers-third-party-data-breach-exposing-passenger-info/)

### 🟠 Polymarket halts trading after crypto-draining script breach, $2.5M traced

Prediction market platform Polymarket temporarily suspended trading on Thursday after hackers compromised a third-party service to distribute cryptocurrency-draining JavaScript, with approximately $2.5 million in assets traced to a suspected attacker wallet. [...]

[BleepingComputer](https://www.bleepingcomputer.com/news/security/polymarket-halts-trading-after-crypto-draining-script-breach-25m-traced/)

### 🟠 Limited reports of PHP bug exploitation emerge

One cyber firm listed a half-dozen exploitations of the PHP2Shell bugs, and another identified a well targeted, suspected Chinese campaign that breached U.S. "government affiliated" servers.

[The Record](https://therecord.media/php2shell-successful-exploitation-reports-emerge)

### 🟠 Fresh WordPress Vulnerability in Attackers’ Crosshairs

Threat actors are attempting to exploit a high-severity unauthenticated race condition leading to remote code execution. The post Fresh WordPress Vulnerability in Attackers’ Crosshairs appeared first on SecurityWeek .

[SecurityWeek](https://www.securityweek.com/fresh-wordpress-vulnerability-in-attackers-crosshairs/)

### 🟠 $2 Million+ Drained From Polymarket Traders in New Supply Chain Attack

Malicious code linked to a website monitoring tool was designed to hijack logged-in Polymarket sessions and siphon user funds. The post $2 Million+ Drained From Polymarket Traders in New Supply Chain Attack appeared first on SecurityWeek .

[SecurityWeek](https://www.securityweek.com/2-million-drained-from-polymarket-traders-in-new-supply-chain-attack/)

### 🟠 Official Claude Code VS Code Extension Compromised to Install Persistent SSH Backdoor

Cybersecurity researchers have disclosed that the official Anthropic Claude Code extension was compromised on the Open VSX registry to install a persistent SSH backdoor on infected hosts. The issue has since been traced to the compromise of the Cursor Marketplace, prompting the AI coding platform Cursor to briefly take down the service to remove the malware.

[The Hacker News](https://thehackernews.com/2026/10/official-claude-code-vs-code-extension.html)

### 🟠 PHP2Shell Attack Roots 25 Servers, Breaches U.S. Government-Affiliated Network

Cybersecurity researchers have disclosed details of what appears to be an artificial intelligence (AI)-assisted attack orchestrated by a suspected China-nexus threat actor that has leveraged the PHP2Shell vulnerabilities to breach exposed systems. The activity, which was observed on October 25, 2026, involved an attacker combining PHP2Shell with a kernel privilege escalation exploit to root

[The Hacker News](https://thehackernews.com/2026/10/php2shell-attack-roots-25-servers.html)

### 🟠 Hackers Target Critical Oracle E-Business Suite RCE Flaw Days After Security Patch
`CVE-2026-101767 · EPSS 0.01`

Threat actors are beginning to probe for a newly patched critical vulnerability in Oracle E-Business Suite (EBS), according to threat intelligence firm Defused Cyber. The vulnerability in question is CVE-2026-101767 (CVSS score: 9.8) , a case of improper authentication in the Oracle Application Object Library of Oracle E-Business Suite.

[The Hacker News](https://thehackernews.com/2026/10/hackers-target-critical-oracle-e.html)

### 🟠 Siemens Mendix SAML Module
`CVE-2026-89209 · EPSS 0.00`

View CSAF Summary Mendix SAML module contains an authentication bypass vulnerability that could allow an unauthenticated remote attacker to gain unauthorized access by replaying a valid SAML assertion in IdP-initiated authentication flows. Siemens has released new versions for the affected products and recommends to update to the latest versions.

[CISA Advisories](https://www.cisa.gov/news-events/ics-advisories/icsa-26-302-01)

