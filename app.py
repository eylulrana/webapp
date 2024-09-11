import streamlit as st
import pandas as pd
import string
from collections import Counter
import itertools
import plotly.express as px
import numpy as np
import wc_quran
import wc_surah
import st_quran
import st_surah
from data_provider import *


# Sekme başlığı ve simgesi ayarları
st.set_page_config(
    page_title="Quranic Insights",
    page_icon=":closed_book:"  # :open_book:
)


# Quranic Insights
st.sidebar.markdown("# Quranic Insights")

st.sidebar.markdown(""" ### How to Use
**Word Cloud** visualizes the most frequently mentioned words in the Quran and the surah of your choice by sizing 
them according to their frequency of occurrence.
#
### Settings""")


selected_translator = st.sidebar.selectbox("Translator:", list(translators.keys()), key="translator_select_quran")
df = pd.read_csv(translators[selected_translator])


wc_page = st.sidebar.selectbox("Analyze the Word Cloud of:", ["Quran", "Surah"], key="wc_page_select")

if wc_page == "Quran":
    wc_quran.app()
elif wc_page == "Surah":
    wc_surah.app()


st_page = st.sidebar.selectbox("Go to Statistics About:", ["Quran", "Surah"], key="st_page_select")

if st_page == "Quran":
    st_quran.app()
elif st_page == "Surah":
    st_surah.app()



st.sidebar.markdown("""For more information visit [here](https://www.streamlit.io)""")


all_words = list(itertools.chain(*df['Verse'].str.split()))


# STOPWORDS REMOVAL

def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))
df['NoPunc_Verse'] = df['Verse'].apply(remove_punctuation)

# stopwords.txt dosyasından stopwords listesini oku
with open('stopwords.txt', 'r') as f:
    stop_words = {line.strip() for line in f}

additional_stop_words = {"lo", "ye", "hath", "unto", "therein", "upon", "ie", "o", "thee", "thy", "thou", "shall", "may"}

custom_stop_words = stop_words.union(additional_stop_words)
df['NoSW_Verse'] = df['NoPunc_Verse'].apply(lambda x: ' '.join([word for word in x.split() if word.lower() not in custom_stop_words]))

all_nonstop_words = list(itertools.chain(*df['NoSW_Verse'].str.split()))
