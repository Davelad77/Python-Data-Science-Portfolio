# Ask the user to enter a sentence
# Determine the length of the sentence
# loop until i = length of sentence
#   if i is even use indexing to make the ith character upper case
#   if i is odd use indexing to make the ith character lower case
#   increment i
# print the new sentence

sentence = input("Please enter a sentence: ")
alt_letter_sentence = ""               # define a new empty variable to contain the new sentence
len_sentence = len(sentence)    # determine string length
i = 0                           # start from 0 as this will be used to index the string

while i < len_sentence:
    if i % 2 == 0:
        alt_letter_sentence += sentence[i].upper()    # convert the ith char to upper case and add to new sentence
    else:
        alt_letter_sentence += sentence[i].lower()    # convert the ith char to lower case and add to new sentence
    i += 1

print(alt_letter_sentence)
print()

# use the sentence previously entered
# convert alternate words to upper then lower case

split_sentence = sentence.split()   # store the sentence as a list having removed the spaces 
len_split_sentence = len(split_sentence)    # determine the number of strings in the list
i = 0
alt_word_sentence = ""

while i < len_split_sentence:    # loop until the counter reaches the number of variables in the list
    if i % 2 == 0:
        alt_word_sentence += split_sentence[i].upper() + " "    #convert even indexed words into upper case
    else:
        alt_word_sentence += split_sentence[i].lower() + " "    #convert odd indexed words into lower case
    i += 1
print(alt_word_sentence)
