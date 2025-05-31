from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class ProductsPage(BasePage):
    url_products = 'https://www.saucedemo.com/inventory.html'
    text_title_page = 'Products'

    def __init__(self, driver):
        super().__init__(driver)

    def is_url_products(self):
        return self.is_url(self.url_products)

    def get_title_page(self):
        return self.driver.find_element(By.CLASS_NAME, 'title').text