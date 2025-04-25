from data import Data
import pytest
import allure


class TestMainPage:

    @allure.title('Проверка текста в выпадающем меню')
    @allure.description('Находим на экране dropdown, кликаем на него и сравниваем фактический текст с ожидаемым')
    @pytest.mark.parametrize('num',[0, 1, 2, 3, 4, 5, 6, 7])
    def test_check_question_and_answer(self, main_page, num):
        answer = main_page.check_question_and_answer(num)

        assert answer == Data.ANSWERS_DATA[num], f'Ожидался текст: {Data.ANSWERS_DATA[num]}, получен текст: {answer}'
