# Security signal: last 7 days

🔴 act now · 🟠 worth knowing

## 2026-11-26

### 🔴 HPE Juniper Session Smart Conductor/Router RCE CVE-2026-103406
`CVE-2026-103406 · EPSS 0.01 · CISA KEV`

HPE Juniper Session Smart Conductor and Session Smart Router contain an OS command injection vulnerability allowing unauthenticated remote command execution as root via a crafted salt minion ID.

**Do:** Apply mitigations or updates per vendor instructions in accordance with CISA BOD 26-04.

[CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-103406)

### 🔴 Mitel MiCollab AWV Auth Bypass CVE-2026-133324
`CVE-2026-133324 · EPSS 0.00 · CISA KEV`

Mitel MiCollab Audio, Web and Video Conferencing component fails securely, allowing unauthenticated attackers to bypass authentication and perform unauthorized actions.

**Do:** Apply vendor mitigations per CISA KEV instructions.

[CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-133324)

### 🔴 Mitel MiCollab AWV Unrestricted File Upload CVE-2026-133275
`CVE-2026-133275 · EPSS 0.00 · CISA KEV`

Mitel MiCollab Audio, Web and Video Conferencing component suffers from insufficient file type validation, enabling arbitrary file uploads by unauthenticated attackers.

**Do:** Apply vendor mitigations per CISA KEV instructions.

[CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-133275)

### 🔴 Mitel MiCollab AWV Weak Authentication CVE-2026-133311
`CVE-2026-133311 · EPSS 0.00 · CISA KEV`

Mitel MiCollab Audio, Web and Video Conferencing component contains a weak authentication flaw allowing unauthenticated access to sensitive information via specific identifiers.

**Do:** Apply vendor mitigations per CISA KEV instructions.

[CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-133311)

### 🔴 Mitel MiCollab AWV XML Injection CVE-2026-133303
`CVE-2026-133303 · EPSS 0.01 · CISA KEV`

Mitel MiCollab Audio, Web and Video Conferencing component contains an XML injection vulnerability allowing unauthenticated command execution using pre-staged content.

**Do:** Apply vendor mitigations per CISA KEV instructions.

[CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-133303)

### 🔴 Mitel MiCollab AWV OS Command Injection CVE-2026-133323
`CVE-2026-133323 · EPSS 0.03 · CISA KEV`

Mitel MiCollab Audio, Web and Video Conferencing component contains an OS command injection vulnerability allowing unauthenticated attackers to execute arbitrary system commands.

**Do:** Apply vendor mitigations per CISA KEV instructions.

[CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-133323)

### 🔴 1Password Discloses Customer Data Breach via GitHub Account Compromise
`exploited`

1Password suffered a data breach after an employee's corporate GitHub account was compromised and used to deploy malicious code to backend services, stealing customer data.

**Do:** Review internal GitHub access controls, tokens, and monitor for unauthorized backend modifications.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/1password-customer-data-stolen-after-employee-github-account-breach/)

### 🔴 D-Link R32 TZLocation OS Command Injection CVE-2026-136821
`CVE-2026-136821 · CVSS 9.9 · exploited`

D-Link R32 1.10B02 contains an OS command injection vulnerability in the SetTimeSettings function of the DHMAPI Action Handler via the TZLocation argument with public exploits available.

**Do:** Discontinue use or apply vendor patches if available.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-136821)

### 🔴 D-Link R32 SetDeviceSettings OS Command Injection CVE-2026-136822
`CVE-2026-136822 · CVSS 9.9 · exploited`

D-Link R32 1.10B02 contains an OS command injection vulnerability in SetDeviceSettings via the TZLocation argument with public exploits available.

**Do:** Discontinue use or apply vendor patches if available.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-136822)

### 🔴 D-Link R32 httpd fpath OS Command Injection CVE-2026-136823
`CVE-2026-136823 · CVSS 10.0 · exploited`

D-Link R32 1.10B02 contains an OS command injection vulnerability in /usr/bin/httpd via the fpath argument with public exploits available.

**Do:** Discontinue use or apply vendor patches if available.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-136823)

### 🔴 Danfoss AK-SM 800A Series Auth Bypass CVE-2025-41450
`CVE-2025-41450 · EPSS 0.01 · CISA KEV`

Danfoss AK-SM 800A Series controllers contain an improper authentication vulnerability allowing attackers to generate web reports exposing sensitive internal data.

**Do:** Apply vendor mitigations and follow CISA KEV guidance.

[CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2025-41450)

### 🔴 Danfoss AK-SM 800A Series Path Traversal CVE-2023-25914
`CVE-2023-25914 · EPSS 0.01 · CISA KEV`

Danfoss AK-SM 800A Series contains a path traversal vulnerability in the XML interface allowing attackers to read server system files.

**Do:** Apply vendor mitigations and follow CISA KEV guidance.

[CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2023-25914)

### 🔴 Danfoss AK-SM 800A Series Input Validation Flaw CVE-2023-25915
`CVE-2023-25915 · EPSS 0.01 · CISA KEV`

Danfoss AK-SM 800A Series contains an input validation vulnerability allowing remote attackers to run arbitrary commands.

**Do:** Apply vendor mitigations and follow CISA KEV guidance.

[CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2023-25915)

### 🟠 France blames Iranian cyber unit for sabotaging supermarket freezers
`exploited`

France attributes cyber sabotage of hundreds of supermarket freezers to an Iranian cyber unit, disrupting operations.

**Do:** Review industrial control system and refrigeration network segmentation and monitoring.

[Ars Technica](https://arstechnica.com/security/2026/11/a-familiar-iranian-hacking-group-has-found-a-new-way-to-cause-chaos/)

### 🟠 openIMIS Report Module Unauthenticated RCE CVE-2026-82489
`CVE-2026-82489 · CVSS 9.8`

openIMIS before 2026-10 contains an unauthenticated RCE and file read vulnerability in the report module via preview printIf expressions and key parameters, leading to root command execution.

**Do:** Upgrade openIMIS to 2026-10 or later.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82489)

### 🟠 build-git-clone OS Command Injection CVE-2026-137090
`CVE-2026-137090 · CVSS 9.8`

build-git-clone before 1.0.4 contains an OS command injection vulnerability in the clone() function via crafted repository URLs containing shell metacharacters.

**Do:** Upgrade build-git-clone to version 1.0.4 or higher.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-137090)

### 🟠 TastyIgniter Media Manager Unrestricted File Upload RCE CVE-2026-69179
`CVE-2026-69179 · CVSS 9.1`

TastyIgniter Media Manager accepts .htaccess uploads, allowing authenticated admin users to achieve remote code execution.

**Do:** Restrict file upload types in Media Manager and upgrade when patches are available.

