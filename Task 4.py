"""
def - declare the function
percentageFunction() - the name of the function
number - argument
return - returns some value
"""

def percentageFunction(number):
    if number < 500:
        return (number * 3) / 100
    elif 500 <= number < 1000:
        return (number * 5) / 100
    elif number <= 1000:
        return (number * 8) / 100

def salaryFunction(number):
    number = 200 + percentageFunction(number)

    return int(number) if number.is_integer() else number

first = int(input('The amount of sales of the first manager: '))
second = int(input('The amount of sales of the first manager: '))
third = int(input('The amount of sales of the first manager: '))

if salaryFunction(first) > salaryFunction(second):
    if salaryFunction(first) > salaryFunction(third):
        print(f'The best manager is first (Prize: $200). Salary: {salaryFunction(first) + 200}\nSalary of the second manager: {salaryFunction(second)}\nSalary of the third manager: {salaryFunction(third)}')
    else:
        print(f'The best manager is second (Prize: $200). Salary: {salaryFunction(second) + 200}\nSalary of the first manager: {salaryFunction(first)}\nSalary of the third manager: {salaryFunction(third)}')
else:
    if salaryFunction(second) > salaryFunction(third):
        print(f'The best manager is second (Prize: $200). Salary: {salaryFunction(second) + 200}\nSalary of the first manager: {salaryFunction(first)}\nSalary of the third manager: {salaryFunction(third)}')
    else:
        print(f'The best manager is third (Prize: $200). Salary: {salaryFunction(third) + 200}\nSalary of the first manager: {salaryFunction(first)}\nSalary of the second manager: {salaryFunction(second)}')