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
    shop_page.add_to_cart()
    shop_page.check_cart()
    cart_page.drop_cart()
    expect(cart_page.item_list).to_have_text(['QTYDescription'])
    cart_page.go_back()
    shop_page.go_reset()

