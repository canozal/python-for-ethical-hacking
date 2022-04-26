import subprocess

interface = input("[*] Enter interface: ")
new_mac = input("[*] Enter new MAC address: ")

print("[*] Changing MAC address for " + interface + " to " + new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])





