import random

def result(a,b):
    if(a == b):
        return 0
    elif(a == "stone" and b == "scissor"):
        return 1
    elif(a == "paper" and b == "stone"):
        return 1
    elif(a == "scissor" and b == "paper"):
        return 1
    else:
        return -1

options = ["stone", "paper", "scissor"]

score = 0
while True:
    choice = input("Enter stone, paper or scissor:\n")
    if choice.lower() == 'exit':
        break
    
    if choice not in options:
        print("Invalid choice. Please choose Stone, Paper, or Scissor.")
        continue

    computerChoice = random.choice(options)
    print(f"Computer chose: {computerChoice}")

    result_value = result(choice, computerChoice)
    
    if result_value >= 0:
        score = score + result_value
    else:
        print("You lost this round.")
        break

print(f"Your final score is: {score}")