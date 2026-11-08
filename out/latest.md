# Security signal: last 7 days

🔴 act now · 🟠 worth knowing

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

### 🟠 imgproxy ICO Loader Integer Overflow Vulnerability (CVE-2026-123614)
`CVE-2026-123614 · CVSS 9.8`

imgproxy 4.0.0 through 4.0.15 contains an integer overflow in the ICO loader, allowing remote attackers to trigger a heap buffer overflow via crafted images.

**Do:** Upgrade imgproxy to version 4.0.16 or later.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123614)

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

### 🟠 Crédit Mutuel Arkéa Hit by $133 Million Cyberattack via Service Provider
`exploited`

French cooperative bank Crédit Mutuel Arkéa suffered a cyberattack via a service provider resulting in $133 million in fraudulent transactions, prompting system suspensions.

[BleepingComputer](https://www.bleepingcomputer.com/news/security/hackers-pull-off-133-million-french-bank-heist-via-service-provider/)

### 🟠 Keycloak Client Management RCE Vulnerability (CVE-2026-120984)
`CVE-2026-120984 · CVSS 9.1`

A vulnerability in Keycloak's client management component allows authenticated attackers with client management permissions to upload and execute malicious JavaScript policies, leading to remote code execution.

**Do:** Apply the latest vendor patches for Keycloak to address CVE-2026-120984.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-120984)

### 🟠 IBM Aspera Faspex Authorization Bypass Flaw (CVE-2026-123218)
`CVE-2026-123218 · CVSS 9.8`

IBM Aspera Faspex versions 5.0.0 through 5.0.19 contain an authorization bypass vulnerability allowing an authorized user to craft specific messages and gain full administrative privileges.

**Do:** Upgrade IBM Aspera Faspex to the latest patched version.

[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123218)

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

[CISA Advisories](https://www.cisa.gov/news-events/alerts/2026/11/06/cisa-adds-one-known-exploited-vulnerability-catalog) · [CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2026-19868) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/sonicwall-warns-of-new-ssl-vpn-mfa-bypass-flaw-exploited-in-attacks/) · [SecurityWeek](https://www.securityweek.com/sonicwall-patches-exploited-sonicos-bug-that-weakens-vpn-logins/)

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

### 🔴 OpenSSH Critical Long Password Authentication Bypass Flaw in Alpine Linux
`CVE-2026-123158`

OpenSSH version 10.6p2 fixes a critical flaw affecting certain Alpine Linux configurations where long passwords can bypass authentication on accounts with no password.

**Do:** Upgrade OpenSSH to version 10.6p2 or later on affected Alpine Linux servers.

[The Hacker News](https://thehackernews.com/2026/11/openssh-issues-emergency-fix-for-flaw.html) · [Ars Technica](https://arstechnica.com/security/2026/11/vulnerability-allows-attackers-to-log-into-some-linux-devices-sans-password/) · [SecurityWeek](https://www.securityweek.com/openssh-rushes-patches-for-sshole-authentication-bypass/) · [The Hacker News](https://thehackernews.com/2026/11/hackers-exploited-openssh-sshole-flaw.html)

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

[The Record](https://therecord.media/fbi-blames-tradertraitor-for-binance-hack) · [SecurityWeek](https://www.securityweek.com/fbi-flags-over-600-addresses-tied-to-north-koreas-binance-heist/) · [The Record](https://therecord.media/binance-cryptocurrency-theft-months-long-campaign-nkorea) · [The Hacker News](https://thehackernews.com/2026/11/binance-reveals-how-fake-job-interviews.html) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/binance-says-fake-job-interview-led-to-63-billion-crypto-heist/) · [SecurityWeek](https://www.securityweek.com/rigged-coding-assignment-abused-ai-tool-opened-path-to-6-billion-binance-heist/) · [Ars Technica](https://arstechnica.com/information-technology/2026/11/binance-says-hackers-who-stole-billions-in-crypto-spent-months-planning-heist/)

### 🟠 Cyberattack Dispatches European Supermarket Refrigeration
`exploited`

A cyberattack disrupted refrigeration systems across European supermarket chains after hackers remotely altered temperature settings on cooling units.

[The Record](https://therecord.media/cyberattack-grocery-freezers-europe) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/hackers-disrupt-refrigeration-systems-at-european-supermarkets/) · [SecurityWeek](https://www.securityweek.com/over-100-european-stores-hit-as-supermarket-fridge-attacks-resume/) · [The Hacker News](https://thehackernews.com/2026/11/second-wave-of-cyberattacks-hits.html) · [The Record](https://therecord.media/british-businesses-caught-in-europe-wide-supermarket-fridge-attacks) · [The Record](https://therecord.media/france-cyberattack-blood-refrigeration) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/cyberattack-disrupts-blood-storage-refrigeration-systems-in-france/)

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

