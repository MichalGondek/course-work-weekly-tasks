# This program keeps reading numbers until the use enters 0
# Author: Michal Gondek

numbers = []

number = int(input('enter number (0 to quit): '))

while number != 0:
    numbers.append(numbers)

    number = int(input('enter another (0 to quit): '))

for value in numbers:
    print (value)

average = float(sum(numbers)) / len(numbers)
print (f'The average is {average}')
