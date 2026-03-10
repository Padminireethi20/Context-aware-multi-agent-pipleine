from datetime import datetime

def generate_report(knowledge_data):
    with open("Executive_Briefing.md", "w", encoding="utf-8") as f:
        f.write(f"# 🧠 Live Agent Brain State\nUpdate: {datetime.now()}\n\n---\n\n")
        
        # Sort by priority
        sorted_items = sorted(knowledge_data.items(), key=lambda x: x[1].get('priority', '0'), reverse=True)
        
        for topic, data in sorted_items:
            f.write(f"## {topic}\n")
            f.write(f"**Sender:** {data.get('last_sender')}\n\n")
            f.write(f"> {data.get('summary')}\n\n---\n")