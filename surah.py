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

def app():
    st.title('Sure Analiz Sayfası')