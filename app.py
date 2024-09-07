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
# nltk.download('stopwords')


# Quranic Insights
st.markdown("# Quranic Insights")

st.sidebar.markdown(""" ### How to Use
**Word Cloud** visualizes the most frequently mentioned words in the Quran or the surah of your choice by sizing 
them according to their frequency of occurrence.
#
# 
# 
# Settings
""")
# *italik* metin ve [bağlantı](https://www.streamlit.io) ekleyebilirsiniz.

translators = {
    'Arthur J. Arberry': 'translations/English_Arthur_J_Arberry.csv',
    'Marmaduke Pickthall': 'translations/English_Marmaduke_Pickthall.csv',
    'Muhammad Tahir-ul-Qadri': 'translations/English_Muhammad_Tahir-ul-Qadri.csv',
    'Yusuf Ali': 'translations/English_Yusuf_Ali.csv'
}

# If running for the first time, initialize the required fields in session_state
if 'selected_translator' not in st.session_state:
    st.session_state['selected_translator'] = None
    st.session_state['wordcloud_updated'] = False

# TRANSLATOR SELECTION
selected_translator = st.sidebar.selectbox("Translator:", list(translators.keys()))
df = pd.read_csv(translators[selected_translator])

# Update word cloud if translator selection has changed
if selected_translator != st.session_state['selected_translator']:
    st.session_state['selected_translator'] = selected_translator
    st.session_state['wordcloud_updated'] = True


# STOPWORDS REMOVAL
def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

# Creating a new column by removing punctuation from the 'Verse' column
df['NoPunc_Verse'] = df['Verse'].apply(remove_punctuation)

# stopwords.txt dosyasından stopwords listesini oku
with open('stopwords.txt', 'r') as f:
    stop_words = {line.strip() for line in f}  # Set olarak oku

# stop_words = set(stopwords.words('english'))
additional_stop_words = {"lo", "ye", "hath", "unto", "therein", "upon", "ie", "o"}
#, "thee", "thy", "thou", "shall", "may"

custom_stop_words = stop_words.union(additional_stop_words)
df['NoSW_Verse'] = df['NoPunc_Verse'].apply(lambda x: ' '.join([word for word in x.split() if word.lower() not in custom_stop_words]))

# Combining all words into one list
all_words = list(itertools.chain(*df['NoSW_Verse'].str.split()))
word_freq = Counter(all_words)



# Quran Word Cloud
st.header('Quran Word Cloud')

text_data = ' '.join(all_words)
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_data)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')

st.pyplot(plt)



# Surah Word Cloud
st.header('Surah Word Cloud')
selected_surah = st.selectbox("Surah Number:", df['Surah'].unique())

surah_data = df[df['Surah'] == selected_surah]
text_data = ' '.join(surah_data['Verse'])
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_data)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')

st.pyplot(plt)


# Bubble Chart
st.header('Quran Bubble Chart')
most_common_25 = word_freq.most_common(25)
df_word_freq = pd.DataFrame(most_common_25, columns=['Word', 'Frequency'])
# df_word_freq = pd.DataFrame(word_freq.items(), columns=['Word', 'Frequency'])

fig = px.scatter(df_word_freq, x='Word', y='Frequency', size='Frequency', color='Word',
                 hover_name='Word', size_max=60)

st.plotly_chart(fig)


# Sankey Diagram
st.header('Quran Sankey Diagram')
import plotly.graph_objects as go

# Kelime çiftleri (source → target) oluşturun
word_pairs = [(all_words[i], all_words[i+1]) for i in range(len(all_words)-1)]

pair_freq = Counter(word_pairs)
most_common_pairs = pair_freq.most_common(10)

# Sankey diyagramı için verileri hazırlayın
sources = [pair[0][0] for pair in most_common_pairs]  # İlk kelime (source)
targets = [pair[0][1] for pair in most_common_pairs]  # İkinci kelime (target)
values = [pair[1] for pair in most_common_pairs]      # Geçiş sıklığı (value)

# Kelimeleri unique hale getirin (source ve target'lar birleşik liste)
all_nodes = list(set(sources + targets))

# Kaynak ve hedeflerin indeksini alın
source_indices = [all_nodes.index(word) for word in sources]
target_indices = [all_nodes.index(word) for word in targets]

# Sankey diyagramını oluşturun
fig = go.Figure(go.Sankey(
    node=dict(
        label=all_nodes,
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5)
    ),
    link=dict(
        source=source_indices,
        target=target_indices,
        value=values
    )))

st.plotly_chart(fig)