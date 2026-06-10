score = 0
name = input("what is your name?")
print("hello" + name + "lets play\n")
#question 1
answer = input("what is  5+5 ? ")
if answer =="10":
    score = score + 1
    print("correct! lets move to next!")
else:
    print("wrong! ans was 10")
#question 2
answer = input("what is capital of the india?")
if answer == "delhi":
    score = score + 1
    print("right! lets move to next")
else:
    print("wrong! ans was delhi")
print("game over " + name +"! your score:" + str(score) + "/2")




