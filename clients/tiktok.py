import requests


class TikTokClient:
    def __init__(self, country_code: str = "US"):
        self.endpoint_base = (
            "https://ads.tiktok.com/creative_radar_api/v1/popular_trend/"
        )
        self.headers = {"anonymous-user-id": "f3b3ee63e76240d6aee25ff4ba9dd256"}
        self.country_code = country_code
        self.industry_codes = {
            "Apparel & Accessories": 22000000000,
            "Baby, Kids & Maternity": 12000000000,
            "Beauty & Personal Care": 14000000000,
            "Education": 10000000000,
            "Financial Services": 13000000000,
            "Food & Beverage": 27000000000,
            "Games": 25000000000,
            "News & Entertainment": 23000000000,
            "Pets": 19000000000,
            "Sports & Outdoor": 28000000000,
            "Tech & Electronics": 15000000000,
            "Travel": 17000000000,
            "Vehicle & Transportation": 11000000000,
        }

    def get_trending_hashtags(self, industry: str = None, limit: int = 50) -> list:
        """Retrieves the top hashtags by popularity.

        Args:
            industry (str, optional): The hashtag industry. If not provided, queries 
                from all industries.
            limit (int, optional): The number of records to return.

        Returns:
            list: A list of hashtag dictionary objects.

        """

        url = self.endpoint_base + "hashtag/list?period=7"
        params = {
            "page": 1,
            "limit": limit,
            "sort_by": "popular",
            "country_code": self.country_code,
        }

        if industry is not None:
            try:
                params["industry_id"] = self.industry_codes[industry]
            except KeyError:
                industries = list(self.industry_codes.keys())
                raise KeyError(f"Industry not found. Must be one of {industries}.")

        response = requests.get(url, params, headers=self.headers)
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
        url = self.endpoint_base + "sound/list?period=7"
        params = {
            "page": 1,
            "limit": limit,
            "search_mode": 1,
            "rank_type": trend,
            "country_code": self.country_code,
        }
        response = requests.get(url, params, headers=self.headers)
        return response.json()["data"]["sound_list"]
