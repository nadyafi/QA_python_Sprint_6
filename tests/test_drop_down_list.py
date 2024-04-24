import allure
import pytest
from data import *
from locators.main_page_locators import *


@allure.story('Тесты выпадающего списка "Вопросы о важном"')
class TestDropDownList:
    @allure.title('Тест соответсвия текста ответа')
    @pytest.mark.parametrize('question, answer, answer_text', [
        [MainPageLocators.question_1, MainPageLocators.answer_1, Answer_text.answer_text_1],
        [MainPageLocators.question_2, MainPageLocators.answer_2, Answer_text.answer_text_2],
        [MainPageLocators.question_3, MainPageLocators.answer_3, Answer_text.answer_text_3],
        [MainPageLocators.question_4, MainPageLocators.answer_4, Answer_text.answer_text_4],
        [MainPageLocators.question_5, MainPageLocators.answer_5, Answer_text.answer_text_5],
        [MainPageLocators.question_6, MainPageLocators.answer_6, Answer_text.answer_text_6],
        [MainPageLocators.question_7, MainPageLocators.answer_7, Answer_text.answer_text_7],
        [MainPageLocators.question_8, MainPageLocators.answer_8, Answer_text.answer_text_8]
    ])
    def test_drop_down_text(self, driver, main_page, question, answer, answer_text):
        main_page.open()
        main_page.accept_cookies()
        main_page.scroll_to_bottom()
        main_page.click(question)
        assert main_page.get_text(answer) == answer_text
