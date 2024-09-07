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
st.title('Quranic Insights')

# Çeviri dosyalarını yükleme
translators = {
    'Arthur J. Arberry': 'English_Arthur_J_Arberry.csv',
    'Marmaduke Pickthall': 'English_Marmaduke_Pickthall.csv',
    'Muhammad Tahir-ul-Qadri': 'English_Muhammad_Tahir-ul-Qadri.csv'
}

# TRANSLATOR SELECTION
selected_translator = st.selectbox("Translator:", list(translators.keys()))
df = pd.read_csv(translators[selected_translator])


# STOPWORDS REMOVAL
def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

# Creating a new column by removing punctuation from the 'Verse' column
df['NoPunc_Verse'] = df['Verse'].apply(remove_punctuation)

# stopwords.txt dosyasından stopwords listesini oku
with open('stopwords.txt', 'r') as f:
    stop_words = {line.strip() for line in f}  # Set olarak oku

# stop_words = set(stopwords.words('english'))
additional_stop_words = {"lo", "ye", "hath", "unto", "therein"}
#, "thee", "thy", "thou", "shall", "may"

custom_stop_words = stop_words.union(additional_stop_words)
df['NoSW_Verse'] = df['NoPunc_Verse'].apply(lambda x: ' '.join([word for word in x.split() if word.lower() not in custom_stop_words]))

# Combining all words into one list
all_words = list(itertools.chain(*df['NoSW_Verse'].str.split()))
word_freq = Counter(all_words)



# Quran Word Cloud
st.title('Quran Word Cloud')

text_data = ' '.join(all_words)
# Temadan uygun arka plan rengini alalım
background_color = st.get_option("theme.backgroundColor")
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_data)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

st.pyplot(plt)



# Surah Word Cloud
st.title('Surah Word Cloud')
selected_surah = st.selectbox("Surah Number:", df['Surah'].unique())

surah_data = df[df['Surah'] == selected_surah]
text_data = ' '.join(surah_data['Verse'])

wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_data)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')

st.pyplot(plt)


most_common_15 = word_freq.most_common(15)

# Word ve frekansları bir DataFrame'e dönüştürün
df_word_freq = pd.DataFrame(most_common_15, columns=['Word', 'Frequency'])
# df_word_freq = pd.DataFrame(word_freq.items(), columns=['Word', 'Frequency'])

# Plotly ile balon grafiği oluştur
fig = px.scatter(df_word_freq, x='Word', y='Frequency', size='Frequency', color='Word',
                 hover_name='Word', size_max=60)

# Streamlit'te göster
st.plotly_chart(fig)




# Örnek veri
data = np.random.rand(10, 10)

# Isı haritası oluştur
fig, ax = plt.subplots()
sns.heatmap(data, ax=ax)

# Streamlit'te göster
st.pyplot(fig)


import plotly.graph_objects as go

# Örnek veri
fig = go.Figure(go.Sankey(
    node=dict(
        label=["Kelime 1", "Kelime 2", "Kelime 3", "Kelime 4"],
        color=["blue", "red", "green", "yellow"]
    ),
    link=dict(
        source=[0, 1, 0, 2],
        target=[2, 3, 3, 1],
        value=[8, 4, 2, 8]
    )))

# Streamlit'te göster
st.plotly_chart(fig)


# df