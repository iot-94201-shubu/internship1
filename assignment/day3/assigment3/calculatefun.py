def add(a,b):
    return a+b
def substract(a,b):
    return a-b
def multipl(a,b):
    return a*b
def division(a,b):
    return a/b
def calculator(operand1,operand2,opration):
      return opration(operand1,operand2)
#main function
print("add:",calculator(6,3,add))
print("substractor:",calculator(6,3,substract))
print("multiplication:",calculator(6,3,multipl))
print("division:",calculator(6,3,division))