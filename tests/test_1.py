import pytest


class Test1:

    @pytest.mark.parametrize('all_browser', ['chrome', 'edge', 'firefox'])
    def test_click_login_button(self, run_all_browser):
        login_page = run_all_browser
        login_page.click_login_button()
        assert login_page.is_url_login(), 'Página requerida não encontrada!'
        assert login_page.get_login_error_message() == login_page.text_login_msg_error, 'Mensagem de erro não incorreta!'
