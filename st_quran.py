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



    # 3 KPI kartını yan yana göstermek için 'st.columns()' kullanıyoruz
    col1, col2, col3 = st.columns(3)

    # Toplam kelime sayısı
    with col1:
        st.metric(label="Toplam Kelime Sayısı", value=total_word_count)

    # Benzersiz kelime sayısı
    with col2:
        st.metric(label="Benzersiz Kelime Sayısı", value=unique_word_count)

    # En sık geçen kelimenin frekansı
    most_common_word, most_common_word_count = word_freq.most_common(1)[0]
    with col3:
        st.metric(label=f"En Sık Geçen Kelime: {most_common_word}", value=most_common_word_count)



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



    total_word_count = len(all_words)
    unique_word_count = len(set(all_words))
    word_freq = Counter(all_words)