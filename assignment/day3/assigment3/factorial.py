def factorial(n):
    if n == 0 or n == 1:  
        return 1
    else:
        return n * factorial(n - 1)
def power(base, exponent):
     if exponent == 0: 
        return 1
     else:
        return base * power(base, exponent - 1)
     
num = int(input("Enter a number: "))
print("Factorial =", factorial(num))    
base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))
print("Power =", power(base, exp))


