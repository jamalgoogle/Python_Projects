import random 
class RPCGame:
    def __init__(self):
        self.player = ""
        self.choices = ["R", "B", "C"]
        self.computer_choice = random.choice(self.choices)
       
    def display_menu(self):
      #   print("R - rock , B - paper , C - Scissor")
        self.player = input("Player 1 : ").upper()
   
       
    def start_game(self):
       print(f"Computer chose: {self.computer_choice}")
       if self.player not in self.choices:
          print("Please enter valid choice")
          return
         
       if self.player == self.computer_choice:
          print("It's a tie!")
       elif self.player == "R" and self.computer_choice == "C":
            print("You win!")
       elif self.player == "C" and self.computer_choice == "R":
            print("Computer wins!")
       elif self.player == "R" and self.computer_choice == "B":
            print("Computer wins!")
       elif self.player == "B" and self.computer_choice == "R":
            print("You win!")
       elif self.player == "B" and self.computer_choice == "C":
            print("Computer wins!")
       elif self.player == "C" and self.computer_choice == "B":
            print("You win!")
      
   
game = RPCGame()
while True:
     game.display_menu()
     game.start_game()
     game.computer_choice = random.choice(game.choices)