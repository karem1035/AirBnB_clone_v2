#!/usr/bin/python3
""" database for file class """
from sqlalchemy import create_engine
form sqlalchemy.orm import sessiomaker, scoped_session
from os import getenv
from models.base_model import Base


class DBStorage:
    """ create a table """
    __engine = None
    __session = None

    def __init__(self):
        """ create a database connection """
        user=getenv("HBNB_MYSQL_USER")
        passwd=getenv("HBNB_MYSQL_PWD")
        host=getenv("HBNB_MYSQL_HOST")
        database=getenv("HBNB_MYSQL_DB")
        env=getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                .format(user, passwd, host, database), pool_pre_ping=TRUE)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)
    def all(self, cls=None):

