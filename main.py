import streamlit as st
from page1 import HomePage
from utl import goto


def Home():
    
    st.set_page_config(page_title="Question Answering Generator",  page_icon="📚", layout="wide", initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    })
    # st.title('Question Answering Generator 📚')
    
    st.title('Question Answering Generator:books:')
    st.markdown('<style>h1{color: orange; text-align: center;}</style>', unsafe_allow_html=True)
    st.subheader('Built for Professionals,Teachers, Students')
    st.markdown('<style>h3{color: pink;  text-align: center;}</style>', unsafe_allow_html=True)

   

    st.button("Go to Ai", icon="🏠", on_click=goto("Main_page")) 
    


if "current_page" not in st.session_state:
    st.session_state.current_page = "home"

if st.session_state.current_page == "home":
    Home()
elif st.session_state.current_page == "Main_page":
    HomePage()


