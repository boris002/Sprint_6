import allure


@allure.title("Заполнить форму заказа и подтвердить")
def make_order(order_page, order_data):
    order_page.set_first_name(order_data["first_name"])
    order_page.set_last_name(order_data["last_name"])
    order_page.set_address(order_data["address"])
    order_page.set_metro_station(order_data["metro"])
    order_page.set_phone(order_data["phone"])
    order_page.click_next_button()

    order_page.set_date(order_data["date"])
    order_page.set_rent_duration(order_data["rent_period"])
    order_page.select_color(order_data["color"])
    order_page.set_comment(order_data["comment"])

    order_page.click_order_button()
    order_page.confirm_order()

    assert order_page.is_order_confirmed()
