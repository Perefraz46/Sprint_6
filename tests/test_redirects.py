from pages.redirect_page import ScooterRedirectPage
import allure


class TestScooterRedirectPage:

    @allure.title('Проверка редиректа на главную страницу')
    @allure.description('Переходим с экрана заказа в главный и проверям, что хедер отобразился')
    def test_click_scooter_logo(self, redirect_page):
        redirect_page.click_scooter_logo_to_redirect()
        header = redirect_page.wait_home_header()

        assert header.is_displayed(), 'Header не отображается на странице'

    @allure.title('Проверка редиректа в дзен')
    @allure.description('На странице нажимаем на "Яндекс",'
                        ' переходим к новой вкладке и проверям налигие лого дзена на экране')
    def test_click_yandex_logo(self, redirect_page, driver):
        redirect_page.click_yandex_logo_to_redirect()
        yandex_page = ScooterRedirectPage(driver)
        yandex_page.change_tab(driver)
        logo = yandex_page.wait_dzen_logo_on_screen()

        assert logo.is_displayed(), 'Иконка дзена не отобразилась на экране'
