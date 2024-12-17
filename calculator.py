import math

print("""Simple Calculator
1. Add
2. Substract
3. Multiply
4. Divide
5. Square
6. Power
7. Square Root
8. Odd/Even
9. Check if Prime
10. Log
11. Remainder
12. Quit""")

while True:
    option = int(input("Enter a number to excute operation: "))

    if option == 12:
        break

    elif option == 1:
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))
        print(number1 + number2)
    
    elif option == 2:
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))
        print(number1 - number2)
   
    elif option == 3:
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))
        print(number1 * number2)
    
    elif option == 4:
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))
        print(number1 / number2)
    
    elif option == 5:
        number1 = float(input("Enter a number: "))
        print(number1**2)
    
    elif option == 6:
        number1 = float(input("Enter the number to find its value: "))
        number2 = float(input("Enter a value of power: "))
        print(number1 ** number2)
    
    elif option == 7:
        number1 = float(input("Enter a number: "))
        print(number1 ** 0.5)
    
    elif option == 8:
        number1 = float(input("Enter a number: "))
        if number1%2==0:
            print("Even")
        else:
            print("Odd")
    
    elif option == 9:
        def prime_no(n) :
            if (n <= 1) :
                return False
            if (n <= 3) :
                return True
            if (n % 2 == 0 or n % 3 == 0) :
                return False
            temp = 5
            while(temp * temp <= n) :
                if (n % temp == 0 or n % (temp + 2) == 0) :
                    return False
                temp = temp + 6

            return True
        number = int(input("Enter a number to check if it is a prime no: "))
        print("You entered {}.".format(number))

        if prime_no(number):
            print("And the number {} is a Prime Number".format(number))
        else:
            print("And the number {} is not a Prime Number.".format(number))

    elif option == 10:
        base = float(input("\nEnter logarithm base: "))
        x    = float(input("Enter number to calculate: "))
        log  = math.log(x, base)
        print(f"\nLog {base} ({x}) = {log:.2f}\n")

    elif option == 11:
        numerator   = float(input("\nEnter number to be divided: "))
        denominator = float(input("Enter number to be divide by: "))
        remainder   = numerator % denominator
        print(f"\nRemainder {numerator}/{denominator} = {remainder}\n")
    else :
        print("Invalid Input")

print("EXIT")
