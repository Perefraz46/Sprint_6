from locators.order_page_locators import OrderPageLocators
from random import randint

class Url:
    URL_MAIN = 'https://qa-scooter.praktikum-services.ru/'
    URL_ORDER = 'https://qa-scooter.praktikum-services.ru/order'


class Data:

    ANSWERS_DATA = ['Сутки — 400 рублей. Оплата курьеру — наличными или картой.',
                    'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.',
                    'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.',
                    'Только начиная с завтрашнего дня. Но скоро станем расторопнее.',
                    'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.',
                    'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.',
                    'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.',
                    'Да, обязательно. Всем самокатов! И Москве, и Московской области.']

    ORDER_DATA_1 = {'name':'Тест',
                    'surname':'Тестов',
                    'address': 'ул.Тестовая',
                    'station_filed': OrderPageLocators.STATION_FIELD,
                    'station_click': OrderPageLocators.FIRST_STATION,
                    'number': f'796{randint(00000000,99999999)}',
                    'delivery': OrderPageLocators.DELIVERY_DAY_FIRST,
                    'order_day': OrderPageLocators.ORDER_DROP_DOWN_1,
                    'scooter' : OrderPageLocators.BLACK_SCOOTER,
                    'comment' : 'обычный комментарий'}

    ORDER_DATA_2 = {'name':'Тестировщик',
                    'surname':'Тестович',
                    'address': 'ул.Тестировщиков',
                    'station_filed': OrderPageLocators.STATION_FIELD,
                    'station_click': OrderPageLocators.SECOND_STATION,
                    'number': f'792{randint(00000000,99999999)}',
                    'delivery': OrderPageLocators.DELIVERY_DAY_SECOND,
                    'order_day': OrderPageLocators.ORDER_DROP_DOWN_2,
                    'scooter' : OrderPageLocators.GREY_SCOOTER,
                    'comment': ''}
