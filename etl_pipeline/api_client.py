import requests

class APIClient:
    def __init__(self, url):
        self.url = url

    def fetch_data(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise error if the request fails
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from API: {e}")
            return None
