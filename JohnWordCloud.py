import nltk
import imageio
import pandas as pd
import matplotlib.pyplot as plt

from wordcloud import WordCloud
from textblob import TextBlob
from pathlib import Path
from nltk.corpus import stopwords
from operator import itemgetter

blob = TextBlob(Path("book of John text.txt").read_text())

stops = stopwords.words("english")

more_stops = [
    "thy",
    "ye",
    "verily",
    "thee",
    "hath",
    "say",
    "thou",
    "art",
    "shall",
    "unto",
    "said",
    "therefore",
    "saith",
    "man",
    "one",
    "things",
    "come",
    "world",
    "answer",
    "answered",
    "came",
    "may",
    "disciples",
    "son",
    "also",
    "went",
    "sent",
    "cometh",
    "life",
    "lord",
    "go",
    "even",
    "witness",
    "yet",
    "given",
    "see",
    "word",
    "heard",
    "spake",
    "made",
    "hast",
    "many",
    "truth",
    "believed",
    "saying",
    "day",
    "knew",
    "light",
    "name",
    "us",
    "hour",
    "give",
    "water",
    "works",
    "feast",
    "take",
    "love",
    "might",
    "seen",
    "saw",
    "called",
    "forth",
    "would",
    "another",
    "bear",
    "true",
]
stops += more_stops

items = blob.word_counts.items()
items = [item for item in items if item[0] not in stops]
# print(items)

sorted_items = sorted(items)
sorted_items = sorted(items, key=itemgetter(1), reverse=True)
top15 = sorted_items[:15]
# print(top15)

###getting words into one long string

top15list = []
top15words = []
top15string = ""

for word in top15:
    top15list += word

for i, word in enumerate(top15list):
    if i % 2 == 0:
        top15words.append(word)

for word in top15words:
    top15string += word + " "


##### wordcloud part
mask_image = imageio.imread("mask_circle.png")

wordcloud = WordCloud(colormap="prism", mask=mask_image, background_color="white")

text = top15string

wordcloud = wordcloud.generate(text)

wordcloud = wordcloud.to_file("BookOfJohnCircle.png")

plt.imshow(wordcloud)

print("done")