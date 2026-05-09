secret_number = 7
guess = int(input("Guess a number between 1 and 10: "))

if guess == secret_number:
    print("You got it right!")
elif guess < secret_number:
    print("Too low!")
else:
    print("Too high!")
print("hi brother")
