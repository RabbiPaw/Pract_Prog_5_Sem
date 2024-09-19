class CartPage():
    def __init__(self, page):
        self.page = page
        self.item_0 = page.locator("[data-test=\"item-0-title-link\"]")
        self.item_1 = page.locator("[data-test=\"item-1-title-link\"]")
        self.item_2 = page.locator("[data-test=\"item-2-title-link\"]")
        self.item_3 = page.locator("[data-test=\"item-3-title-link\"]")
        self.item_4 = page.locator("[data-test=\"item-4-title-link\"]")
        self.item_5 = page.locator("[data-test=\"item-5-title-link\"]")
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

    def creat_order(self):
        self.order.click()