[GitHub Advisory](https://github.com/advisories/GHSA-7wwv-x6mc-pxqx)

### 🟠 TastyIgniter Mail Template Editor SSTI RCE CVE-2026-69178
`CVE-2026-69178 · CVSS 9.1`

TastyIgniter mail template editor suffers from server-side template injection allowing authenticated admins with proper permissions to achieve arbitrary PHP execution.

**Do:** Audit admin mail template permissions and restrict access.

[GitHub Advisory](https://github.com/advisories/GHSA-743w-g9pf-8p94)

### 🟠 CISA Warns of Critical Flaws in Danfoss Refrigeration Controllers

CISA issued a warning regarding critical unpatched vulnerabilities in Danfoss AK-SM 8xxA Series commercial refrigeration controllers.

**Do:** Review CISA advisories and isolate affected controllers from the internet.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/cisa-warns-of-critical-unpatched-flaw-in-danfoss-refrigeration-controllers/)

### 🟠 FIFA Discloses Cyberattack Accessing Personal and Business Data
`exploited`

FIFA announced it is investigating a recent cyberattack that provided hackers access to a limited set of personal and business information.

**Do:** Monitor internal alerts and investigate any unusual activity related to FIFA networks.

[The Record](https://therecord.media/fifa-data-breach-limited)

### 🟠 @waline/client Stored XSS Privilege Escalation CVE-2026-64670
`CVE-2026-64670 · CVSS 9.3 · EPSS 0.00`

@waline/client renders un-sanitized comment edits via v-html, allowing unauthenticated commenters to achieve stored XSS against moderators who click Edit.

**Do:** Upgrade @waline/client to a patched version.

[GitHub Advisory](https://github.com/advisories/GHSA-crj3-q72p-ggqm)

## 2026-11-25

### 🔴 Palo Alto Networks patches Fragnesia flaw used to root firewalls
`exploited`

A China-linked hacking group chained PHP2Shell with the Fragnesia vulnerability in AI-assisted attacks targeting firewall servers.

**Do:** Apply the latest patches from Palo Alto Networks immediately.

[SecurityWeek](https://www.securityweek.com/palo-alto-networks-patches-fragnesia-flaw-used-to-root-firewalls/) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/palo-alto-networks-warns-of-fragnesia-flaw-exploited-in-pan-os-attacks/)

### 🔴 US Treasury FinCEN takes systems offline after cyber incident
`exploited`

The U.S. Treasury Department's Financial Crimes Enforcement Network experienced unauthorized access to a subset of systems and took them offline.

**Do:** Review reporting deadlines and follow FinCEN guidance for BSA filings.

[The Record](https://therecord.media/treasury-fincen-takes-systems-offline-after-cyber-incident) · [The Hacker News](https://thehackernews.com/2026/11/us-treasurys-fincen-takes-some-systems.html) · [SecurityWeek](https://www.securityweek.com/us-treasurys-fincen-disconnects-systems-following-cyber-incident/)

### 🔴 CISA adds Drupal flaw found by Anthropic scanner to KEV
`exploited`

A Drupal vulnerability discovered by an AI scanner is actively exploited in attacks, leading to a CISA emergency directive.

**Do:** Patch Drupal installations per CISA KEV timeline.

[SecurityWeek](https://www.securityweek.com/drupal-flaw-found-by-anthropic-scanner-exploited-in-attacks/)

### 🔴 GeoServer RCE flaws CVE-2026-120705 and CVE-2026-129243 exploited
`CVE-2026-120705, CVE-2026-129243 · exploited`

Threat actors are actively exploiting arbitrary file read and RCE vulnerabilities in GeoServer (CVE-2026-120705 and CVE-2026-129243).

**Do:** Upgrade GeoServer to patched versions immediately.

[The Hacker News](https://thehackernews.com/2026/11/hackers-exploit-two-geoserver-flaws-as.html) · [SecurityWeek](https://www.securityweek.com/two-newly-disclosed-geoserver-vulnerabilities-under-attack/)

### 🔴 npm:ruflo MCP bridge unauthenticated RCE vulnerability
`CVE-2026-59726 · CVSS 10.0 · EPSS 0.06`

The ruflo MCP bridge shipping in ruflo/docker-compose.yml exposes an unauthenticated POST /mcp endpoint, allowing remote attackers to achieve remote code execution and steal provider API keys.

**Do:** Update ruflo and ensure Docker Compose configurations do not bind management ports to all network interfaces.

[GitHub Advisory](https://github.com/advisories/GHSA-c4hm-4h84-2cf3)

### 🟠 Ransomware attack disrupts Guadeloupe hospital operations
`exploited`

A suspected ransomware attack impaired the University Hospital of Guadeloupe, forcing the postponement of surgeries and suspension of cancer treatments.

**Do:** Ensure robust backup and incident response protocols are active.

[The Record](https://therecord.media/guadeloupe-ransomware-hospital-cyber)

### 🟠 Check Point and Hex.pm servers targeted in AI-driven attacks
`exploited`

Attackers compromised Check Point management servers and Hex.pm package registry servers using automated tooling and unauthenticated flaws.

**Do:** Audit Check Point management servers and update dependencies securely.

[The Hacker News](https://thehackernews.com/2026/11/hackers-compromise-24-check-point.html) · [The Hacker News](https://thehackernews.com/2026/11/hackers-exploited-cvss-100-hexpm-rce.html)

### 🟠 WordPress blocks six backdoored WP Connect plugins
`exploited`

WordPress proactively removed six plugins developed by WP Connect after their developer accounts were compromised to inject RCE backdoors.

**Do:** Verify plugin integrity and remove any unauthorized or compromised versions.

[The Hacker News](https://thehackernews.com/2026/11/wordpress-blocks-six-backdoored-wp.html)

### 🟠 Rackspace Shuts Down Spot Cloud After Security Breach
`exploited`

Rackspace is shutting down its Spot cloud platform after a security breach exposed customer Kubernetes clusters and secrets.

**Do:** Migrate services and download data from Rackspace Spot before December 8.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/rackspace-shuts-down-spot-cloud-platform-after-security-breach/)

### 🟠 Unclassified CIA System Breached in Cyberattack
`exploited`

An unclassified CIA system was compromised in a cyberattack, though specific details on the compromised data or attribution remain unclear.

[SecurityWeek](https://www.securityweek.com/an-unclassified-cia-system-was-breached-in-a-cyberattack-ap-source-says/) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/hackers-reportedly-breached-cia-intelligence-analysis-system/)

### 🟠 Com-affiliated threat actors execute vishing campaign for cloud access
`exploited`

Threat actors have used vishing attacks to hijack cloud accounts across financial, healthcare, and legal sectors for extortion.

**Do:** Enforce phishing-resistant MFA across all cloud accounts.

[The Hacker News](https://thehackernews.com/2026/11/com-affiliated-hackers-hijack-cloud.html)

### 🟠 Colorado myColorado App Cyberattack Impacts 150,000
`exploited`

A cyberattack on the myColorado digital identification app resulted in data theft affecting 150,000 users.

**Do:** Monitor accounts and follow guidance from Colorado state agencies.

[The Record](https://therecord.media/mycolorado-app-down-data-breach)

### 🟠 Turnitin Discloses Unauthorized Activity on Systems
`exploited`

Turnitin detected unauthorized activity involving certain customer-facing systems.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/turnitin-discloses-cyberattack-affecting-customer-facing-systems/) · [SecurityWeek](https://www.securityweek.com/plagiarism-checker-turnitin-investigating-cyberattack/)

### 🟠 BusyBox tftpd path traversal vulnerability
`CVE-2026-136411 · CVSS 9.8`

BusyBox through 1.38.0 contains an absolute path traversal vulnerability in tftpd allowing unauthenticated remote attackers to read or overwrite sensitive files.

**Do:** Update BusyBox to a patched version when available.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-136411)

## 2026-11-24

### 🔴 Microsoft SharePoint Path Traversal RCE Vulnerability CVE-2026-70193
`CVE-2026-70193 · CVSS 9.9`

A path traversal vulnerability in Microsoft Office SharePoint allows an authorized attacker to execute code over a network. It carries a CVSS score of 9.9.

**Do:** Apply the latest security updates for Microsoft SharePoint.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-70193)

### 🔴 Azure Event Grid Improper Authentication Flaw CVE-2026-62841
`CVE-2026-62841 · CVSS 10.0`

Improper authentication in Azure Event Grid allows an unauthorized attacker to elevate privileges over a network with a CVSS score of 10.0.

**Do:** Apply the latest security updates for Azure Event Grid.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-62841)

### 🔴 VMware vCenter Hit by Another Critical 9.8-Rated Auth Bypass Flaw After Zero-Day Exploitation
`CVE-2026-123903 · exploited`

Broadcom has shipped patches to address 23 vulnerabilities impacting VMware ESX, vCenter, Workstation, Fusion, and Avi Load Balancer, including one critical bug that could be abused to bypass authentication. The critical vulnerability, tracked as CVE-2026-123903, is rated 9.8 out of 10.0 on the CVSS scoring system.

[The Hacker News](https://thehackernews.com/2026/11/vmware-vcenter-hit-by-another-critical.html) · [SecurityWeek](https://www.securityweek.com/vmware-updates-patch-critical-esx-vcenter-vulnerabilities/)

### 🟠 Korea Electric Power Corporation Breached, Impacting 1.5 Million
`exploited`

A threat actor breached the internal network of Korea Electric Power Corporation (KEPCO) and accessed two systems containing customer, employee, and contractor data, impacting 1.5 million.

**Do:** Monitor internal networks and review access controls for critical infrastructure systems.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/south-koreas-power-giant-kepco-confirms-data-breach-impacting-15-million/)

### 🟠 Profile Data Roaming Service SSRF Privilege Escalation CVE-2026-109480
`CVE-2026-109480 · CVSS 9.6`

A server-side request forgery vulnerability in Profile Data Roaming Service (PDRS) allows an authorized attacker to elevate privileges over a network.

**Do:** Apply available security patches for PDRS.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109480)

### 🟠 Azure Machine Learning SSRF Privilege Escalation CVE-2026-118285
`CVE-2026-118285 · CVSS 9.6`

A server-side request forgery vulnerability in Azure Machine Learning allows an authorized attacker to elevate privileges over a network.

**Do:** Apply the latest Azure Machine Learning updates.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-118285)

### 🟠 Azure Site Recovery Improper Access Control CVE-2026-118286
`CVE-2026-118286 · CVSS 9.1`

Improper access control in Azure Site Recovery allows an unauthorized attacker to elevate privileges over a network.

**Do:** Apply the latest updates for Azure Site Recovery.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-118286)

### 🟠 M365 Copilot Improper Authorization Flaw CVE-2026-50691
`CVE-2026-50691 · CVSS 9.9`

Improper authorization in M365 Copilot allows an authorized attacker to elevate privileges over a network.

**Do:** Apply the latest security updates for M365 Copilot.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-50691)

### 🟠 CVE-2026-123167: SolarWinds Serv-U is affected by a privilege escalation vulnerability that, when exploited, can allow a
`CVE-2026-123167 · CVSS 9.1 · exploited`

SolarWinds Serv-U is affected by a privilege escalation vulnerability that, when exploited, can allow a domain administrator to access files that otherwise would require elevated privileges. The risk is lower for Windows installations.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123167)

### 🟠 CVE-2026-123168: SolarWinds Serv-U is affected by an insufficient validation vulnerability that, when exploited, could l
`CVE-2026-123168 · CVSS 9.1 · exploited`

SolarWinds Serv-U is affected by an insufficient validation vulnerability that, when exploited, could lead to privilege escalation into the root user in Linux installations. The risk is lower for Windows installations.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123168)

### 🟠 CVE-2026-123172: Solarwinds Serv-U is affected by a privilege escalation vulnerability that, when exploited, could lead 
`CVE-2026-123172 · CVSS 9.1 · exploited`

Solarwinds Serv-U is affected by a privilege escalation vulnerability that, when exploited, could lead to the escalation of privileges to root for Linux installations. The risk is lower for Windows installations.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123172)

### 🟠 McDonald’s Japan discloses breach exposing customer purchase and location data

McDonald’s Japan disclosed a cybersecurity breach that exposed customers’ purchase histories and mobile device location data.

[The Record](https://therecord.media/japan-mcdonalds-cyberattack-breach) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/radware-discloses-breach-exposing-customer-cloud-access-keys/)

### 🟠 European Commission Uncovers Data Breach in Cyberattack Investigation

Names and email addresses of EU Academy users were exposed in the AI-assisted cyberattack the European Commission detected in October. The post European Commission Uncovers Data Breach in Cyberattack Investigation appeared first on SecurityWeek .

[SecurityWeek](https://www.securityweek.com/european-commission-uncovers-data-breach-in-cyberattack-investigation/) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/european-commission-confirms-data-theft-in-eu-academy-breach/)

### 🟠 Authentication Methods Portal Extension XSS Flaw CVE-2026-109490
`CVE-2026-109490 · CVSS 9.3`

An XSS vulnerability in the Authentication Methods Portal Extension allows an unauthorized attacker to elevate privileges over a network.

**Do:** Apply available security updates from Microsoft.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109490)

### 🟠 Microsoft Clarity Authorization Bypass Flaw CVE-2026-113824
`CVE-2026-113824 · CVSS 9.1`

An authorization bypass through user-controlled key in Microsoft Clarity allows an unauthorized attacker to elevate privileges over a network.

**Do:** Apply available updates for Microsoft Clarity.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-113824)

### 🟠 Azure DevTest Labs Authentication Bypass CVE-2026-69899
`CVE-2026-69899 · CVSS 9.1`

Authentication bypass by spoofing in Azure DevTest Labs allows an unauthorized attacker to perform spoofing over a network.

**Do:** Apply available patches for Azure DevTest Labs.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-69899)

### 🟠 Azure Portal XSS Flaw CVE-2026-70305
`CVE-2026-70305 · CVSS 9.6`

Cross-site scripting in Azure Portal allows an unauthorized attacker to perform spoofing over a network.

**Do:** Apply the latest updates for Azure Portal.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-70305)

### 🟠 CVE-2026-82315: SolarWinds Serv-U is affected by another Time-of-Check to Time-of-Use (TOCTOU) vulnerability.
`CVE-2026-82315 · CVSS 9.1`

SolarWinds Serv-U is affected by another Time-of-Check to Time-of-Use (TOCTOU) vulnerability. A user with domain administrator or higher privileges may be able to access or modify protected files outside the intended directory, potentially leading to code execution.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82315)

