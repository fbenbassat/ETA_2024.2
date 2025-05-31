from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class LoginPage(BasePage):
    url_login = 'https://www.saucedemo.com/'
    btn_login = (By.CSS_SELECTOR, '#login-button')
    error_message_login = (By.CLASS_NAME, 'error-message-container')
    text_login_msg_error = 'Epic sadface: Username is required'
    username_field = (By.ID, 'user-name')
    password_field = (By.ID, 'password')

    def __init__(self, browser):
        super().__init__(driver=None, browser=browser)

    def open_page(self):
        self.driver.get(self.url_login)

    def is_url_login(self):
        return self.is_url(self.url_login)

    def click_login_button(self):
        self.driver.find_element(*self.btn_login).click()

    def get_login_error_message(self):
        error_message_element = self.driver.find_element(*self.error_message_login)
        if error_message_element.is_displayed():
            return error_message_element.text
        else:
            return None

    def efetuar_login(self, username='standard_user', password='secret_sauce'):
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.click_login_button()
