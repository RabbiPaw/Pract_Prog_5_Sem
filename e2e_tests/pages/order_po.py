class OrderPage:
    def __init__(self,page):
        self.page = page
        self.firstname = page.locator("[data-test=\"firstName\"]")
        self.lastname = page.locator("[data-test=\"lastName\"]")
        self.postal_code = page.locator("[data-test=\"postalCode\"]")
        self.apply = page.locator("[data-test=\"continue\"]")
        self.error = page.locator("[data-test=\"error\"]")
        self.error_button = page.locator("[data-test=\"error-button\"]")

    def input(self,firstname,lastname,postalcode):
        self.firstname.fill(firstname)
        self.lastname.fill(lastname)
        self.postal_code.fill(postalcode)
        self.apply.click()
