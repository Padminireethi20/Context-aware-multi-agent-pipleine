import json
import os

KNOWLEDGE_FILE = "agent_memory/knowledge.json"
FEEDBACK_FILE = "agent_memory/feedback.txt"

def load_knowledge():
    if not os.path.exists(KNOWLEDGE_FILE): return {}
    try:
        with open(KNOWLEDGE_FILE, "r") as f: return json.load(f)
    except: return {}

def save_knowledge(data):
    os.makedirs("agent_memory", exist_ok=True)
    with open(KNOWLEDGE_FILE, "w") as f:
        json.dump(data, f, indent=4)

def get_user_feedback():
    if not os.path.exists(FEEDBACK_FILE): return ""
    with open(FEEDBACK_FILE, "r") as f:
        feedback = f.read().strip()
    with open(FEEDBACK_FILE, "w") as f: f.write("") # Reset after reading
    return feedback