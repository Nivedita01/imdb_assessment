from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.UserHomePage import UserHomePage


class SignInPage(BasePage):

    """By Locators"""
    EMAIL = (By.ID, 'ap_email')
    PASSWORD = (By.ID, 'ap_password')
    SIGNIN_BUTTON = (By.ID, 'signInSubmit')

    """Constructors of Page class"""

    def __init__(self, driver):
        super().__init__(driver)

    """List of Page Actions for Sign In Page"""

    """used to get login page title"""
    def get_login_page_title(self):
        title = self.find_title()
        return title

    def enter_valid_emailid(self, email_id):
        self.do_send_keys_and_tab(self.EMAIL, email_id)

    def enter_valid_password(self, password):
        self.do_send_keys_and_tab(self.PASSWORD, password)

    """Verify if a user will be able to login with emailid and password."""
    def click_create_account_link(self):
        self.enter_valid_emailid(TestData.EMAIL)
        self.enter_valid_password(TestData.PASSWORD)
        self.do_click(self.SIGNIN_BUTTON)
        return UserHomePage(self.driver)
