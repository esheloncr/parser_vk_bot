from .db import Article,Base,Users,engine
from sqlalchemy.orm import sessionmaker
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


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
