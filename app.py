import streamlit as st
import pandas as pd
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

selected_translator = st.sidebar.selectbox("Translator:", list(translators.keys()), key="translator_select_app")
# df = translators[selected_translator]
st.session_state['selected_translator'] = selected_translator

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


# Kelime seçimi
if "word_choice" not in st.session_state:
    st.session_state["word_choice"] = 'All Words'

word_choice = st.radio("Show:", ('All Words', 'Only Meaningful Words'), key="word_choice")