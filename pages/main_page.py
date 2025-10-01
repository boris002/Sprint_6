import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class HomePageSamokat(BasePage):

    # Cookie 
    @allure.step('Принять куки, если баннер есть')
    def click_cookie_accept(self):
        try:
            self.click_on_element(MainPageLocators.COOKIE_ACCEPT_BUTTON)
        except Exception:
            pass

    
    # Кнопки 
    @allure.step('Клик по кнопке "Заказать" в хедере')
    def click_order_button_header(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON_HEADER)

    @allure.step('Клик по кнопке "Заказать" на странице')
    def click_order_button_page(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON_PAGE)

    @allure.step('Клик по логотипу скутера')
    def click_logo_scooter(self):
        self.click_on_element(MainPageLocators.LOGO_SCOOTER)
        self.wait_until(lambda _: "scooter" in self.get_current_url())
        return self.get_current_url()
    
    @allure.step('Клик по логотипу Яндекса и переход на новую вкладку')
    def click_logo_yandex(self):
        self.click_on_element(MainPageLocators.LOGO_YANDEX)
        return self.switch_to_new_tab("dzen.ru")

    # FAQ 
    @allure.step('Клик по вопросу FAQ: {question_locator}')
    def click_faq_question(self, question_locator):
        self.click_with_actionchains(question_locator)

    @allure.step('Получить текст ответа FAQ: {answer_locator}')
    def get_faq_answer_text(self, answer_locator):
        return self.get_text(answer_locator)

    def get_faq_question_locator(self, index):
        return MainPageLocators.FAQ_LOCATORS[index]["question"]

    def get_faq_answer_locator(self, index):
        return MainPageLocators.FAQ_LOCATORS[index]["answer"]
