import pytest

from pages.ProductsPage import ProductsPage


class Test2:

    @pytest.mark.parametrize('all_browser', ['chrome', 'edge'])
    def test_login_sauce_demo(self, run_all_browser):
        login_page = run_all_browser
        login_page.efetuar_login()

        products_page = ProductsPage(login_page.driver)
        assert products_page.is_url_products(), 'Página de produtos não encontrada!'
        assert products_page.get_title_page() == products_page.text_title_page, 'Título products não encontrado!'