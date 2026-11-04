# Security signal: last 7 days

🔴 act now · 🟠 worth knowing

## 2026-11-04

### 🔴 Google Patches Critical Remote Code Execution Flaw in Android
`CVE-2026-58868 · EPSS 0.00`

A critical zero-click RCE flaw, CVE-2026-58868, affects Android 14 through 17. Fixed in the 2026-11-01 security patch level.

**Do:** Apply Android security patch level 2026-11-01 or later.

[The Hacker News](https://thehackernews.com/2026/11/google-patches-critical-android-flaw.html)

### 🟠 Hackers Use N-Day Exploits in Zero-Click Attacks on iOS and Android
`exploited`

A watering hole campaign associated with Russian hackers targets iOS and Android users with n-day exploits.

**Do:** Ensure mobile devices are fully updated and monitor web traffic for suspicious redirects.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/hackers-use-n-day-exploits-in-zero-click-attacks-on-ios-android-devices/)

### 🟠 Ruby on Rails Active Storage Flaw Allows Arbitrary File Write

A critical flaw in Ruby on Rails Active Storage lets unauthenticated attackers write server files via ImageMagick uploads. Fixed in versions 8.1.4.1 and 8.0.5.2.

**Do:** Upgrade Ruby on Rails to versions 8.1.4.1 or 8.0.5.2.

