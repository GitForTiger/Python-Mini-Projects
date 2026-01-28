from random import randint
a=int(input("Enter the lower bound"))
b=int(input("Enter the upper bound"))
guesses=1
x=randint(a,b)
while True:
    y=int(input("Guess the number"))
    if x==y:
        print(f"Yes, the guess is right. You took {guesses} number of guess(es) to reach the correct number {x}.")
        break
    else:
        guesses+=1
        if x>y:
            print("higher number please")
        else:
            print("lower number please")