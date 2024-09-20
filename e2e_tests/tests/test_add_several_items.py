from playwright.sync_api import Page, expect
from pages.login_po import LoginPage
from pages.shop_po import ShopPage
from pages.cart_po import CartPage

def test_adding(page: Page) -> None:
    login_page = LoginPage(page)
    shop_page = ShopPage(page)
    cart_page = CartPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    shop_page.add_to_cart()
    shop_page.check_cart()
    expect(cart_page.item_list).to_have_text(["QTYDescription1Sauce Labs Backpackcarry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection.$29.99Remove1Sauce Labs Bolt T-ShirtGet your"
                                              " testing superhero on with the Sauce Labs bolt T-shirt. From American Apparel, 100% ringspun combed cotton, heather gray with red bolt.$15.99Remove1Sauce Labs OnesieRib snap infant onesie for the junior automation engineer in "
                                              "development. Reinforced 3-snap bottom closure, two-needle hemmed sleeved and bottom won't unravel.$7.99Remove1Sauce Labs Fleece JacketIt's not every day that you come across a midweight quarter-zip fleece jacket capable of hand"
                                              "ling everything from a relaxing day outdoors to a busy day at the office.$49.99Remove"])
    cart_page.go_back()
    shop_page.go_reset()
