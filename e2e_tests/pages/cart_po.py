class CartPage():
    def __init__(self, page):
        self.page = page
        self.item_list = page.locator("[data-test=\"cart-list\"]")
        self.back = page.locator("[data-test=\"continue-shopping\"]")
        self.drop_backpack = page.locator("[data-test=\"remove-sauce-labs-backpack\"]")
        self.drop_bolt_tshirt = page.locator("[data-test=\"remove-sauce-labs-bolt-t-shirt\"]")
        self.drop_onesie = page.locator("[data-test=\"remove-sauce-labs-onesie\"]")
        self.drop_jacket = page.locator("[data-test=\"remove-sauce-labs-fleece-jacket\"]")
        self.order = page.locator("[data-test=\"checkout\"]")

    def drop_cart(self):
        self.drop_backpack.click()
        self.drop_bolt_tshirt.click()
        self.drop_onesie.click()
        self.drop_jacket.click()

    def create_order(self):
        self.order.click()

    def go_back(self):
        self.back.click()
