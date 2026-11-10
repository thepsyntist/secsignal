# Security signal: last 7 days

🔴 act now · 🟠 worth knowing

## 2026-11-10

### 🔴 Google Chrome XML Use-After-Free Vulnerability (CVE-2026-125350)
`CVE-2026-125350 · exploited`

Google has issued an emergency security update to patch a high-severity use-after-free vulnerability in Chrome's XML component (CVE-2026-125350), which is actively exploited in the wild as a zero-day.

**Do:** Update Google Chrome to the latest version immediately.

[SecurityWeek](https://www.securityweek.com/chrome-update-patches-exploited-xml-zero-day-eighth-this-year/) · [The Hacker News](https://thehackernews.com/2026/11/google-issues-chrome-security-update.html) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/google-patches-eighth-chrome-zero-day-exploited-in-attacks-this-year/)

### 🔴 Barracuda ESG Flaws Exploited to Gain Root Access
`exploited`

Barracuda Networks warned that attackers are actively exploiting recently patched Email Security Gateway (ESG) vulnerabilities to achieve root command execution.

**Do:** Ensure all Barracuda Email Security Gateway appliances are fully patched and inspect for signs of compromise.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/hackers-exploit-barracuda-email-security-gateway-flaws-to-get-root-access/)

### 🔴 N-able Takes Cloud Platform Offline Following Zero-Day Disclosures
`exploited`

N-able took hosted N-central environments offline and advised on-premises customers to shut down servers after a researcher published over 30 alleged zero-days.

**Do:** Take N-central servers offline per vendor advisory until patches are available.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/n-able-takes-cloud-platform-offline-after-30-plus-zero-days-published/) · [The Hacker News](https://thehackernews.com/2026/11/n-able-takes-hosted-n-central-offline.html) · [SecurityWeek](https://www.securityweek.com/n-able-takes-n-central-offline-as-researcher-drops-over-30-zero-days/)

### 🔴 SAP NetWeaver Remote Code Execution Vulnerability
`CVE-2026-109795 · CVSS 9.9`

SAP NetWeaver lacks sufficient input validation and authorization checks in remote-enabled functionality, allowing low-privileged attackers to execute arbitrary code.

**Do:** Apply relevant SAP security patches for NetWeaver.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109795) · [The Hacker News](https://thehackernews.com/2026/11/sap-patches-four-cvss-100-flaws.html)

### 🔴 SAP NetWeaver AS ABAP Authentication Bypass Vulnerability
`CVE-2026-120017 · CVSS 10.0`

SAP NetWeaver AS ABAP and ABAP Platform inadequately verify incoming authentication assertions under specific configurations, enabling user impersonation.

**Do:** Apply SAP security updates for AS ABAP.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120017)

### 🔴 SAP NetWeaver Application Server ABAP Memory Corruption Flaw
`CVE-2026-76964 · CVSS 10.0`

SAP NetWeaver Application Server ABAP insufficiently validates network input, allowing unauthenticated attackers to trigger memory corruption and execute code.

**Do:** Apply SAP security patches.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76964)

### 🔴 SAP Gateway Default Access Control List Misconfiguration
`CVE-2026-89103 · CVSS 10.0`

SAP Gateway activates a default Access Control List with high privileges, allowing external attackers to be treated as internal application servers.

**Do:** Review and harden SAP Gateway ACL configurations.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89103)

### 🔴 SAP Web Dispatcher Memory Corruption Vulnerability
`CVE-2026-89126 · CVSS 10.0`

SAP Web Dispatcher improperly validates network input, allowing unauthenticated remote attackers to trigger memory corruption and achieve full system compromise.

**Do:** Apply SAP security patches.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89126)

### 🔴 Turla Threat Group Deploys Cereal Malware Against Exchange Servers
`exploited`

The Russian state-sponsored threat group Turla is using a newly discovered modular malware toolset called 'Cereal' to target Microsoft Exchange servers at government organizations and intercept emails.

**Do:** Audit Microsoft Exchange servers for unauthorized access and monitor for indicators of compromise related to Cereal malware.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/turla-hackers-use-new-ceral-malware-to-spy-on-govt-exchange-servers/) · [The Hacker News](https://thehackernews.com/2026/11/russian-turla-hackers-use-new-cereal.html)

### 🔴 France Blames Iran for Sabotage Attack on Supermarket Refrigerators
`exploited`

The French government stated that an October cyberattack affecting refrigeration controllers at roughly 700 retail sites, causing food losses and fires, was conducted by Iran's IRGC.

**Do:** Isolate and secure industrial refrigeration and HVAC controllers from direct internet access.

[SecurityWeek](https://www.securityweek.com/france-blames-iran-for-a-cyberattack-that-heated-supermarket-refrigerators/) · [The Hacker News](https://thehackernews.com/2026/11/france-blames-iran-for-sabotage-attack.html)

### 🟠 Kubero Authentication Bypass via Hardcoded JWT Secret
`CVE-2026-125370 · CVSS 9.8`

Kubero versions 3.0.0 through 3.1.1 use a hardcoded fallback signing secret when JWT_SECRET is unset, allowing unauthenticated attackers to forge administrative JWTs.

**Do:** Set a secure, unique JWT_SECRET environment variable and upgrade Kubero.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-125370)

### 🟠 INDOTALENT WHMS Authentication Bypass via Hard-coded JWT Key
`CVE-2026-125383 · CVSS 9.8`

INDOTALENT WHMS before 10.20261109 contains a hard-coded JWT signing key and issuer in appsettings.json, allowing attackers to forge administrator tokens.

**Do:** Upgrade INDOTALENT WHMS to version 10.20261109 or later.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-125383)

### 🟠 SAP NetWeaver Knowledge Management XSL Transformation Flaw
`CVE-2026-109803 · CVSS 9.9`

SAP NetWeaver Knowledge Management (XML Forms) permits unauthorized XSL transformations leading to potential code execution.

**Do:** Apply relevant SAP security patches.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109803)

### 🟠 D-Link M60 MQTT Broker Hard-coded Credentials Flaw
`CVE-2026-125086 · CVSS 10.0`

D-Link M60 version 1.12.B01 contains hard-coded credentials within the emDaemon MQTT Broker configuration.

**Do:** Apply firmware updates from D-Link or restrict remote access to the device.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-125086)

### 🟠 SAP NetWeaver ABAP Platform Missing Authorization Check
`CVE-2026-76965 · CVSS 9.9`

SAP NetWeaver AS ABAP lacks authorization checks for internal functionality, enabling low-privileged users to execute OS commands.

**Do:** Apply SAP security patches.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76965)

### 🟠 SAP Web Dispatcher and ICM Request Validation Flaw
`CVE-2026-89119 · CVSS 9.6`

SAP Web Dispatcher and ICM lack sufficient request validation, exposing administrative functionality to cross-site request attacks.

**Do:** Apply SAP security notes.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-89119)

### 🟠 SAP November 2026 Patches Fixes Multiple Maximum-Severity Flaws

SAP released its November 2026 security updates patching 35 vulnerabilities, including four maximum-severity issues affecting NetWeaver, Web Dispatcher, and Gateway software.

**Do:** Apply SAP November 2026 security updates across all affected NetWeaver and Web Dispatcher instances.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/sap-patches-four-maximum-severity-security-vulnerabilities/)

### 🟠 Kubeflow Pipelines API Server Authorization Bypass Vulnerability
`CVE-2026-77596 · CVSS 9.6 · EPSS 0.00`

In multi-user mode, Kubeflow Pipelines API server upload endpoints fail to perform authorization when the target namespace is empty, allowing shared pipeline uploads.

**Do:** Review Kubeflow Pipelines configurations and restrict access to multi-user upload endpoints.

[GitHub Advisory](https://github.com/advisories/GHSA-rjr3-43j3-4q8g)

### 🟠 York University Cyberattack Exposes Personal Data
`exploited`

York University suffered a cybersecurity incident involving the theft of personal information submitted through online forms dating back to 2007.

**Do:** Monitor accounts and review data retention practices for online form submissions.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/york-university-breach-exposed-personal-information-dating-to-2007/)

### 🟠 INDOTALENT WHMS Default Credentials Vulnerability
`CVE-2026-125384 · CVSS 9.8`

INDOTALENT WHMS before 10.20261109 creates a default admin account with hardcoded credentials (admin@root.com / 123456).

**Do:** Change or remove default administrative credentials immediately.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-125384)

### 🟠 SAP BusinessObjects Web Intelligence External Entity Vulnerability
`CVE-2026-109798 · CVSS 9.1`

SAP BusinessObjects BI Platform (Web Intelligence) fails to properly restrict external entity resolution during OLAP connection requests, allowing file reading.

**Do:** Apply SAP security notes for BusinessObjects.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109798)

### 🟠 Apple Patches iMessage Privacy Flaws and Bluetooth Issues

Apple released security updates to fix iMessage privacy vulnerabilities allowing unauthorized users to join group chats and view past messages, alongside Bluetooth pairing flaws.

**Do:** Update Apple devices to the latest available software versions.

