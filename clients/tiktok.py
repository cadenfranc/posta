import requests


class TikTokClient:
    def __init__(self, country_code: str = "US"):
        self.endpoint_base = (
            "https://ads.tiktok.com/creative_radar_api/v1/popular_trend/"
        )
        self.headers = {"anonymous-user-id": "f3b3ee63e76240d6aee25ff4ba9dd256"}
        self.country_code = country_code

    def get_trending_hashtags(self, industry: str = None, limit: int = 50) -> list:
        """Retrieves the top hashtags by popularity.

        Args:
            industry (str, optional): The hashtag industry. If not provided, queries 
                from all industries.
            limit (int, optional): The number of records to return.

        Returns:
            list: A list of hashtag dictionary objects.

        """
        url = (
            self.endpoint_base
            + "hashtag/list?period=7&page=1"
            + f"&limit={limit}&sort_by=popular&country_code={self.country_code}"
        )
        response = requests.get(url, headers=self.headers)
        return response.json()["data"]["list"]

    def get_trending_sounds(self, trend: str = "popular", limit: int = 3) -> list:
        """Retrieves the top trending sounds.

        Args:
            trend ("popular" or "surging", optional): The ranking method used for 
                retrieval. If "popular", returns the most popular sounds in region. 
                If "surging", returns sounds that have recently experienced rapid growth.
            limit (int, optional): The number of records to return.

        Returns:
            list: A list of sound dictionary objects.

        """
        url = (
            self.endpoint_base
            + "sound/list?period=7&page=1"
            + f"&limit={limit}&search_mode=1&rank_type={trend}&country_code={self.country_code}"
        )
        response = requests.get(url, headers=self.headers)
        return response.json()["data"]["sound_list"]
