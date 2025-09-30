import allure
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class HomePageSamokat:

    def __init__(self, driver):
        self.driver = driver

    # Cookie 
    @allure.step('Принять куки, если баннер есть')
    def click_cookie_accept(self):
        try:
            el = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(MainPageLocators.COOKIE_ACCEPT_BUTTON)
            )
            el.click()
        except Exception:
            pass

    # Общие методы 
    @allure.step('Скролл к элементу: {locator}')
    def scroll_to_element(self, locator):
        el = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(locator)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)
        return el

    @allure.step('Клик по элементу: {locator}')
    def click_on_element(self, locator):
        el = self.scroll_to_element(locator)
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(locator)
        )
        el.click()

    @allure.step('Клик по элементу с ActionChains: {locator}')
    def click_element_with_actionchains(self, locator):
        el = self.scroll_to_element(locator)
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(locator)
        )
        ActionChains(self.driver).move_to_element(el).click().perform()

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

    @allure.step('Клик по логотипу Яндекса и переход на новую вкладку')
    def click_logo_yandex(self):
        self.click_on_element(MainPageLocators.LOGO_YANDEX)
        WebDriverWait(self.driver, 5).until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 5).until(lambda d: "dzen.ru" in d.current_url)

    # FAQ 
    @allure.step('Клик по вопросу FAQ: {question_locator}')
    def click_faq_question(self, question_locator):
        el = self.scroll_to_element(question_locator)
        ActionChains(self.driver).move_to_element(el).click().perform()

    @allure.step('Получить текст ответа FAQ: {answer_locator}')
    def get_faq_answer_text(self, answer_locator):
        el = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(answer_locator)
        )
        return el.text.strip()

    def get_faq_question_locator(self, index):
        return MainPageLocators.FAQ_LOCATORS[index]["question"]

    def get_faq_answer_locator(self, index):
        return MainPageLocators.FAQ_LOCATORS[index]["answer"]
