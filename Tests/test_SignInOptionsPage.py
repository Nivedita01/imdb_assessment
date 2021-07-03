import pytest

from Pages.LandingPage import LandingPage
from Tests.test_BasePage import TestBasePage
from Config.config import TestData
from time import sleep


class TestSignInOptionsPage(TestBasePage):

    def test_click_create_account(self):
        self.landingPage = LandingPage(self.driver)
        signin_page = self.landingPage.click_signin_button()
        create_account_page = signin_page.click_create_account_link()
        title = create_account_page.get_title(TestData.CREATE_ACCOUNT_PAGE_TITLE)
        assert title == TestData.CREATE_ACCOUNT_PAGE_TITLE_INCORRECT
