from google import genai
client = genai.Client(api_key ="api_key")
conversation =""
print("===chetanaybuilder===")
print("-"*30)
while True:
    user_input = input("hey boy how can i help you today?")
    if user_input.lower() =="quit":
        break
    print("bye-billionerlab")
    conversation += f"user: {user_input}\n"
    response = client.models.generate_content(model="gemini-2.5-flash",contents=conversation)
    conversation += f"bot: {response.text}\n"
    print("bot:",response.text)
    print("-"*30)
                                                                                          
    



