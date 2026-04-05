# log_classifier.py — Sprint Day 4 (guide version)
# Reads HTTP log lines, sends each to Claude, prints classification table
# Run: python log_classifier.py

import os
import anthropic
from dotenv import load_dotenv        # loads .env file into environment variables

load_dotenv()                         # reads .env and sets ANTHROPIC_API_KEY

# ── SAMPLE LOG LINES ──────────────────────────────
# In production these come from files or SIEM feeds
LOG_LINES = [
    "GET /index.html HTTP/1.1 200 Mozilla/5.0",
    "POST /admin/login HTTP/1.1 401 python-requests/2.28.0",
    "GET /../../../etc/passwd HTTP/1.1 404 curl/7.68.0",
    "GET /api/v1/users HTTP/1.1 200 PostmanRuntime/7.29",
    "POST /wp-login.php HTTP/1.1 200 Nikto/2.1.6",
    "GET /robots.txt HTTP/1.1 200 Googlebot/2.1",
    "POST /xmlrpc.php HTTP/1.1 200 python-requests/2.25.1",
    "GET /phpmyadmin/setup.php HTTP/1.1 404 zgrab/0.x",
    "DELETE /api/users/all HTTP/1.1 403 axios/0.21.1",
    "GET /health HTTP/1.1 200 kube-probe/1.24",
]

# ── CLASSIFIER FUNCTION ───────────────────────────
def classify_log(client, log_line):
    """Send a log line to Claude and get a classification back."""
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",  # fast + cheap model — good for batch tasks
        max_tokens=50,                       # we only need a short answer
        system="""You are a security log classifier.
Classify each log line as exactly one of: BENIGN, SUSPICIOUS, or MALICIOUS.
Respond with ONLY the label and a 3-word reason. Format: LABEL | reason""",
        messages=[
            {"role": "user", "content": log_line}  # the log line is the user message
        ]
    )
    return message.content[0].text.strip()   # extract the text from the response


# ── MAIN ──────────────────────────────────────────
# Initialize the Anthropic client — reads ANTHROPIC_API_KEY from environment
client = anthropic.Anthropic()

print("\n🔍 Classifying logs with Claude...\n")
print(f"{'LOG LINE':<50} {'CLASSIFICATION'}")
print("-" * 80)

for t in LOG_LINES:     # t is the loop variable — never i, never item
    result = classify_log(client, t)

    # colour-code the output based on classification
    label = result.split("|")[0].strip()     # grab just the label before the pipe
    emoji = {"BENIGN": "🟢", "SUSPICIOUS": "🟠", "MALICIOUS": "🔴"}.get(label, "⚪")

    # truncate log line display to 50 chars for readability
    display_log = t[:48] + ".." if len(t) > 50 else t
    print(f"{display_log:<50} {emoji} {result}")

print("\n✅ Done. Claude reasoned about 10 log lines in seconds.")