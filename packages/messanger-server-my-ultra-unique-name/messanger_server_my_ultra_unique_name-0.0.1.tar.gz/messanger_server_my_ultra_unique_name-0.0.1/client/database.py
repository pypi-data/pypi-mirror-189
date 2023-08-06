from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from datetime import datetime

engine = create_engine('sqlite:///server_db.db3', echo=False)
BASE = declarative_base()


class User(BASE):
    __tablename__ = 'user'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)
    last_login = Column('last_login', DateTime)

    @staticmethod
    def login_user(curr_session, username, ip, port):
        curr_time = datetime.now()
        # смотрим, есть ли уже такой юзер в базе
        user_query = curr_session.query(User).filter(User.name == username).first()
        if user_query:
            user_query.last_login = curr_time
        else:
            new_user = User(name=username, last_login=curr_time)
            curr_session.add(new_user)
        curr_session.commit()

        curr_user_id = curr_session.query(User).filter(User.name == username).first().id
        # вписываем в активных юзеров
        new_active_user = ActiveUser(
            user_id=curr_user_id,
            ip_address=ip,
            port=port,
            last_login=curr_time
        )
        curr_session.add(new_active_user)

        # записываем в историю логинов
        new_history_item = LoginHistory(user_id=curr_user_id, date_time=curr_time, ip=ip, port=port)
        curr_session.add(new_history_item)
        curr_session.commit()

    @staticmethod
    def logout_user(curr_session, username):
        curr_user = curr_session.query(User).filter(User.name == username).first()
        curr_session.query(ActiveUser).filter(ActiveUser.user_id == curr_user.id).delete()
        curr_session.commit()


class ActiveUser(BASE):
    __tablename__ = 'active_user'
    id = Column('id', Integer, primary_key=True)
    user_id = Column('user_id', Integer, ForeignKey('user.id'))
    ip_address = Column('ip_address', String)
    port = Column('port', Integer)
    last_login = Column('last_login', DateTime)


class LoginHistory(BASE):
    __tablename__ = 'login_history'
    id = Column('id', Integer, primary_key=True)
    user_id = Column('user_id', Integer, ForeignKey('user.id'))
    date_time = Column('date_time', DateTime)
    ip = Column('ip', String)
    port = Column('port', Integer)


BASE.metadata.create_all(engine)
create_session = sessionmaker(bind=engine)

if __name__ == '__main__':
    session = create_session()
    User.login_user(session, 'username', '192.168.0.1', 5000)
    session.close()
