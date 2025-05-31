
class Test1:

    def test_click_login_button(self, open_sauce_demo):
        login_page = open_sauce_demo
        login_page.click_login_button()
        assert login_page.is_url_login(), 'Página requerida não encontrada!'
        assert login_page.has_login_error_message(), 'Mensagem de erro não exibida!'
