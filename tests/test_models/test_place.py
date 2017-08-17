#!/usr/bin/python3
"""
Unit Test for Place Class
"""
import unittest
from datetime import datetime
import models
import json
from os import getenv

User = models.user.User
Place = models.place.Place
BaseModel = models.base_model.BaseModel


class TestPlaceDocs(unittest.TestCase):
    """Class for testing BaseModel docs"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('..... Testing Documentation .....')
        print('........   Place Class   ........')
        print('.................................\n\n')

    def test_doc_file(self):
        """... documentation for the file"""
        expected = '\nPlace Class from Models Module\n'
        actual = models.place.__doc__
        self.assertEqual(expected, actual)

    def test_doc_class(self):
        """... documentation for the class"""
        expected = 'Place class handles all application places'
        actual = Place.__doc__
        self.assertEqual(expected, actual)

    def test_doc_init(self):
        """... documentation for init function"""
        expected = 'instantiates a new place'
        actual = Place.__init__.__doc__
        self.assertEqual(expected, actual)


class TestPlaceInstances(unittest.TestCase):
    """testing for class instances"""

    @classmethod
    def setUpClass(cls):
        """initializes new place for testing"""
        print('\n\n.................................')
        print('....... Testing Functions .......')
        print('.........  Place Class  .........')
        print('.................................\n\n')

        if (getenv("HBNB_TYPE_STORAGE") == "db"):
            cls.dbs_instance = storage
            cls.session = cls.dbs_instance._DBStorage__session
            cls.engine = cls.dbs_instance._DBStorage__engine
            cls.user = User(email="email@email.com", password="yo")
            cls.user_id = cls.user.id
            cls.state = State(name="California")
            cls.state_id = cls.state.id
            cls.city = City(name="Brentwood", state_id=cls.state_id)
            cls.city_id = cls.city.id
            cls.place = Place(city_id=cls.city_id,
                              user_id=cls.user_id, name="House")
            cls.place.save()
            cls.session.commit()
        else:
            cls.user = User()
            cls.user_id = cls.user.id
            cls.state = State()
            cls.state_id = cls.state.id
            cls.city = City()
            cls.city_id = cls.city.id
            cls.place = Place()

    def test_instantiation(self):
        """... checks if Place is properly instantiated"""
        self.assertIsInstance(self.place, Place)

    def test_to_string(self):
        """... checks if BaseModel is properly casted to string"""
        my_str = str(self.place)
        my_list = ['Place', 'id', 'created_at']
        actual = 0
        for sub_str in my_list:
            if sub_str in my_str:
                actual += 1
        self.assertTrue(3 == actual)

    def test_instantiation_no_updated(self):
        """... should not have updated attribute"""
        my_str = str(self.place)
        actual = 0
        if 'updated_at' in my_str:
            actual += 1
        self.assertTrue(0 == actual)

    def test_updated_at(self):
        """... save function should add updated_at attribute"""
        self.place.save()
        actual = type(self.place.updated_at)
        expected = type(datetime.now())
        self.assertEqual(expected, actual)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == "db",
                     "test uses file for storage")
    def test_to_json(self):
        """... to_json should return serializable dict object"""
        self.place_json = self.place.to_json()
        actual = 1
        try:
            serialized = json.dumps(self.place_json)
        except:
            actual = 0
        self.assertTrue(1 == actual)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == "db",
                     "test uses file for storage")
    def test_json_class(self):
        """... to_json should include class key with value Place"""
        self.place_json = self.place.to_json()
        actual = None
        if self.place_json['__class__']:
            actual = self.place_json['__class__']
        expected = 'Place'
        self.assertEqual(expected, actual)

    def test_max_guest_attribute(self):
        """... add max_guest attribute"""
        self.place.max_guest = 3
        if hasattr(self.place, 'max_guest'):
            actual = self.place.max_guest
        else:
            actual = ''
        expected = 3
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main
