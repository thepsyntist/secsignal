# Security signal: last 7 days

🔴 act now · 🟠 worth knowing

## 2026-11-19

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

### 🟠 NGINX HTTP/2 Remote Code Execution Vulnerability (CVE-2026-123007)
`CVE-2026-123007`

A vulnerability in NGINX's HTTP/2 support (CVE-2026-123007), present since version 1.9.5, allows unauthenticated attackers to execute code on servers with HTTP/2 enabled. Fixed in versions 1.31.9 and 1.30.7.

**Do:** Upgrade NGINX to version 1.30.7, 1.31.9, or later.

[The Hacker News](https://thehackernews.com/2026/11/10-year-old-nginx-http2-flaw-lets.html)

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

### 🟠 F5 Warns of Critical BIG-IP Traffic Management Flaws

Six critical vulnerabilities in F5 BIG-IP allow unauthenticated attackers to crash the Traffic Management Microkernel (TMM) or potentially achieve RCE under specific iRule or APM setups.

**Do:** Review F5 advisory and apply recommended hotfixes or configuration workarounds.

[The Hacker News](https://thehackernews.com/2026/11/f5-warns-6-critical-big-ip-flaws-can.html)

### 🟠 Data Breach Impacts Irish Credit Unions in Wellington IT Hack
`exploited`

A reported cyberattack on Wellington IT exposed sensitive information belonging to members of multiple credit unions in Ireland.

**Do:** Review Wellington IT advisory and monitor credit union accounts.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/data-breach-impacts-40-irish-credit-unions-in-reported-it-provider-hack/)

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

### 🟠 CISA Adds Four Known Exploited Vulnerabilities to Catalog
`CVE-2024-10441, CVE-2026-40217, CVE-2026-90436, CVE-2026-90817 · EPSS 0.17 · CISA KEV`



[CISA Advisories](https://www.cisa.gov/news-events/alerts/2026/11/18/cisa-adds-four-known-exploited-vulnerabilities-catalog)

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

[BleepingComputer](https://www.bleepingcomputer.com/news/security/critical-java4shell-flaw-allows-rce-attacks-on-major-java-applications/)

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

### 🟠 Apache warns of Roller RCE vulnerability exploited in attacks
`CVE-2026-129448 · exploited`

Apache has released security updates to address a critical Roller flaw that threat actors are exploiting to gain code execution on vulnerable servers. [...]

[BleepingComputer](https://www.bleepingcomputer.com/news/security/apache-warns-of-roller-rce-vulnerability-exploited-in-attacks/) · [The Hacker News](https://thehackernews.com/2026/11/critical-apache-roller-rce-flaw-under.html)

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

## 2026-11-13

### 🔴 Now exploited: Check Point Gateways PHP2Shell and Gaia OS Privilege Escalation Exploited
`CVE-2026-114713, CVE-2026-123039 · CISA KEV`

Attackers are actively exploiting PHP2Shell and a local privilege escalation flaw (CVE-2026-123039) in Check Point Security Gateways to achieve root access, deploy the TSGA backdoor, and wipe ESXi files.

**Do:** Apply available patches for Check Point Security Gateways immediately and audit for indicators of compromise.

[SecurityWeek](https://www.securityweek.com/php2shell-exploited-in-destructive-check-point-gateway-attacks/) · [The Hacker News](https://thehackernews.com/2026/11/hackers-exploit-php2shell-flaws-in.html) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/check-point-patches-zero-day-that-lets-hackers-get-root-access/) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/check-point-gateways-hacked-via-php2shell-to-deploy-vmware-esxi-wiper/) · [CISA Advisories](https://www.cisa.gov/news-events/alerts/2026/11/13/cisa-adds-two-known-exploited-vulnerabilities-catalog) · [CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-114713) · [CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-123039) · [The Hacker News](https://thehackernews.com/2026/11/attackers-exploit-unrealircd-flaw-that.html) · [SecurityWeek](https://www.securityweek.com/recent-unrealircd-vulnerability-exploited-in-attacks/)

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

[The Record](https://therecord.media/tsmc-confirms-employee-data-breach-cloud-provider) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/tsmc-employee-data-breach-linked-to-cloud-provider/)

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

