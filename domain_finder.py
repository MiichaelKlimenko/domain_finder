import sys

from crtsh import crtshAPI
import re
import requests
from os import path
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--company', type=str, help="The company's name.")
parser.add_argument('--company-in-domain', type=bool, default=False, help="Specifies if found domain should contain company's name.")
args = parser.parse_args()


company = args.company
find_company_in_domain = bool(args.company_in_domain)

if company is None:
    print("usage: python3 domain_finder.py --company <name> [--company-in-domain]")
    exit(0)
regex = r"[-a-zA-Z0-9.]+\.[a-z]{2,30}"


def check_tld(tld):
    tlds_url = "https://data.iana.org/TLD/tlds-alpha-by-domain.txt"

    if not path.exists("tlds.txt"):
        r = requests.get(tlds_url)
        open('tlds.txt', 'wb').write(r.content)
    f = open('tlds.txt','r')
    tlds_list = (f.read()).split('\n')
    tlds_list.pop(0)
    tlds_list.pop(len(tlds_list) - 1)
    tlds_list = list(map(lambda x: x.lower(), tlds_list))

    for t in tlds_list:
        if t == tld:
            return True
    return False


try:
    results = crtshAPI().search(company)
except Exception:
    print("Problems with crt.sh")
    results = []

all_found = ""

domains = {}

if len(results) == 0:
    print("Nothing found.")
    sys.exit(0)

for result in results:
    all_found += result['common_name'] + "\n"
    all_found += result['name_value'] + "\n"

for result in all_found.split('\n'):
    #print(result)
    domain = re.findall(regex, result)
    #print(domain)
    if len(domain) > 0:
        domain = domain[0]
        domain_parts = domain.split('.')
        final_domain = ""
        #print(domain_parts)
        for i in range(-1,-len(domain_parts)-1,-1):
            if check_tld(domain_parts[i]):
                final_domain = "." + domain_parts[i] + final_domain
            else:
                final_domain = domain_parts[i] + final_domain
                break
        #print(final_domain)
        if find_company_in_domain:
            if not (company in final_domain):
                continue
        domains[final_domain] = ""

domains = dict(sorted(domains.items()))

for domain in domains.keys():
    print(domain)

