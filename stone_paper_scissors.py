import random
computer_choice=random.choice(["Stone","Paper","Scissors"])
user_choice=input("Enter your choice out of Stone, Paper, Scissors")
print(f"Your choice :{user_choice}")
print(f"Computer's choice :{computer_choice}")
if user_choice==computer_choice:
    print("It's a draw")
else:
    if (computer_choice=="Stone" and user_choice=="Paper") or (computer_choice=="Paper" and user_choice=="Scissors") or (computer_choice=="Scissors" and user_choice=="Stone"):
        print("You won the game")
    else:
        print("You lost the game")