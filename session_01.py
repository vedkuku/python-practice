# session_01.py - Track B python, session 1
#Purpose: first python script - simulated threat alert banner

# A string variable - stores the analyst's name
analyst_name = "ved"

# A string variable - stores the type of attack detected
threat_type = "Brute Force"

# An integer variable - whole number no quotes
login_attempts = 47

#A boolena variable - Ture or False, captial first letter (unlike JS)
is_active = True

# print() outputs to terminal - same as console.log() in JavaScript
print("=======THREAT ALERT ====")

# F-STRING - THE F PREFIX  lets you embed variables inside strings
print(f"Analyst: {analyst_name}")
print(f"Threat Type: {threat_type}")
print(f"Failed Logins: {login_attempts}")
print(f"Still Active ? : {is_active}")
print("================")
