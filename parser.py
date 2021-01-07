import requests as r
from bs4 import BeautifulSoup as bs
import time as t

url = "https://pikabu.ru/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}
content = {} # записать контент в виде "url статьи":[содержимое статьи]
# Получаем urls статей
# сделать функцию для проверки подключения
pikabu = r.get(url, headers=headers)
pikabu_src = pikabu.text
soup = bs(pikabu_src, "lxml")
soup.prettify()
get_h2 = soup.findAll(class_="story__title")
url_list = []
for item in get_h2:
    get_url = item.find("a")
    article_url = get_url.get("href")
    url_list.append(article_url)
# Парсим статью
article_main = []
article = r.get(url_list[0], headers=headers)
article_src = article.text
soup = bs(article_src, "lxml")
soup.prettify()
# Парсим h1 тэг
article_title = soup.find(class_="story__title-link").contents[0]
article_main.append(article_title)
# Парсим текст статьи
article_text = soup.find(class_="story-block story-block_type_text")
article_main.append(article_text)
# Проверяем есть-ли видео в статье, если есть - парсим ссылку, если нету - пропускаем
#article_video = soup.findAll(class_="story-block story-block_type_video")
article_video = soup.findAll("data-webm")
print(article_video)
"""if article_video == None:
    print("No videos in Article")
else:
    pass """


