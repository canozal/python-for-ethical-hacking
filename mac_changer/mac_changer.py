import subprocess
import optparse
import random
import re


def random_mac():
    mac = [0x00, 0x16, 0x3e,
           random.randint(0x00, 0x7f),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff)]
    return ':'.join(map(lambda x: "%02x" % x, mac))

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    parser.add_option("-r", "--random", dest="random", help="Random MAC address")

    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    if not options.new_mac and not options.random:
        parser.error("[-] Please specify a new MAC address, use --help for more info.")
    if options.random and options.new_mac:
        parser.error("[-] Please specify only one option, use --help for more info.")
    if options.random:
        options.new_mac = random_mac()

    return options


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


options = get_arguments()

old_mac = get_current_mac(options.interface)

change_mac(options.interface, options.new_mac)

new_mac = get_current_mac(options.interface)

if new_mac == options.new_mac:
    print("[+] MAC address was successfully changed from " + old_mac + " to " + new_mac)
else:
    print("[-] MAC address did not get changed.")



