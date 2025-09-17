import spacy

nlp = spacy.load('en_core_web_sm')

# Create a list holding two garden path sentences
garden_path_sentences = ["The complex houses married and single soldiers and their families.",
                         "The horse raced past the barn fell."]

print(garden_path_sentences)
print()

# Add task defined sentences to the original list
garden_path_sentences.extend(["Mary gave the child a Band-Aid.",
                              "That Jill is never here hurts.",
                              "The cotton clothing is made of grows in Mississippi."]
                             )

print(garden_path_sentences)
print()

# Tokenise each sentence in the list and print
for sentence in garden_path_sentences:
    doc = nlp(sentence)
    print([(token.text, token.orth_, token.orth) for token in doc])

print()

# Loop through each sentence and print named entities
for sentence in garden_path_sentences:
    doc = nlp(sentence)
    print(f"\nSentence: {sentence}")
    
    # Named Entities
    if doc.ents:
        print("Named Entities:")
        for ent in doc.ents:
            print(f"  - {ent.text} ({ent.label_})")
    else:
        print("No named entities found.")

print()

entity_gpe = spacy.explain("GPE")
print(f"FAC:{entity_gpe}")

''' spaCy only found named entities in the third, fourth and fifth sentence because the first two
are garden path sentences so contain no entities by design.
The third and fourth sentences contained one detected entity each, both categorised as 'PERSON'
which is fairly obvious both being names.
The final sentence contains the entity 'Mississippi' which is categorised as 'GPE'. According to
spacy.explain this means "FAC:Countries, cities, states"
'''
