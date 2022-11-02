import requests
import bs4


HEADERS = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language': 'ru,en;q=0.9',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Cookie': '_ym_d=1628840683; _ym_uid=1628840683355101683; _ga=GA1.2.137596937.1628841988; fl=ru; hl=ru; feature_streaming_comments=true; _gid=GA1.2.1021543475.1641571984; habr_web_home=ARTICLES_LIST_ALL; _ym_isad=1; visited_articles=599735:203282; SLG_GWPT_Show_Hide_tmp=1; SLG_wptGlobTipTmp=1',
'Host': 'habr.com',
'Referer': 'https://github.com/netology-code/py-homeworks-advanced/tree/master/6.Web-scrapping',
'sec-ch-ua': '"Chromium";v="94", "Yandex";v="21", ";Not A Brand";v="99"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-User': '?1',
'Upgrade-Insecure-Requests':'1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 YaBrowser/21.11.4.727 Yowser/2.5 Safari/537.36'}




MY_TAGS = {'Тестирование IT-систем', 'фото', 'web', 'python'}
response = requests.get('https://habr.com/ru/all/', headers=HEADERS)
response.raise_for_status()
text = response.text
soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article', class_='tm-articles-list__item')


for article in articles:
    hubs = article.find_all('a', class_='tm-article-snippet__hubs-item-link')
    hubs = set(hub.find('span').text for hub in hubs)
    # print(hubs)
    date = article.find('time').text
    title = article.find('a',class_='tm-article-snippet__title-link')
    span_title = title.find('span').text
    # print(span_title)

    if MY_TAGS & hubs:
        href = title['href']
        url = 'https://habr.com' + href
        print(f'Дата: {date} - Заголовок: {span_title} - Ссылка: {url}')