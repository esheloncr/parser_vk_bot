from .db import Users,Urls, engine, Base
from sqlalchemy.orm import sessionmaker
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


def new(table_name,url=None,encod=None,title=None,name=None,password=None):
    if table_name == Users:
        new_user = Users(name=name, password=password)
        session.add(new_user)
        return session.commit()
    elif table_name == Urls:
        new_url = Urls(url=url, encod=encod, title=title)
        session.add(new_url)
        return session.commit()
    else:
        return "No table name"


def update(table_name,name=None,password=None,changed=None):
    if table_name == Users:
        user = session.query(Users).filter_by(id=id).first()
        if changed == name:
            user.name = name
            session.add(user)
            return session.flush()
        elif changed == password:
            user.password = password
            session.add(user)
            return session.flush()
        else:
            return "No change field detected"