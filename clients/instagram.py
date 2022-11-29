import requests
import streamlit as st


class InstagramClient:
    def __init__(
        self, account_id: str, client_id: str, client_secret: str, access_token: str
    ):
        self.endpoint_base = "https://graph.facebook.com/v12.0/"
        self.account_id = account_id
        self.client_id = client_id
        self.client_secret = client_secret

        self.access_token = requests.get(
            self.endpoint_base + "oauth/access_token",
            {
                "grant_type": "fb_exchange_token",
                "client_id": client_id,
                "client_secret": client_secret,
                "fb_exchange_token": access_token,
            },
        ).json()["access_token"]

    def __get_response(self, url: str, params: dict) -> dict:
        """
        """

        response = requests.get(url, params)
        return response.json()["data"]

    def get_basic_insights(self, fields: str) -> dict:
        """Retrieves basic media insights based on the specified fields.

        Args:
            fields (str): A comma-delimited string of fields to return. Can include id, 
                caption, media_type, media_url, permalink, thumbnail_url, timestamp, 
                username, like_count, and/or comments_count.

        Returns:
            dict: A dictionary of insight data.

        """
        url = self.endpoint_base + self.account_id + "/media"
        params = {"fields": fields, "access_token": self.access_token}
        return self.__get_response(url, params)

    def get_audience_insights(self, fields: str) -> dict:
        """Retrieves audience insights based on the specified fields.     
        
        Args:
            fields (str): A comma-delimited string of fields to return. Can include
            audience_country, and/or audience_gender_age.

        Returns:
            dict: A dictionary of insight data.

        """
        url = self.endpoint_base + self.account_id + "/insights"
        params = {
            "metric": fields,
            "period": "lifetime",
            "access_token": self.access_token,
        }
        return self.__get_response(url, params)
