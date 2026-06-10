from google import genai

# ╔══════════════════════════════════════════╗
# ║       CHETANAYBUILDER AI v1.0            ║
# ║       By Chetanay | BILLIONERLAB         ║
# ║       Day 2 - June 7, 2026               ║
# ╚══════════════════════════════════════════╝

client = genai.Client(api_key="add_key_here")
history = []
 
print("╔══════════════════════════════════════╗")
print("║      CHETANAYBUILDER AI v1.0         ║")
print("║      By Chetanay | BILLIONERLAB      ║")
print("╚══════════════════════════════════════╝")
print()

while True:
    user_input = input("  You → ")
    
    if user_input.lower() == "quit":
        print()
        print("  👋 Bye! Keep building - BILLIONERLAB")
        print()
        break
    
    history.append(user_input)
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_input
    )
    
    print()
    print("  🤖 Bot →", response.text)
    print("  " + "─"*40)
    print()