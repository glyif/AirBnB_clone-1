#!/usr/bin/python3
"""
Unit Test for User Class
"""
import unittest
from datetime import datetime
import models
import json
from os import getenv
from tests import storage

User = models.user.User
BaseModel = models.base_model.BaseModel


class TestUserDocs(unittest.TestCase):
    """Class for testing User Class docs"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('..... Testing Documentation .....')
        print('........   User  Class   ........')
        print('.................................\n\n')

    def test_doc_file(self):
        """... documentation for the file"""
        expected = '\nUser Class from Models Module\n'
        actual = models.user.__doc__
        self.assertEqual(expected, actual)

    def test_doc_class(self):
        """... documentation for the class"""
        expected = 'User class handles all application users'
        actual = User.__doc__
        self.assertEqual(expected, actual)

    def test_doc_init(self):
        """... documentation for init function"""
        expected = 'instantiates a new user'
        actual = User.__init__.__doc__
        self.assertEqual(expected, actual)


class TestUserInstances(unittest.TestCase):
    """testing for class instances"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('....... Testing Functions .......')
        print('.........  User  Class  .........')
        print('.................................\n\n')

    def setUp(self):
        """initializes new user for testing"""
        self.user = User()
        self.user.email = ""
        self.user.password = ""
        self.user.first_name = ""
        self.user.last_name = ""
        if (environ(HBNB_TYPE_STORAGE) == "db"):
            DBStorage.__init__()

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db",
                     "only need to tearDown if database used")
    def tearDown(self):
        """tearDown to close __session and __engine when using database"""
        DBStorage.__session.close()
        DBStorage.__engine.close()

    def test_instantiation(self):
        """... checks if User is properly instantiated"""
        self.assertIsInstance(self.user, User)

    def test_to_string(self):
        """... checks if BaseModel is properly casted to string"""
        my_str = str(self.user)
        my_list = ['User', 'id', 'created_at']
        actual = 0
        for sub_str in my_list:
            if sub_str in my_str:
                actual += 1
        self.assertTrue(3 == actual)

    def test_instantiation_no_updated(self):
        """... should not have updated attribute"""
        self.user = User()
        my_str = str(self.user)
        actual = 0
        if 'updated_at' in my_str:
            actual += 1
        self.assertTrue(0 == actual)

    def test_updated_at(self):
        """... save function should add updated_at attribute"""
        self.user.save()
        actual = type(self.user.updated_at)
        expected = type(datetime.now())
        self.assertEqual(expected, actual)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == "db",
                     "test uses file for storage")
    def test_to_json(self):
        """... to_json should return serializable dict object"""
        self.user_json = self.user.to_json()
        actual = 1
        try:
            serialized = json.dumps(self.user_json)
        except:
            actual = 0
        self.assertTrue(1 == actual)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == "db",
                     "test uses file for storage")
    def test_json_class(self):
        """... to_json should include class key with value User"""
        self.user_json = self.user.to_json()
        actual = None
        if self.user_json['__class__']:
            actual = self.user_json['__class__']
        expected = 'User'
        self.assertEqual(expected, actual)

    def test_email_attribute(self):
        """... add email attribute"""
        self.user.email = "bettyholbertn@gmail.com"
        if hasattr(self.user, 'email'):
            actual = self.user.email
        else:
            actual = ''
        expected = "bettyholbertn@gmail.com"
        self.assertEqual(expected, actual)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db',
                     "this test uses a database for storage")
    def test_amenity_id(self):
        expected = self.user.id
        DBStorage.new(self.user)
        DBStorage.save()
        actual = DBStorage.__session.query(User).filter(
            User.id == expected).one()
        self.assertTrue(expected == actual)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db',
                     "this test uses a database for stroage")
    def test_user_attr_email(self):
        expected = "hiholbie@gmail.com"
        user_id = self.user.id
        DBStorage.new(self.user)
        DBStorage.save()
        user_obj = DBStorage.__session.query(User).filter(
            User.id == user_id).one()
        user_obj.email = "wifi"
        DBStorage.save(user_obj)
        actual = DBStorage.__session.query(User.name).filter(
            User.id == user_id).one()
        self.assertTrue(expected == actual)


if __name__ == '__main__':
    unittest.main
