'''
CS50P Week 1 - Deep Thought
A program to check if statements based on user's specific input
'''

answer = input("What is the answer to the Great Question of Life, the Universe, and Everything?").lower().strip()
if answer == "42" or answer == "forty-two" or answer =="forty two":
    print("Yes")
else:
    print("No")
