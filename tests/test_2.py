import time

from selenium.webdriver.common.by import By

from tests.conftest import url_products


class Test2:

    def test_login_sauce_demo(self, open_sauce_demo):
        driver = open_sauce_demo
        driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        driver.find_element(By.ID, 'login-button').click()

        assert driver.current_url == url_products, 'Página de produtos não encontrada!'
        assert driver.find_element(By.CLASS_NAME, 'title').text == 'Products', 'Título products não encontrado!'