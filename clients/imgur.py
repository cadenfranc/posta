import requests


class ImgurClient:
    def __init__(self, client_id: str, client_secret: str):
        self.client_id = client_id
        self.client_secret = client_secret

    def upload_image(self, image: str):
        payload = {
            "key": self.client_secret,
            "image": image,
        }
        headers = {"Authorization": f"Client-ID {self.client_id}"}
        response = requests.post(
            "https://api.imgur.com/3/upload.json", headers=headers, data=payload
        )
        return response.json()

    def delete_image(self, hash: str):
        headers = {"Authorization": f"Client-ID {self.client_id}"}
        response = requests.delete(
            f"https://api.imgur.com/3/image/{hash}", headers=headers,
        )
        return response.json()
