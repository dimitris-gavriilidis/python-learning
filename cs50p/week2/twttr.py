'''
CS50P Week 2 - Just setting up my twttr
A program that that prompts the user for a str of text and then outputs that same text but with
all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
'''

input_text = input("Input: ")
vowels_text= "AaEeIiOoUu"

for char in input_text:
    if char not in vowels_text:
        print(char, end="")
print()