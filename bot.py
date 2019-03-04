from parser import PageParser
import requests
import time
import hashlib

def main():
    bot = 'bot793791784:AAFL4uP9WstLXxesIYLfkB3a4Kl7gYDA7Xg'
    ids = []
    p = PageParser(url='https://charterflights.r.pl/')
    while True:
        dr = p.find_place('Teneryfa')
        if dr:
            md5 = hashlib.md5(str(dr).encode('utf-8'))
            _id = md5.hexdigest()
            if not _id in ids:
                text = 'Hey! Tenerife found'
                text += '\n'
                text += "<a href='https://charterflights.r.pl/'>link</a>"
                text += '\n'
                text += '€' + dr['price']
                url = f'https://api.telegram.org/{bot}/sendMessage?text={text}&chat_id=143879758&parse_mode=HTML'
                r = requests.get(url).json()
                if r['ok']:
                    ids.append(_id)
        time.sleep(120)

if __name__ == '__main__':
    main()