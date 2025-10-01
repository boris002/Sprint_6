import pytest
import allure
from data.order_data import ORDER_DATA_1, ORDER_DATA_2
from helpers.order_helpers import make_order


@allure.epic("Оформление заказа")
class TestOrderPage:

    @pytest.mark.parametrize("order_data", [ORDER_DATA_1, ORDER_DATA_2])
    @allure.title("Оформление заказа с главной страницы")
    def test_make_order_from_page(self, home_page, order_page, order_data):
        home_page.click_order_button_page()
        make_order(order_page, order_data)

    @pytest.mark.parametrize("order_data", [ORDER_DATA_1, ORDER_DATA_2])
    @allure.title("Оформление заказа с хедера")
    def test_make_order_from_header(self, home_page, order_page, order_data):
        home_page.click_order_button_header()
        make_order(order_page, order_data)

   