import os         # access environment variable
from dotenv import load_dotenv  # reads .env file into os.environ
import anthropic     # official Anthropic SDK

# - Load API key from .env before anything else --
load_dotenv()

# -- create the Anthropic client () picks up key from env automatically) --
client = anthropic.Anthropic()

# -- sample log lines Jarvis will classify --
log_lines = [
    "failed SSH login for root from 192.168.1.105 - 47 attempts in 60s",
    "User admin downloaded 2.3GB via FTP to external IP 185.220.101.45",
    "DNS query for known C2 domain: update-windows-patch.ru",
    "Scheduled task created: c:\\windows\\temp\\svc_update.exe at system startup",
]

verdicts = []             # will store all verdict stings
# -- Loop through each log and ask Claude to classify it --
for t in log_lines:        # t = one log line at a time
    print(f"\n{'-'*60}")
    print(f"Log: {t}")

    # --- API call: send log to claude with SOC analyst context --
    message = client.messages.create(
        model="claude-sonnet-4-20250514",       # always use this model sting
        max_tokens=256,             # short verdict no
        system="You are a SOC analyst. Classify the log line as one of: CRITICAL / HIGH / MEDIUM / LOW / BENIGN. Reply with: Severity: <level> | Reason: <one sentence>",
        messages=[
            {"role": "user", "content": t}         # the log line is the user message

        ]
    )

    #  ---- Extract the text from Claude's response --
    verdict = message.content[0].text               # content is a list; [0] is the first block

    print(f"Verdict: {verdict}")

    verdicts.append(verdict)      # save each verdict for summary

#  ---- Severity Summary ----
print(f"\n{'='*60}")
print("JARVIS Summary")
for level in ["CRITICAL", "HIGH", "MEDIUM", "LOW", "BENIGN"]:
    count = sum(1 for t in verdicts if level in t)     # count verdicts containing this level
    if count > 0:
        print(f"   {level} : {count}")



