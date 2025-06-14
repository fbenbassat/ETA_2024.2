import time

from pages.YourCartPage import YourCartPage


class Test4:

    def test_add_to_cart(self, login_sauce_demo):
        products_page, login_page = login_sauce_demo
        product_name = products_page.add_product_to_cart()
        assert products_page.get_cart_badge() == '1', 'Número de itens no carrinho está incorreto.'
        products_page.open_your_cart_page()

        your_cart_page = YourCartPage(products_page.driver)
        assert your_cart_page.get_first_product_name() == product_name, 'Produto incorreto!'