[The Hacker News](https://thehackernews.com/2026/11/apple-patches-imessage-group-chat.html)

### 🟠 Pocket ID Email Verification Token Reuse Vulnerability
`CVE-2026-115770 · CVSS 9.6 · EPSS 0.00`

Pocket ID allows email verification tokens to remain valid after an account email address change, enabling verified-email spoofing.

**Do:** Upgrade Pocket ID backend to a patched version when available.

[GitHub Advisory](https://github.com/advisories/GHSA-rm8c-2cv8-jwf6)

### 🟠 Fireworks AI Discloses Breach Following Third-Party Cloud Compromise
`exploited`

AI startup Fireworks AI disclosed a security breach where attackers accessed development machines after compromising a third-party cloud provider.

**Do:** Review third-party cloud access controls and audit development machine logs.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/fireworks-ai-discloses-new-breach-after-cloud-provider-hack/)

## 2026-11-09

### 🔴 GPUStack Improper Authentication Vulnerability (CVE-2026-102895)
`CVE-2026-102895, CVE-2026-116779, CVE-2026-123158, CVE-2026-123218 · EPSS 0.00 · CISA KEV`

GPUStack contains an improper authentication vulnerability allowing unauthenticated administrative access, API-key creation, secret disclosure, and code execution. The vulnerability is actively exploited and listed in CISA KEV.

**Do:** Apply vendor mitigations immediately per CISA KEV and BOD 26-04 guidelines.

[CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-102895) · [GitHub Advisory](https://github.com/advisories/GHSA-gj9m-f8ph-pmhr) · [CISA Advisories](https://www.cisa.gov/news-events/alerts/2026/11/09/cisa-adds-four-known-exploited-vulnerabilities-catalog) · [The Hacker News](https://thehackernews.com/2026/11/cisa-warns-of-active-exploitation-of.html) · [SecurityWeek](https://www.securityweek.com/ibm-aspera-faspex-signalwire-freeswitch-vulnerabilities-exploited-in-attacks/)

### 🔴 SignalWire FreeSwitch Code Injection Vulnerability (CVE-2026-116779)
`CVE-2026-116779 · EPSS 0.01 · CISA KEV`

SignalWire FreeSwitch contains a code injection vulnerability enabling configuration/credential disclosure, call control, and command execution. The flaw is actively exploited and listed in CISA KEV.

**Do:** Apply vendor mitigations immediately or discontinue use of the product per CISA KEV guidelines.

[CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-116779)

### 🔴 Qubole AWS Access Compromised to Breach Customer Accounts
`exploited`

Attackers used Qubole trusted AWS access credentials between October 14 and October 26 to breach multiple customer accounts and steal stored secrets and data.

**Do:** Audit AWS accounts connected to Qubole for unauthorized access and rotate exposed credentials.

[The Hacker News](https://thehackernews.com/2026/11/hackers-exploit-quboles-trusted-aws.html)

### 🟠 Russian Cloud Provider Beget Rebuilds After Wiper Attack
`exploited`

Russian cloud services provider Beget was forced to rebuild its cloud infrastructure from scratch following a data-wiping malware attack.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/russian-cloud-firm-beget-rebuilds-from-scratch-after-data-wiper-attack/)

### 🟠 Plex2Shell Exploit Chain Targeted Against QNAP NAS Users
`exploited`

Threat actors are actively exploiting a four-flaw exploit chain targeting the Plex Media Server application on QNAP NAS devices.

**Do:** Audit QNAP NAS devices and update Plex Media Server applications.

[SecurityWeek](https://www.securityweek.com/plex2shell-exploited-against-qnap-nas-users/)

### 🟠 Ethersphere bee-js and Swarm Desktop Compromised for Malware
`exploited`

Attackers compromised release automation to publish malicious versions bee-js 13.3.0 and Swarm Desktop 0.56.2, which steal wallet keys and install backdoors.

**Do:** Downgrade or remove affected versions of bee-js and Swarm Desktop and check for compromised crypto wallets.

[The Hacker News](https://thehackernews.com/2026/11/hackers-compromise-etherspheres-bee-js.html)

### 🟠 Web3Auth Flaw Exploited to Steal Keplr Crypto Wallets
`exploited`

Attackers exploited a security flaw in Web3Auth used by Keplr for Google and Apple sign-in to steal funds from crypto wallets.

**Do:** Review Web3Auth integrations and monitor crypto wallet security.

[The Hacker News](https://thehackernews.com/2026/11/web3auth-flaw-exploited-to-steal-keplr.html)

### 🟠 LNbits Urges Server Shutdown Amid Active Exploitation Attacks
`exploited`

The LNbits Bitcoin Lightning wallet project urged operators to shut down servers immediately due to a wave of attacks exploiting new accounts to drain funds.

**Do:** Shut down LNbits servers immediately until security fixes are released and applied.

[The Hacker News](https://thehackernews.com/2026/11/lnbits-urges-all-operators-to-shut-down.html)

### 🟠 rConfig Core and Pro Deserialization RCE Vulnerability (CVE-2026-124079)
`CVE-2026-124079 · CVSS 9.8`

rConfig Core 8.0.0 before 8.2.19 and rConfig Pro before 8.4.1 contain a deserialization vulnerability allowing unauthenticated network attackers to execute arbitrary code via Redis-backed Laravel Horizon queues.

**Do:** Upgrade rConfig Core to 8.2.19+ and rConfig Pro to 8.4.1+.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124079)

### 🟠 Automaker Apps Vulnerable via Default ForgeRock Credentials

Researchers found default admin credentials on ForgeRock identity servers used by two car brands, allowing complete account takeover, remote door unlocking, and engine starting.

**Do:** Change default credentials on identity provider servers and enforce strict authentication policies.

[The Hacker News](https://thehackernews.com/2026/11/default-adminadmin-server-password.html)

### 🟠 German Web Host Breached via AI Assistant Integration Interface
`exploited`

A German web hosting company was breached after attackers exploited an interface designed to connect customer accounts with AI assistants.

[The Record](https://therecord.media/cyberattack-germany-ai-mittwald)

### 🟠 Frontline Education Data Breach Affects Over 3 Million
`exploited`

Frontline Education reported that an August data breach impacted over 3 million school district staff and students.

[SecurityWeek](https://www.securityweek.com/3-million-people-hit-by-frontline-education-data-breach/)

### 🟠 U.S. Agencies Warn of Attacks on Industrial Refrigeration Controllers
`exploited`

Threat actors are actively targeting unpatched or internet-accessible industrial refrigeration and cold-chain monitoring systems globally, potentially causing service disruptions, fire hazards, and inventory loss. U.S. government agencies issued an alert regarding these attacks.

**Do:** Audit industrial refrigeration controllers, disconnect them from the public internet, and apply available patches.

[The Hacker News](https://thehackernews.com/2026/11/us-agencies-warn-refrigeration.html) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/france-blames-iranian-hackers-for-supermarket-attacks-that-sparked-fires/) · [The Record](https://therecord.media/france-blames-iran-for-fridge-cyberattacks)

### 🟠 Tasmota Heap Out-of-Bounds Write Vulnerability (CVE-2026-119756)
`CVE-2026-119756 · CVSS 9.8`

Tasmota through 16.0.0 contains a heap out-of-bounds write vulnerability in SendReceiveDeviceGroupMessage() allowing local network attackers to corrupt memory via UDP port 4447.

**Do:** Apply patch from commit e97e1e4 or update Tasmota.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-119756)

### 🟠 fastapi-code-generator Import-Time RCE via Route Path (CVE-2026-63471)
`CVE-2026-63471 · CVSS 9.3 · EPSS 0.00`

fastapi-code-generator 0.8.0 emits unescaped route paths into decorators, allowing import-time remote code execution when generated code is loaded by an ASGI server.

**Do:** Update fastapi-code-generator and audit generated application code.

[GitHub Advisory](https://github.com/advisories/GHSA-p2mm-64f6-gmpp)

### 🟠 fastapi-code-generator Import-Time RCE via Status Code (CVE-2026-63469)
`CVE-2026-63469 · CVSS 9.3 · EPSS 0.00`

fastapi-code-generator 0.8.0 emits unescaped response status-code keys into decorator response dictionaries, allowing import-time code execution when generated code is loaded.

**Do:** Update fastapi-code-generator and audit generated application code.

[GitHub Advisory](https://github.com/advisories/GHSA-6xmv-cjr5-w3q8)

### 🟠 fastapi-code-generator Call-Time RCE via Summary (CVE-2026-63470)
`CVE-2026-63470 · CVSS 9.3 · EPSS 0.00`

fastapi-code-generator 0.8.0 emits unescaped operation summaries into docstrings, allowing code execution when the generated route handler endpoint is called.

**Do:** Update fastapi-code-generator and audit generated application code.

[GitHub Advisory](https://github.com/advisories/GHSA-h667-4jj2-cgv4)

### 🟠 Vanderbilt University Announces Cyberattack Impacting Systems
`exploited`

Vanderbilt University warned students and employees of a cyberattack impacting campus devices and systems.

[The Record](https://therecord.media/vanderbilt-cyberattack-ransomware-alert) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/vanderbilt-university-hit-in-byod-ransomware-attack-data-theft-claimed/)

### 🟠 Revolve Data Breach Impacts 1.5 Million Individuals
`exploited`

Online fashion retailer Revolve disclosed that a September cyberattack affected more than 1.5 million individuals.

[SecurityWeek](https://www.securityweek.com/revolve-puts-data-breach-victim-count-at-1-5-million/)

### 🟠 Amplifon Americas Data Breach Impacts 1.3 Million
`exploited`

Amplifon Americas suffered a data breach where hackers stole personal, health, and insurance information, including Social Security numbers.

[SecurityWeek](https://www.securityweek.com/amplifon-americas-data-breach-impacts-1-3-million/) · [The Record](https://therecord.media/amplifon-hearing-aid-company-data-breach)

## 2026-11-08

### 🔴 OpenAM Self-Registration Privilege Escalation Vulnerability (CVE-2026-123549)
`CVE-2026-123549 · CVSS 9.8`

OpenAM before 16.1.4 fails to enforce the Valid Creation Attributes list during self-registration, allowing anonymous attackers to assign themselves to administrative groups and gain full administrative control.

**Do:** Upgrade OpenAM to version 16.1.4 or later.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123549)

### 🔴 OpenAM SAML Authentication Bypass Vulnerability (CVE-2026-123550)
`CVE-2026-123550 · CVSS 9.8`

OpenAM before 16.1.4 contains an authentication bypass in its SAML v2.0 service provider that accepts unsigned assertions, allowing unauthenticated attackers to forge sessions for arbitrary users.

**Do:** Upgrade OpenAM to version 16.1.4 or later.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123550)

### 🔴 OpenAM WebSocket Session Disclosure Vulnerability (CVE-2026-123551)
`CVE-2026-123551 · CVSS 10.0`

OpenAM versions 14.0.0 through 16.1.3 allow unauthenticated attackers to read live session tokens from the notification WebSocket, enabling session hijacking.

**Do:** Upgrade OpenAM to version 16.1.4 or later.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123551)

### 🟠 IBM Concert Unsafe Command Execution Vulnerability (CVE-2026-15266)
`CVE-2026-15266, CVE-2026-6715 · CVSS 9.8`

IBM Concert 1.0 through 3.0.1.1 contains components allowing unsafe command execution, enabling remote attackers to run arbitrary system commands on the host.

**Do:** Apply the latest security updates for IBM Concert versions 1.0 through 3.0.1.1.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-15266) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-6715)

### 🟠 Kyverno Namespace Clamp Authorization Bypass (CVE-2026-124440)
`CVE-2026-124440 · CVSS 9.9`

Kyverno 1.19.1 contains an authorization bypass allowing namespace tenants to issue cluster-scoped API requests and escalate to cluster admin.

**Do:** Upgrade Kyverno to 1.19.2 or later.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124440)

### 🟠 OpenEMR Path Traversal and RCE Vulnerability (CVE-2026-124450)
`CVE-2026-124450, CVE-2026-124490 · CVSS 9.9`

OpenEMR before 8.3.0 contains a path traversal vulnerability in the fax/sms module, allowing low-privilege users to read configuration files and achieve RCE.

**Do:** Upgrade OpenEMR to 8.3.0 or later.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124450) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124490)

### 🟠 imgproxy ICO Loader Integer Overflow Vulnerability (CVE-2026-123614)
`CVE-2026-123614 · CVSS 9.8`

imgproxy 4.0.0 through 4.0.15 contains an integer overflow in the ICO loader, allowing remote attackers to trigger a heap buffer overflow via crafted images.

**Do:** Upgrade imgproxy to version 4.0.16 or later.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123614)

### 🟠 Iris Ohyama Cloud Service Breach Exposes 7.7 Million Records

Japanese manufacturer Iris Ohyama disclosed that unauthorized access to a third-party cloud service exposed personal information of about 7.7 million people.

**Do:** Audit third-party cloud service integrations and monitor affected customer data.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/iris-ohyama-data-cloud-breach-exposes-info-of-77-million-customers/) · [SecurityWeek](https://www.securityweek.com/iris-plaza-breach-may-have-exposed-data-of-7-7-million-customers/)

### 🟠 IBM DataStage on Cloud Pak for Data Path Traversal (CVE-2026-107331)
`CVE-2026-107331 · CVSS 9.9`

IBM DataStage on Cloud Pak for Data 5.4.0.0 contains an absolute-path traversal vulnerability allowing remote authenticated attackers to obtain sensitive information.

**Do:** Apply available patches from IBM for DataStage on Cloud Pak for Data 5.4.0.0.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-107331)

### 🟠 IBM Process Mining Access Control Vulnerability (CVE-2026-114464)
`CVE-2026-114464 · CVSS 9.3`

IBM Process Mining 2.0.0 through 2.2.1 contains an improper access control flaw allowing remote attackers to obtain sensitive information.

**Do:** Upgrade IBM Process Mining to version 2.2.2 or later.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114464)

### 🟠 IBM Optim Path Traversal Vulnerability (CVE-2026-17466)
`CVE-2026-17466 · CVSS 9.1`

IBM Optim 1.0.0, 1.1.0, and 1.2.0 allow remote authenticated attackers to obtain sensitive information via path traversal.

**Do:** Apply fixes provided by IBM for Optim versions 1.0.0, 1.1.0, and 1.2.0.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17466)

### 🟠 Craft CMS GraphQL Auth Bypass Vulnerability (CVE-2026-124427)
`CVE-2026-124427 · CVSS 9.8`

Craft CMS 5.0.0 through 5.11.1 contains an authorization bypass allowing anonymous GraphQL clients to read out-of-scope section entries.

**Do:** Upgrade Craft CMS to 5.11.2 or later.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124427)

### 🟠 OpenEMR OneTimeAuth Token Replay Flaw (CVE-2026-124445)
`CVE-2026-124445 · CVSS 9.8`

OpenEMR 7.0.1 through 8.3.x ignores one-time use flags and lacks rate limiting on PINs, allowing token replay to expose patient data.

**Do:** Upgrade OpenEMR to 8.4.0 or later.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124445)

