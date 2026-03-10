import os
import sys
from dotenv import load_dotenv

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.ingestor import process_inputs
from src.memory_mgr import load_knowledge, save_knowledge, get_user_feedback
from src.brain import reason_and_merge
from src.formatter import generate_report

load_dotenv()

def main():
    print("--- 🤖 Agentic State-Sync Started ---")
    
    # 1. Load Everything
    knowledge = load_knowledge()  # This is your existing Key-Value JSON
    new_mails = process_inputs("input")
    feedback = get_user_feedback()

    if not new_mails and not feedback:
        print("No new input.")
        return

    # 2. Process Files
    # If topic exists in 'knowledge', we summarize it with new info
    for mail in new_mails:
        topic = mail['topic']
        print(f"Updating key: {topic}")
        
        # GET OLD VALUE
        old_summary = knowledge.get(topic, {}).get("summary", "No previous context.")
        
        # BRAIN SUMMARIZES & UPDATES
        updated_data = reason_and_merge(
            topic, mail['sender'], mail['content'], old_summary, feedback
        )
        
        # UPDATE THE KEY (This is the "State Overwrite" you want)
        knowledge[topic] = updated_data

    # 3. Handle Feedback-only Updates
    if feedback and not new_mails:
        for topic in knowledge:
            knowledge[topic] = reason_and_merge(
                topic, knowledge[topic]['last_sender'], "Apply Feedback", knowledge[topic]['summary'], feedback
            )

    # 4. Save and Print
    save_knowledge(knowledge) # Saves the clean, summarized JSON
    generate_report(knowledge)
    print("--- 🏁 State Successfully Merged ---")

if __name__ == "__main__":
    main()