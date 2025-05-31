from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.BasePage import BasePage


class MenuPage(BasePage):
    menu_button = (By.ID, 'react-burger-menu-btn')
    menu_cross_button = (By.CSS_SELECTOR, '#react-burger-cross-btn')
    logout_menu_item = (By.ID, 'logout_sidebar_link')

    def __init__(self, driver):
        super().__init__(driver)

    def open_menu(self):
        self.driver.find_element(*self.menu_button).click()

    def is_url(self, url):
        raise Exception('This method is not available for this class.')

    def is_menu_open(self):
        menu_element = WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.menu_cross_button))
        return menu_element.is_displayed()

    def click_logout(self):
        self.driver.find_element(*self.logout_menu_item).click()
