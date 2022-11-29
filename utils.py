import streamlit as st


@st.experimental_memo
def cache_response(_method, params: dict = dict()):
    return _method(**params)
