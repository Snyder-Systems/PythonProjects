
weight = int(input('Enter a Weight in kilos or pounds: '))
unit = input('Enter "L" for pounds or "K" for grams : ')

if unit.upper() == "L":
    converted = weight * 0.45
    print (f"This is {converted} kilos")
elif unit.upper() == "K":
    converted = weight / 0.45
    print(f"This is {converted} pounds")
else:
    print('Invalid input')

    