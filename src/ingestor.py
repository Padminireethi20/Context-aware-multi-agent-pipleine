import os

def process_inputs(input_dir="input"):
    if not os.path.exists(input_dir):
        os.makedirs(input_dir)
        return []

    incoming = []
    files = [f for f in os.listdir(input_dir) if f.endswith(".txt")]

    for filename in files:
        path = os.path.join(input_dir, filename)
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            if not lines: continue
            sender = lines[0].replace("FROM:", "").strip() if "FROM:" in lines[0] else "Unknown"
            content = "".join(lines[1:]).strip()
            topic = filename.replace(".txt", "").upper()
            incoming.append({"topic": topic, "sender": sender, "content": content})
        os.remove(path)
    return incoming