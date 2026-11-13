# Security signal: last 7 days

🔴 act now · 🟠 worth knowing

## 2026-11-13

### 🔴 Now exploited: Check Point Gateways PHP2Shell and Gaia OS Privilege Escalation Exploited
`CVE-2026-114713, CVE-2026-123039 · CISA KEV`

Attackers are actively exploiting PHP2Shell and a local privilege escalation flaw (CVE-2026-123039) in Check Point Security Gateways to achieve root access, deploy the TSGA backdoor, and wipe ESXi files.

**Do:** Apply available patches for Check Point Security Gateways immediately and audit for indicators of compromise.

[SecurityWeek](https://www.securityweek.com/php2shell-exploited-in-destructive-check-point-gateway-attacks/) · [The Hacker News](https://thehackernews.com/2026/11/hackers-exploit-php2shell-flaws-in.html) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/check-point-patches-zero-day-that-lets-hackers-get-root-access/) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/check-point-gateways-hacked-via-php2shell-to-deploy-vmware-esxi-wiper/) · [CISA Advisories](https://www.cisa.gov/news-events/alerts/2026/11/13/cisa-adds-two-known-exploited-vulnerabilities-catalog) · [CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-114713) · [CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-123039)

### 🔴 VITEC EZ TV Platform Server Unauthenticated File Upload RCE
`CVE-2026-82504 · CVSS 9.8`

VITEC EZ TV Platform Server before 8.5.0 contains an unauthenticated file upload vulnerability allowing remote attackers to upload and execute arbitrary ASPX files, achieving remote code execution. Patches are available.

**Do:** Upgrade VITEC EZ TV Platform Server to version 8.5.0 or apply available patches.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-82504)

### 🔴 XWEB EVO Pre-Auth OS Command Injection (CVE-2026-124002)
`CVE-2026-124002 · CVSS 9.8`

XWEB EVO versions 5.2.3 through 5.6.x contain a pre-authentication OS command injection vulnerability in login.lua, cleanout.lua, and api.lua, allowing root RCE. Note that this product line reached end-of-service in March 2026.

**Do:** Isolate affected XWEB EVO devices from the internet immediately as the product is end-of-life.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124002)

### 🔴 XWEB EVO Hardcoded Backdoor Password (CVE-2026-124004)
`CVE-2026-124004 · CVSS 9.8`

XWEB EVO before 5.6.2 contains a hardcoded backdoor password ('xwebevonewgeneration') allowing unauthenticated remote attackers to gain full administrative access.

**Do:** Disconnect affected XWEB EVO systems and apply vendor patches or replace end-of-life devices.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124004)

### 🔴 XWEB EVO CGIs Command Injection (CVE-2026-124010)
`CVE-2026-124010 · CVSS 9.8`

XWEB EVO before 5.6.2 contains a command injection vulnerability in the setuid-root CGI xwconsole.cgi, allowing unauthenticated remote attackers to execute arbitrary root commands.

**Do:** Restrict access to XWEB EVO administrative interfaces and upgrade to version 5.6.2 or later.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124010)

### 🔴 SilentAir State-Sponsored Group Hijacks Asian Telecom Networks
`exploited`

A state-sponsored threat group named SilentAir hijacked mobile network nodes in at least six Asian countries to intercept calls and SMS 2FA codes, primarily targeting Taiwanese subscribers.

**Do:** Audit mobile network infrastructure and review access controls for telecom nodes.

[The Hacker News](https://thehackernews.com/2026/11/silentair-hijacks-asian-telecom.html) · [SecurityWeek](https://www.securityweek.com/silentair-hackers-intercept-calls-sms-from-inside-mobile-networks/)

### 🔴 Operation Endgame Disrupts Gootloader, CastleRAT, and StealC
`exploited`

Law enforcement seized 235 servers and 257 domains, taking down infrastructure behind Gootloader, CastleRAT, and StealC malware while recovering 6.4 million stolen logins.

[SecurityWeek](https://www.securityweek.com/law-enforcement-disrupts-gootloader-castlerat-and-stealc-infrastructure/) · [The Hacker News](https://thehackernews.com/2026/11/operation-endgame-takes-down-gootloader.html)

### 🔴 OpsTree BuildPiper Manifest Privilege Escalation (CVE-2026-127073)
`CVE-2026-127073 · CVSS 9.9 · EPSS 0.01`

OpsTree BuildPiper before 2.7.0 allows project users to gain Kubernetes cluster-admin rights by submitting unrestricted manifests through the Additional Manifest feature.

**Do:** Upgrade OpsTree BuildPiper to 2.7.0 or later.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-127073)

### 🔴 OpsTree BuildPiper HostPath Authorization Flaw (CVE-2026-127080)
`CVE-2026-127080 · CVSS 9.9 · EPSS 0.01`

OpsTree BuildPiper before 2.7.0 contains an improper authorization flaw allowing deploy users to define arbitrary hostPath volumes and mount the worker node root filesystem read-write.

**Do:** Upgrade OpsTree BuildPiper to 2.7.0 or later.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-127080)

### 🟠 Nightmare Eclipse Drops Windows Zero-Day Exploit 'SignDrop'
`exploited`

Nightmare Eclipse released a Windows zero-day exploit named 'SignDrop' that abuses CLFS and Windows Defender to trigger arbitrary file creation in the context of the antimalware process.

**Do:** Monitor for anomalous CLFS or Windows Defender activity and apply vendor mitigations if available.

[SecurityWeek](https://www.securityweek.com/nightmare-eclipse-drops-windows-zero-day-exploit-signdrop/) · [Ars Technica](https://arstechnica.com/security/2026/11/windows-0-day-dropped-by-disgruntled-researcher-hands-hackers-system-rights/)

### 🟠 NginxPulse Unauthenticated SQL Injection (CVE-2026-129171)
`CVE-2026-129171 · CVSS 9.8`

NginxPulse versions 1.5.0 through 1.6.25 contain an unauthenticated SQL injection vulnerability via /api/stats/:type, allowing attackers to read database contents and execute server files. Patches are available in version 1.6.26.

**Do:** Upgrade NginxPulse to 1.6.26 or later.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129171)

