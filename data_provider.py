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




# import pandas as pd
# import os

# # Dosya yolları
# files = {
#     'Arthur J. Arberry': 'translations/English_Arthur_J_Arberry.csv',
#     'Marmaduke Pickthall': 'translations/English_Marmaduke_Pickthall.csv',
#     'Muhammad Tahir-ul-Qadri': 'translations/English_Muhammad_Tahir-ul-Qadri.csv',
#     'Yusuf Ali': 'translations/English_Yusuf_Ali.csv'
# }

# # Boş bir translators dict oluşturalım
# translators = {}

# # Her dosya yolunu kontrol edelim ve yükleyelim
# for translator, file_path in files.items():
#     if os.path.exists(file_path):
#         translators[translator] = pd.read_csv(file_path)
#         print(f"Dosya başarıyla yüklendi: {file_path}")
#     else:
#         print(f"Dosya bulunamadı: {file_path}")
