import streamlit as st

st.title("👋 Hi, my name is Ian")
st.header("I'm a software engineer and data scientist")

col1, col2 = st.columns(2)

with col1:
    st.image('./images/lion.png')

with col2:
    st.header("🧑‍💻 About Me")
    st.markdown("""
    - School: University of Washington
    - Major: Information Systems
    """)

    st.header("📚 Skills")
    st.markdown("""
    - Python
    - SQL
    - Machine Learning
    """)