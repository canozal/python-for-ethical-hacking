import requests
import sys

sub_list = open("directory-names.txt").read()
directories = sub_list.splitlines()

print("[+] Directory Enumeration Started")
for dir in directories:
    if dir.startswith("#"):
        continue
    url = f"https://{sys.argv[1]}/{dir}"
    r = requests.get(url, allow_redirects=False)
    if r.status_code == 404:
        pass
    elif r.status_code == 302 and "404" in r.headers["Location"]:
        pass
    else:
        print(f"[+] {url} is found")
print("[+] Finished scanning")
