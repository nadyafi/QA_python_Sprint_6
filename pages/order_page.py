import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from locators.base_page_locators import *


class OrderPage(BasePage):
    @allure.step('Заполнение формы "Для кого самокат"')
    def client_form(self, data):
        self.wait_and_send_input(OrderPageLocators.name_INPUT, data.name)
        self.wait_and_send_input(OrderPageLocators.surname_INPUT, data.surname)
        self.wait_and_send_input(OrderPageLocators.address_INPUT, data.address)
        self.wait_and_send_input(OrderPageLocators.underground_INPUT, data.underground)
        self.wait_and_click_element(OrderPageLocators.SELECT_underground)
        self.wait_and_send_input(OrderPageLocators.PHONE_number_INPUT, data.number)
        self.wait_and_click_element(OrderPageLocators.BUTTON_NEXT)

    @allure.step('Заполнение формы "Про аренду"')
    def rent_form(self, data):
        self.wait_and_send_input(OrderPageLocators.date_INPUT, data.date)
        self.wait_and_click_element(OrderPageLocators.SELECT_COLOR_GREY)
        self.wait_and_click_element(OrderPageLocators.RENTAL_PERIOD)
        self.wait_and_click_element(OrderPageLocators.RENTAL_PERIOD_ONE_DAY)
        self.wait_and_send_input(OrderPageLocators.comment_INPUT, data.comment)
        self.wait_and_click_element(OrderPageLocators.BUTTON_ORDER)

    @allure.step('Проверка успешного оформления заказа')
    def order_issued_check(self):
        return self.get_text(OrderPageLocators.ORDER_STATUS)

    @allure.step('Переход по лого Яндекс')
    def click_on_yandex_logo(self):
        self.wait_and_click_element(BasePageLocators.LOGO_SCOOTER)

    @allure.step('Переход по лого Самокат')
    def click_on_scooter_logo(self):
        self.wait_and_click_element(BasePageLocators.LOGO_YANDEX)
        self.tab_switch(DzenLocators.DZEN_LOGO)
