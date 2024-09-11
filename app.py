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
import wc_quran
import wc_surah
import st_quran
import st_surah


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

translators = {
    'Arthur J. Arberry': 'translations/English_Arthur_J_Arberry.csv',
    'Marmaduke Pickthall': 'translations/English_Marmaduke_Pickthall.csv',
    'Muhammad Tahir-ul-Qadri': 'translations/English_Muhammad_Tahir-ul-Qadri.csv',
    'Yusuf Ali': 'translations/English_Yusuf_Ali.csv'
}

# TRANSLATOR SELECTION
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