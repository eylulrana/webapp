import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
import itertools
import plotly.express as px
from data_provider import *

def app():

    if 'selected_translator' in st.session_state:
        selected_translator = st.session_state['selected_translator']
    # selected_translator = st.sidebar.selectbox("Translator: wc_quran", list(translators.keys()), key="translator_select_wc_quran")
    df = translators[selected_translator]


    # STOPWORDS REMOVAL
    all_words = list(itertools.chain(*df['Verse'].str.split()))

    df['NoPunc_Verse'] = df['Verse'].apply(remove_punctuation)
    df['NoSW_Verse'] = df['NoPunc_Verse'].apply(lambda x: ' '.join([word for word in x.split() if word.lower() not in custom_stop_words]))

    all_nonstop_words = list(itertools.chain(*df['NoSW_Verse'].str.split()))

    word_choice = st.radio("Show:", ('All Words', 'Only Meaningful Words'), key="word_choice_wc_quran")
    if word_choice == 'All Words':
        text_data = ' '.join(all_words)
    else:
        text_data = ' '.join(all_nonstop_words)    


    # Quran Word Cloud
    st.header('Quran Word Cloud')

    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_data)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(plt)


    # Bubble Chart
    st.header('Quran Bubble Chart')

    word_freq = Counter(all_nonstop_words)
    most_common_25 = word_freq.most_common(25)
    df_word_freq = pd.DataFrame(most_common_25, columns=['Word', 'Frequency'])

    fig = px.scatter(df_word_freq, x='Word', y='Frequency', size='Frequency', color='Word',
                    hover_name='Word', size_max=60)

    st.plotly_chart(fig)


    # Sankey Diagram
    st.header('Quran Sankey Diagram')
    import plotly.graph_objects as go

    # Kelime çiftleri (source → target) oluşturun
    word_pairs = [(all_nonstop_words[i], all_nonstop_words[i+1]) for i in range(len(all_nonstop_words)-1)]

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