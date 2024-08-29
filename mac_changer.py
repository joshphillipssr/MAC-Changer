#!/usr/bin/env python

import subprocess

interface = input("interface (e.g. eth0) > ")
new_mac = input("mac address (e.g. 00:11:22:33:44:44) > ")

print("[+] Changing MAC address for " + interface + " to " + new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])