### 🟠 OpenEMR SQL Injection Vulnerability (CVE-2026-124469)
`CVE-2026-124469 · CVSS 9.9`

OpenEMR before 8.3.0 contains an SQL injection flaw in the Fee Sheet drug-inventory lookup, enabling data extraction.

**Do:** Upgrade OpenEMR to 8.3.0 or later.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124469)

### 🟠 IBM WebSphere Extreme Scale CSP Bypass (CVE-2026-101117)
`CVE-2026-101117 · CVSS 9.1`

IBM WebSphere Extreme Scale 8.6.1.0 to 8.6.2.2 contains a security restriction bypass due to improper Content Security Policy configuration.

**Do:** Apply fixes provided by IBM for WebSphere Extreme Scale.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-101117)

## 2026-11-07

### 🔴 Microsoft Entra Device Registration Auth Bypass Flaw (CVE-2026-109469)
`CVE-2026-109469 · CVSS 10.0`

An authorization bypass vulnerability in Entra Device Registration (CVE-2026-109469, CVSS 10.0) allows unauthorized attackers to elevate privileges over a network.

**Do:** Apply the latest security updates from Microsoft for Entra Device Registration.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109469)

### 🔴 IBM API Connect Hard-Coded Credentials Flaw (CVE-2026-17360)
`CVE-2026-17360 · CVSS 9.8`

IBM API Connect versions 12.1.0.0 through 12.1.1.2 use hard-coded credentials, allowing remote attackers to gain full administrative control.

**Do:** Apply available vendor patches for IBM API Connect 12.1 immediately.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17360)

### 🔴 IBM API Connect OS Command Injection Flaw (CVE-2026-17402)
`CVE-2026-17402 · CVSS 9.9`

IBM API Connect 10.0.8.0-10.0.8.12 and 12.1.0.0-12.1.1.2 allow remote command execution via unneutralized OS command input.

**Do:** Apply available vendor patches for IBM API Connect immediately.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17402)

### 🔴 IBM API Connect Hard-Coded Credentials Flaw (CVE-2026-17403)
`CVE-2026-17403 · CVSS 9.0`

IBM API Connect 10.0.8.0-10.0.8.12 and 12.1.0.0-12.1.1.2 contain hard-coded credentials allowing full administrative control.

**Do:** Apply available vendor patches for IBM API Connect immediately.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17403)

### 🔴 IBM API Connect OS Command Injection Flaw (CVE-2026-17408)
`CVE-2026-17408 · CVSS 9.8`

IBM API Connect 10.0.8.0-10.0.8.12 and 12.1.0.0-12.1.1.2 allow remote attackers to execute arbitrary code via OS command injection.

**Do:** Apply available vendor patches for IBM API Connect immediately.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17408)

### 🔴 Now exploited: IBM Aspera Faspex Authorization Bypass Flaw (CVE-2026-123218)
`CVE-2026-123218 · CVSS 9.8 · CISA KEV`

IBM Aspera Faspex versions 5.0.0 through 5.0.19 contain an authorization bypass vulnerability allowing an authorized user to craft specific messages and gain full administrative privileges.

**Do:** Upgrade IBM Aspera Faspex to the latest patched version.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123218)

### 🟠 Crédit Mutuel Arkéa Hit by $133 Million Cyberattack via Service Provider
`exploited`

French cooperative bank Crédit Mutuel Arkéa suffered a cyberattack via a service provider resulting in $133 million in fraudulent transactions, prompting system suspensions.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/hackers-pull-off-133-million-french-bank-heist-via-service-provider/)

### 🟠 Keycloak Client Management RCE Vulnerability (CVE-2026-120984)
`CVE-2026-120984 · CVSS 9.1`

A vulnerability in Keycloak's client management component allows authenticated attackers with client management permissions to upload and execute malicious JavaScript policies, leading to remote code execution.

**Do:** Apply the latest vendor patches for Keycloak to address CVE-2026-120984.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120984)

### 🟠 IBM API Connect Authentication Bypass Flaw (CVE-2026-16720)
`CVE-2026-16720 · CVSS 9.8`

IBM API Connect 10.0.8.0-10.0.8.12 and 12.1.0.0-12.1.1.2 allow remote attackers to obtain valid access tokens and assume other users' identities due to improper directory service authentication enforcement.

**Do:** Apply available security patches for IBM API Connect.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-16720)

### 🟠 IBM API Connect Arbitrary Code Execution Flaw (CVE-2026-17117)
`CVE-2026-17117 · CVSS 9.9`

