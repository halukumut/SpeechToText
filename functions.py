import string
import queue

def remove_punctuation(text):
  translator = str.maketrans('', '', string.punctuation)
  return text.translate(translator)

def whitespace_indexes(text):
    i=0
    index = []
    index.append(0)

    for char in text:
        if char.isspace():
            index.append(i)
        i += 1

    return index

def sentiments(text, indexes):
    sentiments = []
    for i in range(len(indexes)):
        if i != len(indexes) - 1 and i != 0:
            sentiments.append(
                text[indexes[i]+1:indexes[i+1]])
        elif i == 0:
            sentiments.append(
                text[indexes[i]:indexes[i + 1]])
        else:
            sentiments.append(
                text[-(len(text) - indexes[i]):]
            )
    return sentiments

def search_keyword(q, keyword="dinle"):
    sentiment = q.get()
    for sentiment in sentiment:
        if sentiment == keyword:
            return True
