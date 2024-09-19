import time

from playwright.sync_api import Page, expect
from pages.login_po import LoginPage


def test_error_login(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("", "")
    time.sleep(2)
    expect(login_page.error).to_be_visible()


