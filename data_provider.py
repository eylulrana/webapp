import pandas as pd
import string

df_arberry = pd.read_csv('translations/English_Arthur_J_Arberry.csv')
df_picktall = pd.read_csv('translations/English_Marmaduke_Pickthall.csv')
df_tahirulqadri = pd.read_csv('translations/English_Muhammad_Tahir-ul-Qadri.csv')
df_yusufali = pd.read_csv('translations/English_Yusuf_Ali.csv')

translators = {
    'Arthur J. Arberry': df_arberry,
    'Marmaduke Pickthall': df_picktall,
    'Muhammad Tahir-ul-Qadri': df_tahirulqadri,
    'Yusuf Ali': df_yusufali
}

# STOPWORDS REMOVAL
def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

# stopwords.txt dosyasından stopwords listesini oku
with open('stopwords.txt', 'r') as f:
    stop_words = {line.strip() for line in f}

additional_stop_words = {"lo", "ye", "hath", "unto", "therein", "upon", "ie", "o", "thee", "thy", "thou", "shall", "may"}

custom_stop_words = stop_words.union(additional_stop_words)