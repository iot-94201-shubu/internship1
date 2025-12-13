#   def func_name():
#       statement(s)

#   def func_name(param):
#       statement(s)

#   def func_name(param1, param2):
#       statement(s)
#       return result

def strlen(str):
    len = 0
    for ch in str:
        len+=1
    return len

str = input("Enter string : ")

len = strlen(str)

print(f"Length = {len}")