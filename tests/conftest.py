import pytest

from pages.LoginPage import LoginPage

url_products = 'https://www.saucedemo.com/inventory.html'


@pytest.fixture
def open_sauce_demo():
    login_page = LoginPage()
    login_page.open_page()
    yield login_page
    login_page.close()


# @pytest.fixture
# def login_sauce_demo(open_sauce_demo):
#     driver = open_sauce_demo
#     if driver.current_url == url_home:
#         driver.find_element(By.ID, 'user-name').send_keys('standard_user')
#         driver.find_element(By.ID, 'password').send_keys('secret_sauce')
#         driver.find_element(By.ID, 'login-button').click()
#     assert driver.current_url == url_products, 'Página de produtos não encontrada!'
#     yield driver
