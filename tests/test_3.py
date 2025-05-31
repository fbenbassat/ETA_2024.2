import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.conftest import url_home


class Test3:

    def test_logout_sauce_demo(self, login_sauce_demo):
        driver = login_sauce_demo
        driver.find_element(By.ID, 'react-burger-menu-btn').click()

        menu_element = WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '#react-burger-cross-btn')))
        assert menu_element.is_displayed(), 'Menu não exibido!'
        driver.find_element(By.ID, 'logout_sidebar_link').click()
        assert driver.current_url == url_home, 'Página Home não encontrada!'
