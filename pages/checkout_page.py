from pages.base_page import BasePage

class CheckoutPage(BasePage):

    CHECKOUT_BUTTON_SELECTOR = '#checkout'
    FIRST_NAME_SELECTOR = '#first-name'
    LAST_NAME_SELECTOR = '#last-name'
    POSTAL_CODE_SELECTOR = '#postal-code'

    def __init__(self, page):
        super().__init__(page)
        # self._endpoint = 'cart.html'
        self._endpoint = 'checkout-step-one.html'

    def start_checkout(self):
        self.wait_for_selector_and_click(self.CHECKOUT_BUTTON_SELECTOR)
        self.assert_element_is_visible(self.FIRST_NAME_SELECTOR)

    def fill_checkout_form(self, firstname, lastname, postal_code):
        self.wait_for_selector_and_type(self.FIRST_NAME_SELECTOR, firstname)
        self.wait_for_selector_and_type(self.LAST_NAME_SELECTOR, lastname)
        self.wait_for_selector_and_type(self.POSTAL_CODE_SELECTOR, postal_code)
        self.assert_input_value(self.POSTAL_CODE_SELECTOR, postal_code)