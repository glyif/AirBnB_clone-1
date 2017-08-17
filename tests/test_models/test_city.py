#!/usr/bin/python3
"""
Unit Test for City Class
"""
import unittest
from datetime import datetime
import models
import json
from os import getenv
from tests import storage

State = models.state.State
City = models.city.City
BaseModel = models.base_model.BaseModel


class TestCityDocs(unittest.TestCase):
    """Class for testing BaseModel docs"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('..... Testing Documentation .....')
        print('........   City Class   ........')
        print('.................................\n\n')

    def test_doc_file(self):
        """... documentation for the file"""
        expected = '\nCity Class from Models Module\n'
        actual = models.city.__doc__
        self.assertEqual(expected, actual)

    def test_doc_class(self):
        """... documentation for the class"""
        expected = 'City class handles all application cities'
        actual = City.__doc__
        self.assertEqual(expected, actual)

    def test_doc_init(self):
        """... documentation for init function"""
        expected = 'instantiates a new city'
        actual = City.__init__.__doc__
        self.assertEqual(expected, actual)


class TestCityInstances(unittest.TestCase):
    """testing for class instances"""

    @classmethod
    def setUpClass(cls):
        """ initializes new city for testing """
        print('\n\n.................................')
        print('....... Testing Functions .......')
        print('.........  City Class  .........')
        print('.................................\n\n')

        if (getenv("HBNB_TYPE_STORAGE") == "db"):
            cls.dbs_instance = storage
            cls.session = cls.dbs_instance._DBStorage__session
            cls.engine = cls.dbs_instance._DBStorage__engine
            cls.state = State(name="California")
            cls.state_id = cls.state.id
            cls.city = City(name="Fresno", state_id=cls.state_id)
            cls.city.save()
            cls.session.commit()
        else:
            cls.state = State()
            cls.state_id = cls.state.id
            cls.city = City()
                
    def test_instantiation(self):
        """... checks if City is properly instantiated"""
        self.assertIsInstance(self.city, City)

    def test_to_string(self):
        """... checks if BaseModel is properly casted to string"""
        my_str = str(self.city)
        my_list = ['City', 'id', 'created_at']
        actual = 0
        for sub_str in my_list:
            if sub_str in my_str:
                actual += 1
        self.assertTrue(3 == actual)

    def test_instantiation_no_updated(self):
        """... should not have updated attribute"""
        self.city = City()
        my_str = str(self.city)
        actual = 0
        if 'updated_at' in my_str:
            actual += 1
        self.assertTrue(0 == actual)

    def test_updated_at(self):
        """... save function should add updated_at attribute"""
        if (getenv("HBNB_TYPE_STORAGE") != "db"):
            self.city.save()
        actual = type(self.city.updated_at)
        expected = type(datetime.now())
        self.assertEqual(expected, actual)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == "db",
                     "test uses file for storage, not database")
    def test_to_json(self):
        """... to_json should return serializable dict object"""
        self.city_json = self.city.to_json()
        actual = 1
        try:
            serialized = json.dumps(self.city_json)
        except:
            actual = 0
        self.assertTrue(1 == actual)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == "db",
                     "test uses file for storage, not database")
    def test_json_class(self):
        """... to_json should include class key with value City"""
        self.city_json = self.city.to_json()
        actual = None
        if self.city_json['__class__']:
            actual = self.city_json['__class__']
        expected = 'City'
        self.assertEqual(expected, actual)

    def test_id_attribute(self):
        """... add id attribute"""
        expected = self.city.state_id
        if hasattr(self.city, 'state_id'):
            actual = self.city.state_id
        else:
            actual = ''
        self.assertEqual(expected, actual)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db",
                     "this test uses a database for storage")
    def test_city_id(self):
        expected = self.city.id
        actual = self.dbs_instance._DBStorage__session.query(City).filter(
            City.id == expected).one()
        self.assertTrue(expected == actual.id)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db",
                     "this test uses a database for stroage")
    def test_city_attr_name(self):
        expected = self.city.name
        city_id = self.city.id
        city_obj = self.dbs_instance._DBStorage__session.query(City).filter(
            City.id == city_id).one()
        actual = self.dbs_instance._DBStorage__session.query(City.name).filter(
            City.id == city_id).one()
        self.assertTrue(expected == actual.name)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db",
                     "this test uses a database for stroage")
    def test_city_attr_state_id(self):
        expected = self.city.state_id
        city_id = self.city.id
        state_id = self.city.state_id
        city_obj = self.dbs_instance._DBStorage__session.query(City).filter(
            City.state_id == state_id).one()
        actual = self.dbs_instance._DBStorage__session.query(City).filter(
            City.id == city_id).one()
        self.assertTrue(expected == actual.state_id)

if __name__ == '__main__':
    unittest.main
