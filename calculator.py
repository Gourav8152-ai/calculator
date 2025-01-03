import os
import math
import platform  # These imports are needed to clear the terminal based on the operating system.

# Function To determine if a number is a prime number
def prime_no(n: int, b: int) -> int:
    if (n <= 1):
        return False
    if (n <= 3):
        return True
    if (n % 2 == 0 or n % 3 == 0):
        return False
    temp = 5
    while(temp * temp <= n):
        if (n % temp == 0 or n % (temp + 2) == 0):
            return False
        temp = temp + 6

    return True

# Function To Get the log
def log(base: int, x: int) -> int:
        log  = math.log(x, base)
        return (f"\nLog {base} ({x}) = {log:.2f}\n")

# Function to add two numbers
def add(a: int, b: int) -> int:
    return a + b

# Function to subtract the second number from the first
def sub(a: int, b: int) -> int:
    return a - b

# Function to multiply two numbers
def multiply(a: int, b: int) -> int:
    return a * b

# Function to divide the first number by the second
def div(a: int, b: int) -> float:
    if b == 0:
        return "Error: Division by zero"
    return a / b

# Function to get the square of a number
def square(a: int, b: int = 0) -> int:  # b is optional and unused
    return a * a

# Function to calculate the power (a raised to b)
def power(a: int, b: int) -> int:
    return a ** b

# Function to calculate the square root of a number
def root(a: int, b: int = 0) -> float:  # b is optional and unused
    if a < 0:
        return "Error: Cannot calculate square root of a negative number"
    return a ** 0.5

# Function to check if a number is even
def even(a: int, b: int = 0) -> bool:  # b is optional and unused
    return a % 2 == 0

# Function to print descriptions of operations
def print_description(descriptions: list[str]) -> None:
    for i, desc in enumerate(descriptions):
        print(f"{i}: {desc}")
    print(f"{len(descriptions)}: Exit")  # Add an option to exit

# Function to clear the terminal screen based on the operating system
def clear() -> None:
    if platform.system() == "Windows":
        os.system("cls")  # Windows command
    else:
        os.system("clear")  # Command for Linux and macOS

# List of operation functions
operations = [
    add,
    sub,
    multiply,
    div,
    square,
    power,
    root,
    even,
    prime_no
]

# List of descriptions for the operations
descriptions = [
    "Add 2 Numbers together",
    "Subtract 2 Numbers",
    "Multiply 2 Numbers Together",
    "Divide One number By Another",
    "Get the square of a number (Second number is ignored)",
    "Take a power of Number 1 ^ Number 2",
    "Take the square root of a number (Second number is ignored)",
    "Check if a number is even (Second number is ignored)",
    "Check if a numb is a prime number (Second number is ignored)"
]

# Main loop to run the program
def main():
    while True:
        clear()
        print_description(descriptions)
        
        # Get user input for the command
        try:
            command = int(input("Please enter a number to execute a command: "))
            if command == len(descriptions):
                print("Exiting the program.")
                break  # Exit the program if the user selects the last option
            
            if command < 0 or command >= len(operations):
                print("Invalid option. Please try again.")
                input("Press Enter to continue...")
                continue
            
            a = int(input("Please enter the first number: "))
            
            # Only ask for the second number if the operation requires it
            if command in [0, 1, 2, 3, 5]:  # Operations that require two numbers
                b = int(input("Please enter the second number: "))
                result = operations[command](a, b)
            else:
                result = operations[command](a)
            
            print(f"Result: {result}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except Exception as e:
            print(f"An error occurred: {e}")
        
        input("Press Enter to continue...")
