import time

from playwright.sync_api import Page, expect
from pages.login_po import LoginPage
from pages.shop_po import ShopPage
from pages.cart_po import CartPage

def test_deleting(page: Page) -> None:
    login_page = LoginPage(page)
    shop_page = ShopPage(page)
    cart_page = CartPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    time.sleep(2)
    shop_page.add_to_cart()
    time.sleep(2)
    shop_page.check_cart()
    time.sleep(2)
    cart_page.drop_cart()
    time.sleep(2)
    expect(cart_page.item_4).not_to_be_visible()
    expect(cart_page.item_1).not_to_be_visible()
    expect(cart_page.item_2).not_to_be_visible()
    expect(cart_page.item_5).not_to_be_visible()