IBM API Connect 10.0.8.0-10.0.8.12 and 12.1.0.0-12.1.1.2 permit remote authenticated attackers to execute arbitrary code via improperly controlled object attribute modifications.

**Do:** Upgrade IBM API Connect to the latest release.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17117)

### 🟠 IBM API Connect SQL Injection Flaw (CVE-2026-17132)
`CVE-2026-17132, CVE-2026-17134 · CVSS 9.9`

IBM API Connect 12.1.0.0 through 12.1.1.2 contains an SQL injection vulnerability allowing remote authenticated attackers to execute arbitrary SQL commands.

**Do:** Update IBM API Connect immediately.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17132) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17134)

### 🟠 IBM API Connect Path Traversal RCE Flaw (CVE-2026-17147)
`CVE-2026-17147, CVE-2026-17239 · CVSS 9.9`

IBM API Connect 10.0.8.0-10.0.8.12 and 12.1.0.0-12.1.1.2 contain a path traversal vulnerability allowing remote code execution and administrative actions.

**Do:** Upgrade IBM API Connect to a patched version.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17147) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17239)

### 🟠 IBM API Connect Custom Module Code Execution Flaw (CVE-2026-17150)
`CVE-2026-17150 · CVSS 9.9`

IBM API Connect 10.0.8.0-10.0.8.12 and 12.1.0.0-12.1.1.2 lack sufficient validation for uploaded custom modules, allowing cross-tenant code execution.

**Do:** Apply security updates for IBM API Connect.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17150)

### 🟠 IBM API Connect Privilege Escalation Flaw (CVE-2026-17158)
`CVE-2026-17158 · CVSS 9.9`

IBM API Connect 10.0.8.0-10.0.8.12 and 12.1.0.0-12.1.1.2 contain an improper authentication issue allowing privilege escalation for authenticated attackers.

**Do:** Update IBM API Connect to the latest release.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17158)

### 🟠 IBM API Connect Improper Authentication Flaw (CVE-2026-17278)
`CVE-2026-17278 · CVSS 9.8`

IBM API Connect 12.1.0.0 through 12.1.1.2 contains an improper authentication flaw allowing unauthorized access to API catalog and runtime configurations.

**Do:** Apply vendor patches for IBM API Connect.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17278)

### 🟠 IBM API Connect BOLA Flaw (CVE-2026-17292)
`CVE-2026-17292 · CVSS 9.1`

IBM API Connect 10.0.8.0-10.0.8.12 and 12.1.0.0-12.1.1.2 contain incomplete access checks allowing remote authenticated attackers to take over organization ownership.

**Do:** Update IBM API Connect to a secured version.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17292)

### 🟠 IBM API Connect Open Redirect Account Takeover (CVE-2026-17297)
`CVE-2026-17297 · CVSS 9.6`

IBM API Connect 10.0.8.0-10.0.8.12 and 12.1.0.0-12.1.1.2 contain an open redirect vulnerability during sign-in that can lead to account takeover.

**Do:** Upgrade IBM API Connect to the patched release.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17297)

### 🟠 IBM API Connect Arbitrary File Read and SSRF (CVE-2026-17299)
`CVE-2026-17299 · CVSS 9.6`

IBM API Connect 10.0.8.0-10.0.8.12 and 12.1.0.0-12.1.1.2 permit arbitrary file reads and SSRF due to unrestricted resolution of external references in definitions.

**Do:** Apply IBM API Connect security updates.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17299)

### 🟠 IBM API Connect Cryptographic Signature Bypass (CVE-2026-17301)
`CVE-2026-17301 · CVSS 9.8`

IBM API Connect 10.0.8.0-10.0.8.12 and 12.1.0.0-12.1.1.2 contain an authentication bypass vulnerability due to improper cryptographic signature verification.

**Do:** Upgrade IBM API Connect to a patched version.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17301)

### 🟠 IBM API Connect Gateway Config Takeover (CVE-2026-17313)
`CVE-2026-17313 · CVSS 9.8`

IBM API Connect 12.1.0.0 through 12.1.1.2 allows remote attackers to take control of gateway configuration and obtain sensitive information via an alternate path authentication bypass.

**Do:** Apply patches provided by IBM for API Connect.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17313)

### 🟠 IBM API Connect SQL Injection Flaw (CVE-2026-17336)
`CVE-2026-17336 · CVSS 9.9`

IBM API Connect versions 12.1.0.0 through 12.1.1.2 allow authenticated remote attackers to execute arbitrary SQL commands.

**Do:** Apply available vendor patches for IBM API Connect 12.1.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17336)

### 🟠 IBM API Connect Path Traversal Flaw (CVE-2026-17339)
`CVE-2026-17339 · CVSS 9.1`

IBM API Connect versions 12.1.0.0 through 12.1.1.2 contain a path traversal vulnerability allowing cross-tenant resource access or deletion.

**Do:** Apply available vendor patches for IBM API Connect 12.1.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17339)

### 🟠 IBM API Connect Path Traversal RCE Flaw (CVE-2026-17340)
`CVE-2026-17340 · CVSS 9.8`

IBM API Connect versions 12.1.0.0 through 12.1.1.2 are vulnerable to path traversal allowing remote code execution.

**Do:** Apply available vendor patches for IBM API Connect 12.1.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17340)

### 🟠 IBM API Connect Code Generation RCE Flaw (CVE-2026-17342)
`CVE-2026-17342 · CVSS 9.9`

IBM API Connect 10.0.8.0-10.0.8.12 and 12.1.0.0-12.1.1.2 allow remote authenticated code execution due to improper code generation control.

**Do:** Apply available vendor patches for IBM API Connect.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17342)

### 🟠 IBM API Connect Arbitrary File Write Flaw (CVE-2026-17354)
`CVE-2026-17354 · CVSS 9.9`

IBM API Connect versions 12.1.0.0 through 12.1.1.2 allow remote authenticated arbitrary file writes via path traversal.

**Do:** Apply available vendor patches for IBM API Connect 12.1.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17354)

### 🟠 IBM API Connect Code Generation RCE Flaw (CVE-2026-17359)
`CVE-2026-17359 · CVSS 9.9`

IBM API Connect 10.0.8.0-10.0.8.12 and 12.1.0.0-12.1.1.2 allow code execution due to user-supplied input influencing generated code.

**Do:** Apply available vendor patches for IBM API Connect.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17359)

### 🟠 IBM API Connect LDAP Injection Flaw (CVE-2026-17392)
`CVE-2026-17392 · CVSS 9.9`

IBM API Connect 10.0.8.0-10.0.8.12 and 12.1.0.0-12.1.1.2 allow LDAP injection leading to unauthorized cross-tenant admin access.

**Do:** Apply available vendor patches for IBM API Connect.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17392)

### 🟠 IBM API Connect SQL Injection Flaw (CVE-2026-17396)
`CVE-2026-17396 · CVSS 9.6`

IBM API Connect 10.0.8.0-10.0.8.12 and 12.1.0.0-12.1.1.2 contain an SQL injection vulnerability allowing sensitive information disclosure.

**Do:** Apply available vendor patches for IBM API Connect.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17396)

### 🟠 IBM API Connect Unvalidated Upload RCE Flaw (CVE-2026-17399)
`CVE-2026-17399 · CVSS 9.9`

IBM API Connect 10.0.8.0-10.0.8.12 and 12.1.0.0-12.1.1.2 allow remote code execution due to insufficient validation of uploaded content.

**Do:** Apply available vendor patches for IBM API Connect.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17399)

### 🟠 IBM API Connect Case Sensitivity Access Flaw (CVE-2026-17409)
`CVE-2026-17409 · CVSS 9.4`

IBM API Connect 10.0.8.0-10.0.8.12 and 12.1.0.0-12.1.1.2 allow unauthorized admin operations due to inconsistent case sensitivity checks.

**Do:** Apply available vendor patches for IBM API Connect.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17409)

### 🟠 IBM API Connect Portal Data Access Flaw (CVE-2026-17410)
`CVE-2026-17410 · CVSS 9.9`

IBM API Connect 10.0.8.0-10.0.8.12 and 12.1.0.0-12.1.1.2 allow cross-tenant portal data access and modification.

**Do:** Apply available vendor patches for IBM API Connect.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17410)

### 🟠 IBM API Connect Authentication Bypass Flaw (CVE-2026-18838)
`CVE-2026-18838 · CVSS 9.4`

IBM API Connect versions 12.1.0.0 through 12.1.1.2 allow callers to impersonate other users due to improper authentication verification.

**Do:** Apply available vendor patches for IBM API Connect 12.1.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-18838)

### 🟠 Claude Code 'Don't Ask Again' File Exposes Secrets on GitHub

Anthropic's Claude Code coding assistant can save sensitive commands containing passwords and API keys into project settings files when users select 'Don't Ask Again', leading to exposed secrets in public GitHub repositories.

**Do:** Audit public repositories for exposed Claude Code settings files and revoke any leaked API keys or credentials.

[The Hacker News](https://thehackernews.com/2026/11/claude-codes-dont-ask-again-file.html)

### 🟠 IBM API Connect XXE Vulnerability (CVE-2026-16884)
`CVE-2026-16884 · CVSS 9.9`

IBM API Connect 12.1.0.0 through 12.1.1.2 contains an XML external entity (XXE) injection vulnerability allowing remote attackers to obtain sensitive information.

**Do:** Apply the latest updates for IBM API Connect.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-16884)

