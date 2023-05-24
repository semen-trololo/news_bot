import requests
from bs4 import BeautifulSoup

def parse():
    url_list = []
    try:
        r = requests.get('https://xakep.ru/')
    except:
        print('[DEBUG] Error get URL')
        return False
    soup = BeautifulSoup(r.text, "html.parser")
    soup_blok = soup.find_all('div', {'class': "block-article-content-wrapper"})
    for tmp in soup_blok:
        try:
            link = tmp.find('h3', {'class': "entry-title"})
            link_a = link.find('a')
            link_news = link_a.get('href')
            url_list.append(link_news)
        except:
            continue
    return url_list