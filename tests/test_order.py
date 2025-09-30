import pytest
import allure
from data.order_data import ORDER_DATA_1, ORDER_DATA_2


@allure.epic("Оформление заказа")
class TestOrderPage:

    @pytest.mark.parametrize("order_data", [ORDER_DATA_1, ORDER_DATA_2])
    @allure.story("Оформление заказа с главной страницы")
    def test_make_order_from_page(self, home_page, order_page, order_data):
        with allure.step("Клик по кнопке 'Заказать' на странице"):
            home_page.click_order_button_page()
        self._make_order(order_page, order_data)

    @pytest.mark.parametrize("order_data", [ORDER_DATA_1, ORDER_DATA_2])
    @allure.story("Оформление заказа с хедера")
    def test_make_order_from_header(self, home_page, order_page, order_data):
        with allure.step("Клик по кнопке 'Заказать' в хедере"):
            home_page.click_order_button_header()
        self._make_order(order_page, order_data)

    @allure.step("Заполнить форму заказа и подтвердить")
    def _make_order(self, order_page, order_data):
        # ---------------- Для кого самокат ----------------
        order_page.set_first_name(order_data["first_name"])
        order_page.set_last_name(order_data["last_name"])
        order_page.set_address(order_data["address"])
        order_page.set_metro_station(order_data["metro"])
        order_page.set_phone(order_data["phone"])
        order_page.click_next_button()

        #Про аренду 
        order_page.set_date(order_data["date"])
        order_page.set_rent_duration(order_data["rent_period"])
        order_page.select_color(order_data["color"])
        order_page.set_comment(order_data["comment"])

        #Подтверждение
        order_page.click_order_button()
        order_page.confirm_order()

        #Проверка
        assert order_page.is_order_confirmed()
