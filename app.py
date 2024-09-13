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

page = st.sidebar.selectbox("Go to:", ["Quran Word Cloud", "Surah Word Cloud", "Quran Statistics", "Surah Statistics"], key="page_select")

if page == "Quran Word Cloud":
    wc_quran.app()
elif page == "Surah Word Cloud":
    wc_surah.app()
elif page == "Quran Statistics":
    st_quran.app()
elif page == "Surah Statistics":
    st_surah.app()


# Kelime seçimi
if "word_choice" not in st.session_state:
    st.session_state["word_choice"] = 'All Words'

word_choice = st.sidebar.radio("Analyze:", ('All Words', 'Only Meaningful Words'), key="word_choice")


st.sidebar.markdown("""For more information visit [here](https://www.streamlit.io)""")
