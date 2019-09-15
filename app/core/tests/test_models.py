from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_successful_email(self):
        """ Test creating a new user with a successful email """
        email = 'testuser@abc.com'
        password = 'userpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Test email for a new user is normailize """
        email = 'testuser@ABC.com'
        user = get_user_model().objects.create_user(email, 'userpass123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_with_invalid_email(self):
        """ Test if user create with no email then raise an ErrorValue """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'userpass123')

    def test_create_new_superuser(self):
        """ Creating a user with admin access """
        user = get_user_model().objects.create_superuser(
            email='testuser@abc.com',
            password='userpass123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
