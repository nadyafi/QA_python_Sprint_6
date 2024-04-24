from pages.base_page import *
from data import *
from locators.base_page_locators import DzenLocators


@allure.story('Тесты переходов по логотипу Яндекс/Самокат')
class TestLogoTransition:
    @allure.title('Тест перехода со страницы заказа на главую по клику на логотип "Самокат"')
    def test_logo_scooter(self, driver, order_page):
        order_page.open()
        order_page.wait_and_click_element(BasePageLocators.LOGO_SCOOTER)
        assert order_page.get_url() == Url.MAIN_PAGE

    @allure.title('Тест перехода с главной на страницу Яндекса по клику на логотиа "Яндекс"')
    def test_logo_yandex(self, driver, main_page):
        main_page.open()
        main_page.wait_and_click_element(BasePageLocators.LOGO_YANDEX)
        main_page.tab_switch(DzenLocators.DZEN_LOGO)
        assert Url.DZEN_PAGE in main_page.get_url()
