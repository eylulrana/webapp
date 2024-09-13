import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import itertools
from data_provider import *

def app():

    if 'selected_translator' in st.session_state:
        selected_translator = st.session_state['selected_translator']
    df = translators[selected_translator]


    # Surah Word Cloud
    st.header('Surah Word Cloud')
    selected_surah = st.selectbox("Surah Number:", df['Surah'].unique())

    surah_data = df[df['Surah'] == selected_surah]



    # STOPWORDS REMOVAL
    all_words = list(itertools.chain(*surah_data['Verse'].str.split()))

    surah_data['NoPunc_Verse'] = surah_data['Verse'].apply(remove_punctuation)
    surah_data['NoSW_Verse'] = surah_data['NoPunc_Verse'].apply(lambda x: ' '.join([word for word in x.split() if word.lower() not in custom_stop_words]))

    all_nonstop_words = list(itertools.chain(*surah_data['NoSW_Verse'].str.split()))

    word_choice = st.session_state.get("word_choice", "All Words")
    if word_choice == 'All Words':
        text_data = ' '.join(all_words)
    else:
        text_data = ' '.join(all_nonstop_words)

    # text_data = ' '.join(surah_data['Verse'])
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_data)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(plt)