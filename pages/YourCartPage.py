from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class YourCartPage(BasePage):

    product_name = (By.CLASS_NAME, 'inventory_item_name')

    def __init__(self, driver):
        super().__init__(driver)

    def get_first_product_name(self):
        return self.driver.find_element(*self.product_name).text