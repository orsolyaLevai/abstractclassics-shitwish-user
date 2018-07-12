from unittest import TestCase
from main import app


class TestMain(TestCase):

    def setUp(self):
        self.app = app.test_client()
        app.config['DEBUG'] = True
        app.config['TESTING'] = True
        app.json_encoder.ensure_ascii = False

    def test_registration_status_code(self):
        result = self.app.post('/registration',
                               json=dict(
                                   firstName="Nagy",
                                   lastName="Béla",
                                   email="bela2@gmail.com",
                                   password="cseresznye",
                                   address="2199, Csömör, Fa utca 1",
                                   phoneNum="23456789"))

        self.assertEqual(result.status_code, 200)

    def test_registration_duplicate(self):
        result = self.app.post('/registration',
                               json=dict(
                                   firstName="Nagy",
                                   lastName="Béla",
                                   email="bela2@gmail.com",
                                   password="cseresznye",
                                   address="2199, Csömör, Fa utca 1",
                                   phoneNum="23456789"))

        self.assertEqual(result.data, b"duplicateEmail")

    def test_login_user_status_ok(self):
        result = self.app.post('/login',
                               json=dict(
                                   email="bela@gmail.com"
                               ))
        self.assertEqual(result.status_code, 200)

    def test_getuser_by_id(self):
        result = self.app.get('/user/2')

        self.assertEqual(result.status_code, 200)

    def test_user_not_found(self):
        result = self.app.get('/user/1000000')

        self.assertEqual(result.data, b"userNotFound")