[The Hacker News](https://thehackernews.com/2026/11/critical-rails-flaw-lets-attackers.html)

### 🟠 Xen Hypervisor Flaws Allow Inter-VM Memory Access

Two flaws in Xen hypervisor versions 4.6 onward allow a malicious guest VM to read and write memory of other VMs, including dom0. Patches are available.

**Do:** Apply Xen hypervisor patches.

[The Hacker News](https://thehackernews.com/2026/11/xen-hypervisor-flaws-let-one-malicious.html)

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

## 2026-11-03

### 🔴 WordPress Core TOCTOU Race Condition Vulnerability Added to KEV
`CVE-2026-119977 · EPSS 0.01 · CISA KEV`

CISA added a time-of-check time-of-use (TOCTOU) race condition vulnerability in WordPress Core (CVE-2026-119977) to its Known Exploited Vulnerabilities catalog, which could allow unauthenticated attackers to execute code during the upgrade window.

**Do:** Apply WordPress security updates and mitigations in accordance with vendor and CISA guidance.

[CISA Advisories](https://www.cisa.gov/news-events/alerts/2026/11/03/cisa-adds-one-known-exploited-vulnerability-catalog) · [CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-119977) · [The Hacker News](https://thehackernews.com/2026/11/cisa-confirms-hackers-exploiting.html) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/cisa-flags-wordpress-rce-flaw-as-actively-exploited-in-attacks/)

### 🔴 Siemens SIMATIC IoT2050 Advanced Missing Auth Flaw Exploited
`CVE-2026-58115 · EPSS 0.01 · exploited`

A critical missing authentication vulnerability (CVE-2026-58115, CVSS 10.0) in Siemens SIMATIC IoT2050 Advanced devices is under active exploitation to plant remote command backdoors.

**Do:** Apply available security updates from Siemens immediately.

[The Hacker News](https://thehackernews.com/2026/11/attackers-exploit-critical-siemens.html)

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

### 🟠 CryptoPayment Gateway WordPress Plugin Flaw Under Attack
`CVE-2026-81648 · EPSS 0.00 · exploited`

An unpatched maximum-severity vulnerability (CVE-2026-81648, CVSS 10.0) in the CryptoPayment Gateway WordPress plugin is being targeted by attackers to delete arbitrary files and extract wallet credentials.

**Do:** Disable or remove the CryptoPayment Gateway WordPress plugin until a patch is available.

[The Hacker News](https://thehackernews.com/2026/11/attackers-target-unpatched.html)

### 🟠 Barracuda Warns of Critical Root Command Injection Vulnerabilities
`CVE-2026-116606`

Barracuda Networks warned customers to patch two vulnerabilities that allow attackers to run commands with root privileges on affected devices.

**Do:** Apply the latest security patches provided by Barracuda immediately.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/barracuda-warns-of-critical-flaws-allowing-root-access-to-devices/) · [The Hacker News](https://thehackernews.com/2026/11/barracuda-flaws-could-be-chained-to.html)

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

[BleepingComputer](https://www.bleepingcomputer.com/news/security/workos-says-attacker-used-artex-ai-to-breach-internal-sales-app/)

### 🟠 Google Reports LLMjacking Attacks Generating High Cloud Charges
`exploited`

Large language model hijacking (LLMjacking) attacks are generating massive fraudulent cloud charges, with some organizations losing over $100,000 per day.

**Do:** Audit cloud AI resource consumption and implement strict billing alerts and access controls.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/google-llmjacking-attacks-rack-up-1-million-in-cloud-ai-charges/)

### 🟠 mSecure Urges Password and 2FA Resets After Suspicious Activity
`exploited`

Password manager mSecure urged users to reset passwords, 2FA, and passkeys following suspicious activity detected on its systems.

**Do:** Reset master passwords and multi-factor authentication for mSecure accounts.

[The Hacker News](https://thehackernews.com/2026/11/msecure-warns-users-to-change-passwords.html)

### 🟠 Russia-Linked Spies Target Ukrainian Investigations and Military Routes
`exploited`

Russia-linked threat actors are using simple malware to steal sensitive documents and credentials from Ukrainian organizations near the front line.

[The Record](https://therecord.media/russia-linked-cyber-spies-target-ukraine-war-support)

### 🟠 Russia-Aligned Gorbag Hackers Exploit WinRAR Flaw Against Ukraine
`exploited`

Gorbag threat actors have been observed exploiting WinRAR vulnerabilities to deploy info-stealer malware against Ukrainian defense and law enforcement targets.

[The Hacker News](https://thehackernews.com/2026/11/russia-aligned-gorbag-hackers-exploit.html)

## 2026-11-02

### 🔴 GitLab Active RCE Attacks Targeting Unpatched Servers
`exploited`

Over 1,000 internet-exposed GitLab servers remain unpatched and vulnerable to ongoing remote code execution attacks.

**Do:** Upgrade GitLab installations immediately to the latest patched version.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/over-1-000-gitlab-servers-vulnerable-to-code-execution-attacks/)

### 🟠 Google Disrupts 1.3M Device Android TV Box Botnet
`exploited`

Google disrupted the 1.3 million-device XCPE Android botnet, consisting largely of set-top boxes manufactured by Videostrong with intentional manufacturer-installed backdoors.

**Do:** Audit network for unverified Android set-top boxes and streaming devices acting as proxies.

[The Hacker News](https://thehackernews.com/2026/11/google-disrupts-13-million-device.html) · [The Hacker News](https://thehackernews.com/2026/11/weekly-recap-critical-cves-linux-ddos.html) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/google-disrupts-million-device-xcpe-android-malware-botnet-bans-tv-box-maker/) · [Krebs on Security](https://krebsonsecurity.com/2026/11/tech-firms-dismantle-botnet-that-turned-1-3m-tv-boxes-into-proxies/) · [SecurityWeek](https://www.securityweek.com/google-dismantles-xcpe-botnet-of-1-3-million-android-devices/) · [Ars Technica](https://arstechnica.com/google/2026/11/google-dismantles-botnet-secretly-running-on-1-3-million-android-tv-boxes/) · [The Record](https://therecord.media/google-dismantles-botnet-hidden-android-tv-boxes)

### 🟠 FBI Blames North Korea for $6.3B Binance Theft
`exploited`

The FBI and U.S. Secret Service attributed the $6.3 billion cryptocurrency theft from Binance to North Korean hackers and flagged over 600 addresses.

**Do:** Block transactions associated with the flagged cryptocurrency addresses.

[The Record](https://therecord.media/fbi-blames-tradertraitor-for-binance-hack) · [SecurityWeek](https://www.securityweek.com/fbi-flags-over-600-addresses-tied-to-north-koreas-binance-heist/) · [The Record](https://therecord.media/binance-cryptocurrency-theft-months-long-campaign-nkorea) · [The Hacker News](https://thehackernews.com/2026/11/binance-reveals-how-fake-job-interviews.html) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/binance-says-fake-job-interview-led-to-63-billion-crypto-heist/) · [SecurityWeek](https://www.securityweek.com/rigged-coding-assignment-abused-ai-tool-opened-path-to-6-billion-binance-heist/)

### 🟠 Cyberattack Dispatches European Supermarket Refrigeration
`exploited`

A cyberattack disrupted refrigeration systems across European supermarket chains after hackers remotely altered temperature settings on cooling units.

[The Record](https://therecord.media/cyberattack-grocery-freezers-europe) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/hackers-disrupt-refrigeration-systems-at-european-supermarkets/) · [SecurityWeek](https://www.securityweek.com/over-100-european-stores-hit-as-supermarket-fridge-attacks-resume/) · [The Hacker News](https://thehackernews.com/2026/11/second-wave-of-cyberattacks-hits.html) · [The Record](https://therecord.media/british-businesses-caught-in-europe-wide-supermarket-fridge-attacks)

### 🟠 Mercado Bitcoin Confirms Cyberattack and Fund Outflows
`exploited`

Brazil's largest crypto exchange, Mercado Bitcoin, confirmed a cyberattack after blockchain security firms noted over $46 million leaving the platform.

[The Record](https://therecord.media/mercado-bitcoin-brazil-cryptocurrency-heist)

### 🟠 BTCPay Server Hot Wallet Crypto Thefts
`exploited`

Maintainers of BTCPay Server warned users that hackers have been draining hot wallets on instances running outdated versions.

**Do:** Update BTCPay Server to the latest version immediately.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/btcpay-server-warns-of-hot-wallet-thefts-targeting-outdated-instances/) · [The Hacker News](https://thehackernews.com/2026/11/hackers-exploit-btcpay-server-flaw-to.html)

### 🟠 Synology Warns of C3RB3R Ransomware NAS Attacks
`exploited`

Synology warned customers to update NAS devices immediately due to a surge in active C3RB3r ransomware attacks.

**Do:** Update Synology NAS devices immediately.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/synology-warns-customers-of-ongoing-c3rb3r-ransomware-attacks/) · [The Hacker News](https://thehackernews.com/2026/11/synology-nas-devices-targeted-in.html)

### 🟠 Malicious Claude Code Extension in Cursor Supply Chain
`exploited`

A malicious Claude Code extension served in a Cursor supply chain attack performed host reconnaissance and attempted a reverse SSH tunnel.

**Do:** Audit Cursor extensions for unauthorized or malicious components.

[SecurityWeek](https://www.securityweek.com/malicious-claude-code-extension-served-in-cursor-supply-chain-attack/)

### 🟠 Teams Impersonation and AD CS Certificate Abuse
`exploited`

Attackers posing as IT support on Microsoft Teams tricked employees into granting remote access, then abused AD CS settings to steal privileged certificates.

**Do:** Audit Active Directory Certificate Services (AD CS) configurations and enforce phishing-resistant MFA.

[The Hacker News](https://thehackernews.com/2026/11/attackers-pose-as-it-support-on.html)

### 🟠 Control Web Panel OS Command Injection Flaw
`CVE-2026-77876 · CVSS 9.8`

Control Web Panel (CWP) before version 1.16 contains an OS command injection vulnerability in the protected_directory module allowing arbitrary command execution.

**Do:** Upgrade Control Web Panel to version 1.16 or later.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-77876)

### 🟠 WAVLINK WN536AX6-A Web Management Interface Command Injection
`CVE-2026-120276 · CVSS 10.0`

An OS command injection vulnerability exists in the web management interface of WAVLINK WN536AX6-A V260507_2.0.0 via the group_name argument. A public exploit is available.

**Do:** Apply available vendor patches or restrict access to the web management interface.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120276)

### 🟠 WAVLINK WN536AX6-A WireGuard CLI Command Injection
`CVE-2026-120277 · CVSS 10.0`

An OS command injection vulnerability affects the WireGuard CLI component in WAVLINK WN536AX6-A V260507_2.0.0 via the group_name argument. A public exploit exists.

**Do:** Apply patches provided by WAVLINK and restrict management access.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120277)

### 🟠 WAVLINK WN536AX6-A OpenVPN Handler Command Injection
`CVE-2026-120279 · CVSS 10.0`

An OS command injection vulnerability exists in the openvpn_cli handler of WAVLINK WN536AX6-A V260507 via the file_id argument. A public exploit is available.

**Do:** Update to patched firmware or disable vulnerable protocol handlers.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120279)

### 🟠 WAVLINK WN536AX6-A WireGuard Component Command Injection
`CVE-2026-120280 · CVSS 10.0`

An OS command injection vulnerability impacts the WireGuard component in WAVLINK WN536AX6-A V260507 via group_id or group_name arguments. A public exploit has been disclosed.

**Do:** Apply available vendor updates.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120280)

### 🟠 WAVLINK WN536AX6-A OpenVPN Handler Buffer Overflow
`CVE-2026-120281 · CVSS 10.0`

A stack-based buffer overflow vulnerability exists in the OpenVPN handler of WAVLINK WN536AX6-A V260507 via the openvpn_ip argument. A public exploit is available.

**Do:** Upgrade to patched firmware versions.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120281)

### 🟠 WAVLINK WN536AX6-A Host Blacklist Command Injection
`CVE-2026-120282 · CVSS 9.9`

An OS command injection vulnerability affects the host_black function in WAVLINK WN536AX6-A V260507 via the mac argument. A public exploit has been released.

**Do:** Apply vendor patches.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120282)

### 🟠 Termix-SSH File Manager Path Traversal Vulnerability
`CVE-2026-120322 · CVSS 9.9`

A path traversal vulnerability exists in Termix-SSH Termix up to 2.9.2 via the destPath argument in the file transfer plugin. A public exploit is available.

**Do:** Update Termix to core v26.10.0 or standalone File Manager plugin v1.0.0+.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120322)

### 🟠 WAVLINK WN551X3-A WireGuard CLI Command Injection
`CVE-2026-120344 · CVSS 10.0`

An OS command injection vulnerability affects the WireGuard CLI handler in WAVLINK WN551X3-A M51X3_V251020-WO-182e965 via the group_name argument. A public exploit is available.

**Do:** Apply vendor firmware updates.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120344)

### 🟠 WAVLINK WN551X3-A DNS Resolution Handler Command Injection
`CVE-2026-120345 · CVSS 10.0`

An OS command injection vulnerability exists in the DNS Resolution Handler of WAVLINK WN551X3-A M51X3_V251020-WO-182e965 via the data argument. A public exploit is available.

**Do:** Upgrade to patched firmware.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120345)

### 🟠 Fintech Platform Sageworks Taken Offline After Attack
`exploited`

Financial technology company Abrigo took its Sageworks risk management platform offline following irregular activity and an outage.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/fintech-platform-sageworks-taken-offline-after-suspected-cyberattack/)

### 🟠 Michigan State Cyber Incident Claimed by Ransomware Gang
`exploited`

The BYOD ransomware gang claimed responsibility for a security incident at Michigan State University that prompted campus-wide response actions.

[The Record](https://therecord.media/michigan-state-university-byod-gang-cyber-incident)

### 🟠 Russia Statistics Agency Confirms Cyberattack
`exploited`

Russia's federal statistics agency, Rosstat, confirmed a cyberattack claimed by Belarusian and pro-Ukrainian hackers who stole government data.

[The Record](https://therecord.media/hackers-ukraine-belarus-russia)

### 🟠 Ukrainian and Russian Air Raid Apps Hacked
`exploited`

Emergency air raid alert systems in Ukraine and Russia were hacked to spread fake nuclear attack warnings.

[The Record](https://therecord.media/ukraine-hackers-russia-alert-system)

### 🟠 Revolve Data Breach Impacts 180,000 Customers
`exploited`

Hackers accessed Revolve's online shopping platform and stole personal and payment card information affecting at least 180,000 individuals.

[SecurityWeek](https://www.securityweek.com/revolve-data-breach-impacts-at-least-180000-people/)

### 🟠 Polymarket Funds Returned Following DNS Hijack
`exploited`

Polymarket returned funds to traders after DebugBear suffered a DNS hijack via its domain registrar affecting a customer.

**Do:** Audit DNS registrar security and enable registry locks.

[SecurityWeek](https://www.securityweek.com/polymarket-returns-3-9-million-to-traders-as-debugbear-cites-dns-hijack/) · [The Record](https://therecord.media/polymarket-returning-funds-to-customers-after-site-compromise)

### 🟠 DarkBlinders Targets Israel and Iraqi Kurdistan Cloud
`exploited`

An Iran-aligned threat actor conducted espionage campaigns compromising targets in Israel and the Kurdistan Region of Iraq between August and October 2026.

[The Hacker News](https://thehackernews.com/2026/11/darkblinders-compromises-israeli-target.html)

### 🟠 Government Linux Servers Targeted by SysGoRAT
`exploited`

Palo Alto Networks discovered a cyber espionage campaign targeting government Linux infrastructure using SysGoRAT and scripts.

**Do:** Monitor Linux environments for unauthorized remote access tools and anomalous scripts.

[The Hacker News](https://thehackernews.com/2026/11/government-linux-servers-targeted-with.html)

### 🟠 ape-volo-admin Auth Bypass via Hardcoded JWT Key
`CVE-2026-120442 · CVSS 9.8`

ape-volo-admin before 3.6.1 contains an authentication bypass vulnerability allowing unauthenticated attackers to forge administrator tokens using a hardcoded JWT signing key.

**Do:** Upgrade ape-volo-admin to version 3.6.1 or later.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120442)

### 🟠 madong-admin-saas Missing Authentication Flaw
`CVE-2026-120446 · CVSS 9.4`

madong-admin-saas through 5.1.4 contains a missing authentication vulnerability in the platform tenant management API, allowing unauthenticated attackers to manage tenants.

**Do:** Upgrade madong-admin-saas beyond version 5.1.4.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120446)

### 🟠 Control Web Panel Auth Bypass Vulnerability
`CVE-2026-73696 · CVSS 9.3`

Control Web Panel (CWP) before version 1.12 contains an execution after redirect vulnerability allowing unauthenticated attackers to bypass authentication.

**Do:** Upgrade Control Web Panel to version 1.12 or later.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-73696)

### 🟠 VOLTA Infostealer Uses LLMs to Rank Stolen Financial Data

A new Windows infostealer called VOLTA harvests browser credentials, Outlook profiles, and Slack workspaces, utilizing large language models to prioritize stolen data by monetization value.

**Do:** Monitor endpoints for unauthorized use of API calls to LLM services by unknown processes and typical credential-stealer behaviors.

[The Hacker News](https://thehackernews.com/2026/11/new-volta-infostealer-uses-claude.html)

## 2026-11-01

### 🟠 Canonical LXD and MicroCloud Client Impersonation Flaw

A critical flaw in Canonical LXD and MicroCloud allows attackers with a trusted client's public certificate to impersonate that client over the HTTPS API without a private key.

**Do:** Apply patches for LXD and MicroCloud provided by Canonical.

[The Hacker News](https://thehackernews.com/2026/11/critical-lxd-and-microcloud-flaw-cvss.html)

### 🟠 WAVLINK WN553X1-B WireGuard CLI Command Injection
`CVE-2026-120240 · CVSS 9.9`

WAVLINK WN553X1-B V260403_2.0.0 contains a remote OS command injection vulnerability in the WireGuard CLI Group Handler. A public exploit has been disclosed.

**Do:** Restrict access to WAVLINK devices and apply vendor patches when available.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120240)

## 2026-10-31

### 🔴 imgproxy ICO Loader Integer Overflow RCE Vulnerability
`CVSS 9.8`

An integer overflow in the ICO loader of imgproxy, imgproxy/v2, and imgproxy/v3 allows remote code execution or denial of service via a crafted network request.

**Do:** Upgrade imgproxy to the latest patched version.

[GitHub Advisory](https://github.com/advisories/GHSA-hff9-5pqw-6w9f)

### 🟠 Northflank Security Breach Exposes API Keys
`exploited`

Cloud application hosting platform Northflank suffered a security breach resulting in the unauthorized use of customers' AI API keys stored on the platform.

**Do:** Rotate all credentials, API keys, and secrets stored on Northflank.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/northflank-security-breach-leads-to-abuse-of-customers-ai-api-keys/)

### 🟠 Jpom Authentication Bypass and RCE Vulnerability
`CVE-2026-120201 · CVSS 9.8`

Jpom 2.10.0 through 2.11.12 contains an authentication bypass flaw via injected query conditions in the JPOM-USER-TOKEN header, allowing unauthenticated attackers to execute commands.

**Do:** Upgrade Jpom to patched versions and restrict network access.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120201)

### 🟠 AJ-Report Hard-Coded JWT Secret RCE Vulnerability
`CVE-2026-120209 · CVSS 9.8`

AJ-Report through 1.7.1 uses a hard-coded JWT secret to sign share tokens, allowing attackers to forge tokens and achieve unauthenticated remote code execution via GroovyClassLoader.

**Do:** Upgrade AJ-Report beyond 1.7.1 and rotate signing keys.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120209)

### 🟠 Signal K Server Path Traversal JWT Secret Disclosure and RCE
`CVSS 9.8`

A path traversal flaw in signalk-server and @signalk/resources-provider allows unauthenticated users to read arbitrary files, including the JWT signing secret, leading to RCE.

**Do:** Upgrade signalk-server and @signalk/resources-provider to patched versions.

[GitHub Advisory](https://github.com/advisories/GHSA-4xm8-rg9h-jhq2)

### 🟠 OpenAI ChatGPT Share Link Arbitrary Code Execution Flaw

A vulnerability in ChatGPT allowed malicious shared links to execute arbitrary code within the logged-in session of users who opened them, exposing private conversations. OpenAI patched the issue.

[The Hacker News](https://thehackernews.com/2026/10/a-shared-chatgpt-link-could-run.html)

### 🟠 Chainalysis Data Breach Exposes Customer Identity Data
`exploited`

Chainalysis confirmed an external actor accessed internal tools and non-sensitive customer identity data, though investigation content and credentials remained uncompromised.

**Do:** Audit access logs and monitor for fraudulent activity related to exposed customer identity data.

[The Hacker News](https://thehackernews.com/2026/10/chainalysis-confirms-intrusion-into.html) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/chainalysis-discloses-data-breach-from-offensive-agentic-techniques/) · [SecurityWeek](https://www.securityweek.com/chainalysis-discloses-data-breach-following-ai-driven-cyberattack/)

### 🟠 Android SMS of Death CVE-2026-58882 PoC Released
`CVE-2026-58882`

A proof-of-concept exploit has been released for CVE-2026-58882, an Android vulnerability enabling remote crashes or cellular service disruption via a crafted text message.

**Do:** Apply the latest Android security patches.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/new-android-sms-of-death-exploit-can-remotely-crash-unpatched-phones/)

## 2026-10-30

### 🔴 Ivanti Connect Secure Predictable Numbers Flaw Added to KEV
`CVE-2026-111357, CVE-2026-118527 · CISA KEV`

CISA added CVE-2026-118527, a predictable numbers vulnerability in Ivanti Connect Secure that allows remote file uploads, to its KEV catalog.

**Do:** Apply vendor mitigations and follow CISA BOD 26-04 guidance immediately.

[CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-118527) · [CISA Advisories](https://www.cisa.gov/news-events/alerts/2026/10/30/cisa-adds-two-known-exploited-vulnerabilities-catalog) · [The Hacker News](https://thehackernews.com/2026/10/attackers-chain-three-ivanti-connect.html) · [SecurityWeek](https://www.securityweek.com/ivanti-patches-two-more-zero-days-exploited-in-connect-secure-attack-chain/) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/ivanti-patches-two-more-connect-secure-zero-days-chained-in-attacks/)

### 🔴 Ivanti Connect Secure Missing Auth Privilege Escalation Flaw Added to KEV
`CVE-2026-111357 · EPSS 0.00 · CISA KEV`

CISA added CVE-2026-111357, a missing authentication vulnerability in Ivanti Connect Secure allowing privilege escalation, to its KEV catalog.

**Do:** Apply vendor mitigations and follow CISA BOD 26-04 guidance immediately.

[CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-111357)

### 🔴 Attacker Tried to Exploit Alpine Linux’s GitLab via CVSS 10.0 Flaw Its Ruby Left Open
`CVE-2026-76418, CVE-2026-97229, CVE-2026-98432 · EPSS 0.18 · CISA KEV`

An attacker tried to exploit a critical GitLab vulnerability on the Alpine Linux project's own GitLab server a week after GitLab released a fix, Alpine Linux said on 28 October. The flaw, CVE-2026-97229 (CVSS score: 10.0), can let an attacker run code on a GitLab server through a crafted regular expression in a CI configuration.

**Do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

[The Hacker News](https://thehackernews.com/2026/10/attacker-tried-to-exploit-alpine-linuxs.html) · [The Hacker News](https://thehackernews.com/2026/10/cisco-patches-actively-exploited-asa.html) · [CISA Advisories](https://www.cisa.gov/news-events/alerts/2026/10/29/cisa-adds-two-known-exploited-vulnerabilities-catalog) · [The Hacker News](https://thehackernews.com/2026/10/linux-kernel-tcp-flaw-with-98-cvss.html) · [The Hacker News](https://thehackernews.com/2026/10/cisa-adds-actively-exploited-gitlab-rce.html) · [SecurityWeek](https://www.securityweek.com/max-severity-gitlab-vulnerability-exploited-against-alpine-linux/) · [CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-97229) · [CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-76418) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/hackers-now-exploiting-max-severity-gitlab-flaw-in-attacks/) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/alpine-linux-rebuilds-gitlab-after-attempted-rce-attack/) · [The Hacker News](https://thehackernews.com/2026/11/red-hat-patches-98-rated-linux-tcp-rce.html)

### 🔴 Hackers Exploited Cisco SD-WAN Flaw to Plant Malware Built to Steal Encryption Keys
`CVE-2026-20127 · EPSS 0.89 · CISA KEV`

Hackers exploited a critical Cisco Catalyst SD-WAN flaw, fixed in February, to plant custom malware inside the systems that control an organization's SD-WAN network. The malware, called KeyDrift, is designed to copy the keys that encrypt traffic between sites and store them for later use, Cisco Talos said on October 28.

[The Hacker News](https://thehackernews.com/2026/10/hackers-exploited-cisco-sd-wan-flaw-to.html) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/hackers-exploit-cisco-sd-wan-flaw-to-deploy-custom-keydrift-malware/)

### 🔴 Binance Suffers Record $6.3 Billion Crypto Heist
`exploited`

Binance experienced a record-breaking crypto heist resulting in the theft of $6.3 billion, linked to North Korean threat actors.

**Do:** Review platform exposures and asset protections if interacting with affected services.

[Ars Technica](https://arstechnica.com/security/2026/10/hackers-steal-6-3-billion-from-binance-in-record-crypto-heist/) · [The Hacker News](https://thehackernews.com/2026/11/fbi-links-north-koreas-tradertraitor-to.html) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/fbi-links-63-billion-binance-crypto-heist-to-north-korean-hackers/)

### 🔴 Linux Kernel MPTCP Remote Root RCE Vulnerability

Researchers developed an exploit for a critical Linux kernel vulnerability enabling unauthenticated remote root execution on servers with MPTCP listeners.

**Do:** Monitor for Linux kernel updates addressing MPTCP vulnerabilities and apply patches promptly.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/critical-linux-kernel-flaw-allows-remote-root-attacks-on-mptcp-servers/)

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

### 🟠 Trezor Warns of Hardware Implant in Reseller Wallet

Trezor warned customers about a suspected hardware implant in a Trezor Safe 5 wallet sold by reseller CryptoBilis that leaks recovery phrases over a mobile network.

**Do:** Move funds to a new wallet with a new recovery phrase if purchased from CryptoBilis.

[The Hacker News](https://thehackernews.com/2026/10/trezor-warns-of-suspected-hardware.html) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/trezor-warns-of-suspected-crypto-theft-implant-in-hardware-wallet/)

### 🟠 Florida Department of Education Data Breach Exposes SSNs
`exploited`

The Florida Department of Education reported that 4.9 million people had Social Security numbers leaked in a data breach involving the Florida Student Financial Aid website.

**Do:** Monitor credit reports if affected.

[The Record](https://therecord.media/florida-warns-5-million-affected-financial-aid-site-breach) · [SecurityWeek](https://www.securityweek.com/florida-student-aid-website-hack-puts-data-of-4-9-million-people-at-risk/)

### 🟠 IBM Langflow OSS Deserialization RCE Vulnerability
`CVE-2026-104317 · CVSS 9.8 · EPSS 0.01`

IBM Langflow OSS 1.0.0 through 1.12.3 contains an insecure deserialization vulnerability allowing remote code execution via message broker access.

**Do:** Upgrade IBM Langflow OSS to version 1.12.5 or later.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-104317) · [The Hacker News](https://thehackernews.com/2026/11/critical-langflow-flaws-could-let.html)

### 🟠 IBM Langflow OSS Stored Python Component Execution Flaw
`CVE-2026-18894 · CVSS 9.8 · EPSS 0.00`

IBM Langflow OSS 1.0.0 through 1.12.4 allows remote attackers to trigger pre-existing stored Python component code in public workflows.

**Do:** Upgrade IBM Langflow OSS to version 1.12.5 or later.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-18894)

### 🟠 OpenDeepWiki Hard-Coded JWT Signing Key Vulnerability
`CVE-2026-119597 · CVSS 9.8`

OpenDeepWiki through 2.0.6 contains a hard-coded JWT signing key vulnerability allowing unauthenticated attackers to forge administrator tokens.

**Do:** Upgrade OpenDeepWiki beyond version 2.0.6.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-119597)

### 🟠 MuseBot Authentication Bypass Vulnerability
`CVE-2026-119660 · CVSS 9.8`

MuseBot before 2.0.0 contains an authentication bypass vulnerability allowing unauthenticated attackers to forge admin sessions using a hard-coded session key.

**Do:** Upgrade MuseBot to version 2.0.0 or later.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-119660)

### 🟠 InternLM LMDeploy Unauthenticated RCE Vulnerability
`CVE-2026-119706 · CVSS 9.8`

InternLM LMDeploy 0.9.0 through 0.18.0 contains an unauthenticated RCE vulnerability allowing attackers to execute OS commands via pickled data sent to the /update_weights endpoint.

**Do:** Upgrade InternLM LMDeploy beyond version 0.18.0.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-119706)

### 🟠 Fake ChatGPT and Claude Apps Abuse Signed Executables to Deploy Crypto Miners

Threat actors are delivering malicious loaders and cryptocurrency miners under the guise of artificial intelligence (AI) desktop applications for Anthropic Claude and OpenAI ChatGPT as part of a campaign dubbed Yoba. The activity involves creating fake GitHub projects that claim to be desktop applications like GPT-5.6 Sol, GPT-6 Astra, and Claude Opus, only to deliver a malware family called

[The Hacker News](https://thehackernews.com/2026/10/fake-chatgpt-and-claude-apps-abuse.html) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/fake-crypto-app-on-apple-app-store-linked-to-23k-wallet-theft/) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/binance-probes-potential-58-billion-crypto-theft-hack/) · [The Record](https://therecord.media/binance-hit-by-record-6-billion-crypto-hack) · [The Hacker News](https://thehackernews.com/2026/10/binance-suffers-security-breach.html) · [SecurityWeek](https://www.securityweek.com/6-billion-binance-hack-bears-hallmarks-of-north-koreas-tradertraitor/) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/binance-links-63-billion-crypto-theft-to-compromised-devops-laptop/)

### 🟠 TeamViewer Host-to-Viewer Attack Vulnerability

TeamViewer patched a vulnerability that allows a compromised or malicious host machine to attack the remote user connecting to control it during a session.

**Do:** Update TeamViewer to the latest patched version.

[The Hacker News](https://thehackernews.com/2026/10/teamviewer-flaw-lets-remote-computers.html)

### 🟠 China-Linked Vapor Panda Uses AI-Powered ARTEX Against Over 200 Orgs
`exploited`

Chinese state-sponsored threat group Vapor Panda used an AI-powered penetration testing framework called ARTEX to target over 200 organizations.

**Do:** Review environment for indicators associated with Vapor Panda and unauthorized penetration testing frameworks.

[The Hacker News](https://thehackernews.com/2026/10/chinese-hackers-use-ai-powered-artex-to.html) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/chinese-hackers-use-artex-ai-in-automated-attacks-against-200-orgs/)

### 🟠 NetamLoader Malware Targets Government Windows Systems in Asia
`exploited`

Attackers are targeting government Windows systems in Asia with NetamLoader, a new malware utilizing legitimate Microsoft software components.

**Do:** Review endpoint telemetry for suspicious use of native Microsoft binaries downloading payloads.

[The Record](https://therecord.media/hackers-target-government-windows-systems-asia-new-malware) · [The Hacker News](https://thehackernews.com/2026/11/netamloader-malware-targets-government.html)

### 🟠 FBI Seizes Domain of Bulletproof Host Virtualine
`exploited`

The FBI seized the domain of bulletproof hosting provider Virtualine, which supported ransomware, infostealers, and hack-for-hire services.

[SecurityWeek](https://www.securityweek.com/bulletproof-host-virtualine-loses-its-domain-to-fbi-seizure/)

### 🟠 CVE-2026-103409: A Missing authentication for critical function vulnerability in Juniper Networks Session Smart Router a
`CVE-2026-103409 · CVSS 9.8 · EPSS 0.00 · exploited`

A Missing authentication for critical function vulnerability in Juniper Networks Session Smart Router allows an unauthenticated network-based attacker to obtain administrative privileges by passing crafted URL parameters to an insecure endpoint running as root. Note that this vulnerability can only be exploited prior to the device being onboarded to Mist/Conductor.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-103409)

### 🟠 actions/pypa/gh-action-pypi-publish: CA trust store issue in PyPI publishing
`CVSS 9.3`

pypi-publish action versions before 1.14.2 bundled a revoked root CA in the certifi trust store used for Sigstore Trusted Publishing and Digital Attestations.

**Do:** Upgrade actions/pypa/gh-action-pypi-publish to version 1.14.2 or later.

[GitHub Advisory](https://github.com/advisories/GHSA-5xjx-3w67-w9x9)

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

[BleepingComputer](https://www.bleepingcomputer.com/news/security/polymarket-halts-trading-after-crypto-draining-script-breach-25m-traced/) · [The Hacker News](https://thehackernews.com/2026/11/hackers-steal-about-27-million-from.html)

### 🟠 Limited reports of PHP bug exploitation emerge

One cyber firm listed a half-dozen exploitations of the PHP2Shell bugs, and another identified a well targeted, suspected Chinese campaign that breached U.S. "government affiliated" servers.

[The Record](https://therecord.media/php2shell-successful-exploitation-reports-emerge)

### 🟠 Fresh WordPress Vulnerability in Attackers’ Crosshairs

Threat actors are attempting to exploit a high-severity unauthenticated race condition leading to remote code execution. The post Fresh WordPress Vulnerability in Attackers’ Crosshairs appeared first on SecurityWeek .

[SecurityWeek](https://www.securityweek.com/fresh-wordpress-vulnerability-in-attackers-crosshairs/) · [The Hacker News](https://thehackernews.com/2026/10/wordpress-rce-flaw-draws-nearly-63000.html)

### 🟠 $2 Million+ Drained From Polymarket Traders in New Supply Chain Attack

Malicious code linked to a website monitoring tool was designed to hijack logged-in Polymarket sessions and siphon user funds. The post $2 Million+ Drained From Polymarket Traders in New Supply Chain Attack appeared first on SecurityWeek .

[SecurityWeek](https://www.securityweek.com/2-million-drained-from-polymarket-traders-in-new-supply-chain-attack/)

### 🟠 Official Claude Code VS Code Extension Compromised to Install Persistent SSH Backdoor

Cybersecurity researchers have disclosed that the official Anthropic Claude Code extension was compromised on the Open VSX registry to install a persistent SSH backdoor on infected hosts. The issue has since been traced to the compromise of the Cursor Marketplace, prompting the AI coding platform Cursor to briefly take down the service to remove the malware.

[The Hacker News](https://thehackernews.com/2026/10/official-claude-code-vs-code-extension.html) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/malicious-claude-code-extension-on-cursor-planted-ssh-backdoors/) · [Ars Technica](https://arstechnica.com/security/2026/10/anthropic-vs-code-extension-on-cursor-backdoored-for-nearly-12-hours/)

### 🟠 PHP2Shell Attack Roots 25 Servers, Breaches U.S. Government-Affiliated Network

Cybersecurity researchers have disclosed details of what appears to be an artificial intelligence (AI)-assisted attack orchestrated by a suspected China-nexus threat actor that has leveraged the PHP2Shell vulnerabilities to breach exposed systems. The activity, which was observed on October 25, 2026, involved an attacker combining PHP2Shell with a kernel privilege escalation exploit to root

[The Hacker News](https://thehackernews.com/2026/10/php2shell-attack-roots-25-servers.html) · [SecurityWeek](https://www.securityweek.com/php2shell-attacks-root-palo-alto-firewalls-but-fail-against-wordpress/)

### 🟠 Hackers Target Critical Oracle E-Business Suite RCE Flaw Days After Security Patch
`CVE-2026-101767 · EPSS 0.01`

Threat actors are beginning to probe for a newly patched critical vulnerability in Oracle E-Business Suite (EBS), according to threat intelligence firm Defused Cyber. The vulnerability in question is CVE-2026-101767 (CVSS score: 9.8) , a case of improper authentication in the Oracle Application Object Library of Oracle E-Business Suite.

[The Hacker News](https://thehackernews.com/2026/10/hackers-target-critical-oracle-e.html)

### 🟠 Siemens Mendix SAML Module
`CVE-2026-89209 · EPSS 0.00`

View CSAF Summary Mendix SAML module contains an authentication bypass vulnerability that could allow an unauthenticated remote attacker to gain unauthorized access by replaying a valid SAML assertion in IdP-initiated authentication flows. Siemens has released new versions for the affected products and recommends to update to the latest versions.

[CISA Advisories](https://www.cisa.gov/news-events/ics-advisories/icsa-26-302-01)

