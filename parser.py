import requests as r
from bs4 import BeautifulSoup as bs
import time as t
import json

url = "https://pikabu.ru/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}
content = {}  # записать контент в виде "url статьи":[содержимое статьи]
# Получаем urls статей
# сделать функцию для проверки подключения
url_list = []
pikabu = r.get(url, headers=headers)
pikabu_src = pikabu.text
soup = bs(pikabu_src, "lxml")
soup.prettify()
get_h2 = soup.findAll(class_="story__title")
for item in get_h2:
    get_url = item.find("a")
    article_url = get_url.get("href")
    url_list.append(article_url)
# Парсим статью
def article_parse(num):
    article_main = []
    article = r.get(url_list[num], headers=headers)
    article_src = article.text
    soup = bs(article_src, "lxml")
    # Парсим id статьи +
    article_id = soup.findAll("article", class_="story")
    for ids in reversed(article_id):
        get_id = ids.get("data-story-id")
    # Парсим h1 тэг
    article_title = soup.find("span", class_="story__title-link").contents
    article_main.append(article_title)
    # Парсим текст статьи
    #article_text = soup.find(class_="story-block story-block_type_text").contents
    article_text = soup.findAll("article",{"data-story-id":"{0}".format(get_id)})
    for text in article_text:
        abc = text.find(class_="story-block story-block_type_text").contents
    article_main.append(abc)
    # Парсим картинки(если есть, и пропускаем если нету)
    article_image = soup.findAll("article", {"data-story-id":"{0}".format(get_id)})
    for img in article_image:
        try:
            img_url = img.find(class_="story-image__content image-lazy").find("a").get("href")
            article_main.append(img_url)
        except AttributeError:
            print("No image in Article")
    # Проверяем есть-ли видео в статье, если есть - парсим ссылку, если нету - пропускаем
    video_urls =[]
    article_video = soup.findAll(class_="player")
    if len(article_video) == 0:
        print("No video in Article")
    else:
        for gg in article_video:
            video_urls.append(gg.get("data-webm"))
        if video_urls[0] == None:
            print("No video URL")
        else:
            video_url = video_urls[0]
            article_main.append(video_url)
    return article_main

counter = 0
while counter != 2:
    content.update({url_list[counter]:article_parse(counter)})
    counter += 1
json.dumps(content, ensure_ascii=False)
print(content)
#разобраться, где приходят не те данные



