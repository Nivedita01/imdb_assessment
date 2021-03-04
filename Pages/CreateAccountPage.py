from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.SignInPage import SignInPage
from Pages.UserHomePage import UserHomePage
from time import sleep


class CreateAccountPage(BasePage):

    """By Locators"""
    USERNAME = (By.ID, 'ap_customer_name')
    PASSWORD = (By.ID, 'ap_password')
    REPASSWORD = (By.ID, 'ap_password_check')
    CREATE = (By.ID, 'continue')
    EMAIL = (By.ID, 'ap_email')
    OTP_PAGE_CREATE = (By.ID, "a-autoid-0")
    SIGNIN_BUTTON = (By.XPATH, "//a[contains(text(), 'Sign-In')]")

    """Constructors of Page class"""

    def __init__(self, driver):
        super().__init__(driver)

    """List of Page Actions for CreateAccountPage"""

    """Verify title of the page"""

    def get_login_page_title(self):
        title = self.find_title()
        return title

    """Enter valid name"""

    def enter_valid_name(self, username):
        self.do_send_keys_and_tab(self.USERNAME, username)

        """Enter valid emailid"""

    def enter_valid_emailid(self, email_id):
        self.do_send_keys_and_tab(self.EMAIL, email_id)

        """Enter valid password"""

    def enter_valid_password(self, password):
        self.do_send_keys_and_tab(self.PASSWORD, password)

        """Enter valid password"""

    def enter_valid_re_password(self, password):
        self.do_send_keys_and_tab(self.REPASSWORD, password)

        """Function to Create new account"""

    def create_new_account(self):
        self.enter_valid_name(TestData.USERNAME)
        self.enter_valid_emailid(TestData.EMAIL)
        self.enter_valid_password(TestData.PASSWORD)
        self.enter_valid_re_password(TestData.PASSWORD)
        self.do_click(self.CREATE)
        sleep(20) #this is the sleep for entering OTP and Captcha
        self.do_click(self.OTP_PAGE_CREATE)
        return UserHomePage(self.driver)

    """Validate login with correct credentials and login successfully"""
    def login_click(self):
        self.do_click(self.SIGNIN_BUTTON)
        return SignInPage(self.driver)
