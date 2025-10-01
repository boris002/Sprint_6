from selenium.webdriver.common.by import By

class OrderPageLocators:
    # Блок "Для кого самокат"
    INPUT_FIRST_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    INPUT_LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    INPUT_ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    INPUT_METRO = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_STATION_LIST = (By.CLASS_NAME, "select-search__select")
    SELECTED_STATION = (By.XPATH, ".//li[@class='select-search__row']")
    INPUT_PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    BUTTON_NEXT = (By.XPATH, "//button[text()='Далее']")

    # Блок "Про аренду"
    INPUT_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    CALENDAR = (By.CLASS_NAME, "react-datepicker__month-container")
    TODAY_DATE_CALENDAR = (By.CLASS_NAME, "react-datepicker__day--today")
    TOMORROW_DATE_CALENDAR = (By.XPATH, "//div[contains(@class, 'react-datepicker__day--today')]/following-sibling::div[1]")
    CURRENT_MONTH = (By.CLASS_NAME, "react-datepicker__current-month")
    NEXT_MONTH_BUTTON = (By.CLASS_NAME, "react-datepicker__navigation--next")
   
    # Выпадающий список аренды
    DROPDOWN_RENT = (By.CLASS_NAME, "Dropdown-control")
    RENT_OPTION = (By.CLASS_NAME, "Dropdown-option")  # общий локатор для элементов списка
    RENT_ONE_DAY = (By.XPATH, ".//div[@class='Dropdown-menu']/div[text()='сутки']")
    RENT_TWO_DAYS = (By.XPATH, ".//div[@class='Dropdown-menu']/div[text()='двое суток']")
    RENT_AFTER_SELECTED = (By.CLASS_NAME, "Dropdown-placeholder.is-selected")

    # Цвет самоката
    CHECKBOX_BLACK = (By.ID, "black")
    CHECKBOX_GREY = (By.ID, "grey")
    LABEL_COLOR_TITLE = (By.XPATH, '//div[text()="Цвет самоката"]')
    # Поле комментария
    INPUT_COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")

    # Кнопки
    BUTTON_BACK = (By.XPATH, "//button[text()='Назад']")
    # Кнопка "Заказать" в форме
    BUTTON_ORDER = (By.XPATH, "//div[contains(@class,'Order_Buttons')]/button[text()='Заказать']")


    # Модалка подтверждения заказа
    MODAL_HEADER = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")
    BUTTON_NO = (By.XPATH, "//button[text()='Нет']")
    BUTTON_YES = (By.XPATH, "//button[text()='Да']")

    # Модалка "Заказ оформлен"
    MODAL_COMPLETE_ORDER = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")
