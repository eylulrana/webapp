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

# def get_df():
#     return df