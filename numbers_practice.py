# numbers_practice.py - Track B session 2
# arithmetic operation using CVE risk scoring

# Base_inputs
base_cvss = 9.8                # CVSS score of the vulnrability
asset_criticality = 3          # scale of  1-3, this is a corwn jewel asset
patch_lag_days = 14            # days since patch was available but not applied

# Basic arithmetic
risk_priority =  base_cvss * asset_criticality
print(f"RISK Priority: {risk_priority}")

# // is integer (floor) division - drops te decimal
weeks_unpatched = patch_lag_days // 7
print(f"Weeks unpatched: {weeks_unpatched}")


# ** is the power operation
entropy_bits = 2 ** 8
print(f"Entropy bits: {entropy_bits}")

# % is modulo - remainder after division
remainder = patch_lag_days % 7
print(f"Days beyound full week: {remainder}")

# combining operations
final_risk = risk_priority * weeks_unpatched
print(f"Final risk score: {final_risk}")

# round() - round to N decimal places
detection_rate = 153 / 200 * 100
print(f"Detection rate: {round(detection_rate, 1)}")

# abs() - absolute value, useful for anomaly detection
baseline = 5000
current = 3200
deviation = abs(current - baseline)
print(f"Traffic deviation: {deviation} req/min")

