# !/usr/bin/env python3

import argparse
import configparser
from colorama import Fore, Style
from recons.apk_extract import apk_info
from recons.vapp import vapp_find
from recons.virustotal import api_check
from recons.smali_extract import smali_de
from recons.smali_extract import smali_re
from recons.smali_extract import apk_sign
from recons.smali_extract import inj_check
from recons.manifest_analysis import man_analyzer
from recons.smarser.parser import parser
from recons.native_recon import lib_pwn
from recons.dynamic import adb_con
from recons.clean import cleaner
from recons.root import check_root


__author__ = 'NerdSploit(info@nerdsploit.com)'
__version__ = "0.1"


class Adhrit:

    def __init__(self):
        self.apk_name = ""

    @staticmethod
    def welcome():
        print(Fore.RED + Style.BRIGHT)
        print("███╗   ██╗ ███████╗ ██████╗  ██████╗  ███████╗ ██████╗  ██╗       ██████╗  ██╗ ████████╗")
        print("████╗  ██║ ██╔════╝ ██╔══██╗ ██╔══██╗ ██╔════╝ ██╔══██╗ ██║      ██╔═══██╗ ██║ ╚══██╔══╝")
        print("██╔██╗ ██║ █████╗   ██████╔╝ ██║  ██║ ███████╗ ██████╔╝ ██║      ██║   ██║ ██║    ██║") 
        print("██║╚██╗██║ ██╔══╝   ██╔══██╗ ██║  ██║ ╚════██║ ██╔═══╝  ██║      ██║   ██║ ██║    ██║ ")  
        print("██║ ╚████║ ███████╗ ██║  ██║ ██████╔╝ ███████║ ██║      ███████╗ ╚██████╔╝ ██║    ██║") 
        print("╚═╝  ╚═══╝ ╚══════╝ ╚═╝  ╚═╝ ╚═════╝  ╚══════╝ ╚═╝      ╚══════╝  ╚═════╝  ╚═╝    ╚═╝ ")  
        print(Fore.YELLOW + Style.BRIGHT + "\n\n| Project\t\t:\t" + Fore.GREEN + "https://github.com/vaibhav-poseidon/android")
        print(Fore.YELLOW + Style.BRIGHT + "| Author\t\t:\t" + Fore.GREEN + __author__)
        print(Fore.YELLOW + Style.BRIGHT + "| Version\t\t:\t" + Fore.GREEN + __version__)


    check_deps = configparser.ConfigParser()
    check_deps.read('config')
    if check_deps.get('config-data', 'dependencies_status') == 'incomplete':
        print(Fore.RED + "\n[ERROR] Not all the necessary tools are installed! Please run " + Fore.YELLOW + 'python3 installer.py' + Fore.RED + " again")
        exit()
    else:
        pass

    print("\n\n")

    # Clean the tool directory for a new project
    @staticmethod
    def cleanproject(apk_name):
        cleaner(apk_name)

    # Extract All the contents of the APK into a directory
    @staticmethod
    def apkextractor(apk_name):
        apk_info(apk_name)

    @staticmethod
    def manifestanalyzer(apk_name):
        man_analyzer(apk_name)

    # Check for virtual app droppers
    @staticmethod
    def vappsearch(apk_name):
        vapp_find(apk_name)

    # Check if the APK has been identified by VirusTotal database
    @staticmethod
    def vtanalyzer(apk_name):
        api_check(apk_name)

    # Extract the source code of the APK in smali
    @staticmethod
    def smaliextractor(apk_name):
        smali_de(apk_name)

    # Bytecode Analysis
    @staticmethod
    def bytecodeanalyzer():
        parser()

    # Recompile smali back into APK
    @staticmethod
    def smalirecompile(apk_name):
        smali_re(apk_name)

    # Sign the apk with a generic signature. For educaational purposes only!
    @staticmethod
    def apk_signing(apk_name):
        apk_sign(apk_name)

    # Check for string injection points
    @staticmethod
    def smali_inj(apk_name, flag_format=''):
        inj_check(apk_name, flag_format)

    # Analyze native library
    @staticmethod
    def native_recon():
        lib_pwn()

    # Install the APK in an emulator and analyze its activities
    @staticmethod
    def dynamicanalysis(apk_name):
        adb_con(apk_name)

    # Check for root access in the emulator/device
    @staticmethod
    def checkroot():
        check_root()


def main():
    aegis = Adhrit()
    parser = argparse.ArgumentParser(description="Android Dynamic Handling, Reversing and Instrumentation Toolkit")
    parser.add_argument("-pen", help="Run aegis in pentest mode")
    parser.add_argument("-mal", help="Run aegis in malware analysis mode")
    parser.add_argument("-c", help="Clean up for a new project")
    parser.add_argument("-a", help="Dump package info and extract contents")
    parser.add_argument("-x", help="Extract APK contents only")
    parser.add_argument("-p", help="Check for virtual apps")
    parser.add_argument("-s", help="Source code of the APK in Smali")
    parser.add_argument("-b", help="Recompile smali back into APK")
    parser.add_argument("-m", help="Sign the APK")
    parser.add_argument("-i", help="Check for injection points")
    parser.add_argument("-pwn", help="Scan for vulnerabilities", action="store_true")
    parser.add_argument("--flag", help="Check for CTF flags")
    parser.add_argument("-w", help="Welcome :P", action='store_true')
    parser.add_argument("-v", help="Check footprints in VirusTotal database")
    parser.add_argument("-d", help="Analyse the behaviour dynamically in a VM")
    parser.add_argument("-cr", help="Check device root status", action='store_true')
    parser.add_argument("-l", help="Extract, parse and analyze manifest")
    parser.add_argument("-r", help="Analyze native library", action='store_true')
    args = parser.parse_args()

    # aegis Welcome ASCII
    aegis.welcome()

    if args.pen:
        aegis.cleanproject(args.pen)
        aegis.apkextractor(args.pen)
        aegis.native_recon()
        aegis.manifestanalyzer(args.pen)
        aegis.smaliextractor(args.pen)
        aegis.bytecodeanalyzer()
        aegis.smali_inj(args.pen)

    if args.mal:
        aegis.vtanalyzer(args.mal)
        aegis.vappsearch(args.mal)

    if args.c:
        aegis.cleanproject(args.c)

    if args.a:
        aegis.cleanproject(args.a)
        aegis.vtanalyzer(args.a)
        aegis.apkextractor(args.a)
        aegis.manifestanalyzer(args.a)
        aegis.native_recon()
        aegis.vappsearch(args.a)
        aegis.smaliextractor(args.a)
        aegis.smali_inj(args.a)
        aegis.bytecodeanalyzer()

    elif args.x:
        aegis.cleanproject(args.x)
        aegis.apkextractor(args.x)

    elif args.p:
        aegis.vappsearch(args.p)

    elif args.s:
        aegis.smaliextractor(args.s)

    elif args.b:
        aegis.smalirecompile(args.b)

    elif args.m:
        aegis.welcome()
        aegis.apk_signing(args.m)

    elif args.i:
        aegis.smali_inj(args.i, args.flag)

    elif args.pwn:
        aegis.bytecodeanalyzer()

    elif args.r:
        aegis.native_recon()

    elif args.w:
        aegis.welcome()

    elif args.v:
        aegis.vtanalyzer(args.v)

    elif args.d:
        aegis.dynamicanalysis(args.d)

    elif args.cr:
        aegis.checkroot()

    elif args.l:
        aegis.manifestanalyzer(args.l)


if __name__ == "__main__":
    main()
