import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import string
from collections import Counter
import itertools
import nltk
from nltk.corpus import stopwords
import plotly.express as px
import seaborn as sns
import numpy as np

def app():

    translators = {
        'Arthur J. Arberry': 'translations/English_Arthur_J_Arberry.csv',
        'Marmaduke Pickthall': 'translations/English_Marmaduke_Pickthall.csv',
        'Muhammad Tahir-ul-Qadri': 'translations/English_Muhammad_Tahir-ul-Qadri.csv',
        'Yusuf Ali': 'translations/English_Yusuf_Ali.csv'
    }

    # TRANSLATOR SELECTION
    # selected_translator = st.sidebar.selectbox("Translator:", list(translators.keys()))
    selected_translator = st.sidebar.selectbox("Translator:", list(translators.keys()), key="translator_select_surah")
    df = pd.read_csv(translators[selected_translator])

    st.sidebar.markdown("""
    #
    For more information visit [here](https://www.streamlit.io)""")


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


    # Surah Word Cloud
    st.header('Surah Word Cloud')
    selected_surah = st.selectbox("Surah Number:", df['Surah'].unique())

    surah_data = df[df['Surah'] == selected_surah]
    text_data = ' '.join(surah_data['Verse'])
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_data)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(plt)