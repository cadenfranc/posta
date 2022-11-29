import streamlit as st

from clients.tiktok import TikTokClient
from utils import cache_response

tiktok = TikTokClient()

with st.form("Form"):
    st.file_uploader("Photo")
    st.text_area("Caption")

    hashtags = cache_response(tiktok.get_trending_hashtags, {"limit": 15})
    suggested_hashtags = [f'#{hashtag["hashtag_name"]}' for hashtag in hashtags]
    st.multiselect("Suggested Hashtags", suggested_hashtags, suggested_hashtags)

    sounds = cache_response(tiktok.get_trending_sounds, {"limit": 10})
    suggested_sounds = [sound["title"] for sound in sounds]
    st.selectbox("Suggested Sounds", suggested_sounds)

    st.selectbox("Schedule", ["Tuesday, 12:00PM MST", "Tuesday, 5:00PM MST"])
    st.form_submit_button()

