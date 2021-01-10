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

class Urls(Base):
	__tablename__ = "Urls"
	
	id = Column("id",Integer,primary_key=True,autoincrement=True)
	url = Column("url",String)
	encod = Column("encod",String)
	title = Column("title",String)
	
	def __repr__(self):
		return self.url + " " + self.encod + " " + self.title
		
#Base.metadata.drop_all(engine)
Base.metadata.create_all()