import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
import itertools
from data_provider import *

def app():

    selected_translator = st.sidebar.selectbox("Translator:", list(translators.keys()), key="translator_select_quran")
    df = translators[selected_translator]

    # STOPWORDS REMOVAL
    all_words = list(itertools.chain(*df['Verse'].str.split()))

    df['NoPunc_Verse'] = df['Verse'].apply(remove_punctuation)
    df['NoSW_Verse'] = df['NoPunc_Verse'].apply(lambda x: ' '.join([word for word in x.split() if word.lower() not in custom_stop_words]))

    all_nonstop_words = list(itertools.chain(*df['NoSW_Verse'].str.split()))

    word_choice = st.radio("Show:", ('All Words', 'Only Meaningful Words'))
    if word_choice == 'All Words':
        text_data = ' '.join(all_words)
    else:
        text_data = ' '.join(all_nonstop_words)


    word_freq = Counter(all_words)