from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.SignInOptionsPage import SignInOptionsPage


class LandingPage(BasePage):
    """By Locators"""
    CLOSE = (By.CSS_SELECTOR, "#imdbHeader-navDrawerOpen")
    SIGNIN_BUTTON = "//div[contains(text(), 'Sign In')]"
    CLOSE_WINDOW = "#imdbHeader-navDrawerOpen"

    """Constructor of Page class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.HOME_URL)

    """List of Page Actions for Landing Page"""

    def close_window(self):
        print("Element is visible? " + str(self.is_present(self.CLOSE)))
        button = self.driver.find_element_by_css_selector(self.CLOSE_WINDOW)
        self.driver.execute_script("arguments[0].click();", button)

    """used to check if clicking on Sign In button redirects to Sign In page"""

    def click_signin_button(self):
        button = self.driver.find_element_by_xpath(self.SIGNIN_BUTTON)
        self.driver.execute_script("arguments[0].click();", button)
        return SignInOptionsPage(self.driver)
