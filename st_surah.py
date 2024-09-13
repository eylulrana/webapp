import streamlit as st
import plotly.express as px
from collections import Counter
import itertools
from data_provider import *

def app():

    if 'selected_translator' in st.session_state:
        selected_translator = st.session_state['selected_translator']
    df = translators[selected_translator]

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



    # STATISTICS
    st.header('Surah Statistics')

    word_freq = Counter(all_words)
    total_word_count = len(all_words)
    unique_word_count = len(set(all_words))
    formatted_total_word_count = f"{total_word_count:,}"
    formatted_unique_word_count = f"{unique_word_count:,}"
    verse_count = len(surah_data)
    average_verse_length = round(total_word_count / verse_count)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(label="Total Verse Count", value=verse_count)

    with col2:
        st.metric(label="Total Word Count", value=formatted_total_word_count)

    with col3:
        st.metric(label="Unique Word Count", value=formatted_unique_word_count)

    with col4:
        st.metric(label="Average Word Count of Verses", value=average_verse_length)


    # Bar chart
    verse_lengths = surah_data['Verse'].str.split().apply(len)
    # st.bar_chart(verse_lengths.value_counts().sort_index())
    verse_length_counts = verse_lengths.value_counts().sort_index()

    # Plotly ile çizim
    fig = px.bar(
        x=verse_length_counts.index,
        y=verse_length_counts.values,
        labels={'x': 'Word Count of Verse', 'y': 'Number of Verses'},
        title="Distribution of Verse Lengths of the Surah"
    )

    st.plotly_chart(fig)