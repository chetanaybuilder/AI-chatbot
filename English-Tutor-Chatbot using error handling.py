from google import genai

class EnglishTutorBot:

    def __init__(self):
        self.client = genai.Client(
            api_key="YOUR_API_KEY"
        )

        self.history = []
        self.bot_name = "English Tutor"

    def chat(self):

        while True:

            try:
                user_input = input("You: ")

                if user_input.lower() == "exit":
                    print("Goodbye!")
                    break

                self.history.append(user_input)

                response = self.client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=f"""
                    You are an English tutor.
                    Correct grammar mistakes and help students learn English.

                    Student: {user_input}
                    """
                )

                print(f"{self.bot_name}: {response.text}")

            except Exception as e:
                print("Error:", e)


bot = EnglishTutorBot()
bot.chat()
