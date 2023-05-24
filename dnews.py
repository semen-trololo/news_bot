import requests
from bs4 import BeautifulSoup

def parse():
    url_list = []
    try:
        r = requests.get('https://3dnews.ru/news')
    except:
        print('[DEBUG] Error get URL')
        return False
    soup = BeautifulSoup(r.text, "html.parser")
    soup_blok = soup.find_all('div', {'class': "cntPrevWrapper"})
    for tmp in soup_blok:
        try:
            link = tmp.find('a', {'class': "entry-header"})
            link_news = link.get('href')
            if 'http' in link_news:
                pass
            else:
                link_news = 'https://3dnews.ru' + link_news
                url_list.append(link_news)
        except:
            continue

    return url_list