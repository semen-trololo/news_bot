import requests
from bs4 import BeautifulSoup

def parse():
    url_list = []
    try:
        r = requests.get('https://www.opennet.ru/')
    except:
        print('[DEBUG] Error get URL')
        return False
    soup = BeautifulSoup(r.text, "html.parser")
    soup_blok = soup.find_all('table', {'class': "tlist"})
    for table in soup_blok:
        try:
            tmp = table.find_all('a')
            for link_tmp in tmp:
                try:
                    link_news = link_tmp.get('href')
                    url_list.append('https://www.opennet.ru' + str(link_news))
                except:
                    continue
        except:
            continue
    return url_list
