import random

def play_guessing_game():
    """
    The main function of guessing numbers game

    """
    secret_number = random.randint(1, 100)
    max_attempts = 7  
    attempts = 0
    guesses = []  
    
    print("Welcome to the numbers game!")
    print(f"I've thought of a secret number between 1 and 100, and you have a maximum of {max_attempts} chances to guess it.")
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"Please enter your {attempts+1} guess (1-100):"))
            
            if guess < 1 or guess > 100:
                print("Please enter an integer between 1 and 100!")
                continue
                
            # 记录猜测
            attempts += 1
            guesses.append(guess)
            
            # 检查猜测结果
            if guess == secret_number:
                print(f"\nCongratulations! You guessed the secret number {secret_number} on the {attempts} time !")
                print("Your guess history:", " -> ".join(map(str, guesses)))
                return
            elif guess < secret_number:
                print("Tip: The secret number is bigger than you guessed!")
            else:
                print("Tip: The secret number is smaller than you guessed!")
                
        except ValueError:
            print("Invalid input! Please enter an integer!")
    
    print(f"\nUnfortunately, you failed to guess the secret number in {max_attempts} attempts.")
    print(f"The secret number is: {secret_number}")
    print("Your guess history:", " -> ".join(map(str, guesses)))
    if __name__ == "__main__":
        play_guessing_game()