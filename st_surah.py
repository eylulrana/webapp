import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import string
from collections import Counter
import itertools
import nltk
import plotly.express as px
import seaborn as sns
import numpy as np
from data_provider import *

def app():

    df = get_df()

    # STOPWORDS REMOVAL
    def remove_punctuation(text):
        return text.translate(str.maketrans('', '', string.punctuation))

    df['NoPunc_Verse'] = df['Verse'].apply(remove_punctuation)

    # stopwords.txt dosyasından stopwords listesini oku
    with open('stopwords.txt', 'r') as f:
        stop_words = {line.strip() for line in f}

    additional_stop_words = {"lo", "ye", "hath", "unto", "therein", "upon", "ie", "o"}
    #, "thee", "thy", "thou", "shall", "may"

    custom_stop_words = stop_words.union(additional_stop_words)
    df['NoSW_Verse'] = df['NoPunc_Verse'].apply(lambda x: ' '.join([word for word in x.split() if word.lower() not in custom_stop_words]))

    # Combining all words into one list
    all_words = list(itertools.chain(*df['NoSW_Verse'].str.split()))
    word_freq = Counter(all_words)
