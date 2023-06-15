import requests
from bs4 import BeautifulSoup


def parse_3dnews():
    try:
        r = requests.get('https://3dnews.ru/news')
    except:
        print('[DEBUG] Error get URL')
        return False
    soup = BeautifulSoup(r.text, "html.parser")
    soup_blok = soup.find_all('div', {'class': "cntPrevWrapper"})
    for tmp in soup_blok:
        try:
            data_news = tmp.find('span').string
            link = tmp.find('a', {'class': "entry-header"})
            link_news = link.get('href')
            if 'http' in link_news:
                pass
            else:
                link_news = 'https://3dnews.ru' + link_news
            text_news = tmp.find('h1').string
            text_news = text_news.replace('\xa0', ' ')
            text_news = text_news.strip()
        except:
            continue
    return True

def parse_4pda():
    t = []
    try:
        r = requests.get('https://4pda.to')
    except:
        print('[DEBUG] Error get URL 4pda')
        return False
    # r.encoding = 'utf8'
    soup = BeautifulSoup(r.text, "html.parser")
    soup_blok = soup.find_all('article')
    for tmp in soup_blok:
        try:
            link = tmp.find('a')
            link_news = link.get('href')
            text_news = link.get('title')
            text_news = text_news.strip()
            t.append((text_news, link_news))

        except:
            continue
    return t

def parse_xaker():

    try:
        r = requests.get('https://xakep.ru/')
    except:
        print('[DEBUG] Error get URL')
        return False
    # r.encoding = 'utf8'
    soup = BeautifulSoup(r.text, "html.parser")
    soup_blok = soup.find_all('div', {'class': "block-article-content-wrapper"})
    for tmp in soup_blok:
        try:
            link = tmp.find('h3', {'class': "entry-title"})
            link_a = link.find('a')
            link_news = link_a.get('href')
            text_news = link.find('span').string
            text_news = text_news.strip()
        except:
            continue
    return True

def parse_opennet():
    try:
        r = requests.get('https://www.opennet.ru/')
    except:
        return False
    soup = BeautifulSoup(r.text, "html.parser")
    soup_blok = soup.find_all('table', {'class': "tlist"})
    for table in soup_blok:
        try:
            tmp = table.find_all('a')
            for link_tmp in tmp:
                try:
                    link_news = link_tmp.get('href')
                    if link_news.split('/')[1] == 'opennews':
                        text_news = link_tmp.get_text()
                        print(link_news)
                        print(text_news)
                    else:

                        continue
                except:
                    continue
        except:
            continue
    return True

t = parse_4pda()
for y in t:
    print(y[0])