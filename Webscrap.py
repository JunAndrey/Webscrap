import requests
import bs4
import datetime, time

base_url = 'https://habr.com'
url = base_url + "/ru/all/"
HEADERS = {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                                                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                                                                      'Chrome/66.0.3359.117 Safari/537.36',
           'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'ru-RU,ru;q=0.9',
           'Upgrade-Insecure-Requests': '1'}

KEYWORDS = ['Дизайн', 'фото', 'web', 'веб', 'приложения', 'python','скоро']
response = requests.get(url, headers=HEADERS)
text = response.text
soup = bs4.BeautifulSoup(text, features="html.parser")
articles = soup.find_all("article")
for article in articles:
    keywords = article.find_all(class_="tm-article-snippet")
    hubs = [hub.text.split() for hub in keywords]
    for hub1 in hubs:
        for i in hub1:
            if i in KEYWORDS:
                title = article.find('h2').find('span').text
                time_ = article.find('time').attrs['title']
                link = article.find(class_='tm-article-snippet__title-link').attrs["href"]
                final_link = base_url + link
                print(f'{time_}  Статья {title} ===> {final_link}')
                link_item = article.find(class_='tm-article-snippet__readmore').attrs["href"]
                paper_link = base_url+link_item
                response1 = requests.get(final_link, headers=HEADERS)
                text1 = response1.text
                soup1 = bs4.BeautifulSoup(text1, features="html.parser")
                paper = soup1.find(class_="article-formatted-body article-formatted-body article-formatted-body_version-2").find_all('p')
                for content in paper:
                    key = content.text.split()
                    for i in key:
                        if i in KEYWORDS:
                            print((f'{time_} <{i}> Статья {title} ===> {final_link}'))



