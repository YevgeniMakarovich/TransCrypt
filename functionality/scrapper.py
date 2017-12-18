from bs4 import BeautifulSoup
from urllib import request


def connect():
    try:
        URL = "https://myfin.by/crypto-rates"
        html = request.urlopen(URL).read()
        soup = BeautifulSoup(html, "html.parser")
        return soup
    except:
        raise Exception('Failure connection')


def prepare_text(text):
    text = text.lower()
    result = ''

    for i in text:
        if i != ' ':
            result += i

    return result


def get_rates_by_name(name):
    name = name.lower()
    soup = connect()
    trs = soup.findAll('tr', {'class': 'odd'}) + soup.findAll('tr', {'class': 'even'})

    for tr in trs:
        currency_name = tr.findAll('a', {'class': 's-bold'})[0].get_text()
        currency_name = prepare_text(currency_name)

        if currency_name == name:
            rates = tr.findAll('td')[1].get_text()
            rates = rates.split(' ')
            rates[0] = rates[0][0:-1]
            rates = list(map(float, rates))
            return rates