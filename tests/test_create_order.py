from data import Data
from locators.main_page_locators import MainPageLocators
from pages.order_page import OrderPage
import pytest
import allure


class TestCreateOrder:

    @allure.title('Проверка создания заказа')
    @allure.description('В главном экране нажимаем кнопку "Заказать", дожидаемся отображения формы заказа,'
                        ' заполняем форму и проверяем наличие поп апа успешного заказа')
    @pytest.mark.parametrize(
        'locator, order_data',
        [
        (MainPageLocators.ORDER_BUTTON_TOP, Data.ORDER_DATA_1),
        (MainPageLocators.ORDER_BUTTON_MIDDLE, Data.ORDER_DATA_2)
                                                     ])
    def test_create_order(self, main_page, driver, locator, order_data):
        main_page.scroll_to_element(locator)
        main_page.click_to_element(locator)
        order_page = OrderPage(driver)
        order_page.set_order(order_data)
        popup = order_page.wait_popup()

        assert popup.is_displayed()
