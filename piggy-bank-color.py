class BankAccount:
    def __init__(self):
        self.balance = 0
        # ANSI color codes
        self.GREEN = '\033[92m'
        self.RED = '\033[91m'
        self.YELLOW = '\033[93m'
        self.BLUE = '\033[94m'
        self.RESET = '\033[0m'
        self.BOLD = '\033[1m'

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.GREEN}Deposited: ${amount:.2f}{self.RESET} Succesfully")

    def withdraw(self, amount):
        if self.balance < amount:
            print(f"{self.RED}Insufficient balance!{self.RESET}")
            print(f"Current balance: {self.YELLOW}${self.balance:.2f}{self.RESET}")
            return False
        else:
            self.balance -= amount
            print(f"{self.RED}Withdrawn: ${amount:.2f}{self.RESET} Succesfully")
            return True

    def show_balance(self):
        if self.balance < 0:
            color = self.RED
        elif self.balance < 100:
            color = self.YELLOW
        else:
            color = self.GREEN
        
        print(f"\n{self.BOLD}Current balance: {color}${self.balance:.2f}{self.RESET}")

    def choose_oper(self):
        print(f"\n{self.BLUE}{self.BOLD}--- Bank Account Menu ---{self.RESET}")
        print(f"{self.GREEN}1. Deposit{self.RESET}")
        print(f"{self.YELLOW}2. Withdraw{self.RESET}")
        print(f"{self.BLUE}3. Check Balance{self.RESET}")
        print(f"{self.RED}4. Exit{self.RESET}")
        
        choose = int(input(f"\n{self.BOLD}Choose an operation (1-4): {self.RESET}"))
        
        if choose == 1:
            amount = float(input("Enter amount to deposit: "))
            self.deposit(amount)
        elif choose == 2:
            amount = float(input("Enter amount to withdraw: "))
            self.withdraw(amount)
        elif choose == 3:
            self.show_balance()
        elif choose == 4:
            print(f"{self.RED}Thank you for using our banking system!{self.RESET}")
            return False
        else:
            print(f"{self.RED}Invalid option!{self.RESET}")
        return True


# Main program
person = BankAccount()
running = True
while running:
    running = person.choose_oper()

print(f"\n{Fore.CYAN}Final balance: {Fore.GREEN if person.balance >= 0 else Fore.RED}${person.balance:.2f}{Style.RESET_ALL}")