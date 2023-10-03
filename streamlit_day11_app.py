import streamlit as st

st.header('st.multiselect')

options = st.multiselect(
    'What are your  favorite color',
    ['Green','Yellow','Red','Blue'].,
    ['Yellow','Red']
)

st. write('you selected:',options)