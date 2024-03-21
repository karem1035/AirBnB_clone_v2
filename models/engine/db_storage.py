#!/usr/bin/python3
""" database for file class """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
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
                .format(user, passwd, host, database), pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)
    def all(self, cls=None):
        """ return the dictionary of an object """
        objects= {}
        if cls:
            query =self.__session.query(cls)
            for element in query:
                key = "{}.{}".format(type(element).__name__, element.id)
                objects[key] = element
        else:
            classes = [State, City, User, Place, Review, Amenity]
            for obj in classes:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                objects[key] = obj
        return (objects)
    def new(self, obj):
        """Adds the object to the current database session"""
        self.__session.add(obj)
    def save(self):
        """Commits all changes of the current database session"""
        self.__session.commit()
    def delete(self, obj=None):
        """Deletes obj from the current database session"""
        if obj:
            self.__session.delete(obj)
    def reload(self):
        """Creates all tables in the database"""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
            expire_on_commit=False))
        self.__session = Session()
    def close(self):
        """calls remove()"""
        self.__session.close()
