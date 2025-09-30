from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from locators.order_page_locators import OrderPageLocators


class OrderFormPage:

    def __init__(self, driver):
        self.driver = driver

    # ---------------- Для кого самокат ----------------
    @allure.step("Установить имя: {value}")
    def set_first_name(self, value):
        self.driver.find_element(*OrderPageLocators.INPUT_FIRST_NAME).send_keys(value)

    @allure.step("Установить фамилию: {value}")
    def set_last_name(self, value):
        self.driver.find_element(*OrderPageLocators.INPUT_LAST_NAME).send_keys(value)

    @allure.step("Установить адрес: {value}")
    def set_address(self, value):
        self.driver.find_element(*OrderPageLocators.INPUT_ADDRESS).send_keys(value)

    @allure.step("Выбрать станцию метро: {value}")
    def set_metro_station(self, value):
        self.driver.find_element(*OrderPageLocators.INPUT_METRO).send_keys(value)
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(OrderPageLocators.SELECTED_STATION)
        ).click()

    @allure.step("Установить телефон: {value}")
    def set_phone(self, value):
        self.driver.find_element(*OrderPageLocators.INPUT_PHONE).send_keys(value)

    @allure.step("Нажать кнопку 'Далее'")
    def click_next_button(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(OrderPageLocators.BUTTON_NEXT)
        ).click()

    #  Про аренду 
    @allure.step("Выбрать дату аренды: {value}")
    def set_date(self, value):
        self.driver.find_element(*OrderPageLocators.INPUT_DATE).click()

        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(OrderPageLocators.CALENDAR)
        )

        if value.lower() == "today":
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(OrderPageLocators.TODAY_DATE_CALENDAR)
            ).click()
        elif value.lower() == "tomorrow":
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(OrderPageLocators.TOMORROW_DATE_CALENDAR)
            ).click()
        else:
            raise ValueError("Поддерживаются только значения 'today' или 'tomorrow'")

    @allure.step("Выбрать длительность аренды: {rent_type}")
    def set_rent_duration(self, rent_type):
        dropdown = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(OrderPageLocators.DROPDOWN_RENT)
        )
        dropdown.click()

        if rent_type == "сутки":
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(OrderPageLocators.RENT_ONE_DAY)
            ).click()
        elif rent_type == "двое суток":
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(OrderPageLocators.RENT_TWO_DAYS)
            ).click()

    @allure.step("Выбрать цвет самоката: {color}")
    def select_color(self, color):
        if color == "black":
            self.driver.find_element(*OrderPageLocators.CHECKBOX_BLACK).click()
        elif color == "grey":
            self.driver.find_element(*OrderPageLocators.CHECKBOX_GREY).click()

    @allure.step("Установить комментарий: {value}")
    def set_comment(self, value):
        self.driver.find_element(*OrderPageLocators.INPUT_COMMENT).send_keys(value)

    @allure.step("Нажать кнопку 'Заказать'")
    def click_order_button(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(OrderPageLocators.BUTTON_ORDER)
        ).click()

    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(OrderPageLocators.BUTTON_YES)
        ).click()

    @allure.step("Проверить, что заказ оформлен")
    def is_order_confirmed(self):
        modal = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(OrderPageLocators.MODAL_COMPLETE_ORDER)
        )
        return "Заказ оформлен" in modal.text.strip()

    @allure.step("Нажать кнопку 'Назад'")
    def click_back_button(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(OrderPageLocators.BUTTON_BACK)
        ).click()
