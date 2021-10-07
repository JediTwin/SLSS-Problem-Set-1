# Quiz Creation Activity

# Quiz has 5 questions the user will answer.
# It will keep track of score and give a final result

questions = [
    ["What is [bold red]5 + 6?[/bold red]", "11"],
    ["What is the capital of the United Kingdom?", "london"],
    ["What was Game of the Year in 2020?", "last of us part", "last of us"],
    ["What is the [bold blue]chemical name[/bold blue] of [bold red]H2O2?[/bold red]", "hydrogen peroxide"],
    [""]
]

print("Quiz Time!")
time.sleep(2)

for question in questions:
    print(question[0])

    user_answer = input().lower().strip(",.?!the2II")

    if user_answer == question[1] or question[2]:
        print("Correct!")
        score += 1
        time.sleep(2)

    else:
        print("That's wrong")
        time.sleep(2)
