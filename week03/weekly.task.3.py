# Account.py
# Author Michal Gondek

# Input Account Number and Show Only Last 4 Digits

# Taking Variable from user
inputString = input('enter account number ')

# Taking Lenght of Variable
lenghtofString = len(inputString)

# Taking variable lenght and masking all digits with X but the last 4
# Making a string 'XXX...' lenght of account number -4 adding the last 4 digits of the inputString to display masked account number 
mask_number = 'X' * (lenghtofString - 4) + inputString [-4:]

print (f'The account number is {mask_number}') 




