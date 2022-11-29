import json

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from plotly.subplots import make_subplots

from clients.instagram import InstagramClient
from utils import cache_response


@st.experimental_memo
def connect_client(
    # account_id: str, client_id: str, client_secret: str, access_token: str
) -> InstagramClient:
    """
    """

    instagram = InstagramClient(
        account_id="17841440890050179",
        client_id="645462017039846",
        client_secret="22b685f8d3ff67476b7daae041db9d7e",
        access_token="EAAJLC1Y93eYBAIRJQo9ormINQX3aZA948w5k2vunvNdsRFrx2STQ5a5DUBqUCqVniKfZBBAZAnqbDoJNRZBdxZB051OrXZA86qYKKw9FklUOGXcny7vctkRLKE8eARC1oBnZB4LeVENRHRVgZByihxEmEyihuAeF4orvegAQfZAJXPKDvvnIToLMpNrXZBycI5Ik89EsTG128rGNtnUria7ZAqjxI94e9fWgwEZD",
    )

    return instagram


def main():

    st.set_page_config(layout="wide", initial_sidebar_state="expanded")

    instagram = connect_client()

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
        {"fields": "audience_country,audience_gender_age"},
    )

    with open("data/country_codes.json", encoding="utf-8-sig") as file:
        country_codes = json.load(file)

    audience_country = audience_insights[0]["values"][0]["value"]
    audience_country_names = [
        country_codes[code] if code in country_codes else code
        for code in audience_country.keys()
    ]
    audience_gender_age = audience_insights[1]["values"][0]["value"]

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


if __name__ == "__main__":
    main()

