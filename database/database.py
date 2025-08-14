from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5435/pomodoro")
Session = sessionmaker(engine)

def get_db_session()-> Session:
    return Session

def new_func():
    pass