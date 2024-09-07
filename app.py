import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import string
from collections import Counter
import itertools
import nltk
from nltk.corpus import stopwords
# nltk.download('stopwords')


# Arka plan rengini kaydetmek için session_state kullanıyoruz
if 'background_color' not in st.session_state:
    st.session_state['background_color'] = 'white'

# Tema seçenekleri için butonlar
if st.button("Switch to Dark Mode"):
    st.session_state['background_color'] = 'black'
if st.button("Switch to Light Mode"):
    st.session_state['background_color'] = 'white'



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

print(word_freq.most_common(10))



# Quran Word Cloud
st.title('Quran Word Cloud')

text_data = ' '.join(all_words)
# Temadan uygun arka plan rengini alalım
background_color = st.get_option("theme.backgroundColor")
wordcloud = WordCloud(width=800, height=400, background_color=st.session_state['background_color']).generate(text_data)

plt.figure(figsize=(10, 5))
plt.clf()
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

# st.pyplot(plt)
st.pyplot(plt.gcf())



# Surah Word Cloud
st.title('Surah Word Cloud')
selected_surah = st.selectbox("Surah Number:", df['Surah'].unique())

surah_data = df[df['Surah'] == selected_surah]
text_data = ' '.join(surah_data['Verse'])

wordcloud = WordCloud(width=800, height=400, background_color=background_color).generate(text_data)

plt.figure(figsize=(10, 5))
plt.clf()
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')

# st.pyplot(plt)
st.pyplot(plt.gcf())

# df