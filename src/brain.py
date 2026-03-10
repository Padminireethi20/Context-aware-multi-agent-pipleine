import requests
import os

def call_ollama(prompt):
    url = "http://localhost:11434/api/generate"
    model = os.getenv("OLLAMA_MODEL", "mistral")
    payload = {"model": model, "prompt": prompt, "stream": False}
    try:
        response = requests.post(url, json=payload, timeout=90)
        return response.json().get('response', "").strip()
    except: return None

def reason_and_merge(topic, sender, new_content, old_summary, feedback):
    """
    Intelligent Merge: 
    Takes the old state + new data + feedback and returns ONE fresh summary.
    """
    prompt = f"""
    You are a Knowledge Consolidation Agent.
    
    TOPIC: {topic}
    PREVIOUS SUMMARY: {old_summary}
    NEW DATA FROM {sender}: {new_content}
    USER FEEDBACK: {feedback if feedback else "None"}

    TASK:
    - Create a SINGLE unified summary (max 3 sentences).
    - If the new data updates or contradicts the previous summary, update it.
    - Do NOT list the items. Merge them into a cohesive story.
    - Incorporate the user feedback if present.
    
    OUTPUT: Just the updated summary text.
    """
    
    new_summary = call_ollama(prompt)
    
    p_prompt = f"Rate urgency (1-10) for this: {new_summary}. Return ONLY the number."
    priority = call_ollama(p_prompt) or "5"
    priority = "".join(filter(str.isdigit, priority))[:1] or "5"

    return {
        "summary": new_summary,
        "priority": priority,
        "last_sender": sender
    }