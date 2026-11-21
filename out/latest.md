# Security signal: last 7 days

🔴 act now · 🟠 worth knowing

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

### 🟠 N-able Server Breach Causes Global Mail Assure and SpamExperts Outage
`exploited`

Attackers breached an N-able server, causing a major worldwide service outage affecting Mail Assure and SpamExperts Hosted Cloud services.

**Do:** Check N-able status updates and advisory guidance.

[BleepingComputer](https://www.bleepingcomputer.com/news/microsoft/n-able-says-recent-security-breach-led-to-major-service-outage/)

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

[The Hacker News](https://thehackernews.com/2026/11/critical-vmware-vcenter-flaw-cvss-98.html) · [SecurityWeek](https://www.securityweek.com/newly-patched-vmware-vcenter-flaw-exploited-as-zero-day-by-chinese-apt/) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/vmware-patches-vcenter-zero-day-exploited-in-attacks-since-september/) · [The Hacker News](https://thehackernews.com/2026/11/china-linked-hackers-exploit-critical.html) · [CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-123890) · [CISA Advisories](https://www.cisa.gov/news-events/alerts/2026/11/20/cisa-adds-four-known-exploited-vulnerabilities-catalog)

### 🔴 F5 Patches Critical NGINX2Root Flaws with Public PoCs
`exploited`

F5 patched critical NGINX2Root vulnerabilities that allow remote, unauthenticated attackers to execute arbitrary code, with public proof-of-concept exploits available.

**Do:** Apply the latest security patches from F5 immediately and monitor for exploitation attempts.

[SecurityWeek](https://www.securityweek.com/f5-patches-critical-nginx2root-flaws-as-poc-exploits-go-public/) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/critical-nginx-nginx2root-bugs-let-attackers-hijack-servers/)

### 🔴 Synology DSM Output Encoding Vulnerability Added to KEV
`CVE-2024-10441 · EPSS 0.01 · CISA KEV`

Synology DiskStation Manager (DSM) contains an improper encoding or escaping vulnerability in the system plugin daemon, which is actively exploited in the wild.

**Do:** Apply vendor mitigations and follow CISA KEV guidance.

[CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2024-10441)

### 🔴 BerriAI LiteLLM Unprotected Channel RCE Added to KEV
`CVE-2026-40217 · EPSS 0.17 · CISA KEV`

BerriAI LiteLLM contains an unprotected alternate channel vulnerability at /guardrails/test_custom_code allowing remote code execution via bytecode rewriting, confirmed exploited in the wild.

**Do:** Apply vendor mitigations and follow CISA KEV guidance.

[CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-40217)

### 🔴 Vanderbilt REDCap Code Injection Vulnerability Added to KEV
`CVE-2026-90817 · EPSS 0.04 · CISA KEV`

Vanderbilt REDCap contains a code injection vulnerability allowing unauthenticated remote code execution via crafted HTTP requests and public survey hashes, actively exploited in the wild.

**Do:** Apply vendor mitigations and follow CISA KEV guidance.

[CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-90817)

### 🔴 Apache Axis Unsafe Reflection Vulnerability Added to KEV
`CVE-2026-90436 · EPSS 0.01 · CISA KEV`

Apache Axis contains an unsafe reflection vulnerability allowing unauthenticated remote code execution via crafted SOAP fault messages, confirmed exploited in the wild.

**Do:** Discontinue use of EoL versions or apply vendor-recommended updates.

[CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-90436)

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

### 🟠 NGINX HTTP/2 Remote Code Execution Vulnerability (CVE-2026-123007)
`CVE-2026-123007`

A vulnerability in NGINX's HTTP/2 support (CVE-2026-123007), present since version 1.9.5, allows unauthenticated attackers to execute code on servers with HTTP/2 enabled. Fixed in versions 1.31.9 and 1.30.7.

**Do:** Upgrade NGINX to version 1.30.7, 1.31.9, or later.

[The Hacker News](https://thehackernews.com/2026/11/10-year-old-nginx-http2-flaw-lets.html)

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

### 🟠 Fleet SAML SSO Authentication Bypass Vulnerability
`CVE-2026-130759 · CVSS 9.9`

Fleet from 4.71.0 before 4.88.2 contains an authentication bypass in the SAML SSO callback using unvalidated client identifiers, allowing attackers to log in as global admin.

**Do:** Upgrade Fleet to version 4.88.2 or later.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130759)

### 🟠 Incus TLS Client Chain Authentication Bypass Vulnerability
`CVE-2026-130778 · CVSS 10.0`

Incus before 7.6.0 contains an authentication bypass allowing remote attackers to authenticate as any trusted certificate by appending its public certificate to the presented TLS client chain.

**Do:** Upgrade Incus to version 7.6.0 or later.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130778)

### 🟠 Atomic Server Unauthenticated Setup Invite Drive Write Access
`CVE-2026-69157 · CVSS 9.8 · EPSS 0.01`

Atomic Server provisions a well-known invite at /setup that ignores redeemer identity, allowing unauthenticated attackers to gain write access to the entire Drive and take over the instance.

**Do:** Upgrade atomic-server or disable unauthenticated setup invites.

[GitHub Advisory](https://github.com/advisories/GHSA-pfwx-xjp4-qxcj)

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

### 🟠 F5 Warns of Critical BIG-IP Traffic Management Flaws

Six critical vulnerabilities in F5 BIG-IP allow unauthenticated attackers to crash the Traffic Management Microkernel (TMM) or potentially achieve RCE under specific iRule or APM setups.

**Do:** Review F5 advisory and apply recommended hotfixes or configuration workarounds.

[The Hacker News](https://thehackernews.com/2026/11/f5-warns-6-critical-big-ip-flaws-can.html)

### 🟠 Data Breach Impacts Irish Credit Unions in Wellington IT Hack
`exploited`

A reported cyberattack on Wellington IT exposed sensitive information belonging to members of multiple credit unions in Ireland.

**Do:** Review Wellington IT advisory and monitor credit union accounts.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/data-breach-impacts-40-irish-credit-unions-in-reported-it-provider-hack/)

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

### 🟠 LaraDashboard SocialAuthService Authentication Bypass
`CVE-2026-130754 · CVSS 9.8`

All versions of LaraDashboard contain an authentication bypass in SocialAuthService::findOrCreateUser() that links social logins by email without provider verification, allowing unauthenticated account takeovers.

**Do:** Apply updates or patches provided by LaraDashboard.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130754)

### 🟠 pnpm exe Embedded Node.js eMudhra CA Trust Issue
`CVE-2026-130756 · CVSS 9.8`

pnpm exe before 10.34.8 embeds an outdated Node.js runtime that trusts compromised eMudhra intermediate CA certificates, enabling network attackers to perform MITM attacks during registry TLS connections.

**Do:** Upgrade pnpm exe to version 10.34.8 or later.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130756)

### 🟠 Incus Backup and Image Metadata Handling Vulnerability
`CVE-2026-130771 · CVSS 9.9`

Incus before 7.6.0 fails to reject special files, hard links, or symlinks in backup or image metadata, allowing restricted project users to read or overwrite host files.

**Do:** Upgrade Incus to version 7.6.0 or later.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130771)

