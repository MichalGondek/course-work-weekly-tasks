# Write a program that reads in text file and outputs the number of E's it contains
# Author: Michal Gondek


# Import sys for filename from an argument on the command line
import sys

# Provide file name to program and exit if not text
try:
    filename = sys.argv[1]

    if not filename.endswith('.txt'):
        raise ValueError("File must be a .txt file.")    

# Run program and read number of "e"

    with open(filename, 'r') as f:
        text = f.read()
        count = text.count('e')
        print(count)

# Prompt error if incorrect file : File not found error
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")

# Print error if file name not given
except IndexError:
    print('Error: No File was given. Run the program like this:')
    print(' python .\ argument.py moby-dick.txt')

    
