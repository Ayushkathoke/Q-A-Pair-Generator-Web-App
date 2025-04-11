import streamlit as st


def goto(path:str):
    st.session_state.current_page = path