import json

score = 0

print("----- Welcome to Chetanay Quiz Game -----")

with open("quiz.json", "r") as file:
    questions = json.load(file)

for q in questions:
    answer = input(q["question"] + " ")

    if answer.lower() == q["answer"].lower():
        print("Correct! 🎉")
        score += 1
    else:
        print("Wrong!")
        print("Correct answer:", q["answer"])

print("\n----- Quiz Finished -----")
print(f"Your score is: {score}/{len(questions)}")