### 🟠 OpenEMR OAuth Scope Canonicalization Flaw (CVE-2026-126473)
`CVE-2026-126473 · CVSS 9.3 · EPSS 0.00`

OpenEMR before 8.4.0 contains OAuth scope canonicalization flaws allowing unauthenticated attackers to obtain unapproved system-level FHIR access and modify patient records.

**Do:** Upgrade OpenEMR to 8.4.0 or later.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126473)

### 🟠 PLANET GS-5220 Switch Cookie Buffer Overflow (CVE-2026-109445)
`CVE-2026-109445 · CVSS 9.8`

PLANET GS-5220-8P2T2S firmware before 3.2412b261008 contains a stack-based buffer overflow via an oversized webstax_auth cookie value, leading to potential denial of service.

**Do:** Apply firmware update version 3.2412b261008 or later.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-109445)

### 🟠 sysPass Installation Authentication Bypass RCE (CVE-2026-129110)
`CVE-2026-129110 · CVSS 9.8`

sysPass 3.0.1 through 3.2.11 contains an authentication bypass flaw allowing unauthenticated attackers to reinstall instances, overwrite configurations, and execute commands via gadget chains.

**Do:** Upgrade sysPass beyond version 3.2.11.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129110)

### 🟠 XWEB EVO Arbitrary File Write (CVE-2026-124014)
`CVE-2026-124014 · CVSS 9.1`

XWEB EVO versions 4.3.0 through 5.8.8 contain an unauthenticated arbitrary file write vulnerability in config.lua allowing attackers to modify /etc/xwebconfig.json and cause denial of service.

**Do:** Restrict network access to vulnerable XWEB EVO installations.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124014)

### 🟠 Rucio Unauthenticated Administrator Impersonation (CVE-2026-100397)
`CVE-2026-100397 · CVSS 9.8`

Rucio accepts SSH challenge tokens as valid authentication credentials without prior validation, allowing unauthenticated attackers to impersonate administrators.

**Do:** Upgrade Rucio to a patched version immediately.

