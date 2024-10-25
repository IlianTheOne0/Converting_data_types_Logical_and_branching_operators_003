number = int(input('Enter the number: '))
a = int(input('Enter an exponent (From 0 to 7 inclusive): '))

if 0 <= a <= 7:
    print(number**a)
else:
    print('Error: The second number is out of range')