import pytest
import time
from selenium.webdriver.common.by import By


def test_items(browser, language):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    browser.get(link)
    if language == 'es':
        browser.find_element(By.CSS_SELECTOR, '[value="es"]').click()
        browser.find_element(By.CSS_SELECTOR, '[class="btn btn-default"]').click()
        time.sleep(4)
        es_button_text = browser.find_element(By.CLASS_NAME, 'btn.btn-lg.btn-primary.btn-add-to-basket').text
        assert es_button_text == 'Añadir al carrito'