[GitHub Advisory](https://github.com/advisories/GHSA-x585-4vv8-2mh2)

### 🟠 Ruby on Rails Active Storage Arbitrary File Read/Write
`CVE-2026-122006 · CVSS 9.8 · EPSS 0.01`

Ruby on Rails Active Storage processing attachments with ImageMagick may allow unauthenticated attackers to write or read arbitrary files on the server.

**Do:** Upgrade Ruby on Rails Active Storage to patched versions.

[GitHub Advisory](https://github.com/advisories/GHSA-f3w6-w445-fwh9)

### 🟠 Vvveb Theme Installer Arbitrary File Upload RCE (CVE-2026-126378)
`CVE-2026-126378 · CVSS 9.4 · EPSS 0.01`

Vvveb through 1.0.8.6 contains an arbitrary file upload vulnerability in the theme installer via path matching flaws, allowing authenticated administrators to achieve remote code execution.

**Do:** Upgrade Vvveb beyond 1.0.8.6 or apply vendor patches.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126378)

### 🟠 City of Osaka Warns of Data Breach Impacting 1 Million
`exploited`

The City of Osaka in Japan warned residents of a data breach impacting 1 million people amid a wave of local cyber incidents.

[The Record](https://therecord.media/city-of-osaka-japan-email-data-breach)

### 🟠 TSMC Confirms Employee Data Breach via Cloud Provider
`exploited`

TSMC confirmed an employee data breach matching information stored in third-party cloud provider system services, though internal operations remained uncompromised.

[The Record](https://therecord.media/tsmc-confirms-employee-data-breach-cloud-provider)

### 🟠 Ransomware Attack Disrupts Belarusian Cloud Firm ActiveCloud
`exploited`

ActiveCloud suffered a ransomware attack that encrypted parts of its cloud infrastructure, leaving customers without access to key services for several days.

[The Record](https://therecord.media/belarus-cloud-provider-activecloud-ransomware-attack)

### 🟠 Citrix Patches 10 Critical NetScaler Vulnerabilities

Citrix has patched 10 critical NetScaler vulnerabilities where successful exploitation could lead to unexpected behavior or denial-of-service (DoS) conditions.

**Do:** Apply the latest NetScaler security updates from Citrix.

[SecurityWeek](https://www.securityweek.com/citrix-patches-10-critical-netscaler-vulnerabilities/)

### 🟠 Microsoft 365 Global Outage Disrupts Outlook and Teams

A widespread outage caused by failed server health checks disrupted Microsoft 365 services globally, including Outlook, Microsoft Teams, and Copilot.

[BleepingComputer](https://www.bleepingcomputer.com/news/microsoft/massive-microsoft-365-outage-disrupts-outlook-teams-copilot-worldwide/) · [SecurityWeek](https://www.securityweek.com/microsoft-365-outage-disrupts-outlook-exchange-online-and-teams/) · [SecurityWeek](https://www.securityweek.com/microsoft-struggles-to-restore-email-and-other-services-in-a-global-outage/)

### 🟠 Vvveb Media Trait Denylist Bypass RCE (CVE-2026-126380)
`CVE-2026-126380 · CVSS 9.4 · EPSS 0.01`

Vvveb before 1.0.9.0 contains a denylist bypass allowing authenticated administrators to upload .phar PHP polyglot files and execute arbitrary OS commands.

**Do:** Upgrade Vvveb to 1.0.9.0 or later.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126380)

### 🟠 OpenMage Magento LTS OAuth CSRF Flaw (CVE-2026-128049)
`CVE-2026-128049 · CVSS 9.4 · EPSS 0.00`

OpenMage Magento LTS before 20.18.2 contains a CSRF vulnerability in OAuth confirm actions, allowing attackers to acquire persistent REST API access tokens.

**Do:** Upgrade OpenMage Magento LTS to 20.18.2 or later.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-128049)

### 🟠 Linksys EA8100 Authentication Bypass (CVE-2026-127275)
`CVE-2026-127275, CVE-2026-127277 · CVSS 10.0`

Linksys EA8100 version 1.0.3.216940 contains a missing authentication vulnerability in the JNAP API ui_server.lua component. A public exploit is available.

**Do:** Apply vendor updates if available or restrict router management interfaces from the internet.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-127275) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-127277)

### 🟠 PostgreSQL Authenticated RCE Flaw (CVE-2026-6460)
`CVE-2026-6460 · EPSS 0.01`

A type confusion vulnerability tracked as CVE-2026-6460 allows authenticated users who can create objects to execute code on the server with operating system rights. PostgreSQL has released patches and recommends rebuilding C-language extensions.

**Do:** Upgrade PostgreSQL to the latest patched versions and rebuild C-language extensions.

[The Hacker News](https://thehackernews.com/2026/11/postgresql-patches-52-flaws-including.html)

### 🟠 University of Texas at Arlington Confirms Data Theft
`exploited`

The University of Texas at Arlington confirmed that personal information was stolen during a recent cyberattack.

[The Record](https://therecord.media/university-of-texas-arlington-warns-data-breach)

### 🟠 German Defense Tech Quantum Systems Confirms Cyberattack
`exploited`

Quantum Systems confirmed a cyberattack in late October orchestrated by hostile actors affecting drone operations infrastructure.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/german-military-drone-operations-disrupted-by-cyberattack/)

### 🟠 DOJ Details Gootloader Ransomware Campaign Impact
`exploited`

U.S. officials reported that Gootloader has been used in at least 44 ransomware attacks totaling $29 million since 2018.

[The Record](https://therecord.media/gootloader-ransomware-doj-details)

### 🟠 Trezor Confirms Hidden Hardware Implants in Resold Wallets

Trezor confirmed that Trezor Safe 5 wallets purchased from reseller CryptoBilis contain a malicious circuit board implant capable of stealing recovery phrases and transmitting them over mobile networks.

**Do:** Audit hardware wallets purchased from third-party resellers like CryptoBilis for physical tampering.

[The Hacker News](https://thehackernews.com/2026/11/trezor-confirms-hidden-hardware.html) · [BleepingComputer](https://www.bleepingcomputer.com/news/cryptocurrency/trezor-confirms-crypto-stealing-implants-in-three-wallets-releases-fix/)

### 🟠 Microsoft Confirms Windows Activation Failures After November Updates

Microsoft confirmed that November Patch Tuesday updates are causing Windows activation and licensing failures accompanied by 0x80041008 error codes.

[BleepingComputer](https://www.bleepingcomputer.com/news/microsoft/microsoft-confirms-windows-activation-failures-after-november-updates/) · [BleepingComputer](https://www.bleepingcomputer.com/news/microsoft/microsoft-says-november-security-updates-cause-printing-issues/)

## 2026-11-12

### 🔴 N-able N-central Zero-Day Vulnerabilities Under Active Exploitation
`exploited`

Following the public release of over 30 zero-days, hackers are actively targeting unauthenticated N-central vulnerabilities, prompting N-able to rush patches.

**Do:** Apply emergency patches for N-able N-central immediately and audit systems for compromise.

[SecurityWeek](https://www.securityweek.com/hackers-target-n-central-zero-days-as-n-able-rushes-patches/) · [SecurityWeek](https://www.securityweek.com/hackers-exploit-new-n-central-zero-day-hours-after-poc-publication/) · [The Hacker News](https://thehackernews.com/2026/11/hackers-exploit-n-central-flaws-to.html)

### 🔴 Active ScreenConnect Attacks Breach MSPs and Customer Devices
`exploited`

An active malware campaign is targeting managed service providers by compromising ScreenConnect environments to deploy rogue remote-access clients.

**Do:** Audit ScreenConnect instances and review connected client devices for unauthorized remote-access tools.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/active-screenconnect-attacks-breach-msps-impact-dozens-of-organizations/) · [The Hacker News](https://thehackernews.com/2026/11/screenconnect-attacks-target-at-least.html)

### 🔴 Siemens Desigo, Gridscale
`CVE-2026-109618, CVE-2026-109619, CVE-2026-111497 · EPSS 1.00 · CISA KEV`

View CSAF Summary On October 21, 2026, the Node.js project released security updates addressing a critical vulnerability in the Brotli decoder bundled with Node.js, commonly referred to as "Node2Shell" (tracked as CVE-2026-111497). The vulnerability is an out-of-bounds write that could allow a remote attacker to cause memory corruption and potentially execute arbitrary code.

[CISA Advisories](https://www.cisa.gov/news-events/ics-advisories/icsa-26-316-02) · [CISA Advisories](https://www.cisa.gov/news-events/ics-advisories/icsa-26-316-04) · [CISA Advisories](https://www.cisa.gov/news-events/ics-advisories/icsa-26-316-03) · [CISA Advisories](https://www.cisa.gov/news-events/ics-advisories/icsa-26-316-05) · [CISA Advisories](https://www.cisa.gov/news-events/ics-advisories/icsa-26-316-01)

### 🔴 Attacker Hijacks 4,837 GitHub Accounts to Run CI Secret Stealer
`exploited`

An attacker used stolen credentials for 4,837 GitHub accounts to plant a secret stealer in CI workflows across at least 1,806 repositories, collecting accessible cloud and repository secrets.

**Do:** Audit GitHub account security, rotate compromised CI secrets, and check workflow logs for unauthorized modifications.

[The Hacker News](https://thehackernews.com/2026/11/4837-hijacked-github-accounts-ran-ci.html) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/hackers-compromise-4-800-github-accounts-to-steal-cloud-credentials/)

### 🔴 Apache HTTP Server HTTP/2 RCE Flaw (CVE-2026-119618)
`CVE-2026-119618`

A critical remote code execution flaw in Apache HTTP Server's mod_http2 module affects versions 2.4.55 through 2.4.70 on servers with HTTP/2 enabled. Fixed in version 2.4.71.

**Do:** Upgrade Apache HTTP Server to version 2.4.71 or disable HTTP/2.

[The Hacker News](https://thehackernews.com/2026/11/critical-apache-http2-flaw-could-let.html) · [SecurityWeek](https://www.securityweek.com/apache-patches-critical-http-server-rce-found-by-anthropic-google/) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/apache-http-server-patches-critical-http-2-remote-code-execution-flaw/)

### 🔴 SCKit Malware Turns ScreenConnect Support Sessions Into Potential MSP Attack Paths
`CVE-2026-84869 · EPSS 0.01 · CISA KEV`

The ongoing campaign targeting ConnectWise ScreenConnect deployments involves the exploitation of a now-patched critical security flaw in the remote access software, and not a new vulnerability, it has emerged. Blackpoint Cyber's Adversary Pursuit Group (APG), which shared the details with The Hacker News, said the recovered attacker toolkit exploits CVE-2026-84869 (CVSS score: 9.9), an

[The Hacker News](https://thehackernews.com/2026/11/sckit-malware-targets-screenconnect.html) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/new-worm-like-sckit-malware-targets-msps-in-screenconnect-attacks/)

### 🟠 Synology DiskStation Manager Auth API SQL Injection (CVE-2026-76954)
`CVE-2026-76954 · CVSS 9.8`

An SQL injection vulnerability in the Auth API of Synology DiskStation Manager (DSM) before 7.2.1-69057-13, 7.2.2-72806-10, 7.3.2-86009-5, and 7.4.1-90080-1 allows remote attackers to read/write files and cause DoS.

**Do:** Update Synology DiskStation Manager to the latest patched versions.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-76954)

### 🟠 OpsTree REMS Authentication Bypass Flaw (CVE-2026-126768)
`CVE-2026-126768 · CVSS 9.8`

OpsTree REMS through 1.0.0 contains an authentication bypass vulnerability allowing unauthenticated attackers to obtain SuperUser access by manipulating the is_local_auth field.

**Do:** Apply available patches or restrict access to OpsTree REMS.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126768)

### 🟠 NextScan Hardcoded JWT Signing Key Flaw (CVE-2026-126797)
`CVE-2026-126797 · CVSS 9.8`

NextScan 1.1.0 through 1.2.0 contains an authentication bypass vulnerability due to a hardcoded JWT signing key, enabling attackers to forge administrator tokens.

**Do:** Update NextScan to a patched version and rotate secrets.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126797)

### 🟠 New N-central Exploits Work Against Patched Servers, Enable Root RCE and Windows SYSTEM Access
`exploited`

N-able on Thursday said it's investigating a new public disclosure containing claims of additional vulnerabilities in on-premise versions of N-central running version 2026.4.1 HF2. "Based on our initial review, the server issue described depends on a non-default configuration in which the Legacy API is turned on and exposed to the public internet," N-able said in a new advisory.

[The Hacker News](https://thehackernews.com/2026/11/new-n-central-exploits-work-against.html) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/new-windows-signdrop-zero-day-gives-hackers-system-privileges/) · [The Hacker News](https://thehackernews.com/2026/11/new-signdrop-zero-day-exploit-turns.html) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/new-n-able-4everable2shell-zero-day-exploited-hours-after-poc-released/)

### 🟠 Node.js and MongoDB Vulnerabilities Threaten Server Stability and Memory
`CVE-2026-118383`

Node.js fixed 16 flaws (including HTTP/2 memory leaks and crashes on release lines 24.x and 26.x), and MongoDB patched a pre-auth crash flaw (CVE-2026-118383) in replica sets.

**Do:** Upgrade Node.js to versions 22.23.5, 24.22.3, or 26.13.1, and update MongoDB server.

[The Hacker News](https://thehackernews.com/2026/11/nodejs-fixes-16-flaws-including-http2.html) · [The Hacker News](https://thehackernews.com/2026/11/critical-pre-auth-mongodb-flaw-cve-2026.html)

### 🟠 blueprintUE Self-Hosted Default Password Flaw (CVE-2026-126812)
`CVE-2026-126812 · CVSS 9.8`

blueprintUE Self-Hosted Edition before 4.3.7 has an insecure default configuration setting MYSQL_ALLOW_EMPTY_PASSWORD=yes, allowing unauthenticated attackers to access MariaDB as root.

**Do:** Update blueprintUE to 4.3.7 or later and secure database credentials.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126812)

### 🟠 Your Endpoint Management Platform Could Be Your Biggest Security Risk

Endpoint management platforms can become powerful attack tools when compromised, allowing hackers to deploy malware, execute commands, and disrupt thousands of devices. Action1 explains how customer-controlled cryptographic authorization can prevent attackers from abusing sensitive endpoint operations.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/your-endpoint-management-platform-could-be-your-biggest-security-risk/) · [The Hacker News](https://thehackernews.com/2026/11/your-soc-sees-alert-but-does-it-know.html)

### 🟠 ThreatsDay: 59 Linux Kernel Bugs, Falcon Spyware, GSocket Backdoors + 17 More Stories

A search result isn't always safe. An access request isn't always harmless.

[The Hacker News](https://thehackernews.com/2026/11/threatsday-59-linux-kernel-bugs-falcon.html)

### 🟠 Citrix Patches 12 NetScaler and Secure Access Client Flaws, Including Authentication Bypass
`CVE-2026-120868`

Citrix has released patches for multiple critical security flaws impacting NetScaler ADC, Citrix NetScaler Gateway, and NetScaler Console that could lead to denial-of-service (DoS) or an authentication bypass. The critical vulnerabilities that impact NetScaler ADC and NetScaler Gateway are listed below - CVE-2026-120868 (CVSS score: 9.3) - A memory overflow vulnerability in Packet

[The Hacker News](https://thehackernews.com/2026/11/citrix-patches-12-netscaler-and-secure.html)

### 🟠 PTC Patches Critical Windchill and FlexPLM Flaw That Could Enable Remote Code Execution
`CVE-2026-126325 · EPSS 0.01 · exploited`

PTC has released patches for a new critical vulnerability impacting Windchill and FlexPLM software that, if successfully exploited, could result in remote code execution. The security flaw, tracked as CVE-2026-126325, carries a CVSS v4 score of 9.2 out of a maximum of 10.0.

[The Hacker News](https://thehackernews.com/2026/11/ptc-patches-critical-windchill-and.html)

### 🟠 Apify rotates API tokens, prompts 2FA resets after breach

Apify has rotated critical internal secrets and revoked some third-party OAuth connections after detecting unauthorized access to its internal systems. [...]

[BleepingComputer](https://www.bleepingcomputer.com/news/security/apify-rotates-api-tokens-prompts-2fa-resets-after-breach/) · [SecurityWeek](https://www.securityweek.com/apify-confirms-customer-data-accessed-in-cyberattack/)

### 🟠 ConnectWise investigates ScreenConnect breaches after reports of incidents at nearly 50 organizations

Abuse of an independent third-party tool led to breaches at ScreenConnect customers, confirmed the software's maker, ConnectWise. Cybersecurity researchers had spotted intrusions at nearly 50.

[The Record](https://therecord.media/connectwise-screenconnect-breaches-third-party-tool)

### 🟠 Hijacked email accounts complicate investigations into European bomb hoaxes

Bomb threats sent to thousands of schools across Europe this week came from a compromised email account at a Taiwanese university, the latest incident in a series of hoax threats that have targeted airports and newsrooms using messages sent from legitimate institutions.

[The Record](https://therecord.media/europe-hoax-email-threats)

### 🟠 Notion Customer Data Compromised in Fireworks AI Hack

The attackers accessed chat transcripts for fewer than 1% of Notion workspaces. Most transcripts were unattributable.

[SecurityWeek](https://www.securityweek.com/notion-customer-data-compromised-in-fireworks-ai-hack/)

## 2026-11-11

### 🟠 Nitori Furniture Data Breach Potentially Exposes 37.6M Records
`exploited`

Japanese retailer Nitori discovered an unauthorized network access that may have compromised up to 37.62 million customer records.

**Do:** Monitor accounts for suspicious activity if you are a Nitori customer.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/japanese-furniture-giant-nitori-says-hackers-stole-376m-customer-records/)

### 🟠 Red Hat Quay Authentication and Key Rotation Flaws
`CVE-2026-123710 · CVSS 9.8`

Unauthenticated clients can obtain anonymous registry tokens and manipulate service key rotation endpoints in Red Hat Quay, allowing unauthorized signing key installation and repository access.

**Do:** Apply Red Hat Quay security updates as provided by Red Hat.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123710) · [SecurityWeek](https://www.securityweek.com/critical-red-hat-quay-vulnerability-could-expose-private-container-images/)

### 🟠 Red Hat Quay SQL Wildcard Flaw Leads to Cross-Tenant Credential Theft
`CVE-2026-110697 · CVSS 9.9`

A flaw in Red Hat Quay's robot account listing function allows attackers to use underscores to query and retrieve decrypted authentication tokens from other tenants' namespaces.

**Do:** Apply available security patches for Red Hat Quay.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110697)

### 🟠 WWBN AVideo Authentication Bypass Vulnerability (CVE-2026-126542)
`CVE-2026-126542 · CVSS 9.8`

WWBN AVideo versions 6.5 through 29.7.1 contain an authentication bypass via Hybridauth social login display names, allowing unauthenticated attackers to log in as any user including administrators.

**Do:** Upgrade WWBN AVideo to a patched version.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126542)

### 🟠 React Server Components Unauthenticated RCE (CVE-2026-126187)
`CVE-2026-126187 · CVSS 9.5`

Certain React Server Components packages contain an unauthenticated remote code execution vulnerability affecting specific versions when processing crafted payloads with multiple typed arrays.

**Do:** Update react-server-dom-webpack, react-server-dom-parcel, and react-server-dom-turbopack to patched versions immediately.

[GitHub Advisory](https://github.com/advisories/GHSA-xqc2-xf4c-x3h3)

### 🟠 AntiFox AI Platform Abused in AWS Credential Theft Attacks
`exploited`

Attackers are leveraging Alibaba Cloud instances hosting the open-source AntiFox penetration testing platform to target web services and steal AWS production secrets.

**Do:** Audit AWS environments for unauthorized credential access and monitor outbound connections to Alibaba Cloud instances running AntiFox.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/hackers-use-antifox-ai-agents-in-aws-credential-theft-attacks/) · [The Hacker News](https://thehackernews.com/2026/11/antifox-ai-pentesting-platform-linked.html)

### 🟠 Railway Cloud Breach Exposes AI API Keys and Causes $740K Fraud
`exploited`

Cloud hosting provider Railway suffered a breach where hackers stole customer authentication secrets and API keys, generating $740,000 in fraudulent AI usage and potentially exposing up to 100,000 workspaces.

**Do:** Rotate all API keys and secrets previously stored on Railway.

[BleepingComputer](https://www.bleepingcomputer.com/news/apple/railway-breach-leads-to-740-000-in-fraudulent-ai-charges/) · [The Hacker News](https://thehackernews.com/2026/11/railway-says-stolen-customer-ai-keys.html)

### 🟠 Critical Zoom Workplace Windows Privilege Escalation (CVE-2026-108186)
`CVE-2026-108186`

An improper input validation vulnerability in Zoom Workplace for Windows (CVE-2026-108186, CVSS 9.6) allows unauthenticated users to conduct privilege escalation.

**Do:** Update Zoom Workplace for Windows to the latest patched version.

[The Hacker News](https://thehackernews.com/2026/11/critical-zoom-workplace-flaw-could.html)

### 🟠 Grok Build Coding Agent Leaks Confidential Info

A security researcher found 35,000 Grok Build applications exposed without authentication, leaking confidential information including data belonging to SpaceX.

**Do:** Audit Grok Build applications and ensure proper authentication controls are enforced.

[Ars Technica](https://arstechnica.com/security/2026/11/grok-build-coding-agent-leaks-oodles-of-confidential-info-some-belonging-to-spacexsi/) · [The Hacker News](https://thehackernews.com/2026/11/over-35000-grok-built-apps-exposed.html)

### 🟠 Maersk Confirms Data Breach Linked to WhiteArmor Ransomware
`exploited`

Maersk confirmed that unauthorized actors accessed a legacy system inherited from a previous acquisition and extracted data, accompanied by a $5 million ransom demand.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/maersk-confirms-data-breach-as-whitearmor-ransomware-demands-5-million/) · [SecurityWeek](https://www.securityweek.com/maersk-confirms-data-theft-amid-5-million-extortion-attempt/) · [The Record](https://therecord.media/shipping-giant-maersk-says-recent-incident-affected-legacy-system)

### 🟠 Poland Shuts Down ePUAP Government Platform Following Cyberattack
`exploited`

Poland took its nationwide ePUAP government administrative services platform offline following a cyberattack.

[The Record](https://therecord.media/poland-shuts-down-government-services-platform-cyberattack)

### 🟠 eMudhra Revokes 8 More Intermediate CAs Following Script Error
`exploited`

eMudhra has revoked 8 additional intermediate certificate authorities following an internal Python script key compromise issue previously disclosed in October.

**Do:** Verify and update trust stores if relying on eMudhra intermediate certificates.

[The Hacker News](https://thehackernews.com/2026/11/emudhra-revokes-8-more-cas-it.html) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/emudhra-revokes-8-more-ca-certificates-after-private-key-mishap/)

### 🟠 Sipay WooCommerce Virtual POS Module Auth Bypass (CVE-2026-85632)
`CVE-2026-85632 · CVSS 9.1`

Versions 26.8.3 up to 26.9.1 of the Sipay WooCommerce Virtual POS Module suffer from missing authentication and integrity checks, allowing authentication bypass and API message manipulation via MitM.

**Do:** Update Sipay WooCommerce Virtual POS Module to version 26.9.1 or higher.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-85632)

### 🟠 Adobe Connect Incorrect Authorization Flaw (CVE-2026-121355)
`CVE-2026-121355 · CVSS 9.1`

Adobe Connect contains an incorrect authorization vulnerability allowing unauthenticated attackers to gain elevated access to sensitive information or functionality without user interaction.

**Do:** Apply the latest updates for Adobe Connect.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121355)

### 🟠 Intel and AMD Patch Over 200 Vulnerabilities

Intel and AMD released their Patch Tuesday advisories addressing more than 200 vulnerabilities, including critical Intel TDX software flaws and AMD graphics bugs.

**Do:** Apply the latest CPU microcode and vendor firmware updates.

[SecurityWeek](https://www.securityweek.com/chipmaker-patch-tuesday-over-200-vulnerabilities-addressed-by-intel-amd/)

### 🟠 WordPress Ninja Forms File Uploads Add-on Arbitrary File Flaw (CVE-2026-126537)
`CVE-2026-126537 · CVSS 9.1`

The Ninja Forms File Uploads add-on for WordPress up to version 3.3.36 contains a vulnerability allowing arbitrary file deletion and potential file read via external storage services.

**Do:** Update Ninja Forms File Uploads add-on beyond version 3.3.36.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126537)

### 🟠 Adobe Connect Stored XSS Vulnerability (CVE-2026-121904)
`CVE-2026-121904 · CVSS 9.6`

Adobe Connect is affected by a stored Cross-Site Scripting vulnerability allowing a low-privileged user to inject malicious scripts into form fields and potentially compromise victim sessions.

**Do:** Apply the latest security updates from Adobe.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-121904)

### 🟠 ICS Patch Tuesday: Siemens and Vendors Flag High-Severity Flaws

Pre-Patch Tuesday advisories highlight high-severity industrial control system vulnerabilities across Siemens, Phoenix Contact, Johnson Controls, and Hitachi Energy.

**Do:** Review vendor ICS advisories and apply patches.

[SecurityWeek](https://www.securityweek.com/ics-patch-tuesday-siemens-flags-high-severity-flaws-node2shell-exposure/)

## 2026-11-10

### 🔴 Microsoft Office Outlook Zero-Day (CVE-2026-124194) Actively Exploited
`CVE-2026-111560, CVE-2026-111793, CVE-2026-116606, CVE-2026-124194 … · CISA KEV`

Microsoft's November 2026 Patch Tuesday fixes an actively exploited Outlook zero-day vulnerability (CVE-2026-124194) involving a missing user interaction for potentially unsafe action.

**Do:** Apply the November 2026 Microsoft security updates immediately.

[BleepingComputer](https://www.bleepingcomputer.com/news/microsoft/microsoft-november-2026-patch-tuesday-fixes-1-235-flaws-outlook-zero-day/) · [SecurityWeek](https://www.securityweek.com/exploited-outlook-zero-day-among-1094-flaws-patched-by-microsoft/) · [CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-124194) · [CISA Advisories](https://www.cisa.gov/news-events/alerts/2026/11/10/cisa-adds-six-known-exploited-vulnerabilities-catalog) · [The Hacker News](https://thehackernews.com/2026/11/cisco-broadworks-and-openwave-flaws.html) · [SecurityWeek](https://www.securityweek.com/threat-actors-exploit-openwave-cisco-broadworks-vulnerabilities/) · [The Hacker News](https://thehackernews.com/2026/11/microsoft-patches-1259-flaws-including.html)

### 🔴 Now exploited: Google Chrome XML Use-After-Free Vulnerability (CVE-2026-125350)
`CVE-2026-125350 · CISA KEV`

Google has issued an emergency security update to patch a high-severity use-after-free vulnerability in Chrome's XML component (CVE-2026-125350), which is actively exploited in the wild as a zero-day.

**Do:** Update Google Chrome to the latest version immediately.

[SecurityWeek](https://www.securityweek.com/chrome-update-patches-exploited-xml-zero-day-eighth-this-year/) · [The Hacker News](https://thehackernews.com/2026/11/google-issues-chrome-security-update.html) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/google-patches-eighth-chrome-zero-day-exploited-in-attacks-this-year/) · [CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-125350)

### 🔴 AhsayCBS Flaws (CVE-2026-105133, CVE-2026-105134) Exploited to Deploy Backdoor
`CVE-2026-105133, CVE-2026-105134 · EPSS 0.84 · CISA KEV`

Attackers exploited vulnerabilities CVE-2026-105133 and CVE-2026-105134 in AhsayCBS to bypass authentication and execute arbitrary commands, deploying a sandbox-evading Python backdoor.

**Do:** Apply available patches for AhsayCBS and audit systems for unauthorized Python backdoors.

[The Hacker News](https://thehackernews.com/2026/11/attackers-exploit-ahsaycbs-flaws-to.html)

### 🔴 Xen Orchestra Auth Bypass (VSA-2026-062) Actively Exploited
`exploited`

A critical authentication bypass vulnerability in Xen Orchestra (VSA-2026-062) is actively exploited in the wild, allowing attackers to gain administrator privileges and take over XCP-ng virtualization hosts.

**Do:** Apply updates provided by Vates VMS immediately and check logs for signs of compromise.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/critical-xen-orchestra-auth-bypass-flaw-exploited-to-hijack-vm-servers/) · [The Hacker News](https://thehackernews.com/2026/11/hackers-exploit-critical-xen-orchestra.html) · [SecurityWeek](https://www.securityweek.com/critical-xen-orchestra-flaws-exploited-in-attacks/)

### 🔴 Now exploited: Barracuda ESG Flaws Exploited to Gain Root Access
`CVE-2026-111560, CVE-2026-116606 · CISA KEV`

Barracuda Networks warned that attackers are actively exploiting recently patched Email Security Gateway (ESG) vulnerabilities to achieve root command execution.

**Do:** Ensure all Barracuda Email Security Gateway appliances are fully patched and inspect for signs of compromise.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/hackers-exploit-barracuda-email-security-gateway-flaws-to-get-root-access/) · [CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-111560) · [CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-116606) · [SecurityWeek](https://www.securityweek.com/recently-patched-barracuda-vulnerabilities-exploited-in-attacks/)

### 🔴 N-able Takes Cloud Platform Offline Following Zero-Day Disclosures
`exploited`

N-able took hosted N-central environments offline and advised on-premises customers to shut down servers after a researcher published over 30 alleged zero-days.

**Do:** Take N-central servers offline per vendor advisory until patches are available.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/n-able-takes-cloud-platform-offline-after-30-plus-zero-days-published/) · [The Hacker News](https://thehackernews.com/2026/11/n-able-takes-hosted-n-central-offline.html) · [SecurityWeek](https://www.securityweek.com/n-able-takes-n-central-offline-as-researcher-drops-over-30-zero-days/) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/n-able-releases-security-hotfixes-for-zero-day-vulnerabilities/)

### 🔴 Cisco BroadWorks XXE Vulnerability (CVE-2026-20320) Added to KEV
`CVE-2026-20320 · EPSS 0.00 · CISA KEV`

Cisco BroadWorks contains an XML external entity reference vulnerability (CVE-2026-20320) allowing remote unauthenticated attackers to read sensitive configuration information.

**Do:** Apply vendor mitigations in accordance with CISA BOD 26-04 guidance.

[CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-20320) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/cisa-flags-cisco-broadworks-flaw-as-actively-exploited-in-attacks/)

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

### 🔴 iOS Sandbox Escape Flaw Threatens Crypto Wallets on iOS 26 and 27
`exploited`

An active iOS sandbox escape published on GitHub affects iOS 26.7.1, 27.0.1, and 27.2, allowing third-party apps to read private files and expose cryptocurrency seed phrases and keys.

**Do:** Exercise caution when installing third-party iOS applications; monitor for an official Apple patch.

[The Hacker News](https://thehackernews.com/2026/11/binance-warns-of-ios-sandbox-escape.html) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/binance-warns-of-ios-flaw-that-could-leak-crypto-wallet-secrets/)

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

### 🔴 Openwave Messaging Webtop Media Transcoder Flaw in KEV
`CVE-2026-111793 · EPSS 0.00 · CISA KEV`

Openwave Messaging Limited Webtop Media Transcoder contains an incorrect resource transfer between spheres vulnerability (CVE-2026-111793) added to CISA KEV.

**Do:** Apply vendor mitigations in accordance with CISA BOD 26-04.

[CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-111793)

### 🟠 Russian Hackers Compromise Government Email Servers in Romania and Kazakhstan
`exploited`

State-linked hackers compromised government email servers in Romania and Kazakhstan to intercept correspondence with NATO and EU officials.

**Do:** Audit government and diplomatic mail infrastructure for unauthorized access and review external mail relay logs.

[The Record](https://therecord.media/russia-hackers-espionage-romania-kazakhstan)

### 🟠 SGLang RCE Exploit Breaches NEAR AI Inference Servers
`exploited`

An attacker exploited an RCE flaw in the SGLang inference engine to run code on a NEAR AI inference server and access processing requests.

**Do:** Upgrade SGLang and review inference server access logs for unauthorized execution.

[The Hacker News](https://thehackernews.com/2026/11/sglang-rce-exploit-breaches-near-ai.html)

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

[BleepingComputer](https://www.bleepingcomputer.com/news/security/sap-patches-four-maximum-severity-security-vulnerabilities/) · [SecurityWeek](https://www.securityweek.com/sap-patches-critical-icm2shell-proxygate-vulnerabilities/)

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

### 🟠 npm:mongoose sanitizeFilter Bypassed in countDocuments (CVE-2026-125120)
`CVE-2026-125120 · CVSS 9.8 · EPSS 0.01`

Mongoose versions prior to patches fail to apply sanitizeFilter on countDocuments queries, risking query selector injection attacks.

**Do:** Upgrade Mongoose to version 9.9.2+, 8.24.3+, 7.8.12+, or 6.13.11+.

[GitHub Advisory](https://github.com/advisories/GHSA-pcrw-h46h-c93h)

### 🟠 npm:bitcoinjs-lib Merkle Node Duplication Vulnerability (CVE-2026-107846)
`CVE-2026-107846 · CVSS 9.3 · EPSS 0.00`

bitcoinjs-lib contains an undetected merkle node duplication flaw in block root computation that can validate forged transaction lists with valid proof of work.

**Do:** Review advisory details and update bitcoinjs-lib packages.

[GitHub Advisory](https://github.com/advisories/GHSA-8vv3-6qpc-gpw6)

### 🟠 npm:node-opcua Namespace-Level RBAC Fail-Open Flaw (CVE-2026-95860)
`CVE-2026-95860 · CVSS 9.1 · EPSS 0.01`

An unauthenticated client can write protected variables and call privileged methods on OPC UA nodes lacking explicit per-node permissions due to a fail-open default in node-opcua.

**Do:** Upgrade node-opcua packages and verify explicit permissions on namespace nodes.

[GitHub Advisory](https://github.com/advisories/GHSA-xggf-m53x-jc3f)

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

### 🟠 Adobe Patches 110 Vulnerabilities Across 9 Products

Adobe fixed 110 vulnerabilities across products including AEM, Premiere, Photoshop, After Effects, and Connect.

**Do:** Apply the latest updates for Adobe products across the enterprise.

[SecurityWeek](https://www.securityweek.com/adobe-patches-110-vulnerabilities-across-9-products/)

### 🟠 Git RCE Vulnerability in Recursive Clones (CVE-2026-111760)
`CVE-2026-111760`

An integer truncation flaw in Git allows malicious repositories to execute code during recursive clones and submodule handling. Fixed in Git versions 2.50.2, 2.51.3, 2.52.1, 2.53.1, 2.54.1, 2.55.1, and 2.56.1.

**Do:** Upgrade Git to versions 2.50.2, 2.51.3, 2.52.1, 2.53.1, 2.54.1, 2.55.1, 2.56.1 or later.

[The Hacker News](https://thehackernews.com/2026/11/git-patches-flaw-that-lets-malicious.html)

### 🟠 China-Nexus Sparrow Malware Ecosystem Targets Telecom and Government

Three threat clusters (including SilentDelivery) linked through shared infrastructure and the Sparrow malware have targeted telecom, government, and critical infrastructure across Latin America, Asia, and Europe.

**Do:** Monitor networks for indicators associated with the Sparrow malware ecosystem and Chinese espionage campaigns.

[The Hacker News](https://thehackernews.com/2026/11/three-china-nexus-espionage-campaigns.html)

### 🟠 Apple Patches iMessage Privacy Flaws and Bluetooth Issues

Apple released security updates to fix iMessage privacy vulnerabilities allowing unauthorized users to join group chats and view past messages, alongside Bluetooth pairing flaws.

**Do:** Update Apple devices to the latest available software versions.

[The Hacker News](https://thehackernews.com/2026/11/apple-patches-imessage-group-chat.html) · [SecurityWeek](https://www.securityweek.com/bluetooth-airplay-pairing-vulnerabilities-patched-across-apple-platforms/)

### 🟠 Pocket ID Email Verification Token Reuse Vulnerability
`CVE-2026-115770 · CVSS 9.6 · EPSS 0.00`

Pocket ID allows email verification tokens to remain valid after an account email address change, enabling verified-email spoofing.

**Do:** Upgrade Pocket ID backend to a patched version when available.

[GitHub Advisory](https://github.com/advisories/GHSA-rm8c-2cv8-jwf6)

### 🟠 Fireworks AI Discloses Breach Following Third-Party Cloud Compromise
`exploited`

AI startup Fireworks AI disclosed a security breach where attackers accessed development machines after compromising a third-party cloud provider.

**Do:** Review third-party cloud access controls and audit development machine logs.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/fireworks-ai-discloses-new-breach-after-cloud-provider-hack/) · [The Record](https://therecord.media/ai-company-fireworks-says-hackers-stole-data-in-oct-attacks) · [The Hacker News](https://thehackernews.com/2026/11/fireworks-ai-breach-widens-to-expose.html) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/notion-says-fireworks-breach-exposed-customer-ai-chat-transcripts/)

## 2026-11-09

### 🔴 GPUStack Improper Authentication Vulnerability (CVE-2026-102895)
`CVE-2026-102894, CVE-2026-102895, CVE-2026-116779, CVE-2026-123158 … · EPSS 0.00 · CISA KEV`

GPUStack contains an improper authentication vulnerability allowing unauthenticated administrative access, API-key creation, secret disclosure, and code execution. The vulnerability is actively exploited and listed in CISA KEV.

**Do:** Apply vendor mitigations immediately per CISA KEV and BOD 26-04 guidelines.

[CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-102895) · [GitHub Advisory](https://github.com/advisories/GHSA-gj9m-f8ph-pmhr) · [CISA Advisories](https://www.cisa.gov/news-events/alerts/2026/11/09/cisa-adds-four-known-exploited-vulnerabilities-catalog) · [The Hacker News](https://thehackernews.com/2026/11/cisa-warns-of-active-exploitation-of.html) · [SecurityWeek](https://www.securityweek.com/ibm-aspera-faspex-signalwire-freeswitch-vulnerabilities-exploited-in-attacks/) · [GitHub Advisory](https://github.com/advisories/GHSA-62m9-f875-rqw6)

### 🔴 SignalWire FreeSwitch Code Injection Vulnerability (CVE-2026-116779)
`CVE-2026-116779 · EPSS 0.01 · CISA KEV`

SignalWire FreeSwitch contains a code injection vulnerability enabling configuration/credential disclosure, call control, and command execution. The flaw is actively exploited and listed in CISA KEV.

**Do:** Apply vendor mitigations immediately or discontinue use of the product per CISA KEV guidelines.

[CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-116779)

### 🔴 Qubole AWS Access Compromised to Breach Customer Accounts
`exploited`

Attackers used Qubole trusted AWS access credentials between October 14 and October 26 to breach multiple customer accounts and steal stored secrets and data.

**Do:** Audit AWS accounts connected to Qubole for unauthorized access and rotate exposed credentials.

[The Hacker News](https://thehackernews.com/2026/11/hackers-exploit-quboles-trusted-aws.html) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/hackers-exploit-trusted-aws-access-to-breach-multiple-cloud-environments/) · [SecurityWeek](https://www.securityweek.com/over-a-dozen-organizations-hit-in-qubole-supply-chain-attack/)

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

