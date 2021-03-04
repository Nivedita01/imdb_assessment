import pytest

from Pages.LandingPage import LandingPage
from Tests.test_BasePage import TestBasePage
from Config.config import TestData
from time import sleep


class TestLandingPage(TestBasePage):

    def test_click_signin(self):
        self.landingPage = LandingPage(self.driver)
        signin_options_page = self.landingPage.click_signin_button()
        title = signin_options_page.get_login_page_title()
        assert title == TestData.SIGN_IN_PAGE_TITLE
