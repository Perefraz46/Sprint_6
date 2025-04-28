from selenium.webdriver.common.by import By

class MainPageLocators:
    """ Локаторы для теста выпадающего списка """
    QUESTION_LOCATOR = [By.XPATH, "//div[@id = 'accordion__heading-{}']"]
    ANSWER_LOCATOR = [By.XPATH, "//div[@aria-labelledby = 'accordion__heading-{}']"]
    SCROLL_LOCATOR = [By.XPATH, "//div[@id = 'accordion__heading-7']"]

    """ Кнопки заказать """
    ORDER_BUTTON_TOP = [By.XPATH, "//button[@class = 'Button_Button__ra12g']"]
    ORDER_BUTTON_MIDDLE = [By.XPATH, "//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM']"]
