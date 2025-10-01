import pytest
import allure
from data.faq_tests import (
    FAQ_ANSWER_1, FAQ_ANSWER_2, FAQ_ANSWER_3, FAQ_ANSWER_4,
    FAQ_ANSWER_5, FAQ_ANSWER_6, FAQ_ANSWER_7, FAQ_ANSWER_8
)

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
    @allure.title("Проверка FAQ ответа для вопроса {index}")
    def test_faq_answers(self, home_page, index, expected_answer):
        home_page.click_cookie_accept()
        question = home_page.get_faq_question_locator(index)
        answer = home_page.get_faq_answer_locator(index)

        home_page.click_faq_question(question)
        actual = home_page.get_faq_answer_text(answer)

        assert actual == expected_answer

    @allure.title("Форма заказа открывается через кнопку хедера")
    def test_order_button_header_opens_form(self, home_page):
        home_page.click_order_button_header()
        assert "order" in home_page.get_current_url()

    @allure.title("Форма заказа открывается через кнопку на странице")
    def test_order_button_page_opens_form(self, home_page):
        home_page.click_order_button_page()
        assert "order" in home_page.get_current_url()

    @allure.title("Переход на главную через логотип скутера")
    def test_logo_scooter_redirect(self, home_page):
        home_page.click_order_button_page()
        url = home_page.click_logo_scooter()
        assert "scooter" in url

    @allure.title("Переход по логотипу Яндекса")
    def test_logo_yandex_redirect(self, home_page):
        url = home_page.click_logo_yandex()
        assert "dzen.ru" in url
