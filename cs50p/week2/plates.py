'''
CS50P Week 2 - Vanity Plates
A program that prompts the user for a vanity plate and then output Valid if meets
all of the requirements or Invalid if it does not. Assume that any letters in the
user’s input will be uppercase.

Rules:
"All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would
be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
“No periods, spaces, or punctuation marks are allowed.”

'''

def check_length(s):
    # check length 2-6 chars
    return 2 <= len(s) <= 6


def check_alphanumeric(s):
    # check if contains alphanumeric meaning alphabet letters (a-z) and numbers (0-9).
    return s.isalnum()


def check_first_letters(s):
    # check if first two chars are letters
    return s[0:2].isalpha()


def get_number_part(s):
    # return the number part. check if numbers only after last letter in leading sequence

    # find index of last letter in the leading sequence
    index_counter = -1
    for char in s:
        if char.isalpha():
            index_counter += 1
            continue
        if char.isdecimal():
            break

    # check after last letter in sequence the 1st number
    first_num_index = index_counter + 1
    remaining_plate = s[first_num_index:]
    return remaining_plate


def check_no_letters_after_numbers(s):
    remaining = get_number_part(s)

    if remaining == "":
        return True
    return remaining.isdecimal()


def check_no_leading_zero(s):
    first_num = get_number_part(s)
    if first_num == "":
        return True
    return int(first_num[0]) != 0


def is_valid(s):
    return (check_length(s) and check_alphanumeric(s) and check_first_letters(s)
            and check_no_letters_after_numbers(s) and check_no_leading_zero(s))


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


main()
