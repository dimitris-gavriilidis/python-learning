'''
CS50P Week 2 - camelCase
A program that prompts the user for the name of a variable in camel case
and outputs the corresponding name in snake case.

name -> name
firstName -> first_name
preferedFirstName -> prefered_first_name
'''


def camel_to_snake(text):

    snake_text = []
    snake_text.append(text[0].lower())

    for char in text[1:]:
        if char.islower():
            snake_text.append(char)
        else:
            snake_text.append("_")
            snake_text.append(char.lower())

    return "".join(snake_text)


def main():
    camel = input("camelCase: ")
    final = camel_to_snake(camel)
    print(final)


if __name__ == "__main__":
    main()