'''
CS50P Week 0 - Playback Speed
Replaces spaces with ellipsis in a sentence
'''

initial_text = input("Say something and i will slow it down....: ")

# the output is a list
splitted_text = initial_text.split(" ")

# str.join(iterable, /)
slowed_text = "...".join(splitted_text)
print(slowed_text)