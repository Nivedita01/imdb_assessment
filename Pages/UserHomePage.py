from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage
from selenium.webdriver.support.ui import Select
from time import sleep


class UserHomePage(BasePage):
    """By Locators"""
    TOGGLE_MENU = (By.CSS_SELECTOR, '.navbar__user')
    SIGNOUT_BUTTON = (By.CSS_SELECTOR, ".imdb-header-account-menu__sign-out")
    SEARCH_BAR = (By.ID, "suggestion-search")
    SEARCH_RESULT = (By.CSS_SELECTOR, '[data-testid = search-result--const]')
    ADD_WATCHLIST = (By.CSS_SELECTOR, '.ribbonize')
    WATCHLIST = (By.XPATH, "//div[contains(text(), 'Watchlist')][1]")

    EDIT_WATCHLIST = (By.CSS_SELECTOR, '.button .button-title')
    REMOVE_FROM_WATCHLIST = (By.CSS_SELECTOR, '.lister-item:nth-child(2) div div')
    DELETE_FROM_WATCHLIST = (By.ID, 'delete_items')
    DELETE = (By.CSS_SELECTOR, '.verify> [value = DELETE]')

    ADD_FROM_WATCHLIST_LIST = (By.ID, 'add-to-list-search')
    SELECT_TO_ADD = (By.CSS_SELECTOR, "#add-to-list-search-results .search_item:nth-child(1)")

    NAMES = ".lister-item h3.lister-item-header"
    SORT = (By.ID, "lister-sort-by-options")

    SELECT = "lister-sort-by-options"

    TITLES = (By.CSS_SELECTOR, "div.lister-details")

    NEW_LIST = (By.XPATH, ".//button[contains(text(), 'create')]")

    REFINE = (By.CSS_SELECTOR, ".lister-controls-expand")
    FIRST_CHECKBOX_FEATURE_FILM = (By.CSS_SELECTOR, ".lister-checkbox")

    """Constructor of Page class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.HOME_URL)

    """List of Page Actions for User Home Page"""

    def sign_out(self):
        self.driver.refresh()
        self.do_click(self.TOGGLE_MENU)
        self.do_click(self.SIGNOUT_BUTTON)

    """used to enter certain names and add to watchlist"""

    def search_show(self):
        for show in TestData.KEYWORDS:
            self.do_send_keys(self.SEARCH_BAR, show)
            self.do_click(self.SEARCH_RESULT)
            self.do_click(self.ADD_WATCHLIST)
        self.do_click(self.WATCHLIST)

    """Used to remove items from watchlist"""

    def remove_from_watchlist(self):
        self.driver.refresh()
        self.do_click(self.WATCHLIST)
        self.do_click(self.EDIT_WATCHLIST)
        self.do_click(self.REMOVE_FROM_WATCHLIST)
        self.do_click(self.DELETE_FROM_WATCHLIST)
        self.do_click(self.DELETE)
        self.driver.refresh()

    """Used to add new names to watchlist from inside watchlist page"""

    def add_to_watchlist(self):
        self.do_click(self.WATCHLIST)
        self.do_click(self.EDIT_WATCHLIST)
        for new_shows in TestData.NEW_KEYWORDS:
            self.do_send_keys(self.ADD_FROM_WATCHLIST_LIST, new_shows)
            self.do_click(self.SELECT_TO_ADD)
            self.driver.refresh()

    """used to sort all possible values"""

    def sort_by_order(self, sort_type):
        self.driver.refresh()
        self.do_click(self.WATCHLIST)
        names = []
        sleep(1)
        dropdown = Select(self.driver.find_element_by_id(self.SELECT))
        if sort_type == "LIST_ORDER":
            dropdown.select_by_index(0)
        if sort_type == "ALPHA":
            dropdown.select_by_index(1)
        if sort_type == "USER_RATING":
            dropdown.select_by_index(2)
        if sort_type == "POPULARITY":
            dropdown.select_by_index(3)
        if sort_type == "YOUR_RATING":
            dropdown.select_by_index(4)
        if sort_type == "NUMBER_OF_RATINGS":
            dropdown.select_by_index(5)
        if sort_type == "RELEASE_DATE":
            dropdown.select_by_index(6)
        if sort_type == "RUNTIME":
            print("Inside runtime")
            dropdown.select_by_index(7)
        if sort_type == "DATE_ADDED":
            dropdown.select_by_index(8)
        sleep(5)
        names.extend([elem.text for elem in self.driver.find_elements_by_css_selector(self.NAMES)])
        return names

    """ADDITIONAL FUNCTIONALITY"""
    """used for refining results based on Movie filter"""
    def refine_results(self):
        self.do_click(self.WATCHLIST)
        names = []
        self.do_click(self.REFINE)
        self.do_click(self.FIRST_CHECKBOX_FEATURE_FILM)
        sleep(0.5)
        names.extend([elem.text for elem in self.driver.find_elements_by_css_selector(self.NAMES)])
        return names
