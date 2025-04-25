from locators.redirect_page_locators import RedirectPageLocators
from pages.base_page import BasePage
import allure


class ScooterRedirectPage(BasePage):

    @allure.step('Клик на лого самоката')
    def click_scooter_logo_to_redirect(self):
        self.click_to_element(RedirectPageLocators.SCOOTER_LOGO)

    @allure.step('Ожидание отображения хедера')
    def wait_home_header(self):
        return self.find_element_with_wait(RedirectPageLocators.HOME_HEADER)

    @allure.step('Клик на лого яндекса')
    def click_yandex_logo_to_redirect(self):
        self.click_to_element(RedirectPageLocators.YANDEX_LOGO)

    @allure.step('Ожидание отображения лого дзена')
    def wait_dzen_logo_on_screen(self):
        return self.find_element_with_wait(RedirectPageLocators.DZEN_LOGO)
