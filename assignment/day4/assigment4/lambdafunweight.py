conversions = [
    lambda t: t * 1000,           # tonnes → kilograms
    lambda kg: kg * 1000,         # kilograms → grams
    lambda g: g * 1000,           # grams → milligrams
    lambda mg: mg * 0.00000220462 # milligrams → pounds
]
tonnes = float(input("Enter weight in tonnes: "))
kg = conversions[0](tonnes)
gm = conversions[1](kg)
mg = conversions[2](gm)
lbs = conversions[3](mg)

print("Weight in kilograms:", kg, "kg")
print("Weight in grams:", gm, "gm")
print("Weight in milligrams:", mg, "mg")
print("Weight in pounds:", lbs, "lbs")
