from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def test_button_add_basket(browser: webdriver.Chrome):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    browser.get(link)

    try:
        __ = browser.find_element(By.CSS_SELECTOR, 'button.btn-add-to-basket')
    except NoSuchElementException:
        assert False, 'Basket was not found'
