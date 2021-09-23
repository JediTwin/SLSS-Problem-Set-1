# Quiz Creation Activity

# Quiz has 5 questions the user will answer.
# It will keep track of score and give a final result

import time

score = 0

print("Quiz Time!")
time.sleep(2)

# Question 1
print("Question 1: What is 5 + 6?")
q1_answer = int(input())

if q1_answer > 11:
    print("A little too high there.")
elif q1_answer < 11:
    print("Just a bit higher.")
else:
    print("Correct!")
    score += 1

time.sleep(2)

# Question 2
print("Question 2: What is the capital of the United Kingdom?")
print("A: Worcestershire")
print("B: Edinburgh")
print("or C: London")

q2_answer = input().upper()

if q2_answer == "A":
    print("Really?")
elif q2_answer == "B":
    print("Not quite...")
elif q2_answer == "C":
    print("Correct!")
    score += 1
else:
    print("That's not an option.")
time.sleep(2)

# Question 3
print("Question 3: What was Game of the Year in 2020?")
q3_answer = input().lower()

if q3_answer == "the last of us part 2" or "the last of us part II" or "the last of us 2":
    print("Correct!")
    score += 1
elif q3_answer == "hades":
    print("I wish...")

time.sleep(2)