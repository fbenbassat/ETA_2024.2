import pytest

from pages.LoginPage import LoginPage
from pages.ProductsPage import ProductsPage


def pytest_addoption(parser):
    parser.addoption('--browser_selenium', default='chrome')


@pytest.fixture
def open_sauce_demo(request):
    selected_browser = request.config.getoption('browser_selenium').lower()
    login_page = LoginPage(browser=selected_browser)
    login_page.open_page()
    yield login_page
    login_page.close()


@pytest.fixture
def run_all_browser(all_browser):
    login_page = LoginPage(browser=all_browser)
    login_page.open_page()
    yield login_page
    login_page.close()


@pytest.fixture
def login_sauce_demo(open_sauce_demo):
    login_page = open_sauce_demo
    if login_page.is_url_login():
        login_page.efetuar_login()
    products_page = ProductsPage(login_page.driver)
    assert products_page.is_url_products(), 'Página de produtos não encontrada!'
    yield products_page, login_page


@pytest.fixture
def add_product(login_sauce_demo):
    products_page, login_page = login_sauce_demo
    products_page.add_product_to_cart()

