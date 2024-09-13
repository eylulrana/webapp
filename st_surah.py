import streamlit as st
import matplotlib.pyplot as plt
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
    # word_choice = st.radio("Show:", ('All Words', 'Only Meaningful Words'), key="word_choice_wc_quran")
    if word_choice == 'All Words':
        text_data = ' '.join(all_words)
    else:
        text_data = ' '.join(all_nonstop_words)

    # STATISTICS
    st.header('Surah Statistics')

    total_word_count = len(all_words)
    unique_word_count = len(set(all_words))
    word_freq = Counter(all_words)

    verse_lengths = df['Verse'].str.split().apply(len)

    # Ayet uzunluğu dağılımını bir histogram ile göster
    fig, ax = plt.subplots()
    ax.hist(verse_lengths, bins=range(1, verse_lengths.max() + 2), edgecolor='black')
    ax.set_title('Ayet Uzunluğu Dağılımı')
    ax.set_xlabel('Kelime Sayısı')
    ax.set_ylabel('Ayet Sayısı')



    # # Streamlit'te grafiği göster
    # st.pyplot(fig)

    # # Alternatif olarak bir çubuk grafik
    # st.bar_chart(verse_lengths.value_counts().sort_index())

    # Ayet uzunluğu dağılımını hesapla
    verse_length_counts = verse_lengths.value_counts().sort_index()

    # Daha geniş bir grafik oluşturma ve bar genişliğini küçültme
    fig, ax = plt.subplots(figsize=(10, 6))  # Genişliği artırıyoruz

    # Bar genişliği 0.3 olarak ayarlandı
    ax.bar(verse_length_counts.index, verse_length_counts.values, width=0.3, edgecolor='black')

    # Eksen isimleri ekleme
    ax.set_xlabel('Kelime Sayısı (Ayet Uzunluğu)', fontsize=12)
    ax.set_ylabel('Ayet Sayısı', fontsize=12)

    # Grafik başlığı
    ax.set_title('Ayet Uzunluğu Dağılımı', fontsize=14)

    # Streamlit'te grafiği göster
    st.pyplot(fig)