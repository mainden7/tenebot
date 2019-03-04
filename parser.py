import bs4
import requests


class PageParser:
    def __init__(self, url):
        self.url = url
        self.page = self.scrap_url()

    def scrap_url(self):
        p = requests.get(self.url)
        if p.status_code == 200:
            return p.text
        else:
            return False

    def find_place(self, place_name):
        soup = bs4.BeautifulSoup(self.page, 'html.parser')
        trs = soup.findAll('tr', attrs={'class': 'dane-promocji'})
        dr = {}
        for tr in trs:
            a = tr.find('a', attrs={'class': 'clear-link'})
            tx = a.text
            if tx.find(place_name) >= 0:
                dr['t'] = a.text
                dr['href'] = 'https://charterflights.r.pl/' + a['href']
                span = tr.find('span', attrs={'class': 'styl-ceny'})
                dr['price'] = span.text
        return dr