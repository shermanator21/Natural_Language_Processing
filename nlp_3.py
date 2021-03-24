import spacy

# Note: shorcyut does not work
# nlp = spacy.load("en")

# The long way
nlp = spacy.load("en_core_web_sm")
# make sure to 'python3 -m spacy download en' in terminal

document = nlp(
    "In 1994, Tim Berners-Lee founded the World Wide Web Consortium (W3C), devoted to developing web technologies"
)

for entity in document.ents:
    print(entity.text, ":", entity.label_)


from pathlib import Path

document1 = nlp(Path("RomeoAndJuliet.txt").read_text())
document2 = nlp(Path("EdwardTheSecond.txt").read_text())

print(document1.similarity(document2))
