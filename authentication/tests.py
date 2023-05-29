from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class AutenticationTest(TestCase):
    def setUp(self) -> None:
        self.register_url = reverse('signup')
        self.login_url = reverse('signin')
        return super().setUp()
    
class SignUpTest(AutenticationTest):
    def test_can_view_siginup_page_correctly(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authetication/signup.html')
        
    def test_can_view_signin_page_correctly(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authetication/signin.html')
        
    def test_should_signup_user(self):
        self.user = {
            "username": "demouser",
            "first_name": "demo",
            "last_name": "user",
            "email": "demo@gmail.com",
            "password1": "password",
            "password2": "password"
        }
        response = self.client.post(reverse("signup"), self.user)
        self.assertEquals(response.status_code, 200)
        
    def test_should_not_signup_user_with_same_username(self):
        self.user = {
            "username": "demouser",
            "first_name": "demo",
            "last_name": "user",
            "email": "demo@gmail.com",
            "password1": "password",
            "password2": "password"
        }
        self.client.post(reverse("signup"), self.user)
        response = self.client.post(reverse("signup"), self.user)
        self.assertEquals(response.status_code, 200)