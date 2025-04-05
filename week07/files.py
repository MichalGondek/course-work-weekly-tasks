# Write a Program that reads in text file and outputs the number of e's it contains
# Author: Michal Gondek

filename = input("Enter the filename: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read().lower().count("e"))  # Count 'e' and print result
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print(f"Error: {e}")



