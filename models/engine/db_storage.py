from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place, PlaceAmenity
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    __engine = None
    __session = None

    CNC = {
        "Amenity": Amenity,
        "City": City,
        "State": State,
        "Place": Place,
        "Review": Review,
        "User": User,
        "PlaceAmenity": PlaceAmenity
    }

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{:s}:{:s}@{:s}/{:s}'.
                                      format(getenv('HBNB_MYSQL_USER'),
                                             getenv('HBNB_MYSQL_PWD'),
                                             getenv('HBNB_MYSQL_HOST'),
                                             getenv('HBNB_MYSQL_DB')))
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(self.__engine)
        self.__session = session()
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        query_data = {}

        if cls is None:
            for valid_key, valid_class in DBStorage.CNC.items():
                for instance in self.__session.query(valid_class):
                    key = type(instance).__name__ + "." + instance.id
                    query_data.update({key: instance})
            return query_data
        else:
            for instance in self.__session.query(cls):
                key = type(instance).__name__ + "." + instance.id
                query_data.update({key: instance})
            return query_data

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(self.__engine)
        self.__session = scoped_session(session)
