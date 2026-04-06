# mini_agent.py  - Sprint Day 5
# A minimal agent loop : Claude picks tools, python runs them
# Run: python mini_agent.py

import socket
import json
import anthropic
import requests 
from dotenv import load_dotenv

load_dotenv()


#   --- Tools python can execute -----------
def lookup_ip(ip: str) -> dict:
    """Geolocate an IP address using ip-api.com"""
    try:
        resp = requests.get(f"http://ip-api.com/json/{ip}?fields=country,city,isp,proxy,hosting", timeout=4)
        return resp.json()
    except Exception as e:
        return {"error": str(e) }


def check_port(host: str, port: int) -> dict:
    """ check if a tcp port is opened on a host"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)            # 2-second timeout per port
        result = sock.connect_ex((host, port))  # returns 0 if open, non-zero if closed
        sock.close()
        return {"host": host, "port": port, "Status": "open" if result == 0 else "closed"}
    except Exception as e:
        return {"Error": str(e)}


# Tool dispatch table - maps tool name -> actual Python function
TOOLS = {"lookup_ip": lookup_ip, "check_port": check_port}

#------TOOL SCHENAS (What Claude sees)----------
# Claudes needs to know what tools exist and what arguments they take
TOOL_SCHEMAS = [
    {
        "name": "lookup_ip",
        "description": "Geolocate an IP address and check if its a proxy or hosting provider",
        "input_schema": {
            "type": "object",
            "properties": {"ip": {"type": "string", "description": "The IP address to look up" }},
            "required": ["ip"]
        }
    },
    {
        "name": "check_port",
        "description": "Check if a TCP port is open on a given host or IP",
        "input_schema": {
            "type": "object",
            "Properties": {
                "host": {"type": "string", "description": "Hostname or IP"},
                "port": {"type": "integer", "description": "TCP Port number"},
            },
            "required": ["host", "port"]
        }
    }
]


#-------------THE AGENT LOOP-------------
def run_agent(goal: str):
    """Run the observer -> think -> act loop until Claude says its done. """
    client = anthropic.Anthropic()
    messages= [{"role": "user", "content": goal}]   # start with the user's goal
    print(f"\n Goal: {goal}\n")
    
    while True:                # indefinate loop only exit with break
        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=1024,
            system="You are a cybersecurity analyst agent. use your tools to answer the user's question. Be concise. ",
            tools=TOOL_SCHEMAS,         # tell claude what tools are available
            messages=messages
        )

        # Stop if Claude is done (no more tool calls needed)
        if response.stop_reason == "end_turn":
            for t in response.content:
                if hasattr(t, "text"):
                    print(f"\n Agent: {t.text}")
            break

        # Claude want to call a tool - execute it
        tool_results = []
        for t  in response.content:
            if t.type == "tool_use":
                print(f"calling: {t.name}({t.input})")
                fn = TOOLS[t.name]        # look up the Python function by name
                result = fn(**t.input)      # ** unpacks the dict as keyword argument
                print(f" Result: {result}")
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": t.id,
                    "content": json.dumps(result)       # tool results must be string
                })
        
        # Add Claudesnresponse + tool results to message history, then loop
        messages.append({"role": "assistant", "content": response.content})
        messages.append({"role": "user", "content": tool_results})


# ----------- MAIN------------------

goal = input("what do you want the agent to investigate?"
              "(e.g. 'Is 8.8.8 running a web server?'):")

run_agent(goal)
    




