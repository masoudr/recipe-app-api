from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='test@test.com', password='testpass'):
    """
    Create a Sample User
    """
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):
    email = 'mymail@TEST.COM'
    password = 'TestPassword'

    def test_create_user_with_email_successful(self):
        """
        Test creating a new user with an email is successful
        """
        user = get_user_model().objects.create_user(
            email=self.email,
            password=self.password
        )

        self.assertEqual(user.email, self.email.lower())
        self.assertTrue(user.check_password(self.password))

    def test_new_user_email_normalized(self):
        """
        Test the email for a new user is normalized
        """
        user = get_user_model().objects.create_user(self.email, self.password)

        self.assertEqual(user.email, self.email.lower())

    def test_new_user_invalid_email(self):
        """
        Test creating user with no email raises error
        """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, self.password)

    def test_create_new_superuser(self):
        """
        Test creating a new superuser
        """

        user = get_user_model().objects.create_superuser(
            self.email,
            self.password,
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """
        Test the tag string representation
        """
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)
