#!/usr/bin/env python3
"""
Simple Python Calculator
Supports basic arithmetic operations: +, -, x, ÷, %, **
"""

import math

class Calculator:
    """A simple calculator class with basic arithmetic operations."""
    
    def add(self, a, b):
        """Add two numbers."""
        return a + b
    
    def subtract(self, a, b):
        """Subtract b from a."""
        return a - b
    
    def multiply(self, a, b):
        """Multiply two numbers."""
        return a * b
    
    def divide(self, a, b):
        """Divide a by b."""
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a / b
    
    def modulo(self, a, b):
        """Return the remainder of a divided by b."""
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a % b
    
    def power(self, a, b):
        """Raise a to the power of b."""
        return a ** b
    
    def square_root(self, a):
        """Return the square root of a."""
        if a < 0:
            raise ValueError("Cannot calculate square root of negative number!")
        return math.sqrt(a)

def get_number(prompt):
    """Get a valid number from user input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def main():
    """Main calculator interface."""
    calc = Calculator()
    
    print("=== Python Calculator ===")
    print("Available operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulo (%)")
    print("6. Power (**)")
    print("7. Square Root (√)")
    print("8. Quit")
    
    while True:
        print("\n" + "-" * 30)
        choice = input("Choose operation (1-8): ").strip()
        
        if choice == '8':
            print("Thanks for using the calculator!")
            break
        
        if choice not in ['1', '2', '3', '4', '5', '6', '7']:
            print("Invalid choice! Please select 1-8.")
            continue
        
        try:
            if choice == '7':  # Square root only needs one number
                num = get_number("Enter number: ")
                result = calc.square_root(num)
                print(f"√{num} = {result}")
            else:
                num1 = get_number("Enter first number: ")
                num2 = get_number("Enter second number: ")
                
                if choice == '1':
                    result = calc.add(num1, num2)
                    print(f"{num1} + {num2} = {result}")
                elif choice == '2':
                    result = calc.subtract(num1, num2)
                    print(f"{num1} - {num2} = {result}")
                elif choice == '3':
                    result = calc.multiply(num1, num2)
                    print(f"{num1} * {num2} = {result}")
                elif choice == '4':
                    result = calc.divide(num1, num2)
                    print(f"{num1} / {num2} = {result}")
                elif choice == '5':
                    result = calc.modulo(num1, num2)
                    print(f"{num1} % {num2} = {result}")
                elif choice == '6':
                    result = calc.power(num1, num2)
                    print(f"{num1} ** {num2} = {result}")
        
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()