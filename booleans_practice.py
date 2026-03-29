# boolean_practice.py - Track B session 2
# Purpose: boolean logic for threat triage decision

# Input variables representing an incident
failed_attempts = 8
max_attempts = 5             # threshold before lockout
ip_is_known_bad = True
mfa_enabled = False


# Comparison operators produce True or False
lockout_required = failed_attempts > max_attempts
print(f"Lockout Required: {lockout_required}")


# 'and' - both conditions must be true (like && in JavaScript)
escalate_to_soc = lockout_required and ip_is_known_bad
print(f"Escalate to SOC: {escalate_to_soc}")

# 'or' - atleast one condition must be true (like || in JavaScript)
needs_attention = lockout_required or ip_is_known_bad
print(f"Need Attentions: {needs_attention}")

# 'not'  - inverts the boolean (like ! in JavaScript)
mfa_missing = not mfa_enabled
print(f"MFA missing: {mfa_missing}")

# Combining - high risk if lockout triggered AND no MFA protection
high_risk_no_mfa = lockout_required and not mfa_enabled
print(f"High Risk no MFA: {high_risk_no_mfa}")

# == check equality, != checks inequality
severity = "CRITICAL"
is_critical = severity == "CRITICAL"
is_not_low = severity != "low"
print(f"Is critical: {is_critical}")
print(f"Is not low: {is_not_low}")
