from playwright.sync_api import Page, expect
from pages.login_po import LoginPage
from pages.shop_po import ShopPage
from pages.cart_po import CartPage
from pages.order_po import OrderPage

def test_error_oder(page: Page) -> None:
    login_page = LoginPage(page)
    shop_page = ShopPage(page)
    cart_page = CartPage(page)
    order_page = OrderPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    shop_page.check_cart()
    cart_page.create_order()
    order_page.input("", "", "")
    expect(order_page.error).to_be_visible()
    order_page.error_button.click()
    order_page.input("A", "", "")
    expect(order_page.error).to_be_visible()
    order_page.error_button.click()
    order_page.input("A", "A", "")
    expect(order_page.error).to_be_visible()
    order_page.error_button.click()
