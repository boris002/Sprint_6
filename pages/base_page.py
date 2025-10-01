import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver, timeout=5):
        self.driver = driver
        self.timeout = timeout

    # ---------------- Общие методы ----------------
    @allure.step('Ожидание кликабельности: {locator}')
    def wait_clickable(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step('Ожидание видимости: {locator}')
    def wait_visible(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step('Ожидание присутствия: {locator}')
    def wait_present(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(locator)
        )

    @allure.step('Скролл к элементу: {locator}')
    def scroll_to_element(self, locator):
        el = self.wait_present(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)
        return el

    @allure.step('Клик по элементу: {locator}')
    def click_on_element(self, locator):
        el = self.scroll_to_element(locator)
        self.wait_clickable(locator)
        el.click()

    @allure.step('Клик с ActionChains: {locator}')
    def click_with_actionchains(self, locator):
        el = self.scroll_to_element(locator)
        self.wait_clickable(locator)
        ActionChains(self.driver).move_to_element(el).click().perform()

    @allure.step('Ввести текст "{text}" в элемент: {locator}')
    def enter_text(self, locator, text):
        el = self.wait_present(locator)
        el.clear()
        el.send_keys(text)

    @allure.step('Получить текст элемента: {locator}')
    def get_text(self, locator):
        el = self.wait_visible(locator)
        return el.text.strip()

    def wait_until(self, condition):
        return WebDriverWait(self.driver, self.timeout).until(condition)

    def switch_to_new_tab(self, url_part):
        self.wait_until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.wait_until(lambda d: url_part in d.current_url)
        return self.driver.current_url

    def get_current_url(self):
        return self.driver.current_url