# Conditionals_practice.py - Track B session 3
# Purpose: if/elif/else logic using threat severity levels

# A CVSS score we want to classify



cvss_score = 8.5      # the vulnerability score to evaluate


if cvss_score >= 9.0:
    severity_label = "Critical"           # 9.0 and above
elif cvss_score >= 7.0:                  # 7.0-8.9 
    severity_label = "High"
elif cvss_score >= 4.0:
    severity_label = "Medium"
else:
    severity_label = "low"

print(f"CVSS {cvss_score} = {severity_label}")

test_scores = [9.8, 7.2, 5.5, 2.1]     # list of scores to classify

for t in test_scores:
    if t >= 9.0:
        label = "Critical"
    elif t >= 7.0:
        label = "High"
    elif t >= 4.0:
        label = "Medium"
    else:
        label = "low"
    print(f" Score {t} = {label}")

    
