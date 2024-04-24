import allure
import pytest

from data import *
from locators.order_page_locators import *


@allure.story('Тесты заказа самоката')
class TestScooterOrder:
    @allure.title('Позитивный тест заказа самоката')
    @pytest.mark.parametrize('button, data', [(OrderPageLocators.ORDER_BUTTON_UP, User1),
                                              (OrderPageLocators.ORDER_BUTTON_DOWN, User2)])
    def test_scooter_order(self, driver, button, data, order_page, main_page):
        main_page.open()
        order_page.accept_cookies()
        order_page.wait_and_click_element(button)
        order_page.client_form(data)
        order_page.rent_form(data)
        order_page.wait_and_click_element(OrderPageLocators.BUTTON_YES)
        assert order_page.order_issued_check() == 'Посмотреть статус'
