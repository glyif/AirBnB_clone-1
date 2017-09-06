from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
"""
Database engine
"""


class DBStorage:
    __engine = None
    __session = None

    CNC = {
        "Amenity": Amenity,
        "City": City,
        "State": State,
        "Place": Place,
        "Review": Review,
        "User": User
    }

    def __init__(self):
        """

        """
        self.__engine = create_engine('mysql+mysqldb://{:s}:{:s}@{:s}/{:s}'.
                                      format(getenv('HBNB_MYSQL_USER'),
                                             getenv('HBNB_MYSQL_PWD'),
                                             getenv('HBNB_MYSQL_HOST'),
                                             getenv('HBNB_MYSQL_DB')))
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

        Base.metadata.create_all(self.__engine)
        session = sessionmaker(self.__engine)
        self.__session = session()

    def all(self, cls=None):
        """
        returns dictonary with all objects
        :param cls: class
        :return: dictonary with objects
        """
        query_data = {}

        if cls is None:
            for valid_key, valid_class in DBStorage.CNC.items():
                for instance in self.__session.query(valid_class).order_by(valid_class.name):
                    key = type(instance).__name__ + "." + instance.id
                    query_data.update({key: instance})
            return query_data
        else:
            for instance in self.__session.query(DBStorage.CNC[cls]).order_by(DBStorage.CNC[cls].name):
                key = type(instance).__name__ + "." + instance.id
                query_data.update({key: instance})
            return query_data

    def new(self, obj):
        """
        adds new db
        :param obj: object to add
        :return: nothing
        """
        self.__session.add(obj)

    def save(self):
        """
        commits to db
        :return: nothing
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete obj
        :param obj: obj to delete
        :return: nothing
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        reloads with scoped session
        :return: nothing
        """
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(self.__engine)
        self.__session = scoped_session(session)

    def close(self):
        """
        removes session
        :return nothing
        """
        self.__session.remove()
