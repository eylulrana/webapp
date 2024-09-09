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
import surah
import home


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


page = st.sidebar.selectbox("Analyze:", ["Quran", "Surah"])

if page == "Quran":
    home.app()
elif page == "Surah":
    surah.app()



from streamlit_extras.app_logo import add_logo

def example():
    if st.checkbox("Use url", value=True):
        add_logo("http://placekitten.com/120/120")  # URL'den logo ekleme
    else:
        add_logo("gallery/kitty.jpeg", height=300)  # Dosya yolundan logo ekleme
    st.write("👈 Check out the cat in the nav-bar!")

# Streamlit başlığı ve fonksiyon çağrısı
st.title("Logo Örneği")
example()
