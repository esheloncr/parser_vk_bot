from .db import Article,Base,Users,engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.inspection import inspect
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = scoped_session(DBSession)


def new_url(url,article_id,title,text,image_url="",video_url=""):
    if image_url == None and video_url == None:
        new_url = Article(url=url,article_id=article_id,title=title,text=text,image_url="No image in article",video_url="No video in article")
        session.add(new_url)
        return session.commit()
    elif image_url == None:
        new_url = Article(url=url, article_id=article_id, title=title, text=text,image_url="No image in article",video_url=video_url)
        session.add(new_url)
        return session.commit()
    elif video_url == None:
        new_url = Article(url=url, article_id=article_id, title=title, text=text, image_url=image_url,video_url="No video in article")
        session.add(new_url)
        return session.commit()
    return "Error"

def show_url(id):
    if id <= len(session.query(Article.url).all()):
        if session.query(Article.image_url).filter_by(id=id).one()[0] == "No image in article" and session.query(Article.video_url).filter_by(id=id).one()[0] == "No video in article":
            a = session.query(Article.title).filter_by(id=id).one()
            b = session.query(Article.text).filter_by(id=id).one()
            return a[0] + "\n" + b[0]
        elif session.query(Article.image_url).filter_by(id=id).one()[0] == "No image in article":
            a = session.query(Article.title).filter_by(id=id).one()
            b = session.query(Article.text).filter_by(id=id).one()
            c = session.query(Article.video_url).filter_by(id=id).one()
            return a[0] + "\n" + b[0] + "\n" + c[0]
        elif session.query(Article.video_url).filter_by(id=id).one()[0] == "No video in article":
            a = session.query(Article.title).filter_by(id=id).one()
            b = session.query(Article.text).filter_by(id=id).one()
            c = session.query(Article.image_url).filter_by(id=id).one()
            return a[0] + "\n" + b[0] + "\n" + c[0]
    else:
        return "No new posts yet"
# Добавить функции для удаления, обновления, и чтения