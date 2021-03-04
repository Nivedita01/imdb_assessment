from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Pages.CreateAccountPage import CreateAccountPage


class SignInOptionsPage(BasePage):

    """By Locators"""
    CREATE_ACCOUNT_LINK = (By.CSS_SELECTOR, ".create-account")
    """Constructors of Page class"""

    def __init__(self, driver):
        super().__init__(driver)

    """List of Page Actions for Sign In Options Page"""

    """used to get login page title"""
    def get_login_page_title(self):
        title = self.find_title()
        return title

    """used to check if create account link exists"""
    def is_create_account_link_exists(self):
        return self.is_visible(self.CREATE_ACCOUNT_LINK)

    """clicking on create account page"""
    def click_create_account_link(self):
        self.do_click(self.CREATE_ACCOUNT_LINK)
        return CreateAccountPage(self.driver)
