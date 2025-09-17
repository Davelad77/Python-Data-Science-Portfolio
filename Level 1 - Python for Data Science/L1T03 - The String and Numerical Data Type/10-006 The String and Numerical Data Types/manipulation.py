# request the user enter a sentence
# calculate and print the length of the sentence
# find the last letter in the sentence and replace it with @ then print the new sentence
# print the last 3 characters of the sentence backwards
# create a new word by combining the first 3 characters of the sentence and the last 2 characters of the sentence

str_manip = input("Please enter a sentence: ")
print(len(str_manip))
last_char = str_manip[-1]
new_str_manip = str_manip.replace(last_char, '@')
print(new_str_manip)
print(str_manip[-1:-4:-1])
new_word = str_manip[:3] + str_manip[-2:]
print(new_word)