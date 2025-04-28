from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
import allure


class OrderPage(BasePage):

    @allure.step('Создание заказа')
    def set_order(self, data):
        self.add_text_to_element(OrderPageLocators.NAME_FIELD,data['name'])
        self.add_text_to_element(OrderPageLocators.SURNAME_FIELD,data['surname'])
        self.add_text_to_element(OrderPageLocators.ADDRESS_FIELD,data['address'])
        self.click_to_element(data['station_filed'])
        self.scroll_to_element(data['station_click'])
        self.click_to_element(data['station_click'])
        self.add_text_to_element(OrderPageLocators.PHONE_FIELD, data['number'])
        self.click_to_element(OrderPageLocators.NEXT_BUTTON)
        self.click_to_element(OrderPageLocators.DELIVERY_TIME)
        self.click_to_element(data['delivery'])
        self.click_to_element(OrderPageLocators.ORDER_TIME)
        self.scroll_to_element(data['order_day'])
        self.click_to_element(data['order_day'])
        self.click_to_element(data['scooter'])
        self.add_text_to_element(OrderPageLocators.COMMENT, data['comment'])
        self.click_to_element(OrderPageLocators.ORDER_BUTTON)
        self.click_to_element(OrderPageLocators.APPROVE_BUTTON)

    @allure.step('Ожидание отображения поп апа на экране')
    def wait_popup(self):
        return self.find_element_with_wait(OrderPageLocators.POPUP_ORDER)
