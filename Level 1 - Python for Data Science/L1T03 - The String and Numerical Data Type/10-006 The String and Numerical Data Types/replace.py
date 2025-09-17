# save a sentence containing multiple !
# replace ! with a space
# replace lower case characters with upper case characters
# print the sentence in reverse

sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog"
new_sentence = sentence.replace('!', ' ')
print(new_sentence)

new_sentence2 = new_sentence.upper()
print(new_sentence2)

print(new_sentence[::-1])
