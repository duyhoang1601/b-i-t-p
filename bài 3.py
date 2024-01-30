import random

def guess_random_number():
    n = random.randint(1, 100)
    
    while True:
        try:
            user_guess = int(input("Guess the number between 1 and 100: "))
            
            if user_guess == n:
                print("EXACTLY! You guessed the correct number.")
                break
            elif user_guess < n:
                print(f"{n} < {user_guess}. Try again.")
            else:
                print(f"{n} > {user_guess}. Try again.")

        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    guess_random_number()
