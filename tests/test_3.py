from pages.MenuPage import MenuPage


class Test3:

    def test_logout_sauce_demo(self, login_sauce_demo):
        products_page, login_page = login_sauce_demo
        menu_page = MenuPage(login_page.driver)
        menu_page.open_menu()
        assert menu_page.is_menu_open(), 'Menu não exibido!'
        menu_page.click_logout()
        assert login_page.is_url_login(), 'Página Home não encontrada!'
