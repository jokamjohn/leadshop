from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver


class MerchantAuthSeleniumTests(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super(MerchantAuthSeleniumTests, cls).setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(MerchantAuthSeleniumTests, cls).tearDownClass()

    def test_merchant_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, "/login/"))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys("jokamjohn@gmail.com")
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys("@Johnkagga1")
        self.selenium.find_element_by_xpath('//button[@value="Sign In"]').click()
