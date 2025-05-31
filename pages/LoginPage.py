from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class LoginPage:
    url = 'https://www.saucedemo.com/'

    def open_page(self):
        options = Options()
        options.add_argument("--incognito")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(self.url)

    def is_url_login(self):
        return self.driver.current_url == self.url

    def click_login_button(self):
        self.driver.find_element(By.CSS_SELECTOR, '#login-button').click()

    def has_login_error_message(self):
        error_message_element = self.driver.find_element(By.CLASS_NAME, 'error-message-container')
        return error_message_element.is_displayed() and error_message_element.text == 'Epic sadface: Usernam is required'

    def close(self):
        self.driver.quit()
