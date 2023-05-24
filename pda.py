import requests
from bs4 import BeautifulSoup

def parse():
    url_list = []
    try:
        r = requests.get('https://4pda.to')
    except:
        print('[DEBUG] Error get URL 4pda')
        return False
    soup = BeautifulSoup(r.text, "html.parser")
    soup_blok = soup.find_all('article')


    for tmp in soup_blok:
        try:
            link = tmp.find('a')
            link_news = link.get('href')
            text_news = link.get('title')
            text_news = text_news.strip()
            url_list.append(link_news)
        except:
            continue
    return url_list