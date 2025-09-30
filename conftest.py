import pytest
from selenium import webdriver
from data.urls import BASE_URL
from pages.main_page import HomePageSamokat
from pages.order_page import OrderFormPage


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def home_page(driver):
    home_page = HomePageSamokat(driver)
    home_page.click_cookie_accept()
    return home_page


@pytest.fixture
def order_page(driver):
    return OrderFormPage(driver)
