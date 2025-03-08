# Messing with dictionaries 
# Author: Michal Gondek

car = {
    'Make' : 'ford',
    'Model' : 'mondeo',
    'Year' : 2006,
    'Owner' : {
        'name' : 'Michal' ,
        'driver-number' : 1234
}
}

print (car['Year'])
print (car['Owner'].get('name'))

