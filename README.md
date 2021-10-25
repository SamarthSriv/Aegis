### Features:

* #### APK Extraction
    * assets
    * classes.dex
    * native libraries
    * jar file from dex (integrated Enjarify)

* #### Source Extraction
    * Certificate/signature
    * Java source
    * smali source
    * Parsed XML resource files
    * Parsed AndroidManifest
    * Native library

* #### Static Analysis
    * **Manifest analysis**
        * Critical permission usage analysis
        * MainActivity identification
        * Backup status
        * Exported activities
        * Exported broadcast receivers
        * Identify intent filters
        * Identify embedded deeplinks
        * Automated ADB payload generation for exported activities
        
    * **Bytecode analysis**
        * **ICC**
            * Dynamic Broadcast Receivers
            * Empty Pending Intents
            * Sticky Broadcasts 
            * Unprotected Broadcast Receivers
            * Weak Dynamic Invocation Checks
        * **Web Issues**
            * JavaScript Execution in WebViews
            * HTTP Connections
            * Unsafe Intent URL Resolving Implementation
            * Overwritable Cookie
            * File Access from URLs
            * Content Provider Access from URLs
            * Supressed SSL Warnings
        * **Storage Issues**
            * Non-parameterized SQL queries
            * Usage of External Storage for application data
        * **Networking**
            * Missing Server Certificate Validity Check
            * Insecure SSL Socket Factory
        * **Crypto Issues**
            * Usage of ECB Block Cipher
        
        * const-strings
        * CTF flags
        * URLs
    * **Native Library analysis**
        * Library info
        * Sections
        * Base64 Decoding of strings from .data

* #### Miscellaneous
    * Rebuilding the APK
    * Signing the APK

---



---

### Pre-requisites:

* Linux or MAC
* Python3
* Java JDK

---

### Quick Setup

1. Dowload the zip or clone the package and extract the tool ( ```git clone https://github.com/abhi-r3v0/Adhrit.git``` ).
2. Open ```config``` and input your VirusTotal API key without any quotes. ([Click here to know how to obtain your VT API key](https://community.mcafee.com/t5/Documents/How-to-get-a-VirusTotal-public-API-Key/ta-p/552797))
3. Open a terminal and cd into the directory.
4. Run the ```installer script``` to install the necessary tools/dependencies:
   ```python3 installer.py```

---
### Usage:

1. Place the application (apk file) in the tool directory.
2. Use ```python3 adhrit.py -h``` for usage help.

Example:  

```python
python3 adhrit.py -a myapp.apk
```

#### Pentest Mode

```python
python3 adhrit.py -pen myapp.apk
```

Refer to the detailed [documentation](hhttps://github.com/abhi-r3v0/Adhrit/wiki) for complete details

---

### Credits:

* [apktool](https://ibotpeaches.github.io/Apktool/)
* [jarsigner](https://github.com/appium/sign)
* [AXML2Printer](https://code.google.com/archive/p/android4me/downloads)
* [jd-cli](https://github.com/kwart/jd-cmd)
* [aapt](https://developer.android.com/studio/command-line/index.html)
* [Enjarify](https://github.com/google/enjarify)
* [Ghera](https://bitbucket.org/secure-it-i/android-app-vulnerability-benchmarks/src/master/)
* [Smalisca](https://github.com/dorneanu/smalisca)

---

