class ShopPage:
    def __init__(self, page):
        self.page = page
        self.add_backpack = page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")
        self.add_tshirt = page.locator("[data-test=\"add-to-cart-sauce-labs-bolt-t-shirt\"]")
        self.add_onesie = page.locator("[data-test=\"add-to-cart-sauce-labs-onesie\"]")
        self.add_jacket = page.locator("[data-test=\"add-to-cart-sauce-labs-fleece-jacket\"]")
        self.cart = page.locator("[data-test=\"shopping-cart-link\"]")
        self.menu = page.get_by_role("button", name="Open Menu")
        self.reset = page.locator("[data-test=\"reset-sidebar-link\"]")

    def add_to_cart(self):
        self.add_backpack.click()
        self.add_tshirt.click()
        self.add_onesie.click()
        self.add_jacket.click()

    def check_cart(self):
        self.cart.click()

    def go_reset(self):
        self.menu.click()
        self.reset.click()