### 🟠 IBM API Connect SSRF Vulnerability (CVE-2026-16918)
`CVE-2026-16918 · CVSS 9.3`

IBM API Connect versions 10.0.8.0 through 10.0.8.12 and 12.1.0.0 through 12.1.1.2 contain a server-side request forgery flaw allowing access to internal network resources.

**Do:** Apply patches provided by IBM for API Connect.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-16918)

### 🟠 IBM API Connect Security Restriction Bypass (CVE-2026-16920)
`CVE-2026-16920 · CVSS 9.9`

IBM API Connect 12.1.0.0 through 12.1.1.2 contains a confused deputy vulnerability enabling remote authenticated attackers to bypass security restrictions.

**Do:** Update IBM API Connect to the latest patched version.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-16920)

### 🟠 IBM API Connect Authorization Bypass Flaw (CVE-2026-17049)
`CVE-2026-17049 · CVSS 9.9`

IBM API Connect 12.1.0.0 through 12.1.1.2 allows remote authenticated attackers to view and modify arbitrary documents via user-controlled keys.

**Do:** Update IBM API Connect to a fixed version.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17049)

### 🟠 IBM API Connect Missing Authorization Flaw (CVE-2026-17066)
`CVE-2026-17066 · CVSS 9.1`

IBM API Connect 12.1.0.0 through 12.1.1.2 contains a missing authorization vulnerability allowing cross-tenant data access and modification.

**Do:** Apply vendor patches for IBM API Connect.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17066)

### 🟠 IBM API Connect SSRF Vulnerability (CVE-2026-17131)
`CVE-2026-17131 · CVSS 9.3`

IBM API Connect 12.1.0.0 through 12.1.1.2 contains an SSRF flaw permitting attackers to bypass outbound request restrictions.

**Do:** Apply IBM API Connect patches.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17131)

### 🟠 IBM API Connect Input Validation Flaw (CVE-2026-17146)
`CVE-2026-17146 · CVSS 9.9`

IBM API Connect 10.0.8.0-10.0.8.12 and 12.1.0.0-12.1.1.2 contain an input validation issue allowing remote authenticated users to execute arbitrary JavaScript.

**Do:** Apply IBM API Connect patches.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17146)

### 🟠 IBM API Connect SSRF Vulnerability (CVE-2026-17296)
`CVE-2026-17296 · CVSS 9.6`

IBM API Connect 10.0.8.0-10.0.8.12 and 12.1.0.0-12.1.1.2 contain an SSRF flaw allowing remote authenticated attackers to obtain sensitive info.

**Do:** Apply IBM API Connect updates.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17296)

### 🟠 IBM API Connect SSRF Vulnerability (CVE-2026-17298)
`CVE-2026-17298 · CVSS 9.9`

IBM API Connect 10.0.8.0-10.0.8.12 and 12.1.0.0-12.1.1.2 contain an SSRF vulnerability exposing sensitive information.

**Do:** Apply vendor patches.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17298)

### 🟠 IBM API Connect Information Disclosure Flaw (CVE-2026-17329)
`CVE-2026-17329 · CVSS 9.3`

IBM API Connect versions 12.1.0.0 through 12.1.1.2 contain an information disclosure vulnerability due to improper endpoint URL validation.

**Do:** Apply available vendor patches for IBM API Connect 12.1.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17329)

### 🟠 IBM API Connect BOLA Flaw (CVE-2026-17338)
`CVE-2026-17338 · CVSS 9.1`

IBM API Connect versions 12.1.0.0 through 12.1.1.2 suffer from broken object-level authorization, allowing sensitive data access.

**Do:** Apply available vendor patches for IBM API Connect 12.1.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17338)

### 🟠 IBM API Connect SSRF Vulnerability (CVE-2026-17344)
`CVE-2026-17344 · CVSS 9.3`

IBM API Connect versions 12.1.0.0 through 12.1.1.2 contain an SSRF flaw allowing unauthenticated requests to unintended destinations.

**Do:** Apply available vendor patches for IBM API Connect 12.1.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17344)

### 🟠 IBM API Connect SSRF and Bypass Flaw (CVE-2026-17353)
`CVE-2026-17353 · CVSS 9.6`

IBM API Connect versions 12.1.0.0 through 12.1.1.2 contain an SSRF flaw allowing security restriction bypass and information disclosure.

**Do:** Apply available vendor patches for IBM API Connect 12.1.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17353)

### 🟠 IBM API Connect Attribute Modification Flaw (CVE-2026-17394)
`CVE-2026-17394 · CVSS 9.6`

IBM API Connect 10.0.8.0-10.0.8.12 and 12.1.0.0-12.1.1.2 allow modification of object attributes leading to sensitive data exposure.

**Do:** Apply available vendor patches for IBM API Connect.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-17394)

### 🟠 IBM API Connect ReDoS and Wildcard Flaw (CVE-2026-18535)
`CVE-2026-18535 · CVSS 9.6`

IBM API Connect 10.0.8.0-10.0.8.12 and 12.1.0.0-12.1.1.2 are vulnerable to ReDoS and improper wildcard query neutralization.

**Do:** Apply available vendor patches for IBM API Connect.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-18535)

### 🟠 IBM API Connect SSRF Vulnerability (CVE-2026-18836)
`CVE-2026-18836 · CVSS 9.3`

IBM API Connect 10.0.8.0-10.0.8.12 and 12.1.0.0-12.1.1.2 contain an SSRF flaw allowing sensitive information disclosure.

**Do:** Apply available vendor patches for IBM API Connect.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-18836)

## 2026-11-06

### 🔴 SonicWall SonicOS SSLVPN Authentication Bypass Added to KEV
`CVE-2026-19868 · CISA KEV`

CISA added CVE-2026-19868, a single-factor authentication vulnerability in SonicWall SonicOS SSLVPN that allows bypassing SAML and MFA controls, to its KEV catalog following active exploitation.

**Do:** Apply vendor-supplied patches immediately and review access logs for unauthorized SSLVPN sessions.

