RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

def print_menu():
   
    print(f"{BLUE}\nHello! Welcome to Simple Calculator{RESET}")
    print(f"{YELLOW}1. Add{RESET}")
    print(f"{YELLOW}2. Subtract{RESET}")
    print(f"{YELLOW}3. Multiply{RESET}")
    print(f"{YELLOW}4. Divide{RESET}")
    print(f"{RED}5. Exit{RESET}")

def get_number(prompt):
 
    while True:
        try:
            return float(input(f"{CYAN}{prompt}{RESET}"))
        except ValueError:
            print(f"{RED}Invalid input. Please enter a number.{RESET}")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        print(f"{RED}Error: Division by zero is not allowed.{RESET}")
        return None
    return x / y

def calculator():
   
    while True:
        print_menu()
        choice = input(f"{CYAN}Select an operation (1-5): {RESET}")

        if choice == '5':
            print(f"{GREEN}Exiting the calculator. Goodbye!{RESET}")
            break

        if choice in ['1', '2', '3', '4']:
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")

            if choice == '1':
                result = add(num1, num2)
                operation = "+"
            elif choice == '2':
                result = subtract(num1, num2)
                operation = "-"
            elif choice == '3':
                result = multiply(num1, num2)
                operation = "*"
            elif choice == '4':
                result = divide(num1, num2)
                operation = "/"

            
            if result is not None:
                print(f"{MAGENTA}Result: {WHITE}{num1} {operation} {num2} = {result}{RESET}")
        else:
            print(f"{RED}Invalid choice. Please select a number between 1 and 5.{RESET}")
        
        
        repeat = input(f"{CYAN}Do you want to perform another calculation? (yes/no): {RESET}").strip().lower()
        if repeat != 'yes':
            print(f"{GREEN}Exiting the calculator. Goodbye!{RESET}")
            break


calculator()