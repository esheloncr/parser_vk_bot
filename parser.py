import requests as r
from bs4 import BeautifulSoup as bs
from parser_vk_bot.db.CRUD import new_url
import time as t
import json

url = "https://pikabu.ru/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}
content = {}
# Получаем urls статей
# сделать функцию для проверки подключения
url_list = []
pikabu = r.get(url, headers=headers)
pikabu_src = pikabu.text
soup = bs(pikabu_src, "html.parser")
soup.prettify()
# Парсим urls
def parse_url():
    get_h2 = soup.findAll(class_="story__title")
    for item in get_h2:
        get_url = item.find("a")
        article_url = get_url.get("href")
        url_list.append(article_url)
    return
# Парсим статью
def article_parse(num):
    article_main = []
    article = r.get(url_list[num], headers=headers)
    article_src = article.text
    soup = bs(article_src, "lxml")
    # Парсим id статьи +
    def parse_id():
        article_id = soup.findAll("article", class_="story")
        for ids in reversed(article_id):
            get_id = ids.get("data-story-id")
        return get_id
    # Парсим h1 тэг
    def parse_h1():
        article_h1 = soup.findAll("h1",class_="story__title")
        for i in article_h1:
            h1 = i.text.replace("\n","")
            article_main.append(h1)
        return h1
    # Парсим текст статьи
    def parse_text():
        article_text = soup.findAll("article",{"data-story-id":"{0}".format(parse_id())})
        for text in article_text:
            try:
                abc = text.find(class_="story-block story-block_type_text")
                bca = abc.text.replace("\n",'')
                article_main.append(bca)
                return bca
            except AttributeError:
                return "No text in Article, only H1"
    # Парсим картинки(если есть, и пропускаем если нету)
    def parse_img():
        article_image = soup.findAll("article", {"data-story-id":"{0}".format(parse_id())})
        for img in article_image:
            try:
                img_url = img.find(class_="story-image__content image-lazy").find("a").get("href")
                article_main.append(img_url)
                return img_url
            except AttributeError:
                return None
    # Проверяем есть-ли видео в статье, если есть - парсим ссылку, если нету - пропускаем
    def parse_video():
        video_urls =[]
        article_video = soup.findAll("article", {"data-story-id": "{0}".format(parse_id())})
        for video in article_video:
            try:
                a = video.find(class_="player").get("data-source")
                article_main.append(a)
                return a
            except AttributeError:
                return None
    new_url(url_list[num], parse_id(), parse_h1(), parse_text(), parse_img(), parse_video())
    return article_main


if __name__ == "__main__":
    counter = 0
    parse_url()
    while counter != len(url_list):
        content.update({url_list[counter]:article_parse(counter)})
        counter += 1
    json.dumps(content, ensure_ascii=False)
