import json
import os
import pandas as pd
import json_lines
import nltk
from nltk.tokenize import word_tokenize 
from nltk.tokenize import sent_tokenize 
from collections import Counter
from nltk import FreqDist
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import numpy as np
import re;
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.corpus import sentiwordnet as swn
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob
import matplotlib.pyplot as plt

# POS tagger dictionary
pos_dict = {'J':wordnet.ADJ, 'V':wordnet.VERB, 'N':wordnet.NOUN, 'R':wordnet.ADV}
def token_stop_pos(text):
    tags = pos_tag(word_tokenize(text))
    newlist = []
    stop_words = set(stopwords.words('english'))
    for word, tag in tags:
        if word.lower() not in stop_words:
            newlist.append(tuple([word, pos_dict.get(tag[0])]))
    return newlist

# Lemmatizing the input data
wordnet_lemmatizer = WordNetLemmatizer()
def lemmatize(pos_data):
    lemma_rew = " "
    for word, pos in pos_data:
        if not pos:
            lemma = word
            lemma_rew = lemma_rew + " " + lemma
        else:
            lemma = wordnet_lemmatizer.lemmatize(word, pos=pos)
            lemma_rew = lemma_rew + " " + lemma
    return lemma_rew


# function to calculate subjectivity
def getSubjectivity(review):
    return TextBlob(review).sentiment.subjectivity
    # function to calculate polarity
def getPolarity(review):
        return TextBlob(review).sentiment.polarity


# -1 - Negative, 0 - Neutral, 1 - positive 
# function to analyze the reviews
def analysis(score):
    if score < 0:
        return -1
    elif score == 0:
        return 0
    else:
        return 1

#Performing the sentiment analysis
def textblob_senti(dataframe):

    dataframe['POS tagged'] = dataframe['text'].apply(token_stop_pos)
    # print(dataframe.head())

    dataframe['Lemma'] = dataframe['POS tagged'].apply(lemmatize)
    # print(dataframe.head())

    fin_data = pd.DataFrame(dataframe[['text', 'Lemma','date']])

    # fin_data['Subjectivity'] = fin_data['Lemma'].apply(getSubjectivity) 
    fin_data['Polarity'] = fin_data['Lemma'].apply(getPolarity) 
    fin_data['text_blob'] = fin_data['Polarity'].apply(analysis)
    # print(fin_data.head())

    tb_counts = fin_data.text_blob.value_counts()
    # print(tb_counts)
    

    df1 = fin_data.groupby('date')['text_blob'].mean().reset_index()
    # print(df1.head())

    return df1
