import random

class NumberGuessingGame:
    def __init__(self):
        self.number = random.randint(1, 100)
        self.attempts = 0
        self.is_game_over = False

    def make_guess(self, guess):
        self.attempts += 1
        
        if guess < self.number:
            return "Too low! Try heigher."
        elif guess > self.number:
            return "Too high! Try lower."
        else:
            self.is_game_over = True
            return f"Congratulations! You guessed the number in {self.attempts} attempts!"

    def play(self):
        print("Welcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100.")
        
        while not self.is_game_over:
            try:
                guess = int(input("Enter your guess: "))
                result = self.make_guess(guess)
                print(result)
            except ValueError:
                print("enter a valid number!")

if __name__ == "__main__":
    game = NumberGuessingGame()
    game.play()
