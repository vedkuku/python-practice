# lists_practice.py - Track B session 2
# Purpose: list operations using a set of suspicious IPs

# A list of suspicious IPs flagged today - square brackets, comma separated
suspicious_ips = ["203.0.113.1", "198.51.100.4", "192.0.2.77", "10.0.0.55"]

#how many items in the list
print(f" Total suspicious IPs: {len(suspicious_ips)}")

# Indexing - access by position, starts at 0 (same as JavaScript)
print(f"First IP: {suspicious_ips[0]}")
print(f"Last IP: {suspicious_ips[-1]}")

# .append() - add a new aIP to the end  of the list
suspicious_ips.append("172.16.0.99")
print(f"After Append {suspicious_ips}")

# .remove() - remove a specific item by value
suspicious_ips.remove("10.0.0.55")
print(f"After remove: {suspicious_ips}")

# 'in' - check if a value exists in the list (very clean Python syntax)
target_ip = "198.51.100.4"
is_flagged = target_ip in suspicious_ips
print(f"{target_ip} is flagged : {is_flagged}")

# for loop - always use 't' as the loop variable
print("-----All flagged IPs------")
for t in suspicious_ips:
    print(f"     Blocked: {t}")  #indent with 4 spaces - python requires this 

# List of mixed alert data - lists can hold any type
alert_scores = [9.8, 7.2, 4.5, 9.1, 6.3]

# sorted() - returns a new sorted list (does not modify original
sorted_scores = sorted(alert_scores, reverse=True)     # highest first
print(f"Scores high to low: {sorted_scores}")

# max() and min()
print(f"Highest score: {max(alert_scores)}")
print(f"Lowest score: {min(alert_scores)}")

