from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""This class is the parent of all pages"""

"""It contains all generic methods and utilities for all pages"""


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            element.click()
        except TimeoutException as exception:
            print(exception)

    def do_send_keys(self, by_locator, text):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            element.send_keys(text)
        except NoSuchElementException as exception:
            print(exception)

    def do_send_keys_and_tab(self, by_locator, text):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            element.send_keys(text, Keys.TAB)
        except NoSuchElementException as exception:
            print(exception)

    def is_visible(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        except NoSuchElementException as exception:
            print(exception)
        return bool(element)

    def find_title(self):
        text = self.driver.title
        return text

    def get_title(self, title):
        try:
            WebDriverWait(self.driver, 10).until(EC.title_is(title))
        except TimeoutException as exception:
            print(exception)
        return self.driver.title

    def is_present(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
        except NoSuchElementException as exception:
            print(exception)
        return bool(element)
