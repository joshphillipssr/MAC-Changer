#!/usr/bin/env python

import subprocess
import argparse
import re

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", help="Interface to change MAC address of")
    parser.add_argument("-m", "--mac", dest="new_mac", help="New MAC address")
    args = parser.parse_args()

    if not options.interface:
        options.interface = input("[*] Please enter the interface (e.g. eth0): ")
    if not options.new_mac:
        options.new_mac = input("[*] Please enter the new MAC address (e.g. 00:11:22:33:44:55): ")

    return args

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address.")
        return None

options = get_arguments()

current_mac = get_current_mac(options.interface)
if current_mac:
    print("Current MAC = " + str(current_mac))

    change_mac(options.interface, options.new_mac)

    current_mac = get_current_mac(options.interface)
    if current_mac == options.new_mac:
        print("[+] MAC address was successfully changed to " + current_mac)
    else:
        print("[-] MAC address did not get changed.")