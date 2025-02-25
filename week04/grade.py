# Write a program that reads in student precentage mark and prints out corresponding grade
# Author Michal Gondek

percantage = float(input('Enter the percantage:'))
#print (percantage)

# be careful with and and ors
if percantage < 0 or percantage > 100:
    print ('Please eter a number between 0 and 100')

elif percantage < 40:
    print ('Fail')
elif  percantage < 50:
    print ('Pass')
elif percantage < 60:
    print ('Merit1')
elif percantage < 70:
    print ('Merit2')  
else:
    print ('Distinction')



