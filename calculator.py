#Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
#Perform the operation based on the user's input and print the result.
#Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = input("Enter operand: ")

def calculate(x, y, z):
        if z == '+':
            return x + y
        elif z == '-':
            return x - y
        elif z == '*':
            return x * y
        elif z == '/':
            return x / y
        else:
            return "Invalid operand"

result = calculate(x, y, z)
print(f"{x} {z} {y} = {result}")