import pytest

from Pages.LandingPage import LandingPage
from Tests.test_BasePage import TestBasePage
from Config.config import TestData


class TestUserHomePage(TestBasePage):

    """TEst to add items into watchlist using search bar"""
    @pytest.mark.order(1)
    def test_search_show(self):
        self.landingPage = LandingPage(self.driver)
        signin_options_page = self.landingPage.click_signin_button()
        create_account_page = signin_options_page.click_create_account_link()
        signin_page = create_account_page.login_click()
        user_home_page = signin_page.click_create_account_link()
        user_home_page.search_show()
        user_home_page.sign_out()

    """Test to remove items from watchlist"""
    @pytest.mark.order(2)
    def test_remove_show(self):
        self.landingPage = LandingPage(self.driver)
        signin_options_page = self.landingPage.click_signin_button()
        create_account_page = signin_options_page.click_create_account_link()
        signin_page = create_account_page.login_click()
        user_home_page = signin_page.click_create_account_link()
        user_home_page.remove_from_watchlist()
        user_home_page.sign_out()

    """Test to add items to watchlist using watchlist menu"""
    @pytest.mark.order(3)
    def test_add_to_watchlist(self):
        self.landingPage = LandingPage(self.driver)
        signin_options_page = self.landingPage.click_signin_button()
        create_account_page = signin_options_page.click_create_account_link()
        signin_page = create_account_page.login_click()
        user_home_page = signin_page.click_create_account_link()
        user_home_page.add_to_watchlist()
        user_home_page.sign_out()

    """Test to check all sorting functionalities"""
    @pytest.mark.order(4)
    def test_all_sorts(self):
        self.landingPage = LandingPage(self.driver)
        signin_options_page = self.landingPage.click_signin_button()
        create_account_page = signin_options_page.click_create_account_link()
        signin_page = create_account_page.login_click()
        user_home_page = signin_page.click_create_account_link()
        for sort_type in TestData.SORT_TYPES:
            sorted_list = user_home_page.sort_by_order(sort_type)
            print(sort_type)
            assert sorted_list == TestData.SORTING[sort_type]
        user_home_page.sign_out()

    """Test to refine results based on movie filter"""
    @pytest.mark.order(5)
    def test_refine_results(self):
        self.landingPage = LandingPage(self.driver)
        signin_options_page = self.landingPage.click_signin_button()
        create_account_page = signin_options_page.click_create_account_link()
        signin_page = create_account_page.login_click()
        user_home_page = signin_page.click_create_account_link()
        refined_list = user_home_page.refine_results()
        assert refined_list == TestData.REFINED_LIST
        user_home_page.sign_out()
