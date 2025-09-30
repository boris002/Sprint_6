import pytest
import allure
from data.faq_tests import (
    FAQ_ANSWER_1, FAQ_ANSWER_2, FAQ_ANSWER_3, FAQ_ANSWER_4,
    FAQ_ANSWER_5, FAQ_ANSWER_6, FAQ_ANSWER_7, FAQ_ANSWER_8
)
from selenium.webdriver.support.ui import WebDriverWait

@allure.epic("Главная страница")
class TestMainPage:

    @pytest.mark.parametrize("index, expected_answer", [
        (0, FAQ_ANSWER_1),
        (1, FAQ_ANSWER_2),
        (2, FAQ_ANSWER_3),
        (3, FAQ_ANSWER_4),
        (4, FAQ_ANSWER_5),
        (5, FAQ_ANSWER_6),
        (6, FAQ_ANSWER_7),
        (7, FAQ_ANSWER_8),
    ])
    @allure.step('Проверка FAQ ответа для вопроса {index}')
    def test_faq_answers(self, home_page, index, expected_answer):
        home_page.click_cookie_accept()
        question = home_page.get_faq_question_locator(index)
        answer = home_page.get_faq_answer_locator(index)

        home_page.click_faq_question(question)
        actual = home_page.get_faq_answer_text(answer)

        assert actual == expected_answer

    @allure.step('Проверка открытия формы заказа через кнопку хедера')
    def test_order_button_header_opens_form(self, home_page, driver):
        home_page.click_order_button_header()
        assert "order" in driver.current_url

    @allure.step('Проверка открытия формы заказа через кнопку страницы')
    def test_order_button_page_opens_form(self, home_page, driver):
        home_page.click_order_button_page()
        assert "order" in driver.current_url

    @allure.step('Проверка перехода на главную через логотип скутера')
    def test_logo_scooter_redirect(self, home_page, driver):
        home_page.click_order_button_page()
        WebDriverWait(driver, 5).until(lambda d: "order" in d.current_url)

        home_page.click_logo_scooter()
        WebDriverWait(driver, 5).until(lambda d: "scooter" in driver.current_url)

        assert "scooter" in driver.current_url

    @allure.step('Проверка перехода по логотипу Яндекса')
    def test_logo_yandex_redirect(self, home_page, driver):
        home_page.click_logo_yandex()
        assert "dzen.ru" in driver.current_url
