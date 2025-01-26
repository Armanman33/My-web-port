import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image('D:\Gongzuo\My-webproject\images2\Hell.png', width=600)

with col2:
    st.title('Introduction')
    # Fix the syntax for reading the text file
    with open('intro.txt', 'r', encoding='utf-8') as file:
        intro_text = file.read()
    st.info(intro_text)  # Changed `content` to `intro_text`

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""

st.write(content2)

# Create columns for app display
col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

# Load data from CSV file
df = pd.read_csv('data.csv', sep=';')

with col3:
    for index, row in df[:4].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images2/' + row['image'])

with col4:
    for index, row in df[4:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images2/' + row['image'])
