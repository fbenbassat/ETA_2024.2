import random

from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class ProductsPage(BasePage):
    url_products = 'https://www.saucedemo.com/inventory.html'
    text_title_page = 'Products'
    product_card = (By.CLASS_NAME, 'inventory_item')
    add_to_cart_btn = (By.CLASS_NAME, 'btn_primary')
    remove_btn = (By.CLASS_NAME, 'btn_secondary')
    product_name = (By.CLASS_NAME, 'inventory_item_name')
    cart_badge = (By.CLASS_NAME, 'shopping_cart_badge')
    shopping_cart_icon = (By.CLASS_NAME, 'shopping_cart_link')

    def __init__(self, driver):
        super().__init__(driver)

    def is_url_products(self):
        return self.is_url(self.url_products)

    def get_title_page(self):
        return self.driver.find_element(By.CLASS_NAME, 'title').text

    def add_product_to_cart(self):
        product_list = self.driver.find_elements(*self.product_card)
        rand_index = random.randint(0, len(product_list) - 1)
        product_card = product_list[rand_index]

        add_to_cart_btn = product_card.find_element(*self.add_to_cart_btn)
        if add_to_cart_btn.text != 'Add to cart':
            raise Exception('Nome do botão ADD TO CART está incorreto!')
        add_to_cart_btn.click()
        if product_card.find_element(*self.remove_btn).text != 'Remove':
            raise Exception('Nome do botão REMOVE está incorreto!')
        return product_card.find_element(*self.product_name).text

    def get_cart_badge(self):
        return self.driver.find_element(*self.cart_badge).text

    def open_your_cart_page(self):
        self.driver.find_element(*self.shopping_cart_icon).click()