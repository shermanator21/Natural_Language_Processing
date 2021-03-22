from textblob import Word
from textblob.sentiments import NaiveBayesAnalyzer
from textblob import TextBlob

text = "Today is a beautiful day. Tomorrow looks like bad weather."

blob = TextBlob(text)

print(blob)

# this returns each sentence as an object in a list
print(blob.sentences)

# this returns each word as an object in a list
print(blob.words)

# this returns words and their word type (noun, verb, etc.)
print(blob.tags)

# this returns only words that are noun phrases in a list
print(blob.noun_phrases)

# this returns a sentiment object with a polarity (positive 1 to negative -1) and subjectivity (how subjective 0-1)
print(blob.sentiment)

# looking at sentiment seperately (one number)
print(round(blob.sentiment.polarity, 3))
print(round(blob.sentiment.subjectivity, 3))

sentences = blob.sentences

for sentence in sentences:
    print(sentence)
    print(sentence.sentiment)
    print(round(sentence.sentiment.polarity, 3))


blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())

# returns a classification of pos or neg based on which number is higher
print(blob.sentiment)


######################
# language stuff now

print(blob.detect_language())

spanish = blob.translate(to="es")
# es = español en = english

print(spanish)


index = Word("index")

print(index.pluralize())

cacti = Word("cacti")

print(cacti.singularize())

animals = TextBlob("dog cat fish bird").words

print(animals.pluralize())

############################
# spell check and correction
word = Word("theyr")

# returns words that it could mean and how likely it is that word
print(word.spellcheck())

# corrects the word with the most likely word
corrected_word = word.correct()

print(corrected_word)

sentence = TextBlob("Ths sentence has missplled wrds.")

corredted_sentence = sentence.correct()

print(corrected_sentence)
