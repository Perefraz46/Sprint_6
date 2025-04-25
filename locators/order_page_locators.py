from selenium.webdriver.common.by import By

class OrderPageLocators:
    """ экран Для кого самокат """
    NAME_FIELD = [By.XPATH, '//input[@placeholder = "* Имя"]']
    SURNAME_FIELD = [By.XPATH, "//input[@placeholder = '* Фамилия']"]
    ADDRESS_FIELD = [By.XPATH, "//input[@placeholder = '* Адрес: куда привезти заказ']"]
    STATION_FIELD = [By.XPATH, "//input[@placeholder = '* Станция метро']"]
    FIRST_STATION = [By.XPATH, "//button[@value='1']"]
    SECOND_STATION = [By.XPATH, "//button[@value='23']"]
    STATION_DROP_DOWN = [By.CSS_SELECTOR, '.select-search__select']
    PHONE_FIELD = [By.XPATH, "//input[@placeholder = '* Телефон: на него позвонит курьер']"]
    NEXT_BUTTON = [By.XPATH, '//button[@class = "Button_Button__ra12g Button_Middle__1CSJM"]']

    """ экран Про аренду """
    ABOUT_ORDER_HEADER = [By.XPATH, "//div[@class = 'Order_Header__BZXOb']"]
    DELIVERY_TIME = [By.XPATH, "//input[@placeholder = '* Когда привезти самокат']"]
    DELIVERY_DAY_FIRST = [By.XPATH, "//div[contains(@class, 'day react-datepicker__day--026')]"]
    DELIVERY_DAY_SECOND = [By.XPATH, "//div[contains(@class, 'day react-datepicker__day--030')]"]
    ORDER_TIME = [By.XPATH, "//div[@class= 'Dropdown-root']"]
    ORDER_DROP_DOWN_1 = [By.XPATH, "//div[@class= 'Dropdown-option' and text()='сутки']"]
    ORDER_DROP_DOWN_2 = [By.XPATH, "//div[@class= 'Dropdown-option' and text()='семеро суток']"]
    BLACK_SCOOTER = [By.XPATH, "//input[@id= 'black']"]
    GREY_SCOOTER = [By.XPATH, "//input[@id= 'grey']"]
    COMMENT = [By.XPATH, "//input[@placeholder= 'Комментарий для курьера']"]
    ORDER_BUTTON = [By.XPATH, "//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM' and text() = 'Заказать']"]
    APPROVE_BUTTON = [By.XPATH, "//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM' and text() = 'Да']"]
    POPUP_ORDER = [By.XPATH, "//div[@class = 'Order_Modal__YZ-d3']"]
