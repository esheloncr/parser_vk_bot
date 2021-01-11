from sqlalchemy import Table,Column,String,Integer,Boolean,create_engine,MetaData,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
engine = create_engine("sqlite:///base.db",echo=True)
Base.metadata.bind = engine


class Users(Base):
	__tablename__ = "Users"
	
	id = Column("id",Integer,primary_key=True,autoincrement=True)
	name = Column("name",String(25),nullable=False)
	password = Column("password",String)
	
	def __repr__(self):
		return self.name

class Article(Base):
	__tablename__ = "Article"
	
	id = Column("id",Integer,primary_key=True,autoincrement=True)
	url = Column("url",String)
	article_id = Column("article_id",Integer)
	title = Column("title",String)
	text = Column("text",String)
	image_url = Column("image",String)
	video_url = Column("video",String)

	def __repr__(self):
		return self.url + " " + self.title + " " + self.image_url + " " + self.video_url
		
#Base.metadata.drop_all(engine)
#Base.metadata.create_all(engine)
