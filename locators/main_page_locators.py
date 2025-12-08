from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопки
    COOKIE_ACCEPT_BUTTON = (By.ID, "rcc-confirm-button")
    ORDER_BUTTON_HEADER = (By.CLASS_NAME, "Button_Button__ra12g")          # Заказать (в хедере)
    ORDER_STATUS_BUTTON = (By.CLASS_NAME, "Header_Link__1TAG7")            # Статус заказа (в хедере)
    ORDER_BUTTON_PAGE = (By.CLASS_NAME, "Button_Middle__1CSJM")            # Заказать (на странице)

    # Логотипы
    LOGO_YANDEX = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    LOGO_SCOOTER = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")

    # Тексты на главной
    HOW_IT_WORKS_TEXT = (By.XPATH, "//div[text()='Как это работает']")
    IMPORTANT_QUESTIONS_TEXT = (By.XPATH, "//div[text()='Вопросы о важном']")

    # FAQ (вопросы и ответы)
    FAQ_LOCATORS = [
        {
            "question": (By.ID, "accordion__heading-0"),
            "answer": (By.ID, "accordion__panel-0"),
        },
        {
            "question": (By.ID, "accordion__heading-1"),
            "answer": (By.ID, "accordion__panel-1"),
        },
        {
            "question": (By.ID, "accordion__heading-2"),
            "answer": (By.ID, "accordion__panel-2"),
        },
        {
            "question": (By.ID, "accordion__heading-3"),
            "answer": (By.ID, "accordion__panel-3"),
        },
        {
            "question": (By.ID, "accordion__heading-4"),
            "answer": (By.ID, "accordion__panel-4"),
        },
        {
            "question": (By.ID, "accordion__heading-5"),
            "answer": (By.ID, "accordion__panel-5"),
        },
        {
            "question": (By.ID, "accordion__heading-6"),
            "answer": (By.ID, "accordion__panel-6"),
        },
        {
            "question": (By.ID, "accordion__heading-7"),
            "answer": (By.ID, "accordion__panel-7"),
        },
    ]
