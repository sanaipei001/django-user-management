from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import UserProfile

class UserProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass123')
        self.profile = UserProfile.objects.create(user=self.user)

    def test_generate_verification_token(self):
        token = self.profile.generate_verification_token()
        self.assertTrue(len(token) <= 50)
        self.assertEqual(UserProfile.objects.get(user=self.user).verification_token, token)

class UserViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass123')
        self.profile = UserProfile.objects.create(user=self.user)

    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')

    def test_dashboard_view(self):
        self.client.login(username='testuser', password='testpass123')
        self.profile.is_verified = True
        self.profile.save()
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/dashboard.html')