# Quiz Creation Activity

# Quiz has 5 questions the user will answer.
# It will keep track of score and give a final result

import time
from rich import print

score = 0

print("Quiz Time!")
time.sleep(2)

# Question 1
print("Question 1: What is [bold red]5 + 6[/bold red]?")
q1_answer = int(input())

if q1_answer > 11:
    print("Too high.")
elif q1_answer < 11:
    print("Too low.")
elif q1_answer == 11:
    print("Correct!")
    score += 1

time.sleep(2)

# Question 2
print("Question 2: What is the [bold blue]capital[/bold blue] of the [bold red]United Kingdom[/bold red]?")
print("A: Worcestershire")
print("B: Edinburgh")
print("or C: London")

q2_answer = input().lower().strip(".")

if q2_answer == "a":
    print("Really?")
elif q2_answer == "b":
    print("Not quite...")
elif q2_answer == "c":
    print("Correct!")
    score += 1
else:
    print("That's not an option.")
time.sleep(2)

# Question 3
print("Question 3: What was [bold blue]Game of the Year[/bold blue] in [bold red]2020[/bold red]?")
q3_answer = input().lower().strip(".,the")

if q3_answer == "last of us part 2" or "last of us part II" or "last of us 2":
    print("Correct!")
    score += 1
elif q3_answer == "hades":
    print("I wish...")
else:
    print("That's not it...")

time.sleep(2)

# Question 4
print("Question 4!")
print("What is the [bold blue]chemical name[/bold blue] of [bold red]H2O2[/bold red]?")
q4_answer = input().lower().strip(".")

if q4_answer == "hydrogen peroxide":
    print("Correct!")
    score += 1
elif q4_answer == "Water":
    print("That's H2O...")
else:
    print("What?")

time.sleep(2)

# Question 5
print("Final Question!")
print("What is a [bold red]group of crows[/bold red] called?")
print("A: A murder")
print("B: A congress")
print("or C: An unkindness")

q5_answer = input().lower().strip(".")

if q5_answer == "a" or "b" or "c":
    print("They're all correct!")
    score += 1
else:
    print("That question was free, how did you mess that up?")

time.sleep(2)

# Show final results
print("The quiz is now over.")

print(f"Your score is [bold blue]{score}/5[/bold blue] or [bold red]{(score / 5) * 100}%[/bold red]")
