import time

from playwright.sync_api import Page, expect


class Test2_pw:

    def test_login_pw(self, page: Page):
        page.goto('https://www.saucedemo.com/')

        page.locator('#user-name').fill('standard_user')

        page.locator('id=password').fill('secret_sauce')

        page.locator('[name="login-button"]').click()

        expect(page).to_have_url('https://www.saucedemo.com/inventory.html')

        expect(page.locator('.title')).to_have_text('Products')

        assert page.locator('.title').text_content() == 'Products', 'Title incorreto!'
        time.sleep(3)

