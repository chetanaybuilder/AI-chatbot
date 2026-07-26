from google import genai
print("💕😍 love guru by chetanay")
print("-"*30)
client = genai.Client(api_key ="GEMINI_API_KEY")
personality = personality = """You are LoveGuru, a relationship advice bot 
created by Chetanay from BILLIONERLAB. You give warm, honest 
and caring advice about relationships, love, friendships and 
emotions. You speak like a trusted friend, never judge anyone, 
always listen carefully and help people build stronger 
connections. You are wise but talk casually and friendly."""
conversation = personality + "\n\n"
while True: 
    user_input = input("ask me anything about your relationship?") 
    if user_input.lower() == "quit":
        break
    print("your love guru!")
    conversation += f"user: {user_input}\n"
    response = client.models.generate_content(model= "gemini-2.5-flash",contents = conversation)
    conversation += f"bot: {response.text}\n"
    print()
    print(response.text)

    

