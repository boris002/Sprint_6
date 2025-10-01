import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage

class OrderFormPage(BasePage):

    #  Для кого самокат 
    @allure.step("Установить имя: {value}")
    def set_first_name(self, value):
        self.enter_text(OrderPageLocators.INPUT_FIRST_NAME, value)
    
    @allure.step("Установить фамилию: {value}")
    def set_last_name(self, value):
        self.enter_text(OrderPageLocators.INPUT_LAST_NAME, value)

    @allure.step("Установить адрес: {value}")
    def set_address(self, value):
        self.enter_text(OrderPageLocators.INPUT_ADDRESS, value)

    @allure.step("Выбрать станцию метро: {value}")
    def set_metro_station(self, value):
        self.enter_text(OrderPageLocators.INPUT_METRO, value)
        self.click_on_element(OrderPageLocators.SELECTED_STATION)

    @allure.step("Установить телефон: {value}")
    def set_phone(self, value):
        self.enter_text(OrderPageLocators.INPUT_PHONE, value)

    @allure.step("Нажать кнопку 'Далее'")
    def click_next_button(self):
        self.click_on_element(OrderPageLocators.BUTTON_NEXT)


    #  Про аренду 
    @allure.step("Выбрать дату аренды: {value}")
    def set_date(self, value):
        self.click_on_element(OrderPageLocators.INPUT_DATE)
        self.wait_visible(OrderPageLocators.CALENDAR)

        if value.lower() == "today":
            self.click_on_element(OrderPageLocators.TODAY_DATE_CALENDAR)
        elif value.lower() == "tomorrow":
            self.click_on_element(OrderPageLocators.TOMORROW_DATE_CALENDAR)
        else:
            raise ValueError("Поддерживаются только значения 'today' или 'tomorrow'")

    @allure.step("Выбрать длительность аренды: {rent_type}")
    def set_rent_duration(self, rent_type):
        self.click_on_element(OrderPageLocators.DROPDOWN_RENT)

        if rent_type == "сутки":
            self.click_on_element(OrderPageLocators.RENT_ONE_DAY)
        elif rent_type == "двое суток":
            self.click_on_element(OrderPageLocators.RENT_TWO_DAYS)


    @allure.step("Выбрать цвет самоката: {color}")
    def select_color(self, color):
        if color == "black":
            self.click_on_element(OrderPageLocators.CHECKBOX_BLACK)
        elif color == "grey":
            self.click_on_element(OrderPageLocators.CHECKBOX_GREY)

    @allure.step("Установить комментарий: {value}")
    def set_comment(self, value):
        self.enter_text(OrderPageLocators.INPUT_COMMENT, value)

    @allure.step("Нажать кнопку 'Заказать'")
    def click_order_button(self):
       self.click_on_element(OrderPageLocators.BUTTON_ORDER)
    
    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        self.click_on_element(OrderPageLocators.BUTTON_YES)

    @allure.step("Проверить, что заказ оформлен")
    def is_order_confirmed(self):
        return "Заказ оформлен" in self.get_text(OrderPageLocators.MODAL_COMPLETE_ORDER)


    @allure.step("Нажать кнопку 'Назад'")
    def click_back_button(self):
        self.click_on_element(OrderPageLocators.BUTTON_BACK)