### 🟠 Incus Custom Volume Snapshot Path Traversal Flaw
`CVE-2026-130779 · CVSS 9.6`

Incus before 7.6.0 contains a path traversal vulnerability in custom volume imports, allowing attackers to use traversal sequences in snapshot names to delete arbitrary host directories as root.

**Do:** Upgrade Incus to version 7.6.0 or later.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130779)

### 🟠 Incus Migration Peer Path Traversal Vulnerability
`CVE-2026-130780 · CVSS 9.9`

Incus before 7.6.0 contains a path traversal vulnerability allowing malicious migration peers to write outside intended directories via unvalidated volume and snapshot names.

**Do:** Upgrade Incus to version 7.6.0 or later.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130780)

### 🟠 Incus Event Stream Secret Exposure Vulnerability
`CVE-2026-130783 · CVSS 9.6`

Incus before 7.6.0 exposes certificate and cluster join token secrets through the default project event stream, allowing restricted clients to capture tokens and enroll unrestricted certificates.

**Do:** Upgrade Incus to version 7.6.0 or later.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130783)

### 🟠 Incus Default Project Resource Authorization Bypass
`CVE-2026-130784 · CVSS 9.9`

Incus before 7.6.0 contains an authorization bypass allowing restricted clients to create and access default project resources, potentially enabling arbitrary code execution on the host.

**Do:** Upgrade Incus to version 7.6.0 or later.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130784)

### 🟠 Incus OCI Configuration Injection Vulnerability
`CVE-2026-130786 · CVSS 9.9`

Incus before 7.6.0 contains a configuration injection vulnerability allowing users launching instances from controlled images to inject LXC directives and run commands as root.

**Do:** Upgrade Incus to version 7.6.0 or later.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130786)

### 🟠 DrayTek Vigor2960 setSWMProfile Buffer Overflow
`CVE-2026-132139 · CVSS 9.9`

DrayTek Vigor2960 up to 1.5.1.6 contains a remote stack-based buffer overflow in the setSWMProfile function via manipulated filename arguments, with public exploits available.

**Do:** Upgrade DrayTek Vigor2960 to version 1.5.1.7 or later.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-132139)

### 🟠 DrayTek Vigor2960 Jsonstatus Buffer Overflow
`CVE-2026-132141 · CVSS 9.9`

DrayTek Vigor2960 up to 1.5.1.6 contains a remote stack-based buffer overflow in the Jsonstatus component via manipulated usefile arguments, with public exploits available.

**Do:** Upgrade DrayTek Vigor2960 to version 1.5.1.7 or later.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-132141)

### 🟠 DrayTek Vigor2960 CGI Process Buffer Overflow
`CVE-2026-132142 · CVSS 9.1`

DrayTek Vigor2960 up to 1.5.1.6 contains a remote stack-based buffer overflow in the dataflowstatus CGI function via manipulated option arguments, with public exploits available.

**Do:** Upgrade DrayTek Vigor2960 to version 1.5.1.7 or later.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-132142)

### 🟠 DrayTek Vigor2960 Backup Handler Buffer Overflow
`CVE-2026-132143 · CVSS 9.9`

DrayTek Vigor2960 up to 1.5.1.6 contains a remote stack-based buffer overflow in doWebBackup via manipulated path/value arguments, with public exploits available.

**Do:** Upgrade DrayTek Vigor2960 to version 1.5.1.7 or later.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-132143)

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

### 🟠 CISA Adds Four Known Exploited Vulnerabilities to Catalog
`CVE-2024-10441, CVE-2026-40217, CVE-2026-90436, CVE-2026-90817 · EPSS 0.17 · CISA KEV`



