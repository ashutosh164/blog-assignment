from django.test import TestCase
from rest_framework.exceptions import ValidationError
from .serializers import RegisterSerializer


class TestRegisterSerializer(TestCase):
    def setUp(self):
        self.valid_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'password123'
        }
        self.invalid_data = {
            'username': '',
            'email': 'not-an-email',
            'password': ''
        }

    def test_successful_user_creation(self):
        serializer = RegisterSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertEqual(user.username, self.valid_data['username'])
        self.assertEqual(user.email, self.valid_data['email'])
        self.assertTrue(user.check_password(self.valid_data['password']))

    def test_password_write_only(self):
        serializer = RegisterSerializer(data=self.valid_data)
        serializer.is_valid()
        self.assertNotIn('password', serializer.data)

    def test_validation_errors(self):
        serializer = RegisterSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('username', serializer.errors)
        self.assertIn('email', serializer.errors)
        self.assertIn('password', serializer.errors)

        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)
