# types_practice.py Track B session 2
# Purpose : verify all 5 types using security context

# Str - device that generate alert

device_name = "Fortigate-100f"

# int - Number of blocked IPs today
block_count = 142

#fload - CVSS vulnerability score
cvss_score = 9.8

#bool - is the threat currently active
is_active = True

# None - timestamp not yet recorded
resolved_at = None

#  type() tells you what python sees this variable as
print(type(device_name))
print(type(block_count))
print(type(cvss_score))
print(type(is_active))
print(type(resolved_at))
