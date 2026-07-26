from google import genai

class chatbot:
    def __init__(self, api_key):
        self.client = genai.Client(api_key = api_key)
        self.history = [] 

    def chat(self):
        print("chetanay bot is ready to chat with you!")
        while True:
            user_input = input("ask me anything: ")
            if user_input.lower() == "exit":
                break
            
            self.history.append(user_input)
            response = self.client.models.generate_content(
                model = "gemini-2.5-flash",
                contents = self.history
            )
            print("bot: ", response.text)


bot = chatbot("api_key_here")
bot.chat()
