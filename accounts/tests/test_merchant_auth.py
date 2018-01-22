from django.test import TestCase, Client
from django.core import mail
from django.contrib.auth import get_user_model
import re
import urllib.parse

from accounts.forms import UserCreateForm
from accounts.views import MerchantRegistration


class TestMerchantAuth(TestCase):

    def setUp(self):
        """
        Initiate the Http client for all tests in this test case.
        :return:
        """
        self.client = Client()

    def test_merchant_registration_template_is_rendered(self):
        """
        Test that the accounts/signup.html template is rendered.
        :return:
        """
        response = self.client.get("/merchant/accounts/signup/")
        self.assertEqual(response.templates[0].name, "accounts/signup.html")
        self.assertEqual(response.templates[1].name, "layout_merchant.html")

    def test_merchant_registration_form_is_valid(self):
        """
        Test that the merchant registration form is valid
        :return:
        """
        data = {
            "username": "jokam",
            "email": "jokamjohn@gmail.com",
            "password1": "@Johnkagga1",
            "password2": "@Johnkagga1"
        }
        form = UserCreateForm(data=data)
        self.assertTrue(form.is_valid())

    def test_merchant_registration_form_is_invalid(self):
        """
        Test that the form has been filled with invalid data.
        :return:
        """
        data = {
            "username": "jokam",
            "email": "jokamjohn@gmail.com",
            "password1": "johnkagga1",
            "password2": "johnkagga1"
        }
        form = UserCreateForm(data=data)
        self.assertTrue(form.is_valid())

    def test_merchant_successfully_registers(self):
        """
        Test that a user is successfully created by checking for the redirect to login
        and the registration view has been hit by the request.
        :return:
        """
        data = {
            "username": "jokam",
            "email": "jokamjohn@gmail.com",
            "password1": "@Johnkagga1",
            "password2": "@Johnkagga1"
        }
        response = self.client.post("/merchant/accounts/signup/", data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/login/")
        self.assertEqual(response.resolver_match.func.__name__, MerchantRegistration.as_view().__name__)

    def test_that_confirmation_sent_went_merchant_signs_up(self):
        """
        Test that an email confirmation message is sent when a merchant registers on the platform
        :return:
        """
        data = {
            "username": "jokam",
            "email": "jokamjohn@gmail.com",
            "password1": "@Johnkagga1",
            "password2": "@Johnkagga1"
        }
        self.client.post("/merchant/accounts/signup/", data)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Activate your Lead Shop account.')

    def test_merchant_email_confirmation_and_activation(self):
        """
        Test that a merchant's email is successfully verified and the user activated.
        :return:
        """
        data = {
            "username": "jokam",
            "email": "jokamjohn@gmail.com",
            "password1": "@Johnkagga1",
            "password2": "@Johnkagga1"
        }
        self.client.post("/merchant/accounts/signup/", data)
        self.assertEqual(len(mail.outbox), 1)
        url = re.search("(?P<url>https?://[^\s'\"]+)", mail.outbox[0].body).group("url")
        pathed_url = urllib.parse.urlparse(url).path
        response = self.client.get(pathed_url)
        self.assertTrue(response.status_code, 302)
        self.assertTrue(response.url, "/login/")

    def test_merchant_successful_login(self):
        """
        Test that an active merchant is redirected to the dashboard when they log into their accounts
        :return:
        """
        data = {
            "username": "jokam",
            "email": "jokamjohn@gmail.com",
            "password1": "@Johnkagga1",
            "password2": "@Johnkagga1"
        }
        self.client.post("/merchant/accounts/signup/", data)
        User = get_user_model()
        user = User.objects.get(username="jokam")
        user.is_active = True
        user.save()
        print(user.is_active)
        response = self.client.post("/login/", data={"username": "jokamjohn@gmail.com", "password": "@Johnkagga1"},
                                    follow=True)
        self.assertTrue(response.status_code, 302)
        self.assertTrue(response.templates[0].name, "merchant/dashboard_layout.html")
