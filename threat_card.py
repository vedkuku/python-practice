# threat_card.py - Jarvis Sprint Day 1
# A CLI Threat Intelligence Card generator
# Run: python threat_card.py

from ctypes import addressof
from string import capwords


def get_severity_label(score):
    # Converts a numeric score into a labelled string
    if score >= 80:
        return f"Critical ({score}/100)"
    elif score >= 50:
        return f"High ({score}/100)"
    elif score >= 20:
        return f"Medium ({score}/100)"
    else:
        return f"Low ({score}/100)"

def build_threat_card(ip, severity, country, isp, last_seen, action):
    # f-string with :<30 pads the value to 30 characters - keeps column aligned
    card = f"""
+-----------------------------------------------+
|             THREAT INTELLIGENC CARD           |
+-----------------------------------------------+
|   IP ADDRESS  :  {ip:<30} |
|   Severity    :  {severity:<30} |
|   Country     :  {country:<30} |
|   ISP         :  {isp:<30}  |
|   Last Seen   :  {last_seen:<30} |
+-----------------------------------------------+
|   Action  : {action:<36} |
+-----------------------------------------------+"""
    return card

# Dictionary - stores threat data keyed by IP address
threat_database = {
    "185.220.101.45": {
        "score": 92,
        "country": "Germany",
        "isp": "Tor Project",
        "last_seen": "2026-04-03 22:14 UTC",
        "action": "BLOCK IMMEDIATELY"
    },
    "8.8.8.8": {
        "score": 2,
        "country": "United States",
        "isp": "Google LLC",
        "last_seen": "N/A",
        "action": "allowed"
    },
    "103.74.22.11": {
        "score": 61,
        "country": "Hong Kong",
        "isp": "Unknown Hosting",
        "last_seen": "2026-04-02 10:05 UTC",
        "action": "MONITOR"
    }
}


# input() pauses and waits for the user to type someting
target_ip = input("ENter IP to check:")

# Check if the IP exists in our database
if target_ip in threat_database:
    # retrieve the dic for this ip
    data = threat_database[target_ip]

    # pass the score to our function to get a label
    severity = get_severity_label(data["score"])

    # build and print the card
    card =build_threat_card(
        ip=target_ip,
        severity=severity,
        country=data["country"],
        isp=data["isp"],
        last_seen=data["last_seen"],
        action=data["action"]
    )
    print (card)
else:
    print(f"ip {target_ip} not found in threat database.")
