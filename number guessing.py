import random
attempts = 0
best_score = [0] 
def ran_num():
    return random.randint(1, 100)

print("Welcome to the number guessing game!")
x = ran_num()
while True:
    try:
        guess = int(input("Type a number: "))
        if guess > 100 or guess < 1:
            print("*Type a number between 1 and 100*")
            continue
        else:
            attempts += 1
    except ValueError:
        print("*Type an integer*")
        continue
    
    if guess == x:
        print(f"Congratulations, {guess} is the correct answer")
        print(f"Number of attempts: {attempts}")
        if best_score[0] == 0 or attempts < best_score[0]:
            best_score[0] = attempts
            print(f"New best score: {best_score[0]} attempts")
        else:
            print(f"Best score: {best_score[0]} attempts")
        ask = input("Do you want to play again? (y/n): ")
        if ask.lower() == "y":
            x = ran_num()
            attempts = 0
            continue
        elif ask.lower() == "n":
            print("Thanks for playing!")
            break
        else:
            print("*Invalid input, exiting the game*")
            break
    elif guess > x:
        print("Lower")
    elif guess < x:
        print("Higher")

