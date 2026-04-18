'''
CS50P Week 1 - Home Federal Savings Bank
A program to check if an input starts with a specific word or letter
'''

greeting = input("Greeting: ").lower().lstrip()
if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")