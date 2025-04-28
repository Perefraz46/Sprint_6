from pages.main_page import MainPage
from selenium import webdriver
from data import Url
import pytest

from pages.redirect_page import ScooterRedirectPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(Url.URL_MAIN)
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.go_to_url(Url.URL_MAIN)
    return page

@pytest.fixture
def redirect_page(driver):
    page2 = ScooterRedirectPage(driver)
    page2.go_to_url(Url.URL_ORDER)
    return page2
