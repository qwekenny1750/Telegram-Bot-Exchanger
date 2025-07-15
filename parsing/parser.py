import requests
from bs4 import BeautifulSoup

class ExchangeParser:
    def __init__(self, count: int | float | str, currency_from, currency_to) -> str:
        self.curF = currency_from
        self.curT = currency_to
        self.count = count

    def connection(self):
        self.url = f"https://www.x-rates.com/calculator/?from={self.curF}&to={self.curT}&amount={self.count}"

        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        html = requests.get(self.url, headers=headers)
        bs = BeautifulSoup(html.text, 'lxml')
        return bs
    
    def parse(self):
        try:
            bs = self.connection()
            cur = (
                bs
                .find('span', {'class': 'ccOutputRslt'})
                .get_text()
            
                )
            return cur
        except:
            return "Server error. Try again or later"



