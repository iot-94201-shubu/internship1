def overlapping(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False
a = [1, 6, 3, 2]
b = [4, 7, 3, 8]

print(overlapping(a, b))   # True
