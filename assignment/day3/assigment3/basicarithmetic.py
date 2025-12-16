# Function definitions
def numbers_add(num1, num2):
    return num1 + num2

def numbers_substraction(num1, num2):
    return num1 - num2

def numbers_multiplication(num1, num2):
    return num1 * num2

def numbers_division(num1, num2):
    if num2 == 0:
        return "Division by zero not allowed"
    return num1 / num2


# Main program
num1 = int(input("Enter a number: "))
num2 = int(input("Enter second number: "))

s = numbers_add(num1, num2)
sub = numbers_substraction(num1, num2)
mul = numbers_multiplication(num1, num2)
div = numbers_division(num1, num2)

print("Sum:", s)
print("Subtraction:", sub)
print("Multiplication:", mul)
print("Division:", div)