[CISA Advisories](https://www.cisa.gov/news-events/alerts/2026/11/06/cisa-adds-one-known-exploited-vulnerability-catalog) · [CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-19868) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/sonicwall-warns-of-new-ssl-vpn-mfa-bypass-flaw-exploited-in-attacks/) · [SecurityWeek](https://www.securityweek.com/sonicwall-patches-exploited-sonicos-bug-that-weakens-vpn-logins/) · [The Hacker News](https://thehackernews.com/2026/11/cisa-flags-sonicwall-sonicos-mfa-bypass.html)

### 🔴 Canonical LXD Restricted Project Bypass RCE Flaw
`CVSS 9.9`

Canonical LXD contains a vulnerability where instance snapshots ignore lowlevel restriction settings, leading to arbitrary command execution via raw hooks.

**Do:** Upgrade LXD to the latest patched version.

[GitHub Advisory](https://github.com/advisories/GHSA-47w9-6r3f-938g)

### 🔴 Canonical LXD Arbitrary File Write via Image Hash
`CVSS 9.9`

An arbitrary file write exists in the LXD client when a malicious image server returns a crafted image hash header, leading to potential root RCE.

**Do:** Upgrade LXD to the latest patched version.

[GitHub Advisory](https://github.com/advisories/GHSA-pjff-c2wc-f6jm)

### 🔴 Canonical LXD Backup Compression Argument Injection Flaw
`CVSS 9.9`

Improper validation of user-provided backup compression algorithms in LXD leads to argument injection, arbitrary file write, and potential RCE.

**Do:** Upgrade LXD to the latest patched version.

[GitHub Advisory](https://github.com/advisories/GHSA-fmc8-p6q7-75cc)

### 🔴 Canonical LXD Host File Read/Write via Rootfs Symlink
`CVSS 9.9`

A specially crafted image can exploit symlink handling in LXD to read or write arbitrary files on the host system.

**Do:** Upgrade LXD to the latest patched version.

[GitHub Advisory](https://github.com/advisories/GHSA-vghh-5rfx-xhq8)

### 🔴 Canonical LXD Host File Read/Write via Templates Symlink
`CVSS 9.9`

Container image extraction in LXD fails to reject top-level templates symlinks, allowing arbitrary file read and write on the host.

**Do:** Upgrade LXD to the latest patched version.

[GitHub Advisory](https://github.com/advisories/GHSA-jpf8-86f3-wp38)

### 🔴 Canonical LXD Arbitrary File Write via Exec-Output Symlink
`CVSS 9.9`

Improper handling of the exec-output parameter in LXD endpoints allows writing stdout/stderr files to arbitrary locations, leading to RCE.

**Do:** Upgrade LXD to the latest patched version.

[GitHub Advisory](https://github.com/advisories/GHSA-9j25-mm2h-2f76)

### 🟠 QNAP NAS Devices Targeted in Plex2Shell Attacks
`exploited`

Hackers are actively exploiting vulnerabilities via Plex Media Server on QNAP NAS devices in Plex2Shell attack chains.

**Do:** Update Plex Media Server to the latest version via the QNAP App Center.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/qnap-says-hackers-breaching-nas-devices-in-plex2shell-attacks/)

### 🟠 Craft CMS Unauthenticated SQL Injection Vulnerability
`CVE-2026-123488 · CVSS 9.8`

Craft CMS versions 4.0.0 through 4.18.8 and 5.0.0 through 5.11.1 contain an unauthenticated SQL injection vulnerability in the element search endpoint, allowing remote attackers to read and write the database and gain administrator access.

**Do:** Upgrade Craft CMS to version 4.18.9 or 5.11.2 and above.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123488)

### 🟠 Fake Security Tools on GitHub Deliver Backdoors and Infostealers
`exploited`

Cybersecurity professionals are being targeted by malicious GitHub repositories posing as security tools that deploy backdoors and infostealers.

**Do:** Audit third-party security repositories and check endpoints for unauthorized infostealers.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/fake-security-tools-on-github-push-backdoors-and-infostealers/)

### 🟠 D-Link Warns of Zero-Day Vulnerabilities in DGS-3130 Series Switches
`exploited`

D-Link shared mitigation measures for unpatched security flaws affecting DGS-3130 series managed Gigabit stackable switches.

**Do:** Apply vendor mitigations for D-Link DGS-3130 series switches.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/d-link-warns-of-multiple-zero-days-in-dgs-3130-series-switches/)

### 🟠 Microsoft Paint Remote Code Execution Flaw Fixed in Microsoft Store
`CVE-2026-83844 · EPSS 0.01`

An out-of-bounds read RCE vulnerability in Microsoft Paint (CVE-2026-83844) can be fixed by updating to build 11.2609.401.0 via the Microsoft Store.

**Do:** Update Microsoft Paint via the Microsoft Store to build 11.2609.401.0 or later.

[The Hacker News](https://thehackernews.com/2026/11/microsoft-paint-rce-fix-now-available.html)

### 🟠 WordPress Flaw Update Vulnerability During Installation
`exploited`

Some WordPress sites remain vulnerable to code execution while installing updates for an actively exploited flaw because files are unpacked using unpatched code.

**Do:** Temporarily block web access to vulnerable installation files during update procedures.

[The Hacker News](https://thehackernews.com/2026/11/installing-fix-for-exploited-wordpress.html)

## 2026-11-05

### 🔴 Apple Multiple Products Authentication Flaw Added to KEV
`CVE-2024-27834 · EPSS 0.01 · CISA KEV`

Apple iOS, iPadOS, macOS, Safari, tvOS and watchOS contain an improper authentication vulnerability (CVE-2024-27834) allowing pointer authentication bypass. The flaw is actively tracked in CISA's KEV.

**Do:** Apply mitigations or updates in accordance with vendor instructions.

[CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2024-27834) · [The Hacker News](https://thehackernews.com/2026/11/hackers-exploit-patched-apple-flaw-to.html) · [CISA Advisories](https://www.cisa.gov/news-events/alerts/2026/11/04/cisa-adds-one-known-exploited-vulnerability-catalog)

### 🔴 Now exploited: OpenSSH Critical Long Password Authentication Bypass Flaw in Alpine Linux
`CVE-2026-123158 · CISA KEV`

OpenSSH version 10.6p2 fixes a critical flaw affecting certain Alpine Linux configurations where long passwords can bypass authentication on accounts with no password.

**Do:** Upgrade OpenSSH to version 10.6p2 or later on affected Alpine Linux servers.

[The Hacker News](https://thehackernews.com/2026/11/openssh-issues-emergency-fix-for-flaw.html) · [Ars Technica](https://arstechnica.com/security/2026/11/vulnerability-allows-attackers-to-log-into-some-linux-devices-sans-password/) · [SecurityWeek](https://www.securityweek.com/openssh-rushes-patches-for-sshole-authentication-bypass/) · [The Hacker News](https://thehackernews.com/2026/11/hackers-exploited-openssh-sshole-flaw.html) · [SecurityWeek](https://www.securityweek.com/hackers-exploiting-sshole-authentication-bypass-in-openssh/) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/hackers-exploit-sshole-openssh-flaw-to-breach-linux-systems/) · [CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-123158)

### 🔴 Zyxel Fixes Zero-Day Exploit on Network Switches
`exploited`

Zyxel patched a zero-day vulnerability in its GS1900 series network switches exploited in the wild to compromise nearly 1,000 devices and steal configuration files and credentials.

**Do:** Apply the latest security patches for Zyxel GS1900 series switches immediately.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/zyxel-fixes-zero-day-exploited-to-hack-nearly-1-000-network-switches/)

### 🔴 US Agencies Warn of Global Cyber Activity Targeting Industrial Refrigeration
`exploited`

CISA, FBI, HHS, USDA, and DoT issued an advisory regarding malicious cyber activity targeting industrial refrigeration and cold chain monitoring systems globally.

**Do:** Harden industrial refrigeration and cold chain monitoring systems against unauthorized access.

[CISA Advisories](https://www.cisa.gov/resources-tools/resources/us-government-partners-urge-hardening-industrial-refrigeration-and-cold-chain-monitoring-systems) · [The Record](https://therecord.media/cyberattacks-refrigeration-cisa-fbi) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/fbi-cisa-warn-of-cyberattacks-targeting-refrigeration-systems/) · [SecurityWeek](https://www.securityweek.com/us-agencies-urge-organizations-to-harden-refrigeration-controllers/)

### 🟠 Multiple Asian Airlines Announce Breaches via Amadeus IT
`exploited`

Japan Airlines, Cathay Pacific, Korean Air, Asiana Airlines, Singapore Airlines and Malaysia Airlines reported data breaches traced back to supplier Amadeus IT Group.

**Do:** Monitor vendor supply-chain communications and review reservation system access controls.

[The Record](https://therecord.media/asian-airlines-announce-data-breach-it-provider-incident)

### 🟠 BTCPay Server Information Disclosure Exposes LND Macaroon Credentials
`CVE-2026-119757 · CVSS 9.8`

BTCPay Server before 2.4.2 contains an information disclosure vulnerability allowing unauthenticated remote attackers to retrieve LND node .macaroon files and gain full control of funds.

**Do:** Upgrade BTCPay Server to version 2.4.2 or later.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-119757)

### 🟠 vtenext Authentication Bypass Flaw Allows Password Change
`CVE-2025-71457 · CVSS 9.8`

vtenext versions 25.02 before 25.02.1 contain an authentication bypass vulnerability allowing unauthenticated attackers to change account passwords via hub/rpwd.php and log in as administrators.

**Do:** Upgrade vtenext to 25.02.1 or later.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-71457)

### 🟠 IBM Watson Speech Services Cartridge Use-After-Free Flaw
`CVE-2026-82418 · CVSS 9.8`

IBM Watson Speech Services Cartridge 4.0.0 through 5.4.0 contains a use-after-free vulnerability that allows a remote attacker to execute arbitrary code.

**Do:** Apply available patches from IBM.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82418)

### 🟠 VitaFit Cloud API Authentication Bypass Flaw
`CVE-2026-54384 · CVSS 9.8`

VitaFit cloud API before 2026-10-30 contained an authentication bypass vulnerability allowing attackers to forge logins via social identifiers and access victim accounts.

**Do:** Update VitaFit cloud API to the latest version.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-54384)

### 🟠 Queens Public Library Suffers Ransomware Attack Disrupting Services
`exploited`

A ransomware attack disrupted Wi-Fi and on-site computers across the Queens Public Library system's 66 branches.

[The Record](https://therecord.media/queens-library-ransomware-causes-disruptions)

### 🟠 Cisco, WatchGuard Release Patches; SonicWall Won’t Fix GMS Flaws

Cisco patched an RCE in UCS Central Software; WatchGuard fixed authentication and MitM flaws. The post Cisco, WatchGuard Release Patches; SonicWall Won’t Fix GMS Flaws appeared first on SecurityWeek .

[SecurityWeek](https://www.securityweek.com/cisco-watchguard-release-patches-sonicwall-wont-fix-gms-flaws/)

### 🟠 VitaFit Cloud API Broken Access Control Flaw
`CVE-2026-54378 · CVSS 9.6`

VitaFit cloud API before 2026-10-30 contained a broken access control vulnerability allowing authenticated users to obtain temporary AWS credentials and access shared storage buckets.

**Do:** Update VitaFit cloud API to the patched version.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-54378)

### 🟠 go:github.com/chainguard-dev/kaniko: kaniko can send the build's Azure (Entra ID) access token to lookalike ACR registry
`CVE-2026-105769 · CVSS 9.3 · EPSS 0.00`

Affected packages: go:github.com/chainguard-dev/kaniko. ### Summary kaniko before v1.25.20 can send a Microsoft Entra ID (Azure AD) access token for Azure Resource Manager to a registry host an attacker controls.

[GitHub Advisory](https://github.com/advisories/GHSA-5q7h-w9jf-cx97)

### 🟠 CVE-2026-122310: Kyverno from 1.19.1 before 1.19.2 validates a Policy's context.apiCall urlPath after cleaning it but ex
`CVE-2026-122310 · CVSS 9.9`

Kyverno from 1.19.1 before 1.19.2 validates a Policy's context.apiCall urlPath after cleaning it but executes the raw path, whose fragment or query the Kubernetes client discards. A namespace-scoped user who can create a Policy can hide ../ segments behind # or ?

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-122310)

### 🟠 Zyxel Switch Hacks Blamed on Patched Flaw Actually Exploited a Zero-Day
`CVE-2026-107441 · EPSS 0.00 · exploited`

Tracked as CVE-2026-107441, the out-of-bounds write flaw could allow attackers to execute OS commands via crafted HTTP requests. The post Zyxel Switch Hacks Blamed on Patched Flaw Actually Exploited a Zero-Day appeared first on SecurityWeek .

[SecurityWeek](https://www.securityweek.com/zyxel-switch-hacks-blamed-on-patched-flaw-actually-exploited-a-zero-day/)

### 🟠 Zyxel GS1900 Patch Fails to Block Zero-Day Exploit Allowing Root Command Execution
`exploited`

Zyxel GS1900 network switches that received the vendor's earlier fix for an actively exploited flaw are still open to the exploit attackers used, researchers at Binarly found. The exploit lets anyone who can reach a switch's web management interface run commands on it without logging in.

[The Hacker News](https://thehackernews.com/2026/11/zyxel-gs1900-patch-fails-to-block-zero.html)

### 🟠 OpenAI ChatGPT Lockdown Mode Bypass Vulnerability

A patched vulnerability in OpenAI ChatGPT allowed attackers to bypass Lockdown Mode protections and exfiltrate chat data without user interaction.

**Do:** Ensure ChatGPT instances are updated to the latest patched version.

[The Hacker News](https://thehackernews.com/2026/11/researchers-bypass-chatgpt-lockdown.html)

### 🟠 Hackers backdoor Linux servers using trojanized CWP web server

A new Linux malware called CWPdoor is being distributed through a trojanized version of cwpsrv, the web server behind the Control Web Panel (CWP) management interface. [...]

[BleepingComputer](https://www.bleepingcomputer.com/news/security/hackers-backdoor-linux-servers-using-trojanized-cwp-web-server/) · [The Hacker News](https://thehackernews.com/2026/11/hackers-hide-linux-backdoor-in-control.html)

### 🟠 DigiCert data breach exposes customer information, identity documents

DigiCert warns it suffered a data breach after a server migration mistakenly exposed an internal business system to the internet, allowing unauthorized access to customer information and identity documents. [...]

[BleepingComputer](https://www.bleepingcomputer.com/news/security/digicert-data-breach-exposes-customer-information-identity-documents/) · [SecurityWeek](https://www.securityweek.com/digicert-data-breach-impacts-business-customer-information/) · [The Record](https://therecord.media/digicert-certificate-authority-reports-data-breach)

### 🟠 Chainalysis warns all users hit in cyber breach involving ‘agentic’ techniques

Chainalysis, the blockchain analytics company, said Wednesday night that some information belonging to all its users — which its website says include those in the law enforcement and national security sectors — had been exposed in a cyberattack.

[The Record](https://therecord.media/chainalysis-all-users-hit-by-agentic-cyberattack) · [The Hacker News](https://thehackernews.com/2026/11/chainalysis-breach-exposes-all-users.html) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/chainalysis-says-breach-exposed-credentials-for-all-customers/) · [Ars Technica](https://arstechnica.com/security/2026/11/chainalysis-says-hackers-stole-credentials-and-tokens-for-all-of-its-customers/)

### 🟠 Cyberattack Hits French Blood Bank Site but No Blood Products Are Compromised

The incident comes after supermarkets in a number of European countries reported this week that their fridges and freezers warmed up after they were remotely hacked. The post Cyberattack Hits French Blood Bank Site but No Blood Products Are Compromised appeared first on SecurityWeek .

[SecurityWeek](https://www.securityweek.com/cyberattack-hits-french-blood-bank-site-but-no-blood-products-are-compromised/)

### 🟠 ThreatsDay: Apache OFBiz RCE, DreamHost Breach, DeFi Site Hijacks + 17 More Stories

How much damage can someone do without breaking much? Quite a lot, it seems.

[The Hacker News](https://thehackernews.com/2026/11/threatsday-apache-ofbiz-rce-dreamhost.html)

### 🟠 5 Active Cyber Threats That Put US Enterprises at Risk in October 2026

October 2026 brought another wave of cyber threats targeting US businesses, with attackers exploiting trusted platforms, legitimate authentication processes, and everyday business workflows. For enterprises, these campaigns raise the stakes beyond individual security incidents, increasing the risk of financial losses, data breaches, and costly operational disruption.

[The Hacker News](https://thehackernews.com/2026/11/5-active-cyber-threats-that-put-us.html)

### 🟠 CERT-In Flags AI-Driven Attacks as Backdoored ARTEX Exposes 62 Consoles to Root Access

The Indian Computer Emergency Response Team (CERT-In) has disclosed that an artificial intelligence (AI)-assisted threat actor it tracks as Crafty Falcon is targeting organizations in the Banking, Financial Services, and Insurance (BFSI) sectors in the country. Describing the threat as active and ongoing, the activity involves the use of publicly-available AI-driven offensive security tools

[The Hacker News](https://thehackernews.com/2026/11/backdoored-docker-image-for-artex-ai.html)

## 2026-11-04

### 🔴 Debian and Ubuntu APT Flaw Allows Package Swap and Root RCE

A flaw in the APT package manager for Debian and Ubuntu allows a MitM attacker during retry attempts to swap verified packages with malicious ones, executing code as root. Affects Debian 12 and newer.

**Do:** Apply official APT updates from Debian and Ubuntu immediately.

[The Hacker News](https://thehackernews.com/2026/11/debian-and-ubuntu-apt-flaw-lets-mitm.html)

### 🔴 Google Patches Critical Remote Code Execution Flaw in Android
`CVE-2026-58868 · EPSS 0.00`

A critical zero-click RCE flaw, CVE-2026-58868, affects Android 14 through 17. Fixed in the 2026-11-01 security patch level.

**Do:** Apply Android security patch level 2026-11-01 or later.

[The Hacker News](https://thehackernews.com/2026/11/google-patches-critical-android-flaw.html)

### 🟠 NIKKE PC Game Launcher Compromised to Deliver Malware
`exploited`

Developers of Goddess of Victory: NIKKE confirmed a supply-chain attack where PC launcher scripts were tampered with to distribute data-stealing malware targeting credentials and crypto wallets.

**Do:** Check systems running the NIKKE PC launcher for compromise and scan for malware.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/nikke-pc-game-launcher-hacked-to-spread-remote-access-data-stealing-malware/)

### 🟠 Crédit Mutuel Arkéa Suffers Cyber Heist via Supplier Compromise
`exploited`

French bank Crédit Mutuel Arkéa reported a cyber heist where attackers compromised an unnamed supplier to execute unauthorized transfers totaling an estimated $133 million.

**Do:** Audit third-party vendor access and monitor high-value fund transfers.

[The Record](https://therecord.media/french-bank-confirms-cyber-heist)

### 🟠 Hackers Use N-Day Exploits in Zero-Click Attacks on iOS and Android
`exploited`

A watering hole campaign associated with Russian hackers targets iOS and Android users with n-day exploits.

**Do:** Ensure mobile devices are fully updated and monitor web traffic for suspicious redirects.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/hackers-use-n-day-exploits-in-zero-click-attacks-on-ios-android-devices/) · [The Hacker News](https://thehackernews.com/2026/11/apt29-linked-hackers-hijack-web.html) · [Ars Technica](https://arstechnica.com/security/2026/11/hackers-exploited-ios-and-android-flaws-to-infect-phones/)

### 🟠 Ruby on Rails Active Storage Flaw Allows Arbitrary File Write

A critical flaw in Ruby on Rails Active Storage lets unauthenticated attackers write server files via ImageMagick uploads. Fixed in versions 8.1.4.1 and 8.0.5.2.

**Do:** Upgrade Ruby on Rails to versions 8.1.4.1 or 8.0.5.2.

[The Hacker News](https://thehackernews.com/2026/11/critical-rails-flaw-lets-attackers.html)

### 🟠 Xen Hypervisor Flaws Allow Inter-VM Memory Access

Two flaws in Xen hypervisor versions 4.6 onward allow a malicious guest VM to read and write memory of other VMs, including dom0. Patches are available.

**Do:** Apply Xen hypervisor patches.

[The Hacker News](https://thehackernews.com/2026/11/xen-hypervisor-flaws-let-one-malicious.html)

### 🟠 DreamHost Confirms Data Breach Exposing FTP and Webmail Credentials
`exploited`

DreamHost disclosed a data breach where attackers accessed its File Manager platform for two months, stealing customer FTP and SFTP usernames and passwords.

**Do:** Reset FTP and SFTP credentials and review account activity.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/dreamhost-confirms-data-breach-exposed-ftp-logins-and-webmail-sessions/)

### 🟠 Google Calendar Phishing Campaign Bypasses MFA
`exploited`

A phishing campaign used Google Calendar invites and fake login pages to hijack corporate Google sessions and bypass MFA protections, prompting nearly 900 malicious domains to be taken down.

**Do:** Audit Google Workspace integrations and train users on calendar invite phishing.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/google-calendar-phishing-campaign-hijacks-sessions-bypasses-mfa/)

### 🟠 Russian Hosting Provider Beget Suffers Cloud Data Wiping Attack
`exploited`

Russian web hosting provider Beget suffered a cyberattack that destroyed data across its cloud infrastructure and disrupted hundreds of websites.

[The Record](https://therecord.media/russia-cyberattack-beget-cloud)

### 🟠 Sogou Input Method DNS Requests Hijacked to Deploy DarkVigil Backdoor
`exploited`

China-aligned threat actors hijacked DNS requests via insecure HTTP in Windows versions of Sogou Input Method to deploy DarkVigil.

**Do:** Audit software using insecure HTTP communication channels and monitor for unauthorized DNS modifications.

[The Hacker News](https://thehackernews.com/2026/11/china-aligned-hackers-hijack-sogou.html)

### 🟠 Etrel INCH AC Charging Station Hard-Coded Credentials
`CVE-2026-112354 · CVSS 9.8`

Etrel INCH AC charging station management web interface prior to firmware 7.1.2 and 8.0.1 contains a hard-coded default credential vulnerability allowing remote attackers to gain full administrator access.

**Do:** Upgrade Etrel INCH AC firmware to versions 7.1.2 or 8.0.1 and change default credentials.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-112354)

### 🟠 OpenAI Codex Jailbreak Toolkit Found Containing Prompt Adware
`exploited`

Researchers discovered an OpenAI Codex jailbreak bundle named Haiou that modifies AI agent instructions to insert unauthorized advertisements for a third-party AI gateway.

**Do:** Audit AI agent configuration files and remove untrusted jailbreak toolkits.

[The Hacker News](https://thehackernews.com/2026/11/researchers-uncover-prompt-adware.html)

## 2026-11-03

### 🔴 WordPress Core TOCTOU Race Condition Vulnerability Added to KEV
`CVE-2026-119977 · EPSS 0.01 · CISA KEV`

CISA added a time-of-check time-of-use (TOCTOU) race condition vulnerability in WordPress Core (CVE-2026-119977) to its Known Exploited Vulnerabilities catalog, which could allow unauthenticated attackers to execute code during the upgrade window.

**Do:** Apply WordPress security updates and mitigations in accordance with vendor and CISA guidance.

[CISA Advisories](https://www.cisa.gov/news-events/alerts/2026/11/03/cisa-adds-one-known-exploited-vulnerability-catalog) · [CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-119977) · [The Hacker News](https://thehackernews.com/2026/11/cisa-confirms-hackers-exploiting.html) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/cisa-flags-wordpress-rce-flaw-as-actively-exploited-in-attacks/)

### 🟠 Chainstack Discloses Production Infrastructure Breach and Data Exposure
`exploited`

Blockchain infrastructure provider Chainstack disclosed a production systems breach exposing customer data and password hashes as part of a wider AI-powered campaign.

**Do:** Reset API keys and passwords associated with Chainstack accounts.

[The Hacker News](https://thehackernews.com/2026/11/chainstack-reports-production-systems.html)

### 🟠 BlackX UEFI Bootkit Infects Fully Patched Windows Machines
`exploited`

The BlackX UEFI bootkit exploits Microsoft's lack of clarity around Secure Boot protections to infect fully patched Windows systems.

[Ars Technica](https://arstechnica.com/security/2026/11/uefi-bootkit-infected-fully-patched-windows-machines-is-microsoft-to-blame/)

### 🟠 Critical Node-RED Flaw Exploited to Deploy Botnets and Webshells
`exploited`

Active exploitation of a critical Node-RED vulnerability has been observed from a single IP address attempting to deploy Linux botnets and webshells.

**Do:** Audit and patch Node-RED instances immediately.

[SecurityWeek](https://www.securityweek.com/critical-node-red-flaw-exploited-in-attacks/)

### 🟠 cPGuard Security Tool Update Channel Hijacked to Backdoor Linux Servers
`exploited`

Attackers breached the cPGuard update system to push a malicious script to Linux servers, installing a backdoor and harvesting password hashes. Affects versions prior to cPGuard 5.88.25.

**Do:** Upgrade cPGuard to version 5.88.25 or later and audit Linux servers for unauthorized backdoors and credential compromise.

[The Hacker News](https://thehackernews.com/2026/11/cpguard-update-channel-hijacked-to.html) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/hackers-hijack-cpguard-autoupdate-to-deploy-backdoor-steal-data/) · [SecurityWeek](https://www.securityweek.com/malicious-cpguard-updates-served-in-opsshield-supply-chain-attack/)

### 🟠 Barracuda Warns of Critical Root Command Injection Vulnerabilities
`CVE-2026-111560, CVE-2026-116606`

Barracuda Networks warned customers to patch two vulnerabilities that allow attackers to run commands with root privileges on affected devices.

**Do:** Apply the latest security patches provided by Barracuda immediately.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/barracuda-warns-of-critical-flaws-allowing-root-access-to-devices/) · [The Hacker News](https://thehackernews.com/2026/11/barracuda-flaws-could-be-chained-to.html) · [SecurityWeek](https://www.securityweek.com/barracuda-email-security-gateway-authentication-bypass-opens-path-to-root/) · [watchTowr Labs](https://labs.watchtowr.com/barracuda-networks-is-your-new-best-friend-barracuda-email-security-gateway-pre-auth-remote-root-rce-cve-2026-116606-cve-2026-111560/) · [The Hacker News](https://thehackernews.com/2026/11/experts-demonstrate-barracuda-email.html)

### 🟠 Apple Warns German Lawmakers and Staff of Spyware Targeting
`exploited`

Several German politicians and foreign policy staff received threat notifications from Apple regarding targeted spyware campaigns.

**Do:** Enable Lockdown Mode on Apple devices if considered a high-risk target.

[The Record](https://therecord.media/german-officials-among-apple-spyware-warning-recipients)

### 🟠 3AM Ransomware Affiliate Targets UK School Estate
`exploited`

A 3AM ransomware affiliate targeted a UK school estate from an unmanaged host, successfully encrypting around 37 machines.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/uk-school-estate-hit-by-3am-ransomware-in-suspected-ai-assisted-attack/)

### 🟠 Harvard University Data Breach Exposes Over 850,000 Accounts
`exploited`

Hackers breached Harvard University's Alumni Affairs and Development systems, stealing data linked to more than 850,000 unique email addresses.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/harvard-university-data-breach-exposed-info-of-851-000-accounts/)

### 🟠 Frontline Education Data Breach Impacts Over 1.3 Million
`exploited`

Hackers exploited a vulnerability in third-party software to steal personal information of school district staff and students affecting over 1.3 million individuals.

[SecurityWeek](https://www.securityweek.com/frontline-education-data-breach-impacts-over-1-3-million/)

### 🟠 npm:@enspirit/elo Sandbox Escape and Code Execution Vulnerability
`CVE-2026-44267 · CVSS 9.8`

The Elo JavaScript emitter (@enspirit/elo) contains a vulnerability allowing unauthenticated attackers with control over parsed strings to escape the sandbox and execute arbitrary code via unfiltered .constructor member access.

**Do:** Upgrade npm:@enspirit/elo to a patched version or avoid passing untrusted strings to emission paths.

[GitHub Advisory](https://github.com/advisories/GHSA-33r5-xmm8-v6x5)

### 🟠 npm:@enspirit/elo Ruby Backend RCE via Unescaped Interpolation
`CVE-2026-44266 · CVSS 9.8`

The Elo Ruby backend contains a remote code execution vulnerability due to unescaped interpolation sequences in emitted string literals and subtype-constraint labels, permitting arbitrary shell execution.

**Do:** Upgrade npm:@enspirit/elo and review Elo source strings passed to the Ruby backend.

[GitHub Advisory](https://github.com/advisories/GHSA-7w38-ggh5-v542)

### 🟠 Subnet Solutions PowerSYSTEM Center SQL Injection and Authorization Flaws
`CVE-2026-63017, CVE-2026-63774`

Subnet Solutions PowerSYSTEM Center versions 2020, 2024, and 2026 contain vulnerabilities (including CVE-2026-63017 and CVE-2026-63774) allowing unauthorized SQL command execution and resource access.

**Do:** Upgrade PowerSYSTEM Center to patched versions in accordance with vendor advisories.

[CISA Advisories](https://www.cisa.gov/news-events/ics-advisories/icsa-26-307-01)

### 🟠 Android November 2026 Updates Patch Over 200 Vulnerabilities

Android's November 2026 updates fix over 200 vulnerabilities, including a critical Framework remote code execution flaw requiring no user interaction.

**Do:** Apply Android November 2026 security updates to mobile devices.

[SecurityWeek](https://www.securityweek.com/androids-november-2026-updates-patch-over-200-vulnerabilities/)

### 🟠 WorkOS Discloses Internal Sales App Breach via AI Tool
`exploited`

Developer platform WorkOS suffered a data breach after a threat actor used ARTEX AI to access business contact records and customer communication summaries.

**Do:** Review access controls for internal sales and communication applications.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/workos-says-attacker-used-artex-ai-to-breach-internal-sales-app/) · [SecurityWeek](https://www.securityweek.com/ai-linked-breaches-mount-as-workos-northflank-trigger-dev-disclose-hacks/)

### 🟠 Google Reports LLMjacking Attacks Generating High Cloud Charges
`exploited`

Large language model hijacking (LLMjacking) attacks are generating massive fraudulent cloud charges, with some organizations losing over $100,000 per day.

**Do:** Audit cloud AI resource consumption and implement strict billing alerts and access controls.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/google-llmjacking-attacks-rack-up-1-million-in-cloud-ai-charges/)

### 🟠 mSecure Urges Password and 2FA Resets After Suspicious Activity
`exploited`

Password manager mSecure urged users to reset passwords, 2FA, and passkeys following suspicious activity detected on its systems.

**Do:** Reset master passwords and multi-factor authentication for mSecure accounts.

[The Hacker News](https://thehackernews.com/2026/11/msecure-warns-users-to-change-passwords.html) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/msecure-password-manager-hack-prompts-password-reset-warnings/)

### 🟠 Russia-Linked Spies Target Ukrainian Investigations and Military Routes
`exploited`

Russia-linked threat actors are using simple malware to steal sensitive documents and credentials from Ukrainian organizations near the front line.

[The Record](https://therecord.media/russia-linked-cyber-spies-target-ukraine-war-support)

### 🟠 Russia-Aligned Gorbag Hackers Exploit WinRAR Flaw Against Ukraine
`exploited`

Gorbag threat actors have been observed exploiting WinRAR vulnerabilities to deploy info-stealer malware against Ukrainian defense and law enforcement targets.

[The Hacker News](https://thehackernews.com/2026/11/russia-aligned-gorbag-hackers-exploit.html)

