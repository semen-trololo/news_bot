import requests
from bs4 import BeautifulSoup

def get_urls_dnews():
    url_list = []
    try:
        r = requests.get('https://3dnews.ru/news')
        if r.status_code != 200:
            print('[DEBUG] ', r.status_code)
            return False
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

def get_urls_opennet():
    url_list = []
    try:
        r = requests.get('https://www.opennet.ru/')
        if r.status_code != 200:
            print('[DEBUG] ', r.status_code)
            return False
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

def get_urls_xakep():
    url_list = []
    try:
        r = requests.get('https://xakep.ru/')
        if r.status_code != 200:
            print('[DEBUG] ', r.status_code)
            return False
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

def get_urls_pda():
    url_list = []
    try:
        r = requests.get('https://4pda.to')
        if r.status_code != 200:
            print('[DEBUG] ', r.status_code)
            return False
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