### 🟠 CVE-2026-82316: SolarWinds Serv-U is affected by a Time-of-Check to Time-of-Use (TOCTOU) vulnerability.
`CVE-2026-82316 · CVSS 9.1`

SolarWinds Serv-U is affected by a Time-of-Check to Time-of-Use (TOCTOU) vulnerability. A user with domain administrator or higher privileges may be able to access or modify protected files outside the intended directory, potentially leading to code execution.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82316)

### 🟠 CVE-2026-82319: SolarWinds Serv-U is affected by a time-of-check to time-of-use (TOCTOU) vulnerability.
`CVE-2026-82319 · CVSS 9.1`

SolarWinds Serv-U is affected by a time-of-check to time-of-use (TOCTOU) vulnerability. A user with domain administrator or higher privileges may allow a user to modify protected files outside their home directory.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82319)

### 🟠 CVE-2026-82320: SolarWinds Serv-U was found to be affected by another type confusion vulnerability that may allow domain
`CVE-2026-82320 · CVSS 9.1`

SolarWinds Serv-U was found to be affected by another type confusion vulnerability that may allow domain administrators to escalate privileges to that of a system administrator. The risk is lower for Windows installations.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82320)

### 🟠 CVE-2026-82321: SolarWinds Serv-U was found to be affected by a type confusion vulnerability that may allow domain admin
`CVE-2026-82321 · CVSS 9.1`

SolarWinds Serv-U was found to be affected by a type confusion vulnerability that may allow domain administrators to escalate privileges to that of a system administrator. The risk is lower for Windows installations.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82321)

### 🟠 CVE-2026-82322: SolarWinds Serv-U is affected by an Insecure Direct Object Reference (IDOR) vulnerability that allows a 
`CVE-2026-82322 · CVSS 9.1`

SolarWinds Serv-U is affected by an Insecure Direct Object Reference (IDOR) vulnerability that allows a domain group administrator to bypass restrictions and escalate privileges to the server administrator level. The risk is lower for Windows installations.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82322)

### 🟠 Amazon says hackers' AI agents found and exploited 0-day with little human input
`exploited`

The Cairn AI framework is proving to be a boon for defenders and attackers.

[Ars Technica](https://arstechnica.com/security/2026/11/amazon-says-hackers-ai-agents-found-and-exploited-0-day-with-little-human-input/)

### 🟠 From Vulnerability Noise to Resilience: Rethinking Security in the AI Era

AI-driven development is adding complexity to software supply chains, leaving security teams overwhelmed by vulnerabilities that may pose little actual risk. RapidFort explains how runtime visibility, container hardening, and automated remediation can reduce vulnerability noise and improve software resilience.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/from-vulnerability-noise-to-resilience-rethinking-security-in-the-ai-era/)

### 🟠 McDonald's Japan data breach exposes customer location information

McDonald's Japan, the fast-food giant's Japanese subsidiary, has disclosed a data breach after attackers accessed a database containing sensitive information for users of the company's official smartphone app. [...]

