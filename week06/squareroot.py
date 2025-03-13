# Write a Program that takes a positive floating point number as input and outputs an approx of its square root
# Author: Michal Gondek


# Define function sqrt(x) that calculates the squre root without using built-in functions
def sqrt(x, tolerance=1e-10):

# Check if positive number - raise error if not    
    if x <= 0:
        raise ValueError("Input must be a positive number.")

# User input guess
    guess = x 
    while True:
        newtonmethod = 0.5 * (guess + x / guess) 

# If Difference Between the New and Old Guess is Smaller than Tolerance the Fucntion Returns the Result     
        if abs(newtonmethod - guess) < tolerance: 
            return newtonmethod

 # Update guess if not yet accurate          
        guess = newtonmethod 
    
# Print the Results
x = float(input("Enter a positive number: "))
result = sqrt(x)
print(f"The square root of {x} is approximately {result}")

