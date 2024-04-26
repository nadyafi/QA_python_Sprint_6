import allure
from pages.base_page import BasePage
from locators.main_page_locators import *


class MainPage(BasePage):

    @allure.step('Выполняем скролл до последнего вопроса')
    def scroll_to_bottom(self):
        self.scroll_to_element(MainPageLocators.question_8)
        self.wait_for_visibility(MainPageLocators.question_8)
