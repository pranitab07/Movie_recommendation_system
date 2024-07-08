import streamlit as st
import pickle as pk
import pandas as pd

def recommendation(entity):
    entity_index = df[df['title_x'] == entity].index[0]
    distances = similarity[entity_index]
    entity_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[0:10]
    list_re = []
    img = []
    for i in entity_list:
        list_re.append(df.iloc[i[0]].title_x)
        img.append(df.iloc[i[0]].poster_path)
    return list_re, img

st.header("Movie Recommender System")
df = pd.DataFrame(pk.load(open("dataset.pkl", "rb")))
similarity = pk.load(open("similarity.pkl", "rb"))

option = st.selectbox('Select your Movie from here:', df['title_x'])

'You selected:', option

if st.button('Recommend'):
    st.write("Here are the top 10 movies recommended for you!!")
    col1, col2, col3, col4, col5 = st.columns(5)
    list_re, image_urls = recommendation(option)
    
    with col1:
        st.image(image_urls[0], use_column_width=True, caption=list_re[0])
    
    with col2:
        st.image(image_urls[1], use_column_width=True, caption=list_re[1])
    
    with col3:
        st.image(image_urls[2], use_column_width=True, caption=list_re[2])
    
    with col4:
        st.image(image_urls[3], use_column_width=True, caption=list_re[3])
    
    with col5:
        st.image(image_urls[4], use_column_width=True, caption=list_re[4])

    col6, col7, col8, col9, col10 = st.columns(5)
    
    with col6:
        st.image(image_urls[5], use_column_width=True, caption=list_re[5])
    
    with col7:
        st.image(image_urls[6], use_column_width=True, caption=list_re[6])
    
    with col8:
        st.image(image_urls[7], use_column_width=True, caption=list_re[7])
    
    with col9:
        st.image(image_urls[8], use_column_width=True, caption=list_re[8])
    
    with col10:
        st.image(image_urls[9], use_column_width=True, caption=list_re[9])

else:
    pass
