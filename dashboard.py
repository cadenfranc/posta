import json

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from plotly.subplots import make_subplots

from clients.instagram import InstagramClient
from clients.tiktok import TikTokClient
from utils import cache_response


@st.experimental_memo
def connect_client(credentials: dict) -> InstagramClient:
    """
    """

    instagram = InstagramClient(
        account_id=credentials["account_id"],
        client_id=credentials["client_id"],
        client_secret=credentials["client_secret"],
        access_token=credentials["access_token"],
    )

    return instagram


def main():

    st.set_page_config(layout="wide", initial_sidebar_state="expanded")

    tiktok = TikTokClient()

    st.sidebar.title("Posta")
    navigation = st.sidebar.empty()

    with st.sidebar.form("Authentication"):
        profile = st.file_uploader("Profile", type="json")
        st.form_submit_button("Log In")

    if profile is None:
        st.warning("Please upload a valid credentials file.")
        st.stop()

    profile = json.loads(profile.getvalue())
    page = navigation.selectbox("Navigation", ["Dashboard", "Create", "Settings"])

    if page == "Dashboard":
        instagram = connect_client(profile)

        user, posts, followers, following = st.columns([4, 1, 1, 1])
        user.title("modernaholic")
        posts.metric("Posts", 34, 2)
        followers.metric("Followers", 500, 10)
        following.metric("Following", 100, -10)

        media_insights = cache_response(
            instagram.get_basic_insights,
            {
                "fields": "id,caption,media_type,media_url,timestamp,like_count,comments_count"
            },
        )
        media_insights = pd.DataFrame(media_insights)
        media_insights["hashtags"] = media_insights["caption"].apply(
            lambda caption: [word for word in caption.split() if word[0] == "#"]
        )

        audience_insights = cache_response(
            instagram.get_audience_insights,
            {"fields": "audience_country,audience_gender_age,online_followers"},
        )

        with open("data/country_codes.json", encoding="utf-8-sig") as file:
            country_codes = json.load(file)

        audience_country = audience_insights["data"][0]["values"][0]["value"]
        audience_country_names = [
            country_codes[code] if code in country_codes else code
            for code in audience_country.keys()
        ]
        audience_gender_age = audience_insights["data"][1]["values"][0]["value"]

        # st.write(instagram.get_audience_insights("online_followers"))

        fig = make_subplots(rows=1, cols=2)
        fig.add_trace(
            go.Bar(x=audience_country_names, y=list(audience_country.values())),
            row=1,
            col=1,
        )
        fig.add_trace(
            go.Bar(
                x=list(audience_gender_age.keys()), y=list(audience_gender_age.values())
            ),
            row=1,
            col=2,
        )
        fig.update_layout(height=500, width=900)
        st.plotly_chart(fig)

    if page == "Create":
        target_industry = st.selectbox(
            "Target Industry", list(tiktok.industry_codes.keys())
        )
        with st.form("Form"):
            st.file_uploader("Photo")
            st.text_area("Caption")

            hashtags = cache_response(
                tiktok.get_trending_hashtags,
                {"industry": target_industry, "limit": 15},
            )
            suggested_hashtags = [f'#{hashtag["hashtag_name"]}' for hashtag in hashtags]
            st.multiselect("Suggested Hashtags", suggested_hashtags, suggested_hashtags)

            # sounds = cache_response(tiktok.get_trending_sounds, {"limit": 10})
            # suggested_sounds = [sound["title"] for sound in sounds]
            # st.selectbox("Suggested Sounds", suggested_sounds)

            st.selectbox("Schedule", ["Tuesday, 12:00PM MST", "Tuesday, 5:00PM MST"])
            st.form_submit_button()

    if page == "Settings":
        pass


if __name__ == "__main__":
    main()

