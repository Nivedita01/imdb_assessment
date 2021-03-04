import pytest

from Pages.LandingPage import LandingPage
from Tests.test_BasePage import TestBasePage
from Config.config import TestData


class TestCreatePage(TestBasePage):

    """Test to create a new user account"""
    @pytest.mark.order(1)
    def test_create_new_account(self):
        self.landingPage = LandingPage(self.driver)
        signin_page = self.landingPage.click_signin_button()
        create_account_page = signin_page.click_create_account_link()
        user_home_page = create_account_page.create_new_account()
        title = user_home_page.get_title(TestData.USER_HOME_PAGE)
        assert title == TestData.USER_HOME_PAGE
        user_home_page.sign_out()

    """Test to verify if login is successful"""

    def test_valid_login(self):
        self.landingPage = LandingPage(self.driver)
        signin_options_page = self.landingPage.click_signin_button()
        create_account_page = signin_options_page.click_create_account_link()
        signin_page = create_account_page.login_click()
        user_home_page = signin_page.click_create_account_link()
        title = user_home_page.get_title(TestData.USER_HOME_PAGE)
        assert title == TestData.USER_HOME_PAGE
