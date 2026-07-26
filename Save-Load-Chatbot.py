from google import genai
import json
import os

client = genai.Client(api_key="paste_your_api_key")

# 1. Load data from file first
history_data = []
if os.path.exists("memory.json"):
    with open("memory.json", "r") as f:
        try:
            history_data = json.load(f)
        except json.JSONDecodeError:
            history_data = [] # File was empty, start fresh

# 2. Create chat with history
model = client.chats.create(model="gemini-2.0-flash", history=history_data)

print("--- BuilderChetanay Bot Ready ---")

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break
    
    response = model.send_message(user_input)
    print("Bot:", response.text)
    
    # 3. Save the actual history object
    with open("memory.json", "w") as f:
        json.dump(model.get_history(), f) # Use get_history()
