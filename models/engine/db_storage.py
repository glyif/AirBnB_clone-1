from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from models import base_model, amenity, city, place, review, state, user
from models.base_model import Base

class DBStorage:
    __engine = None
    __session = None

    CNC = {
        'BaseModel': base_model.BaseModel,
        'Amenity': amenity.Amenity,
        'City': city.City,
        'Place': place.Place,
        'Review': review.Review,
        'State': state.State,
        'User': user.User
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
                    query_data.update({instance.id: instance})
            return query_data
        else:
            for instance in self.__session.query(cls):
                query_data.update({instance.id: instance})
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
