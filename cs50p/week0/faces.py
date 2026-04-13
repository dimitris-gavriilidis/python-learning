'''
CS50P Week 0 - faces
Converts text emoticons to their emoji equivalents
'''


def convert(text):
    return str(text).replace(":)", "🙂" ).replace(":(", "🙁")


def main():
    initial_text = input("Hello there! How are you?")
    final_text = convert(initial_text)
    print(final_text)

main()