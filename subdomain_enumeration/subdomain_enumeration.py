import requests
import sys

sub_list = open("subdomain.txt").read()
subdoms = sub_list.splitlines()

print("[+] Subdomain Enumeration Started")
for index, sub in enumerate(subdoms):
    sub_domains = f"https://{sub}.{sys.argv[1]}"

    try:
        print(f"[+] {(index * 100) / len(subdoms)}/{100}%")
        requests.get(sub_domains)
    except requests.exceptions.ConnectionError:
        pass
    else:
        print("[+] Discovered subdomain: " + sub_domains)

print("[+] Finished scanning")

