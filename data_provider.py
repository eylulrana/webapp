import pandas as pd

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
"""
import os

# Dosya yolları
arberry_path = 'translations/English_Arthur_J_Arberry.csv'
picktall_path = 'translations/English_Marmaduke_Pickthall.csv'
tahirulqadri_path = 'translations/English_Muhammad_Tahir-ul-Qadri.csv'
yusufali_path = 'translations/English_Yusuf_Ali.csv'

# Dosyaların var olup olmadığını kontrol ediyoruz
if os.path.exists(arberry_path):
    df_arberry = pd.read_csv(arberry_path)
else:
    print(f"File not found: {arberry_path}")

if os.path.exists(picktall_path):
    df_picktall = pd.read_csv(picktall_path)
else:
    print(f"File not found: {picktall_path}")

if os.path.exists(tahirulqadri_path):
    df_tahirulqadri = pd.read_csv(tahirulqadri_path)
else:
    print(f"File not found: {tahirulqadri_path}")

if os.path.exists(yusufali_path):
    df_yusufali = pd.read_csv(yusufali_path)
else:
    print(f"File not found: {yusufali_path}")

# Eğer dosyalar bulunmuşsa, onları 'translators' dict içinde saklayalım
translators = {
    'Arthur J. Arberry': df_arberry,
    'Marmaduke Pickthall': df_picktall,
    'Muhammad Tahir-ul-Qadri': df_tahirulqadri,
    'Yusuf Ali': df_yusufali
}
"""