# system_snapshot.py - Jarvis Sprint Day 3
# Runs OS commands from Python, structures output, write a JSON report
# Run: python system_snapshot.py

import subprocess    # runs shell commands from python
import json           # converts python dicts to JSON and back
import datetime      # for timestamping the report
from pathlib import Path      # modern file path handling


def run_cmd(cmd_list):
    # subprocess.run() executes any shell command
    # capture_output= True captures stdout and stderr
    #text= True decodes bytes to string automatically
    result = subprocess.run(cmd_list, capture_output=True, text=True)

    if result.returncode !=0:       # 0 = success, anything else = error
        return f"Error: {result.stderr.strip()}"       #.strip() removes trailing newlines

    return result.stdout.strip()    # .strip() removes trailing newlines


def collect_snapshot():
    print("collecting system data...")

    # build a dict - each value comes from a real OS command
    snapshot = {
        "timestamp": datetime.datetime.now(datetime.UTC).isoformat() + "Z",
        "hostname": run_cmd(["hostname"]),
        "uptime": run_cmd(["uptime"]),
        "disk_usage": run_cmd(["df", "-h"]),
        "who_is_logged_in": run_cmd(["who"]),
    }
    return snapshot

def write_report(snapshot):
    # Path() creates a cross-platform path object
    output_dir =  Path("snapshots")
    output_dir.mkdir(exist_ok=True)    # creates folder if it doesn't exist

    # build a timestamped filename - / joins path components cleanly
    ts = datetime.datetime.now(datetime.UTC).strftime("%Y%m%d_%H%M%S")
    filename = output_dir / f"snapshot_{ts}.json"

    # write the dic to a JSON file - indent=2 makes it human-readable
    with open(filename, "w") as f:
        json.dump(snapshot, f, indent=2)

    return filename

 # -------------MAIN-------
snapshot = collect_snapshot()
output_file = write_report(snapshot)

print(f" Report writeen to : {output_file}")
print(f"Timestamp : {snapshot['timestamp']}")
print(f"Hostname  : {snapshot['hostname']}")
print(f"Uptime : {snapshot['uptime']}")
print(f"\nOpen {output_file} in Cursor to see the full Json report.")


    