number = int(input('Enter the number: '))

if 1 <= number <= 100:
    if  number % 3 == 0 and  number % 5 == 0:
        print('Fizz Buzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)
else:
    print('Error: The number is out of range')

# Для перевірки:
# for number in range(1, 101):