import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
from collections import Counter
import itertools
from data_provider import *

def app():

    if 'selected_translator' in st.session_state:
        selected_translator = st.session_state['selected_translator']
    df = translators[selected_translator]

    # STOPWORDS REMOVAL
    all_words = list(itertools.chain(*df['Verse'].str.split()))

    df['NoPunc_Verse'] = df['Verse'].apply(remove_punctuation)
    df['NoSW_Verse'] = df['NoPunc_Verse'].apply(lambda x: ' '.join([word for word in x.split() if word.lower() not in custom_stop_words]))

    all_nonstop_words = list(itertools.chain(*df['NoSW_Verse'].str.split()))

    word_choice = st.session_state.get("word_choice", "All Words")
    if word_choice == 'All Words':
        text_data = ' '.join(all_words)
    else:
        text_data = ' '.join(all_nonstop_words)


    # STATISTICS
    st.header('Quran Statistics')

    word_freq = Counter(all_words)
    total_word_count = len(all_words)
    unique_word_count = len(set(all_words))
    formatted_total_word_count = f"{total_word_count:,}"
    formatted_unique_word_count = f"{unique_word_count:,}"
    verse_count = len(df)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(label="Total Surah Count", value=114)

    with col2:
        st.metric(label="Total Verse Count", value=verse_count)

    with col3:
        st.metric(label="Total Word Count", value=formatted_total_word_count)

    with col4:
        st.metric(label="Unique Word Count", value=formatted_unique_word_count)


    # Bar chart
    verse_lengths = df['Verse'].str.split().apply(len)
    # st.bar_chart(verse_lengths.value_counts().sort_index())
    verse_length_counts = verse_lengths.value_counts().sort_index()

    # Plotly ile çizim
    fig = px.bar(
        x=verse_length_counts.index,
        y=verse_length_counts.values,
        labels={'x': 'Word Count of Verse', 'y': 'Number of Verses'},
        title="Distribution of Length of Quranic Verses"
    )

    st.plotly_chart(fig)
