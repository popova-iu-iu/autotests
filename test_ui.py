
from playwright.sync_api import sync_playwright
import  time

from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

# playwright = sync_playwright().start()
# browser = playwright.chromium.launch(headless=False, slow_mo=1000)
# page = browser.new_page()
# page.goto('https://www.saucedemo.com/')
#
# page.type(selector='[id="user-name"]', text='standard_user', delay=100)
# page.fill(selector='#password', value='secret_sauce')
# page.click(selector='.submit-button')
#
# page.wait_for_url('https://www.saucedemo.com/inventory.html', timeout=5000)
# page.wait_for_selector(selector='#inventory_container')
#
# button_add_cart = '#add-to-cart-sauce-labs-backpack'
# alt_locator_for_card = '.inventory_item a:has-text("Sauce Labs Backpack")'
# card_button_backpack = '.inventory_item_description:has-text("Sauce Labs Backpack") button:has-text("Add to cart")'
# card_button_light = '.inventory_item_description:has-text("Sauce Labs Bike Light") button:has-text("Add to cart")'
# cart_button = '[data-test="shopping-cart-link"]'
#
# remove_light_button = '#remove-sauce-labs-bike-light'
# checkout_button = '#checkout'
#
# first_name = '#first-name'
# last_name = '#last-name'
# zip = '#postal-code'
# continue_button = '#continue'
# finish_button = '#finish'
# back_home = '#back-to-products'
#
# page.is_visible(selector=button_add_cart)
# page.is_enabled(selector=button_add_cart)
# # page.click(selector=button_add_cart)
# # page.click(selector=alt_locator_for_button)
# page.click(selector=card_button_backpack)
# page.click(selector=card_button_light)
#
# time.sleep(2)
# page.click(selector=cart_button)
# page.wait_for_selector('#cart_contents_container')
# page.click(selector=remove_light_button)
#
# time.sleep(2)
#
# page.click(selector=checkout_button)
#
# page.wait_for_selector('#checkout_info_container')
# page.type(selector=first_name, text='Mishka', delay=100)
# page.type(selector=last_name, text='Krevetkina', delay=100)
# page.type(selector=zip, text='123123', delay=100)
# page.click(selector=continue_button)
#
# page.wait_for_load_state('load')
# page.click(selector=finish_button)
#
# page.wait_for_selector('#checkout_complete_container')
# page.click(selector=back_home)
#
# time.sleep(5)
#
# browser.close()
# playwright.stop()



def test_add_items_and_checkout(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    checkout_page = CheckoutPage(page)

    login_page.login('standard_user', 'secret_sauce')
    inventory_page.add_first_item_to_cart()
    checkout_page.start_checkout()
    checkout_page.fill_checkout_form('Mishka', 'Krevetkina', '123')
