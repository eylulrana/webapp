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


# Quranic Insights
st.markdown("# Quranic Insights")

st.sidebar.title('Analyze')
page = st.sidebar.selectbox("Sayfa Seç", ["Quran", "Surah"])

if page == "Quran":
    home.app()
elif page == "Surah":
    surah.app()