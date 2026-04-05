# ip_lookup.py Jarvis Sprint Day 2
# Makes a real HTTP request to a threat intelligence API
# Run: python ip_lookup.py

import requests         # handles HTTP calls - like fetch() in JavaScript

def lookup_ip(ip_address):
    #ip-api.com is a free API - no key needed for basic lookup
    url = f"http://ip-api.com/json/{ip_address}"     #f-string builds the URL

    # request.get() makes a GET request - like fetch() in JS
    response = requests.get(url)

    # .status code is the HTTP status - 200 means success
    print(f"Status Code: {response.status_code}")

    # .json() parses the response body into a Python dict

    data = response.json()

    return data

def print_ip_report(ip_address):
    print(f"\n=== IP LOOKUP {ip_address} ===")

    data = lookup_ip(ip_address)

    # access dict field with square brackets - same as threat_card.py
    print(f"Status  :  {data['status']}")
    print(f"Country  : {data.get('country', 'Unknown')}")       # .get() = safe access
    print(f"Region   :  {data.get('regionName', 'Unknkown')}")
    print(f"City     : {data.get('city', 'Unknown')}")
    print(f"ISP      :  {data.get('city', 'Unknown')}")
    print(f"ORG      :  {data.get('org', 'Uknown')}")
    flag = get_threat_flag(data)           # assess the risk
    print(f"Verdict: {flag}")
   # print(f"Timezone  :  {data.get('timezone', 'Uknown')}")

    # test with three IPs - one known bad, one clean, one private
def get_threat_flag(data):
    # private/reserved IPs return 'fail' - not routable on internet
    if data['status'] == 'fail':
        return "⚪ Private / Reserved"

    org = data.get('org', '').lower()    # .lower() for case-insensitive check

    # known bad org keywords - crude but effective for demo
    if 'tor' in org or 'privacy' in org or  'anonymous' in org:
        return "🔴 HIGH RISK — anonymisation service detected"
    elif 'hosting' in org or 'datacenter' in org or 'cloud' in org:
        return "🟠 MEDIUM — hosting/cloud infrastructure"
    else:
        return "🟢 LOW — residential or commercial ISP"



ip_list = ["185.220.101.45", "8.8.8.8", "192.168.1.1"]

for t in ip_list:
        print_ip_report(t)