[BleepingComputer](https://www.bleepingcomputer.com/news/security/mcdonalds-japan-data-breach-exposes-customer-location-information/)

### 🟠 Carnegie Endowment for International Peace says third-party breach leaked donation info

Some donors to the Carnegie Endowment for International Peace had their information leaked due to a cyberattack on a third-party vendor named Soapbox Engage.

[The Record](https://therecord.media/carnegie-endowment-data-breach)

### 🟠 1.5 Million Impacted by Data Breach at South Korean Electric Company KEPCO

Hackers stole personal information from the company’s customer portal and supplier relationship management platform. The post 1.5 Million Impacted by Data Breach at South Korean Electric Company KEPCO appeared first on SecurityWeek .

[SecurityWeek](https://www.securityweek.com/1-5-million-impacted-by-data-breach-at-south-korean-electric-company-kepco/)

### 🟠 Iran-Aligned Volant Manticore Uses IPFS-Based KuboShell Backdoor in Espionage Campaigns

A previously undocumented Iran-aligned cyber espionage group called Volant Manticore has targeted telecommunications companies, airlines, and critical infrastructure in Cyprus. Central to the group's operations is a backdoor called KuboShell that uses the InterPlanetary File System (IPFS) for command-and-control (C2) and deploys Homa, a post-compromise framework that's a reimplementation of

[The Hacker News](https://thehackernews.com/2026/11/iran-aligned-volant-manticore-uses-ipfs.html)

## 2026-11-23

### 🔴 ConnectWise ScreenConnect Client Flaw CVE-2026-84869 Exploited
`CVE-2026-84869 · EPSS 0.01 · CISA KEV`

Threat actors are actively exploiting CVE-2026-84869, a critical client-side vulnerability in ConnectWise ScreenConnect allowing guests to execute payloads on technicians' hosts.

**Do:** Upgrade ScreenConnect immediately to the latest patched version.

[The Hacker News](https://thehackernews.com/2026/11/hackers-exploit-critical-screenconnect.html)

### 🔴 Microsoft Azure API Management Flaw Exploited in Energy Sector Attacks
`exploited`

Hackers exploited an Azure API Management Classic tier vulnerability to steal API credentials, targeting Norwegian energy companies like Equinor and Skagerak Energi.

**Do:** Review Azure API Management configurations and rotate compromised API credentials.

[The Record](https://therecord.media/norway-microsoft-cyberattack-equinor) · [SecurityWeek](https://www.securityweek.com/azure-flaw-exploited-to-target-secrets-at-norwegian-energy-firms/) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/microsoft-azure-flaw-exploited-to-steal-customers-api-credentials/)

### 🔴 Cisco Expressway RCE Flaw Actively Exploited
`exploited`

CISA added a critical Cisco Expressway RCE vulnerability to its KEV catalog after confirming active exploitation in the wild.

**Do:** Apply the latest security updates from Cisco immediately.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/cisa-flags-critical-cisco-expressway-rce-flaw-as-actively-exploited/)

### 🔴 Now exploited: Idunno.AntiCsrf ASP.NET Library RCE Flaw CVE-2026-131914 Exploited
`CVE-2026-131914, CVE-2026-132165, CVE-2026-132224 · EPSS 0.01 · CISA KEV`

A critical RCE vulnerability in the legacy Idunno.AntiCsrf ASP.NET library (versions 0.9.1.0 and 0.9.1 Beta) is being exploited in the wild.

**Do:** Discontinue using Idunno.AntiCsrf immediately.

[The Hacker News](https://thehackernews.com/2026/11/hackers-exploit-critical-aspnet-anti.html) · [CISA Advisories](https://www.cisa.gov/news-events/alerts/2026/11/24/cisa-adds-three-known-exploited-vulnerabilities-catalog) · [CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-132224) · [CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-131914) · [CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-132165) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/hackers-now-exploit-critical-drupal-rce-flaw-to-hijack-sites/) · [The Hacker News](https://thehackernews.com/2026/11/drupal-fail2install-exploit-details.html) · [SecurityWeek](https://www.securityweek.com/hackers-exploit-unpatched-flaw-in-defunct-idunno-anticsrf-library/)

### 🔴 SAP NetWeaver and Cisco Expressway Flaws Exploited in Attacks
`exploited`

Threat actors are actively exploiting vulnerabilities in SAP NetWeaver and Cisco Expressway to leak/modify server info and execute root commands.

**Do:** Apply the latest security updates for SAP NetWeaver and Cisco Expressway.

[SecurityWeek](https://www.securityweek.com/sap-netweaver-cisco-expressway-flaws-exploited-in-attacks/)

### 🔴 Now exploited: Xen Orchestra xo-server Empty-Object Login Token Flaw
`CVE-2023-25914, CVE-2023-25915, CVE-2025-41450, CVE-2026-103406 … · CVSS 9.8 · CISA KEV`

Xen Orchestra npm package xo-server contains a REST cookie parsing vulnerability allowing attackers to authenticate via an empty-object token.

**Do:** Update xo-server to the latest patched version.

[GitHub Advisory](https://github.com/advisories/GHSA-2r3w-c2vx-fv5g) · [CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-133469) · [CISA Advisories](https://www.cisa.gov/news-events/alerts/2026/11/25/cisa-adds-10-known-exploited-vulnerabilities-catalog)

### 🟠 Synology DiskStation Manager OAuth API Command Vulnerability
`CVE-2026-120382 · CVSS 9.8 · EPSS 0.01`

Synology DiskStation Manager (DSM) versions before 7.1.1-42962-10, 7.2.1-69057-14, 7.2.2-72806-11, 7.3.2-86009-6, and 7.4.1-90080-2 contain an argument delimiter command vulnerability in the OAuth API allowing arbitrary file read/write and DoS.

**Do:** Update Synology DSM to the latest fixed versions.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120382)

### 🟠 Kerberos Agent Authentication Bypass Flaw CVE-2026-135208
`CVE-2026-135208 · CVSS 9.8`

Kerberos Agent before 3.14.4 contains an authentication bypass flaw due to a hard-coded JWT secret key, allowing attackers to forge administrator tokens.

**Do:** Update Kerberos Agent to version 3.14.4 or later.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-135208)

### 🟠 Binary-Parser Code Injection Flaw CVE-2026-134814
`CVE-2026-134814 · EPSS 0.01`

Binary-parser versions prior to 2.3.1 contain a code injection vulnerability allowing attackers who control parser definitions to execute arbitrary code.

**Do:** Update binary-parser to version 2.3.1 or higher.

[The Hacker News](https://thehackernews.com/2026/11/critical-binary-parser-flaw-enables.html)

### 🟠 Spanish LaLiga Confirms Data Breach Exposing Fan Data
`exploited`

Spain's LaLiga disclosed a data breach exposing personal info of users and affiliated club services.

**Do:** Monitor accounts for potential phishing or credential reuse.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/spanish-laliga-confirms-hackers-stole-soccer-fans-personal-data/)

### 🟠 Austrian Foreign Ministry Website Breached
`exploited`

Hackers breached an Austrian Foreign Ministry website, accessing employee names and official contact details.

**Do:** Audit web application perimeters and authentication logs.

[The Record](https://therecord.media/austrian-foreign-ministry-says-website-hacked)

### 🟠 BadBox 3.0 Ad Fraud Operation Disrupted
`exploited`

Law enforcement or researchers disrupted the BadBox 3.0 operation involving backdoors on low-cost consumer devices used for ad fraud and proxies.

**Do:** Scan consumer and IoT devices for unauthorized proxy or ad-fraud activity.

[SecurityWeek](https://www.securityweek.com/badbox-3-0-ad-fraud-operation-generating-40-billion-daily-bid-requests-disrupted/)

### 🟠 phpAfterShell Deserialization RCE Vulnerability

Interrupted session overwrites in phpAfterShell can allow attackers controlling fresh data to trigger deserialization and RCE.

**Do:** Apply available patches or security updates for phpAfterShell.

[SecurityWeek](https://www.securityweek.com/phpaftershell-vulnerability-revives-php2shells-attack-path/)

### 🟠 GlobeTopper Suffers Cyberattack Disrupting Operations
`exploited`

B2B top-up provider GlobeTopper suffered a disruption and financial loss after a cyberattack involving stolen gift cards.

**Do:** Review access controls for B2B top-up platforms.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/globetopper-loses-25-million-after-hackers-steal-70k-in-gift-cards/)

### 🟠 Webworm Uses Modified SoftEther VPN for Stealth Access
`exploited`

China-aligned actor Webworm is using a customized SoftEther VPN Bridge disguised as network-monitoring software to evade detection.

**Do:** Monitor network perimeters for anomalous or disguised SoftEther VPN traffic signatures.

[The Hacker News](https://thehackernews.com/2026/11/webworm-suspected-of-modifying.html)

## 2026-11-22

### 🟠 GL.iNet Cloud Remote Management Flaw Exploited
`exploited`

Hackers are actively exploiting a vulnerability in GL.iNet cloud remote management services to install custom malware, backdoors, and reverse shells on customer routers and KVM devices.

**Do:** Disable cloud remote management on GL.iNet devices and check for unauthorized backdoors.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/hackers-exploit-glinet-cloud-flaw-to-infect-routers-kvm-devices/) · [The Hacker News](https://thehackernews.com/2026/11/hackers-exploited-glinet-cloud-flaw-to.html) · [SecurityWeek](https://www.securityweek.com/gl-inet-routers-kvms-compromised-via-remote-management-service-flaw/)

### 🟠 Rackspace Spot Cloud Platform Breach Exposes Kubernetes Secrets
`exploited`

Rackspace notified customers that compromised credentials led to a breach of its Rackspace Spot platform, enabling attackers to deploy unauthorized workloads and access Kubernetes secrets in customer clusters.

**Do:** Audit Rackspace Spot environments, rotate compromised credentials, and check Kubernetes clusters for unauthorized workloads.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/rackspace-spot-breach-let-hackers-access-customer-kubernetes-secrets/)

### 🟠 Cleverbridge Data Breach Exposes Credit Card Numbers and CVVs
`exploited`

E-commerce platform Cleverbridge suffered a data breach exposing customer payment card information, including credit card numbers and CVV security codes.

**Do:** Review statements for unauthorized transactions if you made purchases via Cleverbridge.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/cleverbridge-warns-hackers-stole-credit-card-numbers-cvvs-in-data-breach/)

### 🟠 OpenRouter Drops AI Providers Following Months of Prompt Theft
`exploited`

Attackers stole prompts and data from inside three AI inference providers for months, prompting OpenRouter to drop the providers.

**Do:** Audit AI vendor data retention policies and review integrations with third-party inference providers.

[The Hacker News](https://thehackernews.com/2026/11/openrouter-drops-3-providers-after.html) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/openrouter-drops-ai-providers-over-leaked-prompts-and-secrets/)

### 🟠 Ghostscript Sandbox-Escape RCE Vulnerability in File Processing Apps

A now-patched flaw in Ghostscript allows crafted files to escape the security sandbox and achieve remote code execution on servers processing PDFs and images.

**Do:** Update Ghostscript to the latest patched version across all Linux servers handling user-uploaded documents.

[The Hacker News](https://thehackernews.com/2026/11/researchers-demonstrate-ghostscript.html)

## 2026-11-21

### 🔴 Microsoft Entra Connect Health Flaw Exploited in Tenant Breach
`exploited`

Attackers exploited a vulnerability in Microsoft Entra Connect Health to gain unauthorized access to administrator email addresses and tenant configuration information.

**Do:** Review Microsoft security advisories and audit Entra tenant configuration and access logs.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/microsoft-entra-connect-health-flaw-exploited-to-steal-tenant-data/)

### 🔴 FBI National Crime Information Center Database Breached
`exploited`

FBI systems containing the National Crime Information Center (NCIC) database used for law enforcement information sharing have reportedly been breached.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/fbi-reportedly-hacked-again-this-time-targeting-nationwide-police-database/) · [SecurityWeek](https://www.securityweek.com/fbi-investigating-apparent-hack-of-its-key-national-criminal-justice-database-ap-source-says/) · [The Record](https://therecord.media/fbi-cyberattack-data-breach)

### 🔴 MONAI Label Arbitrary File Write Zero-Day Exploited by AI Agents
`exploited`

China-linked threat actors used autonomous AI agents to discover and exploit a zero-day arbitrary file write vulnerability in MONAI Label 0.8.5 and earlier, gaining root access to a university server.

**Do:** Upgrade MONAI Label beyond version 0.8.5 or restrict network access to the server.

[The Hacker News](https://thehackernews.com/2026/11/attackers-ai-agents-found-zero-day-in.html) · [SecurityWeek](https://www.securityweek.com/amazon-china-linked-hackers-ai-agents-exploited-medical-software-zero-day/)

### 🟠 GnuPG GPGME Memory Bug CVE-2026-129975
`CVE-2026-129975`

A memory bug in GPGME versions prior to 2.3.0, triggered by a malicious OpenPGP key with a long user ID, could expose application data. Fixed versions have been released.

**Do:** Upgrade GPGME to version 2.3.0 or later.

[The Hacker News](https://thehackernews.com/2026/11/gnupg-warns-critical-gpgme-flaw-could.html)

## 2026-11-20

### 🔴 SAP NetWeaver JNDI Data Query Logic Flaw
`CVE-2025-42884 · EPSS 0.00 · CISA KEV`

SAP NetWeaver Enterprise Portal contains an improper neutralization vulnerability in data query logic (CVE-2025-42884) allowing unauthenticated attackers to disclose or modify server information. Listed in CISA KEV.

**Do:** Apply vendor mitigations and follow CISA BOD 26-04 guidance.

[CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2025-42884)

### 🔴 IBM Guardium Data Protection Insecure Deserialization Vulnerability
`CVE-2026-84236 · CVSS 9.8`

IBM Guardium Data Protection 12.2 contains an insecure deserialization vulnerability in the SharePoint Tap MulticastTransceiver component (CVE-2026-84236), enabling unauthenticated remote code execution.

**Do:** Apply patches provided by IBM for Guardium Data Protection 12.2 immediately.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-84236)

### 🔴 Daptin Unauthenticated SQL Injection via Sort Parameter
`CVE-2026-77367 · CVSS 9.4`

Daptin contains an unauthenticated SQL injection vulnerability via the 'sort' query parameter on entity list endpoints (CVE-2026-77367), allowing attackers to inject arbitrary SQL.

**Do:** Update Daptin to the patched version.

[GitHub Advisory](https://github.com/advisories/GHSA-hq2p-f2vj-v3cm)

### 🔴 Now exploited: N-able Server Breach Causes Global Mail Assure and SpamExperts Outage
`CVE-2026-133968, CVE-2026-134624 · CISA KEV`

Attackers breached an N-able server, causing a major worldwide service outage affecting Mail Assure and SpamExperts Hosted Cloud services.

**Do:** Check N-able status updates and advisory guidance.

[BleepingComputer](https://www.bleepingcomputer.com/news/microsoft/n-able-says-recent-security-breach-led-to-major-service-outage/) · [The Hacker News](https://thehackernews.com/2026/11/n-able-discloses-critical-mail-assure.html) · [SecurityWeek](https://www.securityweek.com/n-able-patches-critical-flaw-disclosed-after-mail-assure-cyberattack/) · [CISA Advisories](https://www.cisa.gov/news-events/alerts/2026/11/23/cisa-adds-two-known-exploited-vulnerabilities-catalog) · [CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-133968) · [CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-134624) · [The Hacker News](https://thehackernews.com/2026/11/hackers-exploit-n-able-mailassure-flaw.html)

### 🟠 F5 Patches Critical BIG-IP RCE and DoS Vulnerabilities

F5 released emergency patches for five critical BIG-IP vulnerabilities that could allow attackers to trigger denial-of-service or achieve remote code execution. Patches are available from F5.

**Do:** Apply the latest F5 BIG-IP security patches immediately.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/f5-releases-emergency-patches-for-critical-big-ip-rce-flaws/)

### 🟠 SBC Medical Group Data Breach Exposes 1.6 Million Customers
`exploited`

SBC Medical Group disclosed two cybersecurity incidents exposing sensitive customer and employee personal data belonging to 1.6 million people.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/hackers-steal-data-of-16-million-sbc-medical-group-customers/) · [SecurityWeek](https://www.securityweek.com/sbc-medical-group-data-breach-impacts-over-2-million/)

### 🟠 Etherpad Pre-Auth Arbitrary File Read Vulnerability
`CVE-2026-114516 · CVSS 9.8`

Etherpad-lite contains an unauthenticated path-traversal vulnerability in the static file handler (CVE-2026-114516) allowing remote users to read arbitrary files on the server.

**Do:** Update ep_etherpad-lite to the latest patched version.

[GitHub Advisory](https://github.com/advisories/GHSA-mc8w-wjhw-45x5)

### 🟠 Flyto2 Core Arbitrary File Write Incomplete Fix
`CVE-2026-77312 · CVSS 10.0`

Flyto2 Core contains an arbitrary file write vulnerability via unguarded write modules (CVE-2026-77312, building on CVE-2026-67429), allowing authenticated clients to achieve code execution.

**Do:** Update pip:flyto-core to the latest patched version.

[GitHub Advisory](https://github.com/advisories/GHSA-p34x-fmph-9fjx)

### 🟠 Refitter OpenAPI Content-Type Code Execution Vulnerability
`CVE-2026-63344 · CVSS 9.3 · EPSS 0.00`

Refitter allows arbitrary code execution through unescaped OpenAPI content-type values (CVE-2026-63344), injecting a top-level file class with a ModuleInitializer method.

**Do:** Update Refitter to the latest patched version.

[GitHub Advisory](https://github.com/advisories/GHSA-p32v-8v8j-j534)

### 🟠 Refitter OpenAPI Header Parameter Code Execution Flaw
`CVE-2026-63346 · CVSS 9.3 · EPSS 0.00`

Refitter allows code execution through unescaped OpenAPI header parameter names (CVE-2026-63346), injecting malicious .NET code executed at assembly load time.

**Do:** Update Refitter to the latest patched version.

[GitHub Advisory](https://github.com/advisories/GHSA-58x9-vjvp-6mx8)

### 🟠 Refitter OpenAPI Path Code Execution Vulnerability
`CVE-2026-63345 · CVSS 9.3 · EPSS 0.00`

Refitter allows arbitrary code execution through unescaped OpenAPI paths (CVE-2026-63345), injecting a top-level file class with a ModuleInitializer method.

**Do:** Update Refitter to the latest patched version.

[GitHub Advisory](https://github.com/advisories/GHSA-3fhm-p725-h3g3)

### 🟠 NLTK Incomplete JVM/JAR Sandbox Bypass Vulnerability
`CVE-2026-128138 · CVSS 9.8`

NLTK 3.10.3 contains an incomplete fix for JVM argument-injection and untrusted JAR execution (CVE-2026-128138), allowing sandbox bypass through unvalidated launcher tokens.

**Do:** Update NLTK beyond version 3.10.3 or apply vendor guidance.

[GitHub Advisory](https://github.com/advisories/GHSA-x8q7-6c7m-52gw)

### 🟠 Fabio Access-Control Bypass via Unnormalized Request Paths
`CVE-2026-104099 · CVSS 9.1 · EPSS 0.00`

go:github.com/fabiolb/fabio has an access-control bypass (CVE-2026-104099) where route selection uses raw unnormalized request paths, allowing unauthenticated attackers to bypass per-route ACL and basic-auth gates using dot-segments or encoded dots.

**Do:** Update fabio to a version with normalized request path handling.

[GitHub Advisory](https://github.com/advisories/GHSA-4hrh-34w3-5ww8)

### 🟠 Gladys Assistant Backup Restore OS Command Injection
`CVE-2026-133500 · CVSS 9.1 · exploited`

Gladys Assistant up to 4.71.0 contains an OS command injection vulnerability in the gateway.downloadBackup.js component via manipulation of the file_url argument. A public exploit is available, and version 4.72.0 fixes the issue.

**Do:** Upgrade Gladys Assistant to version 4.72.0 or later.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-133500)

### 🟠 Gladys Assistant Backup Restore Path Traversal Flaw
`CVE-2026-133501 · CVSS 9.0 · exploited`

Gladys Assistant up to 4.71.0 contains a path traversal flaw in the backup download handler. Public exploits exist, and upgrading to version 4.72.0 mitigates the issue.

**Do:** Upgrade Gladys Assistant to version 4.72.0 or later.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-133501)

### 🟠 Linux KVM Flaw Lets Guest VMs Access Host Memory on AMD
`CVE-2026-99312 · EPSS 0.00`

A flaw tracked as CVE-2026-99312 in Linux KVM allows guest VMs to read host memory on systems with AMD processors and nested virtualization enabled. Fixed kernels have been released.

**Do:** Update Linux kernel to a patched version with the KVM fix.

[The Hacker News](https://thehackernews.com/2026/11/new-linux-kvm-flaw-cve-2026-99312-lets.html)

### 🟠 IBM Guardium Data Protection SharePoint S-TAP RelayService Flaw
`CVE-2026-82339 · CVSS 9.1`

IBM Guardium Data Protection 12.2 contains a missing authentication vulnerability in the SharePoint S-TAP RelayService (CVE-2026-82339) allowing unauthenticated network attackers to inject forged audit events and access monitoring policies.

**Do:** Apply available security updates from IBM for Guardium Data Protection 12.2.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82339)

### 🟠 Daptin Broken Access Control in YJS Collaboration Endpoint
`CVE-2026-77369 · CVSS 9.6`

Daptin is vulnerable to broken access control (IDOR) in the generic YJS WebSocket collaboration endpoint (CVE-2026-77369), allowing any authenticated user to read documents without proper per-resource checks.

**Do:** Update Daptin to the latest patched version.

[GitHub Advisory](https://github.com/advisories/GHSA-wj7x-58c2-5793)

### 🟠 ASUS Control Center Express Hard-Coded Key and Critical Flaws

ASUS released Control Center Express v1.7.29 to fix three critical vulnerabilities including hard-coded keys that could let remote attackers gain administrative control.

**Do:** Upgrade ASUS Control Center Express to v1.7.29 or later.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/asus-warns-of-critical-hard-coded-key-flaw-in-control-center-express/)

### 🟠 Bell Canada Breach Exposes Enterprise Customer Data
`exploited`

Bell Canada confirmed a threat actor breached its systems and stole enterprise customer data, including circuit provisioning information.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/bell-canada-says-agentic-hacker-stole-enterprise-customer-data/)

### 🟠 J.P. Morgan Chase Third-Party Data Breach
`exploited`

J.P. Morgan Chase suffered a data breach following a cyberattack at a third-party service provider that exposed customer personal information and marketing data.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/vendor-data-breach-exposes-chase-visa-mastercard-customer-info/)

### 🟠 SonicWall Warns Generation 6 Firewalls Unpatched for Critical Flaws

SonicWall urged customers running Generation 6 firewalls to retire and replace them immediately, noting they will not receive security patches for critical flaws amid rising AI-assisted attacks.

**Do:** Retire and replace SonicWall Gen 6 firewalls and remove them from the internet edge.

[The Hacker News](https://thehackernews.com/2026/11/sonicwall-warns-gen-6-firewalls-wont.html)

### 🟠 D-Link DCS-935L Local Recording CGI OS Command Injection
`CVE-2026-133680 · CVSS 9.9`

D-Link DCS-935L version 1.10.01 contains an OS command injection vulnerability (CVE-2026-133680) in the loginRouter function of web/cgi-bin/localrecording/setconf.cgi via manipulated account/password arguments. A public exploit is available.

**Do:** Restrict access to vulnerable D-Link devices or replace end-of-life hardware.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-133680)

### 🟠 Jupyter MCP Server DNS Rebinding Management Route Flaw
`CVE-2026-77359 · CVSS 9.3`

Jupyter MCP Server contains a DNS rebinding vulnerability in custom management routes (CVE-2026-77359), allowing malicious websites to replace the active Jupyter backend.

**Do:** Update jupyter-mcp-server to the latest patched version.

[GitHub Advisory](https://github.com/advisories/GHSA-9x8x-crjq-g64h)

### 🟠 WhatsApp for Android Incomplete Ad-Reply URL Validation Flaw
`CVE-2026-23871 · exploited`

WhatsApp for Android and WhatsApp Business for Android before 2.26.17.4 contain a vulnerability (CVE-2026-23871) involving incomplete validation of external ad-reply URLs, suspected of exploitation in scam campaigns.

**Do:** Update WhatsApp for Android to version 2.26.17.4 or later.

[SecurityWeek](https://www.securityweek.com/whatsapp-fixes-flaw-uncovered-while-disrupting-scam-campaign/) · [The Hacker News](https://thehackernews.com/2026/11/whatsapp-patches-3-security-flaws.html)

### 🟠 Ruby Patches Ruby2Shell Heap Buffer Overflow RCE Vulnerability
`CVE-2026-132825 · EPSS 0.00`

Ruby patched a heap-based buffer overflow vulnerability tracked as CVE-2026-132825, known as Ruby2Shell, which could lead to remote code execution.

**Do:** Update Ruby to the latest patched version.

[SecurityWeek](https://www.securityweek.com/ruby-patches-ruby2shell-vulnerability-that-could-lead-to-rce/)

### 🟠 West Virginia Legislature Hit by Ongoing Cyber Incident
`exploited`

The West Virginia Legislature experienced an ongoing cybersecurity incident affecting IT systems without spreading to other government entities.

[The Record](https://therecord.media/west-virginia-legislature-cyberattack)

### 🟠 The Container Store Restores Systems Following Cyberattack
`exploited`

The Container Store restored its website and systems following a cybersecurity incident.

[The Record](https://therecord.media/container-store-restores-systems-cyberattack)

### 🟠 Bazuka Android Malware Framework Disclosed
`exploited`

Researchers disclosed a new Android malware framework called Bazuka featuring fake screen overlays and LLM integration for command and control at scale.

[The Hacker News](https://thehackernews.com/2026/11/bazuka-android-malware-uses-fake-screen.html)

### 🟠 ROMULUS ClickFix Attacks Deliver New CNCMachineRMS RAT Variant
`exploited`

Threat actors are using the ROMULUS ClickFix malware delivery platform to distribute an undocumented remote access trojan similar to CNCMachineRMS via signed binary sideloading.

**Do:** Monitor endpoints for suspicious ClickFix lures and binary sideloading activity.

[The Hacker News](https://thehackernews.com/2026/11/romulus-clickfix-attacks-deliver-rat.html)

### 🟠 Unpatched Windows FastUnlock Flaw Allows Program Execution on Locked PCs

An unpatched local zero-day technique called FastUnlock allows a user with physical access to a locked Windows PC to run limited-privilege programs without signing in.

**Do:** Restrict physical access to endpoints.

[The Hacker News](https://thehackernews.com/2026/11/new-unpatched-windows-0-day-fastunlock.html)

## 2026-11-19

### 🔴 Palo Alto Networks PAN-OS Flaws CVE-2026-109618/19 Exploited
`CVE-2026-109618, CVE-2026-109619 · EPSS 1.00 · CISA KEV`

Attackers are actively exploiting unauthenticated RCE vulnerabilities CVE-2026-109618 and CVE-2026-109619 against internet-exposed PAN-OS management interfaces.

**Do:** Apply emergency patches and restrict management access from the internet.

[The Hacker News](https://thehackernews.com/2026/11/everything-is-web-application-including.html)

### 🔴 Now exploited: VMware vCenter Authentication Bypass Exploited as Zero-Day
`CVE-2025-42884, CVE-2026-123890, CVE-2026-129448, CVE-2026-76466 · CISA KEV`

A critical authentication bypass flaw in VMware vCenter was exploited as a zero-day by a China-linked espionage group before Broadcom released patches.

**Do:** Apply the latest updates for VMware vCenter across all supported branches immediately.

[The Hacker News](https://thehackernews.com/2026/11/critical-vmware-vcenter-flaw-cvss-98.html) · [SecurityWeek](https://www.securityweek.com/newly-patched-vmware-vcenter-flaw-exploited-as-zero-day-by-chinese-apt/) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/vmware-patches-vcenter-zero-day-exploited-in-attacks-since-september/) · [The Hacker News](https://thehackernews.com/2026/11/china-linked-hackers-exploit-critical.html) · [CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-123890) · [CISA Advisories](https://www.cisa.gov/news-events/alerts/2026/11/20/cisa-adds-four-known-exploited-vulnerabilities-catalog) · [The Hacker News](https://thehackernews.com/2026/11/hackers-exploit-critical-vmware-cisco.html)

### 🔴 F5 Patches Critical NGINX2Root Flaws with Public PoCs
`exploited`

F5 patched critical NGINX2Root vulnerabilities that allow remote, unauthenticated attackers to execute arbitrary code, with public proof-of-concept exploits available.

**Do:** Apply the latest security patches from F5 immediately and monitor for exploitation attempts.

[SecurityWeek](https://www.securityweek.com/f5-patches-critical-nginx2root-flaws-as-poc-exploits-go-public/) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/critical-nginx-nginx2root-bugs-let-attackers-hijack-servers/)

### 🔴 Now exploited: Cisco Expressway Vulnerability Exploited Following PoC Release
`CVE-2026-76466 · CISA KEV`

Attackers have exploited clustered Cisco Expressway devices at an organization shortly after proof-of-concept code was released, preparing for lateral movement.

**Do:** Review Cisco Expressway devices for indicators of compromise and apply vendor patches.

[SecurityWeek](https://www.securityweek.com/hackers-exploit-cisco-expressway-vulnerability-soon-after-poc-release/) · [The Hacker News](https://thehackernews.com/2026/11/hackers-exploit-critical-cisco.html) · [CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-76466)

### 🟠 Drupal Patches Critical Remote Code Execution Vulnerability

The Drupal Security Team has patched a critical remote code execution vulnerability that could allow full site takeover.

**Do:** Update Drupal core to the latest security release immediately.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/drupal-patches-critical-rce-flaw-warns-exploits-may-surface-quickly/) · [The Hacker News](https://thehackernews.com/2026/11/drupal-patches-critical-installer-flaw.html)

### 🟠 PHP Prepares Critical Security Updates for Session Upload RCE
`CVE-2026-115560, CVE-2026-126714`

PHP is preparing updates for a critical RCE vulnerability in session upload progress (CVE-2026-115560) disclosed shortly after previous patches.

**Do:** Prepare to apply PHP security updates upon release.

[The Hacker News](https://thehackernews.com/2026/11/php-warns-of-critical-security-flaws.html) · [SecurityWeek](https://www.securityweek.com/php-readies-critical-security-updates-to-patch-another-rce-flaw/) · [The Hacker News](https://thehackernews.com/2026/11/php-fixes-7-critical-flaws-including.html) · [SecurityWeek](https://www.securityweek.com/php-patches-seven-critical-rce-vulnerabilities/) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/php-security-updates-fix-18-flaws-including-critical-rce-bugs/) · [The Hacker News](https://thehackernews.com/2026/11/phpaftershell-explained-how-hackers.html)

### 🟠 N-able Cloud Server Breach Disrupts Email Security Management
`exploited`

Unauthorized access to an N-able Mail Assure and Spam Experts Hosted Cloud server caused management interfaces and APIs to be disabled.

**Do:** Monitor N-able security advisories and review cloud management logs.

[The Hacker News](https://thehackernews.com/2026/11/n-able-confirms-hackers-accessed-cloud.html) · [SecurityWeek](https://www.securityweek.com/n-able-blames-service-disruption-on-cyberattack/)

### 🟠 Splunk Enterprise Security Arbitrary Code Execution Flaw
`CVE-2026-131202 · CVSS 9.1`

Splunk Enterprise Security versions below 8.7.0 contain a vulnerability allowing users with the ess_admin role to execute arbitrary code on the search head.

**Do:** Upgrade Splunk Enterprise Security to version 8.7.0 or higher.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-131202)

### 🟠 Splunk SOAR App Wizard Code Execution Vulnerability
`CVE-2026-131253 · CVSS 9.9`

Splunk SOAR versions below 8.8.0 contain a vulnerability allowing authenticated users with specific permissions to execute arbitrary code via the App Wizard.

**Do:** Upgrade Splunk SOAR to version 8.8.0 or higher.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-131253)

### 🟠 Splunk Enterprise RapidDiag Unauthenticated SPL Search Vulnerability
`CVE-2026-76535 · CVSS 9.1`

Splunk Enterprise versions below 10.6.1, 10.4.5, 10.2.9, 10.0.12, and 9.4.17 allow unauthenticated users to run arbitrary SPL searches via RapidDiag due to an empty shared secret.

**Do:** Upgrade Splunk Enterprise to the latest patched versions.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76535)

### 🟠 Splunk Enterprise Clustering REST API Configuration Flaw
`CVE-2026-76536 · CVSS 9.4`

Splunk Enterprise versions below 10.4.5, 10.2.9, 10.0.12, and 9.4.17 allow unauthenticated users to modify clustering configuration via the REST API using an empty clustering shared secret.

**Do:** Upgrade Splunk Enterprise to patched versions.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76536)

### 🟠 Miren Runtime Authentication Bypass in RPC Layer
`CVE-2026-75521 · CVSS 10.0`

Miren Runtime RPC server fails to verify client certificates against the cluster CA, allowing any network-reachable party to present a self-signed cert and gain superuser access.

**Do:** Upgrade Miren Runtime to a patched version and restrict network access to the RPC listener.

[GitHub Advisory](https://github.com/advisories/GHSA-8fh7-7q4q-cq52)

### 🟠 Elecbrakes EB2, VM1, and ELBC2000 Safety Flaws
`CVE-2026-124281, CVE-2026-125273, CVE-2026-96805`

Multiple vulnerabilities (CVE-2026-124281, CVE-2026-125273, CVE-2026-96805) in Elecbrakes EB2 (<=3.0.4.2.0), VM1 (<1.3.4.2.1), and ELBC2000 allow attackers to gain control of trailer brakes or modify firmware.

**Do:** Check vendor advisory for available firmware updates.

[CISA Advisories](https://www.cisa.gov/news-events/ics-advisories/icsa-26-323-02)

### 🟠 Ruby Fixes Regex and String Memory-Safety Flaws

Ruby released fixes for seven memory-safety flaws in its regex engine and string case-conversion code, with PoCs showing RCE potential for five of them.

**Do:** Update Ruby to the latest fixed versions.

[The Hacker News](https://thehackernews.com/2026/11/ruby-releases-fixes-for-7-regex-and.html)

### 🟠 Transport for London Data Breach Exposes Oyster Card Users
`exploited`

Transport for London announced a data breach exposing account details for approximately 265,000 Oyster photocard customers.

**Do:** Notify affected users and monitor accounts for suspicious activity.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/transport-for-london-breach-exposes-265-000-oyster-card-users-data/)

### 🟠 European Commission Confirms Cyberattack Using AI Tool
`exploited`

The European Commission confirmed a cyberattack in which threat actors utilized the ARTEX open-source AI hacking platform.

**Do:** Review systems for indicators associated with AI-driven attack frameworks.

[The Record](https://therecord.media/european-commission-confirms-cyberattack-using-ai) · [SecurityWeek](https://www.securityweek.com/european-commission-confirms-ai-assisted-cyberattack-disrupted-services/)

### 🟠 Ukrainian Authorities Arrest International Ransomware Suspects
`exploited`

Ukrainian authorities arrested four suspects linked to an international ransomware network that extorted over $40 million globally.

[The Record](https://therecord.media/ukraine-ransomware-arrests-cyber)

### 🟠 Splunk SOAR Playbook Reference Binding Vulnerability
`CVE-2026-131287 · CVSS 9.6`

Splunk SOAR versions below 8.8.0 allow users with playbook permissions to cause cross-repository playbook references to run attacker-controlled code when repository names are reused.

**Do:** Upgrade Splunk SOAR to version 8.8.0 or higher.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-131287)

### 🟠 Todoist MCP Server DNS Rebinding Data Access Vulnerability
`CVE-2026-76807 · CVSS 9.3 · EPSS 0.00`

The self-hosted todoist-mcp-http server (version 10.3.1) is vulnerable to browser DNS rebinding, allowing malicious websites to write and delete data through local MCP endpoints.

**Do:** Update todoist-mcp and avoid running the optional Streamable HTTP server exposed to browsers.

[GitHub Advisory](https://github.com/advisories/GHSA-833v-v58w-294h)

### 🟠 Jane PHP Open-API-3 PHPDoc Breakout RCE Vulnerability
`CVE-2026-63412 · CVSS 9.3 · EPSS 0.00`

jane-php/open-api-3 emits raw PHPDoc comment text for query parameters, allowing attackers to inject closing comment syntax and execute arbitrary PHP code during client generation.

**Do:** Update jane-php/open-api-3 to a patched version when available.

[GitHub Advisory](https://github.com/advisories/GHSA-q8v2-3j4h-xg2p)

### 🟠 Jane PHP Open-API-3 Header Parameter PHPDoc Breakout RCE
`CVE-2026-63413 · CVSS 9.3 · EPSS 0.00`

jane-php/open-api-3 allows remote code execution via header parameter names due to unescaped insertion into PHPDoc blocks.

**Do:** Update jane-php/open-api-3 to a patched version.

[GitHub Advisory](https://github.com/advisories/GHSA-x9xr-53qx-9qcf)

### 🟠 Jane PHP Open-API-3 Parameter Description PHPDoc Breakout RCE
`CVE-2026-63411 · CVSS 9.3 · EPSS 0.00`

jane-php/open-api-3 contains an RCE vulnerability via parameter descriptions due to raw PHPDoc comment emission.

**Do:** Update jane-php/open-api-3 to a patched version.

[GitHub Advisory](https://github.com/advisories/GHSA-xwcw-j52r-34x4)

### 🟠 Splunk Patches Multiple Flaws Across Core Products

Splunk released security updates resolving critical and high-severity issues leading to authentication bypass, RCE, and privilege escalation.

**Do:** Apply the latest Splunk security patches.

[SecurityWeek](https://www.securityweek.com/splunk-patches-nearly-140-flaws-across-three-core-products/)

### 🟠 libumqtt Integer Underflow Vulnerability CVE-2026-125132
`CVE-2026-125132`

libumqtt <=1.1.1 contains an integer underflow vulnerability (CVE-2026-125132) allowing remote DoS, memory corruption, or information disclosure.

**Do:** Upgrade libumqtt beyond version 1.1.1.

[CISA Advisories](https://www.cisa.gov/news-events/ics-advisories/icsa-26-323-03)

### 🟠 Autonomy Logic OpenPLC Runtime Race Condition CVE-2026-126088
`CVE-2026-126088`

Autonomy Logic OpenPLC Runtime <=4.2.4 contains a race condition flaw (CVE-2026-126088) allowing unauthenticated creation of admin accounts.

**Do:** Update OpenPLC Runtime to versions above 4.2.4.

[CISA Advisories](https://www.cisa.gov/news-events/ics-advisories/icsa-26-323-01)

### 🟠 Database RCE Exploits Affecting PostgreSQL, MySQL and Oracle

A researcher published proof-of-concept exploits against memory-corruption bugs in PostgreSQL, MySQL, ClickHouse, and Oracle allowing low-privilege database accounts to run code.

**Do:** Review database permissions and apply vendor patches for underlying memory-corruption issues.

[The Hacker News](https://thehackernews.com/2026/11/researcher-demonstrates-database-rce.html)

### 🟠 NVIDIA Investigating Gentlemen Ransomware Breach Claims

NVIDIA is investigating claims by the Gentlemen ransomware group after the company was listed on their dark web leak site.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/nvidia-investigating-gentlemen-ransomware-breach-claims/) · [SecurityWeek](https://www.securityweek.com/nvidia-responds-to-gentlemen-ransomware-claim/)

