# Collatz.py
# Author Michal Gondek

# Ask user to input any positive interger and outputs the successive values of calculation
# Calculate the next value by taking the current value and, if it is even, divide it by two 
# But if it is odd, multiply it ny three and add one

# Input Positive Interger
num = int(input('Please enter a postivie interger:'))

# Print anything < 1 as Not Positive Interger
if num < 1:
    print('Not positive interger:')    

# Anything >1 if even divide by two
# Anything >1 if odd multiply by three and add one 
else:  
    answer = []
    answer.append(num)
    for _ in range(100):
        if num == 1:
            break

        if (num % 2) == 0:
            num = num / 2
            answer.append(num)

        else:
            num = (num * 3) + 1
            answer.append(num)

# Print answer in sequence without and decimal place 
for value in answer:
    print (f' {int(value)}', end=" ")




        





