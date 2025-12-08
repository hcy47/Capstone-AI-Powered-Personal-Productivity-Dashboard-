import unittest
from app import create_app
from app.models import db, User

class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('DevelopmentConfig')
        self.client = self.app.test_client()
        with self.app.app_context():
            db.drop_all()
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_user_registration(self):
        response = self.client.post('/users', json={
            'name': 'Test',
            'last_name': 'User',
            'email': 'test@example.com',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertIn('user', data)
        self.assertEqual(data['user']['email'], 'test@example.com')

    def test_duplicate_email(self):
        self.client.post('/users', json={
            'name': 'Test',
            'last_name': 'User',
            'email': 'test@example.com',
            'password': 'password123'
        })
        response = self.client.post('/users', json={
            'name': 'Test2',
            'last_name': 'User2',
            'email': 'test@example.com',
            'password': 'password456'
        })
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertIn('error', data)

    def test_login(self):
        self.client.post('/users', json={
            'name': 'Test',
            'last_name': 'User',
            'email': 'test@example.com',
            'password': 'password123'
        })
        response = self.client.post('/users/login', json={
            'email': 'test@example.com',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('token', data)

if __name__ == '__main__':
    unittest.main()
