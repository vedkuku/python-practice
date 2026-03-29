# string_practive.py -Track B session 2
# purpose practice string method - using log data

# A raw log entry - messy, like a real log data
raw_log = "   Alert: src_ip=203.0.113.42 severity=CRITICAL   "

# .strip() - remove leading and trailing whitespaces
clean_log =  raw_log.strip()
print(f"Striped: {clean_log}")

# .lower - normalise case - useful when comparing log fields
lower_log = clean_log.lower()
print(f"Lowerecase: {lower_log}")

# .replace - replace one string for another
updated_log = clean_log.replace("CRITICAL", "P1")

# .find() returns the index where word starts (-1 if not found)
position = clean_log.find("severity")
print(f"'severity' starts at index: {position}")

# slicing - extract a porttion using [start:end]
# "Alert: src_ip=203.0.113.42 severity=CRITICAL"
# count charaters to find where the IP starts
ip_slice = clean_log[14:26]
print(f"sliced IP area: {ip_slice}")

# len() - length of the string
print(f"Log length: {len(clean_log)}")

# f-string with calculation inside
alert_source = "FortiGate"
threat_name = "CVE-2024-21762"
full_alert = f"Alert From: {alert_source}: {threat_name} detected"
print(full_alert)


