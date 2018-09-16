import unittest
from app.models import Admin,Blog
from app import db

class adminModelCase(unittest.TestCase):
    def setUp(self):
        self.admin_James = (id=1,username = 'James',password = 'potato', email = 'james@ms.com')
    def tearDown(self):
        admin.query.delete()
    def test_password_hashing(self):
        u = admin(username='hannah')
        u.set_password('1234')
        self.assertFalse(u.check_password('pass123'))
        self.assertTrue(u.check_password('1234'))
    def test_save_admin(self):
    def test_check_instance_variables(self):
        self.assertEquals(self.admin_James.username,'James')
        self.assertEquals(self.admin_James.password,'potato')
        self.assertEquals(self.admin_James.email,"james@ms.com")
    def test_save_review(self):
        self.admin_James.save_admin()
        self.assertTrue(len(Admin.query.all())>0)
    def test_get_admin_by_id(self):
        self.admin_James.save_admin()
        fetched_admin = Admin.get_admin(1)
        self.assertTrue(len(fetched_admin) == 1)