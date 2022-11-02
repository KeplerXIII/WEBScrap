from constants import HEADERS
import requests
import bs4

KEYWORDS = {'дизайн', 'фото', 'web', 'python'}

response = requests.get('https://habr.com/ru/all/', headers=HEADERS)
response.raise_for_status()
text = response.text
soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article', class_='tm-articles-list__item')

for article in articles:
    hubs = article.find_all('a', class_='tm-article-snippet__hubs-item-link')
    hubs = set(hub.find('span').text for hub in hubs)
    date = article.find('time').text
    title = article.find('a', class_='tm-article-snippet__title-link')
    span_title = title.find('span').text

    if KEYWORDS in hubs:
        href = title['href']
        url = 'https://habr.com' + href
        print(f'Дата: {date} - Заголовок: {span_title} - Ссылка: {url}')
