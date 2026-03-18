import requests

class NSE_BSE_Integration:
    def __init__(self):
        self.base_url = 'https://example-api.com'

    def get_market_data(self):
        response = requests.get(f'{self.base_url}/marketdata')
        return response.json() if response.status_code == 200 else None