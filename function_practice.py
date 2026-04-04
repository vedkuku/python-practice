# functions_practice.py - Jarvis Guide P1
# Purpose: reusable functions for security logic

# ddef defines the function - classify_threat is the name, cvss_score is the  input
def classify_threat(cvss_score):
    if cvss_score >= 9.0:
        return"Critical"
    elif cvss_score >= 7.0:
        return "High"
    elif cvss_score >= 4.0:
        return "Medium"
    else:
        return "Low"

# calling the function - pass a value in, get a result back
result = classify_threat(8.5)
print(f"Score 8.5 + {result}")

# function with two parameters

def assess_risk(cvss_score, patch_lag_days):
    severity = classify_threat(cvss_score)       # calling a function inside another function

    if patch_lag_days > 30:
        urgency = "Overdue"
    elif patch_lag_days > 7:
        urgency = "Delayed"
    else:
        urgency = "Recent"

    return F"{severity} severity - patch status: {urgency}"

print(assess_risk(9.8, 45))
print(assess_risk(7.2, 5))
print(assess_risk(4.5, 14))


# default parameter - used when caller doesnt provide a value

def generate_alert(ip_address, threat_type, severity="Unknown"):
    return f"Alert | IP: {ip_address} | {threat_type} | Severity: {severity}"

print(generate_alert("203.4.5.76", "Brute Force", "High"))
print(generate_alert("10.6.3.4", "Port Scan"))       # Severity falls back to default value