[CISA Advisories](https://www.cisa.gov/news-events/alerts/2026/11/18/cisa-adds-four-known-exploited-vulnerabilities-catalog) · [The Hacker News](https://thehackernews.com/2026/11/cisa-warns-of-4-exploited-flaws-linked.html)

### 🟠 NVIDIA Investigating Gentlemen Ransomware Breach Claims

NVIDIA is investigating claims by the Gentlemen ransomware group after the company was listed on their dark web leak site.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/nvidia-investigating-gentlemen-ransomware-breach-claims/) · [SecurityWeek](https://www.securityweek.com/nvidia-responds-to-gentlemen-ransomware-claim/)

## 2026-11-18

### 🔴 Optimizely Third-Party Script Vulnerability Used to Serve Malware
`exploited`

At least 178 major websites unknowingly served malware via compromised Optimizely integrations, injecting data-stealing payloads to visitors over a 24-hour period.

**Do:** Audit third-party script integrations and enforce strict Content Security Policy (CSP) headers.

[Ars Technica](https://arstechnica.com/security/2026/11/malicious-code-delivered-through-optimizely-hits-visitors-to-hundreds-of-sites/) · [Krebs on Security](https://krebsonsecurity.com/2026/11/attackers-used-optimizely-to-a-b-test-malware-on-top-websites/)

### 🔴 Microsoft Agent Framework PyPI Package Compromised with Credential Stealer
`exploited`

Threat actors compromised Microsoft's agent-framework PyPI package (versions 1.26.1 and 1.26.2) to deploy a cloud credential stealer on Python startup.

**Do:** Remove affected versions of agent-framework and rotate compromised cloud credentials immediately.

[The Hacker News](https://thehackernews.com/2026/11/attackers-compromise-microsofts-agent.html)

### 🔴 Java4Shell Critical RCE Vulnerability in OpenJDK and Enterprise Apps

A critical vulnerability dubbed Java4Shell in OpenJDK allows unauthenticated attackers to execute remote code on major enterprise applications like Jenkins, Jira, Confluence, and Keycloak.

**Do:** Apply emergency patches for OpenJDK and affected enterprise applications as provided by vendors.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/critical-java4shell-flaw-allows-rce-attacks-on-major-java-applications/) · [SecurityWeek](https://www.securityweek.com/java4shell-exploitation-attempts-begin-as-vendors-rush-out-advisories/)

### 🔴 Now exploited: Apache warns of Roller RCE vulnerability exploited in attacks
`CVE-2026-129448 · CISA KEV`

Apache has released security updates to address a critical Roller flaw that threat actors are exploiting to gain code execution on vulnerable servers. [...]

[BleepingComputer](https://www.bleepingcomputer.com/news/security/apache-warns-of-roller-rce-vulnerability-exploited-in-attacks/) · [The Hacker News](https://thehackernews.com/2026/11/critical-apache-roller-rce-flaw-under.html) · [SecurityWeek](https://www.securityweek.com/critical-apache-roller-axis-vulnerabilities-exploited-in-attacks/) · [CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-129448)

### 🟠 COLD RELIC Hackers Exploit Stolen Google Workspace Data in Breaches
`exploited`

Russian state-sponsored group Cold Relic weaponized a single cloud compromise to breach a second U.S. organization using stolen Google Workspace data.

**Do:** Audit Google Workspace access logs, enforce phishing-resistant MFA, and monitor for unauthorized token usage.

[The Hacker News](https://thehackernews.com/2026/11/russian-cold-relic-hackers-use-stolen.html)

### 🟠 OwnTracks Recorder Format String RCE Vulnerability
`CVE-2026-131852 · CVSS 9.8`

OwnTracks Recorder before 1.0.5 contains a format string vulnerability in json_response() allowing unauthenticated attackers to execute code and leak memory via malicious tid values.

**Do:** Upgrade OwnTracks Recorder to version 1.0.5 or later.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-131852)

### 🟠 Microsoft Agent Framework Releases Poisoned With Credential Stealer

Versions 1.26.1 and 1.26.2 of agent-framework on PyPI steal Azure, Azure DevOps, and GitHub Actions credentials when Python starts. The post Microsoft Agent Framework Releases Poisoned With Credential Stealer appeared first on SecurityWeek .

[SecurityWeek](https://www.securityweek.com/microsoft-agent-framework-releases-poisoned-with-credential-stealer/) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/microsofts-agent-framework-pypi-package-compromised-to-steal-credentials/)

### 🟠 CVE-2026-130675: Craft CMS from 5.0.0 before 5.11.4 contains a remote code execution vulnerability in ImageTransforms::n
`CVE-2026-130675 · CVSS 9.8`

Craft CMS from 5.0.0 before 5.11.4 contains a remote code execution vulnerability in ImageTransforms::normalizeTransform() that allows attackers to instantiate arbitrary classes by supplying class:null with a __class key. Attackers can reach the method through Craft Commerce's payments/pay redirect template calling customer.photo.getUrl() with a crafted transform to instantiate classes like yii\rb

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130675)

### 🟠 CVE-2018-25443: Baidu UEditor 1.4.0 through 1.4.3.3 contains an unrestricted file upload vulnerability in the catchimage
`CVE-2018-25443 · CVSS 9.8`

Baidu UEditor 1.4.0 through 1.4.3.3 contains an unrestricted file upload vulnerability in the catchimage action of /ueditor/net/controller.ashx that only validates the Content-Type header. Unauthenticated attackers can supply a source[] URL like x.jpg?.aspx to retain a malicious extension and write an executable .aspx file for remote code execution.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2018-25443)

### 🟠 CVE-2021-48023: Weaver E-cology 9.0 contains an unrestricted file upload vulnerability in /page/exportImport/uploadOpera
`CVE-2021-48023 · CVSS 9.8`

Weaver E-cology 9.0 contains an unrestricted file upload vulnerability in /page/exportImport/uploadOperation.jsp that allows unauthenticated attackers to upload arbitrary JSP files. Attackers can send a crafted multipart POST request with a JSP webshell written to /page/exportImport/fileTransfer/ to achieve remote code execution.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2021-48023)

### 🟠 CVE-2023-54422: iDocView before 13.10.1_20231115 contains an unrestricted file upload vulnerability in the /html/2word e
`CVE-2023-54422 · CVSS 9.8`

iDocView before 13.10.1_20231115 contains an unrestricted file upload vulnerability in the /html/2word endpoint that allows unauthenticated attackers to write arbitrary files by supplying a malicious url parameter. Attackers can send a crafted GET request with the url parameter to download linked resources with an unsanitized path and unblocked .jsp extension, achieving remote code execution.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2023-54422)

### 🟠 CVE-2026-126755: ArangoDB before 3.12.11 contains an authentication bypass vulnerability caused by a parser differential
`CVE-2026-126755 · CVSS 9.8`

ArangoDB before 3.12.11 contains an authentication bypass vulnerability caused by a parser differential between the raw path authentication gate and the URL-decoded dispatch logic. Attackers can send requests with a %5f-encoded leading underscore to endpoints like /_db/_system/%5fapi/simple/first-example to reach /_api/* actions as superuser without authentication.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-126755)

### 🟠 rubygems:mustache: Mustache for Ruby: RCE using built-in method access
`CVE-2026-130001 · CVSS 9.8`

Affected packages: rubygems:mustache. > [!NOTE] > The vulnerability was fully disclosed to the maintainer in private prior to security advisories were enabled for the project.

[GitHub Advisory](https://github.com/advisories/GHSA-5hrj-7fc3-cmx9)

### 🟠 Russian APT Poses as Employee of Hacked Firm to Breach Another US Organization

Star Blizzard weaponized data and identities stolen in late 2025 to phish and compromise a US organization. The post Russian APT Poses as Employee of Hacked Firm to Breach Another US Organization appeared first on SecurityWeek .

[SecurityWeek](https://www.securityweek.com/russian-apt-poses-as-employee-of-hacked-firm-to-breach-another-us-organization/)

### 🟠 Java4Shell Vulnerability Puts Enterprise Applications at Risk of Takeover

Calif demonstrated remote code execution in Jira, Jenkins and Keycloak, while VulnCheck says real-world RCE requires per-target work The post Java4Shell Vulnerability Puts Enterprise Applications at Risk of Takeover appeared first on SecurityWeek .

[SecurityWeek](https://www.securityweek.com/java4shell-vulnerability-puts-many-enterprise-applications-at-risk-of-takeover/)

## 2026-11-17

### 🔴 Siemens Software Impacted by Node2Shell Brotli Vulnerability
`CVE-2026-111497 · EPSS 0.83 · CISA KEV`

Siemens products are affected by the critical 'Node2Shell' out-of-bounds write vulnerability (CVE-2026-111497) in the Node.js Brotli decoder, which allows remote code execution and is actively exploited.

**Do:** Update Siemens software products to the latest patched versions provided in the advisory.

[CISA Advisories](https://www.cisa.gov/news-events/ics-advisories/icsa-26-321-04) · [CISA Advisories](https://www.cisa.gov/news-events/ics-advisories/icsa-26-321-03)

### 🔴 MSP ScreenConnect Servers Targeted in Exploitation Campaign
`CVE-2026-84869 · EPSS 0.01 · CISA KEV`

More than 40 ScreenConnect servers received over 688,000 requests exploiting CVE-2026-84869 to execute guest-pushed files.

**Do:** Audit ScreenConnect servers for unauthorized guest-pushed files and apply vendor updates.

[The Hacker News](https://thehackernews.com/2026/11/connectwise-warns-screenconnect-attacks.html) · [SecurityWeek](https://www.securityweek.com/msp-screenconnect-servers-targeted-in-month-long-campaign/)

### 🔴 Perforce Puppet Enterprise Deserialization Flaw Added to KEV
`CVE-2026-115731 · EPSS 0.00 · CISA KEV`

Perforce Puppet Enterprise contains a deserialization vulnerability (CVE-2026-115731) in report-processing code allowing remote code execution, added to CISA KEV due to active exploitation.

**Do:** Apply mitigations and updates provided by Perforce for Puppet Enterprise immediately.

[CISA Advisories](https://www.cisa.gov/news-events/alerts/2026/11/17/cisa-adds-one-known-exploited-vulnerability-catalog) · [CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-115731) · [The Hacker News](https://thehackernews.com/2026/11/hackers-exploiting-critical-puppet-rce.html) · [SecurityWeek](https://www.securityweek.com/critical-perforce-puppet-rce-exploited-in-attacks/)

### 🔴 Critical Oracle Java Base64 Memory Corruption Vulnerability
`CVE-2026-114938 · exploited`

Oracle Java is affected by a critical memory-corruption vulnerability known as 'Java4Shell' (CVE-2026-114938) in the x86-64 HotSpot JVM Base64 decoder, allowing unauthenticated RCE.

**Do:** Identify affected Java installations and apply emergency patches from Oracle.

[CISA Advisories](https://www.cisa.gov/news-events/alerts/2026/11/17/critical-java-vulnerability-requires-immediate-patching) · [The Hacker News](https://thehackernews.com/2026/11/oracle-to-patch-11-java-flaws-today-as.html) · [The Hacker News](https://thehackernews.com/2026/11/java4shell-cve-2026-114938-enables-pre.html) · [The Hacker News](https://thehackernews.com/2026/11/cisa-urges-immediate-patching-of.html)

### 🔴 N-able Patches 17 N-central Flaws Including Zero-Days
`exploited`

N-able released N-central 2026.4 Hotfix 3 to patch 17 critical security flaws, including zero-days exploited in the wild to deploy crypto miners.

**Do:** Upgrade N-central to 2026.4 Hotfix 3 immediately.

[The Hacker News](https://thehackernews.com/2026/11/n-able-patches-17-n-central-flaws-as.html) · [SecurityWeek](https://www.securityweek.com/n-able-kills-legacy-apis-patches-17-n-central-zero-days/)

### 🔴 Cloud Keys Leaked in Docker Hub Images Stolen Within Seconds
`exploited`

Credentials and access secrets exposed in public Docker Hub images are actively extracted and exploited by attackers within seconds of publication.

**Do:** Audit public Docker Hub repositories for leaked secrets and implement automated scanning.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/cloud-keys-leaked-in-docker-hub-images-are-stolen-within-seconds/)

### 🔴 Operation ShadowCloud Deploys GitDoor and GraphDoor Backdoors
`exploited`

Active cyber intrusion campaign targets government sectors in Asia and Africa using Microsoft SharePoint and GitHub for C2.

**Do:** Monitor GitHub and SharePoint access logs for abnormal API usage and unauthorized C2 channels.

[The Hacker News](https://thehackernews.com/2026/11/new-gitdoor-and-graphdoor-backdoors.html)

### 🔴 Optimizely Supply Chain Attack Injects Malicious JavaScript on Major Sites
`exploited`

A supply chain attack targeting Optimizely has led to malicious JavaScript loading on popular websites including Zoom, CNN, and Salesforce, exposing visitors to credential theft and payment skimming.

**Do:** Audit third-party JavaScript integrations and monitor web apps for unauthorized script execution.

[SecurityWeek](https://www.securityweek.com/cursor-supply-chain-attack-started-at-fireworks/) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/optimizely-supply-chain-attack-infects-major-brands-sites-with-malware/) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/optimizely-supply-chain-attack-delivers-malware-to-cnn-fox-news-bbc-salesforce-sites/) · [The Hacker News](https://thehackernews.com/2026/11/hijacked-optimizely-scripts-served-card.html) · [SecurityWeek](https://www.securityweek.com/optimizely-vulnerability-exploited-to-serve-malware-on-major-websites/) · [The Record](https://therecord.media/optimizely-malicious-code-customer-sites)

### 🔴 BO Team Exploits Log4Shell in VMware vCenter to Compromise Code-Signing Server
`exploited`

Threat actor BO Team used Log4Shell to breach VMware vCenter at a Russian software developer, resulting in a months-long compromise of its development infrastructure and code-signing server.

**Do:** Patch VMware vCenter against Log4Shell and audit development infrastructure for unauthorized access.

[The Hacker News](https://thehackernews.com/2026/11/bo-team-exploits-log4shell-in-vmware.html)

### 🔴 Barracuda Links Cloud Breach to ARTEX AI Framework and Stolen Key
`exploited`

Attackers who breached Barracuda's cloud environment used a stolen cloud access key combined with the ARTEX AI penetration testing framework.

**Do:** Rotate cloud access keys and audit access logs for automated AI framework activity.

[SecurityWeek](https://www.securityweek.com/barracuda-hacked-amid-surge-in-artex-powered-cyberattacks/) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/barracuda-links-cloud-breach-to-artex-ai-powered-cyberattack/)

### 🔴 Oracle WebLogic Server Unauthenticated Core RCE Vulnerability
`CVE-2026-91456 · CVSS 9.8`

Oracle WebLogic Server versions 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0, and 15.1.1.0.0 contain a critical unauthenticated RCE vulnerability (CVE-2026-91456) via SOAP.

**Do:** Apply the latest Oracle CPU patches for WebLogic Server.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91456)

### 🔴 Oracle WebLogic Server T3 and IIOP RCE Vulnerability
`CVE-2026-91470 · CVSS 9.8`

Oracle WebLogic Server versions 12.2.1.4.0 through 15.1.1.0.0 contain an unauthenticated RCE vulnerability (CVE-2026-91470) via T3 and IIOP protocols.

**Do:** Apply Oracle CPU patches and restrict T3/IIOP access.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91470)

### 🔴 Oracle WebLogic Server TopLink Integration RCE Vulnerability
`CVE-2026-91569 · CVSS 10.0`

Oracle WebLogic Server versions 12.2.1.4.0 to 15.1.1.0.0 are vulnerable to an unauthenticated RCE via TopLink Integration (CVE-2026-91569) with CVSS 10.0.

**Do:** Apply Oracle CPU patches immediately.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91569)

### 🟠 Japan RIKEN Fugaku Supercomputer Taken Offline After Cyberattack
`exploited`

Japan's Fugaku supercomputer operated by the RIKEN Center for Computational Science was taken offline following a security breach.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/japan-takes-fugaku-supercomputer-offlline-after-cyberattack/)

### 🟠 Copeland XWEB EVO Controllers Probed by Hackers Following Disclosures
`exploited`

Threat actors are actively probing newly disclosed vulnerabilities in Copeland XWEB EVO refrigeration controllers following disclosures by Vulncheck.

**Do:** Audit exposure of Copeland XWEB EVO controllers and apply vendor mitigations if available.

[SecurityWeek](https://www.securityweek.com/hackers-probe-newly-disclosed-flaws-in-copeland-refrigeration-controllers/)

### 🟠 BISHENG Hard-Coded JWT Secret Authentication Bypass
`CVE-2026-130840 · CVSS 9.8`

BISHENG before 3.0.0 contains an authentication bypass vulnerability (CVE-2026-130840) due to a hard-coded default JWT secret, allowing admin takeover.

**Do:** Upgrade BISHENG to version 3.0.0 or later.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130840)

### 🟠 Oracle Business Intelligence Enterprise Edition Takeover Flaw
`CVE-2026-114784 · CVSS 10.0`

Oracle Business Intelligence Enterprise Edition versions 8.2.0.0.0 and 26.01.0.0.0 contain an unauthenticated takeover vulnerability (CVE-2026-114784) with CVSS 10.0.

**Do:** Apply Oracle Critical Patch Update.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114784)

### 🟠 Oracle Platform Security for Java Takeover Vulnerability
`CVE-2026-114824 · CVSS 10.0`

Oracle Platform Security for Java versions 12.2.1.4.0 and 14.1.2.0.0 contain an unauthenticated remote takeover flaw (CVE-2026-114824) with CVSS 10.0.

**Do:** Apply Oracle Critical Patch Update.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114824)

### 🟠 Oracle Access Manager Admin Console Takeover Vulnerability
`CVE-2026-114835 · CVSS 10.0`

Oracle Access Manager versions 12.2.1.4.0 and 14.1.2.1.0 contain an unauthenticated takeover vulnerability (CVE-2026-114835) in the Admin Console with CVSS 10.0.

**Do:** Apply Oracle Critical Patch Update.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114835)

### 🟠 Oracle APEX Unauthenticated Takeover Vulnerability (CVE-2026-114849)
`CVE-2026-114849 · CVSS 9.8`

An easily exploitable vulnerability in Oracle APEX versions 24.1.22, 24.2.21, 26.1.5 and 26.2.0 allows unauthenticated attackers with HTTPS network access to achieve a complete system takeover.

**Do:** Apply the latest Oracle Critical Patch Update for Oracle APEX.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114849)

### 🟠 Oracle APEX Unauthenticated Takeover Vulnerability (CVE-2026-114850)
`CVE-2026-114850 · CVSS 9.8`

An easily exploitable vulnerability in Oracle APEX versions 24.1.22, 24.2.21, 26.1.5 and 26.2.0 allows unauthenticated attackers with HTTPS network access to achieve a complete system takeover.

**Do:** Apply the latest Oracle Critical Patch Update for Oracle APEX.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114850)

### 🟠 Oracle E-Business Suite Universal Work Queue RCE (CVE-2026-114863)
`CVE-2026-114863 · CVSS 9.8`

An unauthenticated remote takeover vulnerability affects Oracle E-Business Suite Universal Work Queue versions 12.2.3-12.2.15 via HTTP network access.

**Do:** Apply the latest Oracle Critical Patch Update for Oracle E-Business Suite.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114863)

### 🟠 Oracle E-Business Suite Document Management RCE (CVE-2026-114880)
`CVE-2026-114880 · CVSS 9.8`

An unauthenticated remote takeover vulnerability affects Oracle E-Business Suite Document Management and Collaboration versions 12.2.3-12.2.15.

**Do:** Apply the latest Oracle Critical Patch Update for Oracle E-Business Suite.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114880)

### 🟠 Oracle E-Business Suite Application Object Library RCE (CVE-2026-114924)
`CVE-2026-114924 · CVSS 9.8`

An unauthenticated remote takeover vulnerability affects Oracle E-Business Suite Application Object Library versions 12.2.3-12.2.15.

**Do:** Apply the latest Oracle Critical Patch Update for Oracle E-Business Suite.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114924)

### 🟠 Oracle E-Business Suite Applications Framework RCE (CVE-2026-114925)
`CVE-2026-114925 · CVSS 9.8`

An unauthenticated remote takeover vulnerability affects Oracle E-Business Suite Applications Framework versions 12.2.3-12.2.15 via REST Services.

**Do:** Apply the latest Oracle Critical Patch Update for Oracle E-Business Suite.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114925)

### 🟠 Oracle Hyperion Infrastructure Technology Takeover Vulnerability (CVE-2026-115047)
`CVE-2026-115047 · CVSS 9.8`

An unauthenticated remote takeover vulnerability affects Oracle Hyperion Infrastructure Technology version 11.2.26.0.000.

**Do:** Apply the latest Oracle Critical Patch Update for Hyperion.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-115047)

### 🟠 Oracle Hyperion Infrastructure Technology Takeover Vulnerability (CVE-2026-115048)
`CVE-2026-115048 · CVSS 9.8`

An unauthenticated remote takeover vulnerability affects Oracle Hyperion Infrastructure Technology version 11.2.26.0.000.

**Do:** Apply the latest Oracle Critical Patch Update for Hyperion.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-115048)

### 🟠 Oracle Hyperion Infrastructure Technology Takeover Vulnerability (CVE-2026-115080)
`CVE-2026-115080 · CVSS 9.8`

An unauthenticated remote takeover vulnerability affects Oracle Hyperion Infrastructure Technology version 11.2.26.0.000.

**Do:** Apply the latest Oracle Critical Patch Update for Hyperion.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-115080)

### 🟠 Oracle Hyperion Planning RMI Takeover Vulnerability (CVE-2026-115086)
`CVE-2026-115086 · CVSS 9.8`

An unauthenticated vulnerability via RMI allows remote takeover of Oracle Hyperion Planning version 11.2.26.0.000.

**Do:** Apply the latest Oracle Critical Patch Update for Hyperion.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-115086)

### 🟠 Oracle Hyperion Planning ADF Takeover Vulnerability (CVE-2026-115089)
`CVE-2026-115089 · CVSS 9.8`

An unauthenticated remote takeover vulnerability affects Oracle Hyperion Planning version 11.2.26.0.000 via Application Development Framework.

**Do:** Apply the latest Oracle Critical Patch Update for Hyperion.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-115089)

### 🟠 Oracle AutoVue Unauthenticated Takeover Vulnerability (CVE-2026-127324)
`CVE-2026-127324 · CVSS 9.8`

An unauthenticated remote takeover vulnerability affects Oracle AutoVue version 21.1.0 via HTTP.

**Do:** Apply the latest Oracle Critical Patch Update for Oracle AutoVue.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-127324)

### 🟠 Oracle AutoVue Unauthenticated Takeover Vulnerability (CVE-2026-127325)
`CVE-2026-127325 · CVSS 9.8`

An unauthenticated remote takeover vulnerability affects Oracle AutoVue version 21.1.0 via HTTP.

**Do:** Apply the latest Oracle Critical Patch Update for Oracle AutoVue.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-127325)

### 🟠 Oracle AutoVue Unauthenticated Takeover Vulnerability (CVE-2026-127326)
`CVE-2026-127326 · CVSS 9.8`

An unauthenticated remote takeover vulnerability affects Oracle AutoVue version 21.1.0 via HTTP.

**Do:** Apply the latest Oracle Critical Patch Update for Oracle AutoVue.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-127326)

### 🟠 Oracle AutoVue Unauthenticated Takeover Vulnerability (CVE-2026-127327)
`CVE-2026-127327 · CVSS 9.8`

An unauthenticated remote takeover vulnerability affects Oracle AutoVue version 21.1.0 via HTTP.

**Do:** Apply the latest Oracle Critical Patch Update for Oracle AutoVue.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-127327)

### 🟠 Oracle Access Manager Authentication Engine Vulnerability
`CVE-2026-91500 · CVSS 10.0`

A critical CVSS 10.0 vulnerability (CVE-2026-91500) in Oracle Access Manager versions 12.2.1.4.0 and 14.1.2.1.0 allows unauthenticated attackers to compromise the system via HTTP.

**Do:** Apply the latest security updates from Oracle.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91500)

### 🟠 Oracle Access Manager Authentication Engine Vulnerability
`CVE-2026-91510 · CVSS 10.0`

A critical CVSS 10.0 vulnerability (CVE-2026-91510) in Oracle Access Manager versions 12.2.1.4.0 and 14.1.2.1.0 allows unauthenticated network compromise via HTTP.

**Do:** Apply the latest security patches from Oracle.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91510)

### 🟠 NodePress Hardcoded JWT Secret Authentication Bypass Vulnerability
`CVE-2026-129952 · CVSS 9.8`

NodePress through 8.5.1 contains an authentication bypass via a hardcoded JWT fallback key ('nodepress-secret'), allowing unauthenticated attackers to forge administrator tokens.

**Do:** Upgrade NodePress beyond version 8.5.1.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129952)

### 🟠 NodePress Default Admin Password Authentication Bypass Vulnerability
`CVE-2026-129955 · CVSS 9.8`

NodePress through 8.5.1 contains an authentication bypass using a hardcoded default admin password when NP_ADMIN_DEFAULT_PASSWORD is unset.

**Do:** Upgrade NodePress and ensure default credentials are changed.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129955)

### 🟠 Ghost by muneeb141 OTP Verification Bypass Vulnerability
`CVE-2026-130070 · CVSS 9.3`

Ghost contains an authentication bypass in the convert_to_real_user method, allowing attackers to skip OTP verification by supplying the bypass_otp parameter and taking over accounts.

**Do:** Apply available patches from the repository.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130070)

### 🟠 TridotsTech go1cms Missing Authentication Privilege Escalation Vulnerability
`CVE-2026-130071 · CVSS 9.8`

TridotsTech go1cms contains a missing authentication flaw in update_doc, allowing unauthenticated attackers to modify user records and escalate privileges.

**Do:** Update go1cms to fixed commits.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130071)

### 🟠 Cloud Commander Path Traversal and Authentication Bypass Vulnerability
`CVE-2026-130072 · CVSS 9.1`

Cloud Commander (cloudcmd) before 19.21.4 contains an authentication bypass and path traversal vulnerability via PUT /rename requests, allowing unauthenticated file manipulation.

**Do:** Upgrade Cloud Commander to 19.21.4 or later.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130072)

### 🟠 Zyxel DX3301-T0/EX3301-T0 Out-of-Bounds Write Vulnerability
`CVE-2026-79614 · CVSS 9.8`

Zyxel DX3301-T0 and EX3301-T0 firmware through 5.50(ABVY.8.3)C0 contain an out-of-bounds write in libclinkc.so allowing unauthenticated attackers to elevate privileges via crafted HTTP requests.

**Do:** Upgrade Zyxel router firmware to patched versions.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79614)

### 🟠 Oracle PeopleSoft Enterprise PeopleTools WebLogic Component Flaw
`CVE-2026-114862 · CVSS 9.1`

Oracle PeopleSoft Enterprise PeopleTools versions 8.61-8.63 contain an unauthenticated vulnerability in the Weblogic component (CVE-2026-114862) allowing data modification.

**Do:** Apply Oracle Critical Patch Update for PeopleSoft.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114862)

### 🟠 Danfoss AK-SM800A Refrigeration Controllers Unpatched Remote Takeover Flaws

Six unpatched vulnerabilities in Danfoss AK-SM800A refrigeration controllers allow remote takeover without authentication, with no fix available in firmware version 5.4.0.

**Do:** Isolate Danfoss AK-SM800A controllers from the internet immediately.

[The Hacker News](https://thehackernews.com/2026/11/six-unpatched-danfoss-refrigeration.html)

### 🟠 Hugging Face Account Hijacked for Kokoro AI Model
`exploited`

Lack of ownership verification on Hugging Face allowed researchers to take control of the Kokoro text-to-speech model used across major tech platforms.

**Do:** Verify model provenance and monitor dependencies for unauthorized modifications.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/researchers-hijack-hugging-face-account-for-popular-kokoro-ai-model/)

### 🟠 Tor Releases Emergency Update Amid Ongoing DDoS Attack
`exploited`

The Tor Project released a security update for its network relay software to defend against an ongoing distributed denial-of-service attack overwhelming relays.

**Do:** Update Tor relay software to the latest version.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/tor-releases-emergency-update-amid-ongoing-ddos-attack/)

### 🟠 Google Warns Chinese State Group Developing AI Attack Tools

Google reported that threat actors are increasingly using autonomous multi-agent offensive frameworks like Artex and PentAGI to execute multi-stage intrusions.

[SecurityWeek](https://www.securityweek.com/ai-framework-autonomously-weaponized-flaws-in-real-attacks-google-says/) · [The Record](https://therecord.media/chinese-state-group-developing-automated-attack-tool-espionage)

### 🟠 NSA Classified Internal Network Faces Unspecified Disruptions
`exploited`

The NSA reported disruptions to its classified internal network NSA Net, leading to staggered arrivals at its headquarters.

[The Record](https://therecord.media/nsa-net-disruptions) · [SecurityWeek](https://www.securityweek.com/classified-communications-network-at-the-national-security-agency-goes-down-defense-official-says/)

### 🟠 Access Dental Management Discloses Data Breach Impacting 340,000
`exploited`

Hackers breached Access Dental's network and stole personal, health, and insurance information affecting over 340,000 individuals.

**Do:** Monitor affected systems and provide notifications as required by regulatory frameworks.

[SecurityWeek](https://www.securityweek.com/access-dental-management-data-breach-impacts-over-340000/)

### 🟠 Rootways Authorize.net CIM Pro for Magento 2 SSRF Flaw
`CVE-2026-130583 · CVSS 9.3`

Rootways Authorize.net CIM Pro extension for Magento 2 before 4.1.5 contains an unauthenticated SSRF vulnerability (CVE-2026-130583) allowing credential theft.

**Do:** Upgrade Rootways Authorize.net CIM Pro extension to version 4.1.5 or later.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130583)

### 🟠 BZFlag bzfs Heap Out-of-Bounds Write Vulnerability
`CVE-2026-130849 · CVSS 9.8`

BZFlag bzfs before 2.4.32 contains a heap out-of-bounds write vulnerability (CVE-2026-130849) allowing remote unauthenticated code execution.

**Do:** Upgrade BZFlag bzfs to version 2.4.32 or later.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130849)

### 🟠 53AIHub Missing Authentication Account Takeover Flaw
`CVE-2026-130856 · CVSS 9.8`

53AIHub before 0.5.5 contains a missing authentication vulnerability (CVE-2026-130856) in the initialization endpoint allowing account takeover.

**Do:** Upgrade 53AIHub to version 0.5.5 or later.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-130856)

### 🟠 Oracle Database Server Oracle Text Takeover Vulnerability (CVE-2026-114848)
`CVE-2026-114848 · CVSS 9.9`

A vulnerability in the Oracle Text component of Oracle Database Server versions 19.3-19.33, 21.3-21.24 and 23.4.0-23.26.3 allows low-privileged attackers with network access via Oracle Net to compromise the component.

**Do:** Apply the latest Oracle Critical Patch Update to affected Database Server installations.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114848)

### 🟠 Oracle REST Data Services Takeover Vulnerability (CVE-2026-114856)
`CVE-2026-114856 · CVSS 9.6`

A vulnerability in Oracle REST Data Services versions 24.2.0-26.3.0 allows unauthenticated attackers with HTTPS access to compromise the product, requiring user interaction.

**Do:** Apply the latest Oracle Critical Patch Update for Oracle REST Data Services.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114856)

### 🟠 Oracle E-Business Suite Document Management DoS (CVE-2026-114881)
`CVE-2026-114881 · CVSS 9.1`

An unauthenticated vulnerability in Oracle E-Business Suite Document Management and Collaboration versions 12.2.3-12.2.15 allows unauthorized data access and denial of service.

**Do:** Apply the latest Oracle Critical Patch Update for Oracle E-Business Suite.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114881)

### 🟠 Oracle PeopleSoft Enterprise PeopleTools Vulnerability (CVE-2026-114934)
`CVE-2026-114934 · CVSS 9.3`

An unauthenticated vulnerability in Oracle PeopleSoft Enterprise PeopleTools versions 8.61-8.63 allows unauthorized data access or complete system disruption.

**Do:** Apply the latest Oracle Critical Patch Update for PeopleSoft.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114934)

### 🟠 Oracle MySQL Server Client Programs Vulnerability (CVE-2026-114952)
`CVE-2026-114952 · CVSS 9.1`

An unauthenticated vulnerability affects MySQL Server versions 8.4.0-8.4.13, 9.7.0-9.7.4, 26.10, and MySQL Cluster versions 8.0.0-8.0.50, 8.4.0-8.4.13, 9.7.0-9.7.4, 26.10, allowing unauthorized data manipulation.

**Do:** Apply the latest Oracle Critical Patch Update for MySQL.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114952)

### 🟠 Oracle Hyperion Planning Security Vulnerability (CVE-2026-114956)
`CVE-2026-114956 · CVSS 9.3`

An unauthenticated vulnerability with required user interaction affects Oracle Hyperion Planning version 11.2.26.0.000.

**Do:** Apply the latest Oracle Critical Patch Update for Hyperion.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114956)

### 🟠 Oracle Hyperion Financial Management Takeover Vulnerability (CVE-2026-114978)
`CVE-2026-114978 · CVSS 9.9`

A vulnerability in Oracle Hyperion Financial Management version 11.2.26.0.000 allows low-privileged attackers with network access to achieve a takeover.

**Do:** Apply the latest Oracle Critical Patch Update for Hyperion.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114978)

### 🟠 Oracle AutoVue Security Takeover Vulnerability (CVE-2026-114980)
`CVE-2026-114980 · CVSS 9.9`

A vulnerability in Oracle AutoVue version 21.1.0 allows low-privileged attackers with network access to take over the component.

**Do:** Apply the latest Oracle Critical Patch Update for Oracle AutoVue.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114980)

### 🟠 Oracle Hyperion Infrastructure Technology Vulnerability (CVE-2026-115050)
`CVE-2026-115050 · CVSS 9.1`

An unauthenticated vulnerability in Oracle Hyperion Infrastructure Technology version 11.2.26.0.000 allows unauthorized data creation, deletion, or modification.

**Do:** Apply the latest Oracle Critical Patch Update for Hyperion.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-115050)

### 🟠 Oracle Hyperion Infrastructure Technology Vulnerability (CVE-2026-115139)
`CVE-2026-115139 · CVSS 9.3`

An unauthenticated vulnerability requiring user interaction affects Oracle Hyperion Infrastructure Technology version 11.2.26.0.000.

**Do:** Apply the latest Oracle Critical Patch Update for Hyperion.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-115139)

### 🟠 Oracle Hyperion Financial Close Management Unauth. Vulnerability
`CVE-2026-127362 · CVSS 9.1`

An easily exploitable unauthenticated vulnerability (CVE-2026-127362) in Oracle Hyperion Financial Close Management version 11.2.26.0.000 allows network compromise via HTTP.

**Do:** Apply the latest security patches provided by Oracle.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-127362)

### 🟠 Oracle Hyperion Financial Close Management Net Vulnerability
`CVE-2026-127369 · CVSS 9.1`

An easily exploitable unauthenticated vulnerability (CVE-2026-127369) in Oracle Hyperion Financial Close Management version 11.2.26.0.000 allows network compromise via Oracle Net.

**Do:** Apply the latest security patches provided by Oracle.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-127369)

### 🟠 Oracle Access Manager Authentication Engine Vulnerability
`CVE-2026-91507 · CVSS 9.3`

A vulnerability (CVE-2026-91507) in Oracle Access Manager versions 12.2.1.4.0 and 14.1.2.1.0 allows unauthenticated attackers to compromise the system via HTTP.

**Do:** Apply the latest security patches from Oracle.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91507)

### 🟠 Oracle Service Bus Core RMI Vulnerability
`CVE-2026-91561 · CVSS 9.6`

A vulnerability (CVE-2026-91561) in Oracle Service Bus versions 12.2.1.4.0 and 14.1.2.0.0 allows low-privileged attackers with network access via RMI to compromise the system.

**Do:** Apply the latest security patches from Oracle.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91561)

### 🟠 Oracle ADF Security Framework Vulnerability
`CVE-2026-91618 · CVSS 9.1`

An easily exploitable vulnerability (CVE-2026-91618) in Oracle Application Development Framework version 12.2.1.4.0 allows unauthenticated network compromise via HTTP.

**Do:** Apply the latest security patches from Oracle.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-91618)

### 🟠 Phoenix Format String Injection in applyChatTemplate
`CVE-2026-53998 · CVSS 10.0 · EPSS 0.00`

A format string injection vulnerability (CVE-2026-53998) in the applyChatTemplate GraphQL endpoint of arize-phoenix allows unauthenticated or low-privileged attackers to read server-side environment variables and secrets.

**Do:** Upgrade arize-phoenix to a patched version and ensure authentication is enabled.

[GitHub Advisory](https://github.com/advisories/GHSA-gfv3-m769-5xm3)

### 🟠 Uber Third-Party Breach Exposes Data of 150,000 People
`exploited`

Hackers compromised a third-party service provider using stolen internal credentials, accessing Uber data including names, addresses, and driver's license numbers for nearly 150,000 individuals.

[SecurityWeek](https://www.securityweek.com/uber-data-breach-impacts-150000-people/) · [The Record](https://therecord.media/uber-says-150000-impacted-third-party-breach) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/uber-notifies-drivers-of-data-breach-affecting-nearly-150-000-people/)

### 🟠 Researchers Claim RCE Exploits Bypass Telegram Android Defenses

Security researchers claim malicious chat widgets can bypass Telegram's Android security filters and execute code outside the sandbox.

**Do:** Update Telegram to the latest version once patches are available.

[The Hacker News](https://thehackernews.com/2026/11/researchers-claim-two-rce-exploits-that.html)

### 🟠 Siemens meta-iot2050 Firmware Update Command Injection
`CVE-2026-109830 · EPSS 0.00`

Siemens meta-iot2050 from version V01.03.01 contains a command injection vulnerability in the firmware update tool allowing root execution via manipulated configuration files.

**Do:** Apply vendor mitigations and prepare fixes for Siemens meta-iot2050.

[CISA Advisories](https://www.cisa.gov/news-events/ics-advisories/icsa-26-321-11)

### 🟠 NoisyTCP 11-Year-Old Linux Kernel Vulnerability Impacts Servers

An 11-year-old Linux kernel vulnerability dubbed NoisyTCP affects most distributions and allows attackers to crash servers running Nginx, Apache, and SSH with default configurations.

**Do:** Apply Linux kernel security updates when available.

[BleepingComputer](https://www.bleepingcomputer.com/news/linux/new-noisytcp-linux-kernel-flaw-lets-attackers-crash-servers/)

### 🟠 Market Research Giant Ipsos Investigates Internal System Breach
`exploited`

Ipsos disclosed it is investigating a breach of its internal system after filing a complaint with authorities.

[SecurityWeek](https://www.securityweek.com/market-research-giant-ipsos-investigating-breach-of-internal-system/)

### 🟠 Fandango Media Discloses Payment Card Data Breach on Checkout Pages
`exploited`

Fandango Media is notifying customers of a breach that exposed payment card details entered on checkout pages.

**Do:** Monitor payment cards used on affected checkout pages for fraudulent activity.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/fandango-says-hackers-stole-payment-card-details-from-checkout-pages/) · [SecurityWeek](https://www.securityweek.com/fandango-warns-ticket-buyers-of-payment-card-data-exposure/)

### 🟠 Siemens ROS# Code Injection Vulnerability
`CVE-2026-109097 · EPSS 0.00`

Siemens ROS# before version 2.3.1 contains a code injection vulnerability allowing arbitrary code execution via crafted message definition files. Patches are available.

**Do:** Update Siemens ROS# to version 2.3.1 or later.

[CISA Advisories](https://www.cisa.gov/news-events/ics-advisories/icsa-26-321-06)

### 🟠 Dorsett Controls InfoScan Multiple Vulnerabilities
`CVE-2026-117659, CVE-2026-120157, CVE-2026-120255, CVE-2026-120260 …`

Dorsett Controls InfoScan <=1.45.0 contains multiple vulnerabilities allowing sensitive information disclosure, unauthorized data access, credential recovery, and network traffic manipulation.

**Do:** Review vendor advisories and apply updates or mitigations for Dorsett Controls InfoScan.

[CISA Advisories](https://www.cisa.gov/news-events/ics-advisories/icsa-26-321-01)

### 🟠 Siemens Mendix Studio Pro MCP Server Vulnerabilities
`CVE-2026-112136, CVE-2026-112137 · EPSS 0.00`

Siemens Mendix Studio Pro 11 versions 11.15.0 up to 11.16.0 contain vulnerabilities in the MCP Server allowing unauthorized data access and system compromise.

**Do:** Update Siemens Mendix Studio Pro to the latest version.

[CISA Advisories](https://www.cisa.gov/news-events/ics-advisories/icsa-26-321-05)

### 🟠 Siemens SIMATIC and .NET Client Library Vulnerabilities
`CVE-2026-58114, CVE-2026-59082, CVE-2026-85114, CVE-2026-85115 · EPSS 0.00`

Siemens SIMATIC components and .NET Client Library for SIMATIC S7 Webserver API contain authentication bypass, file write, and active content execution flaws.

**Do:** Apply available Siemens updates and recommended security mitigations for SIMATIC and S7 APIs.

[CISA Advisories](https://www.cisa.gov/news-events/ics-advisories/icsa-26-321-02) · [CISA Advisories](https://www.cisa.gov/news-events/ics-advisories/icsa-26-321-08) · [CISA Advisories](https://www.cisa.gov/news-events/ics-advisories/icsa-26-321-09)

### 🟠 Siemens Simcenter Femap Out-of-Bounds Read Vulnerability
`CVE-2026-64629 · EPSS 0.00`

Siemens Simcenter Femap before version 2606.0002 contains an out-of-bounds read vulnerability triggered when parsing X_T files, leading to application crashes or code execution.

**Do:** Update Siemens Simcenter Femap to version 2606.0002 or later.

[CISA Advisories](https://www.cisa.gov/news-events/ics-advisories/icsa-26-321-10)

### 🟠 Australian Retailer Coles Investigates Cybersecurity Incident

Coles Group Limited is investigating a cyber security incident, though in-store operations remain unaffected.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/australian-retail-giant-coles-investigates-cybersecurity-incident/)

## 2026-11-16

### 🟠 Autonomous AI Agent Attacks Target LiteLLM and Dify Deployments to Steal API Keys
`exploited`

Attackers are deploying autonomous AI agents to scan and exploit internet-exposed AI applications like LiteLLM, One API, and Dify to steal AI provider API keys. Stolen API keys are reportedly being fed back to power the automated agents conducting further scans.

**Do:** Ensure LiteLLM, Dify, and One API deployments are not exposed to the public internet without authentication.

[The Hacker News](https://thehackernews.com/2026/11/amazon-uncovers-ai-agent-campaign.html)

## 2026-11-15

### 🟠 Cyrus SASL Authentication Bypass in SRP Server Mechanism
`CVE-2026-129483 · CVSS 9.3`

Cyrus SASL through 2.1.28 contains an authentication bypass vulnerability in the SRP server mechanism due to improper validation of client public values. Unauthenticated attackers can authenticate as any user and learn session keys.

**Do:** Check vendor advisories and apply available patches for Cyrus SASL.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129483)

### 🟠 FBI Warns ARTEX AI Tool Used in Global Cyberattacks
`exploited`

The FBI warned that threat actors are using the ARTEX AI penetration testing framework to automate global attacks, including a ConnectWise supply-chain breach impacting Microsoft 365 environments.

**Do:** Review ConnectWise and Microsoft 365 environments for unauthorized access and monitor for ARTEX indicators.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/fbi-warns-artex-ai-hacking-tool-is-powering-global-cyberattacks/)

### 🟠 DrayTek Vigor2960 mainfunction.cgi Command Injection
`CVE-2026-129449, CVE-2026-129452 · CVSS 9.9`

DrayTek Vigor2960 up to version 1.5.1.6 contains an OS command injection vulnerability in mainfunction.cgi via the swmconfigupload argument. An updated version 1.5.1.7 is available.

**Do:** Upgrade DrayTek Vigor2960 to version 1.5.1.7 or later.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129449) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129452)

## 2026-11-14

### 🟠 Cursor Confirms Breach and Malicious Claude Code Extension
`exploited`

Cursor suffered a security breach resulting in the distribution of a malicious Claude Code extension through its marketplace following credential theft from Fireworks AI.

**Do:** Audit and remove unauthorized Claude Code extensions from Cursor.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/cursor-confirms-security-breach-led-to-malicious-claude-code-extension/) · [The Hacker News](https://thehackernews.com/2026/11/stolen-fireworks-ai-key-led-to-cursor.html)

### 🟠 Dokploy getComposeContainerCommand OS Command Injection (CVE-2026-129433)
`CVE-2026-129433 · CVSS 9.9`

Dokploy before 0.31.1 contains an OS command injection vulnerability in getComposeContainerCommand() that allows authenticated organization members to execute shell commands via the serviceName parameter, potentially taking over the host.

**Do:** Upgrade Dokploy to 0.31.1 or later.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-129433)

