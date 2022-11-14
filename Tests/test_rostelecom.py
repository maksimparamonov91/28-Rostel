# python -m pytest -v --driver chrome --driver-path chromedriver.exe tests/test_rostelecom.py

from config import TestData
from Pages.rostelecom import RostelecomPage

import time
import pytest


@pytest.mark.xfail
def test_loud_page(web_browser):
    page = RostelecomPage(web_browser)
    page.wait_page_loaded()
    assert page.check_js_errors()


# 1
def test_visible_block_page_right(web_browser):
     """ Правая часть блока аторизации видна на странице """
     page = RostelecomPage(web_browser)
     assert page.LOCATOR_page_right.is_visible()

#2
def test_visible_block_page_left(web_browser):
     """ Левая часть блока аторизации видна на странице """
     page = RostelecomPage(web_browser)
     assert page.LOCATOR_BLOCK_page_left.is_visible()

# 3
def test_clic_icon_forgot_password(web_browser):
    """ Переход по кнопке Забыл пароль переводит на страницу Восстановление пароля"""
    page = RostelecomPage(web_browser)
    page.LOCATOR_ICON_forgot_password.click()
    time.sleep(2)
    assert page.get_current_url()[:56] == TestData.forgot_password_url

#4
def test_clic_icon_OK(web_browser):
    """ Переход по иконке OK ведет на соответствующую страницу """
    page = RostelecomPage(web_browser)
    page.LOCATOR_ok.click()
    time.sleep(2)
    assert page.get_current_url()[:21] == TestData.ok_url

#5
def test_clic_icon_VK(web_browser):
    """ Переход по иконке VK ведет на соответствующую страницу """
    page = RostelecomPage(web_browser)
    page.LOCATOR_vk.click()
    time.sleep(2)
    assert page.get_current_url()[:20] == TestData.vk_url

#6
def test_clic_icon_mail(web_browser):
    """ Переход по иконке mail ведет на соответствующую страницу """
    page = RostelecomPage(web_browser)
    page.LOCATOR_mail.click()
    time.sleep(2)
    assert page.get_current_url()[:23] == TestData.mail_url

#7
def test_clic_icon_google(web_browser):
    """ Переход по иконке google ведет на соответствующую страницу """
    page = RostelecomPage(web_browser)
    page.LOCATOR_google.click()
    time.sleep(2)
    assert page.get_current_url()[:27] == TestData.google_url

#8
def test_clic_icon_ya(web_browser):
    """ Переход по иконке ya ведет на соответствующую страницу """
    page = RostelecomPage(web_browser)
    page.LOCATOR_ya.click()
    time.sleep(2)
    assert page.get_current_url()[:26] == TestData.ya_url

#9
def test_clic_icon_widget_bar(web_browser):
    """ Нажатие на "Отправить" в "Поддержке" """
    page = RostelecomPage(web_browser)
    page.LOCATOR_ICON_widget_bar.click()
    assert page.LOCATOR_ICON_widget_sendPrechat.is_clickable()

#10
def test_clic_icon_telegarm(web_browser):
    """ Наведение на Чат и проверка перехода на соответствующий телеграмм """
    page = RostelecomPage(web_browser)
    page.wait_page_loaded()
    page.LOCATOR_ICON_widget_bar.move_to_element()
    page.LOCATOR_telegarm.is_visible()
    page.LOCATOR_telegarm.click()
    time.sleep(2)
    page.get_current_url()[:2] == TestData.telegarm_url

#11
def test_clic_icon_viber(web_browser):
    """ Наведение на Чат и проверка перехода на соответствующий вайбер """
    page = RostelecomPage(web_browser)
    page.wait_page_loaded()
    page.LOCATOR_ICON_widget_bar.move_to_element()
    page.LOCATOR_viber.is_visible()
    page.LOCATOR_viber.click()
    time.sleep(2)
    assert page.get_current_url()[:20] == TestData.viber_url

#12
def test_clic_icon_88001000800(web_browser):
    """ Кликабельность кнопки 88001000800 """
    page = RostelecomPage(web_browser)
    page.wait_page_loaded()
    assert page.LOCATOR_88001000800.is_clickable()
    #page.get_current_url() == TestData.viber_url

#13
def test_clic_checkbox(web_browser):
    """ Кликабельность кнопки checkbox """
    page = RostelecomPage(web_browser)
    page.wait_page_loaded()
    assert page.LOCATOR_checkbox.is_clickable()

# 14
def test_wrong_login_or_password(web_browser):
    """ введение невалидного логина и пароля """
    page = RostelecomPage(web_browser)
    page.wait_page_loaded()
    page.LOCATOR_username.send_keys('абвгд')
    page.LOCATOR_password.send_keys('ежзик')
    page.LOCATOR_kc_login.click()
    page.LOCATOR_captcha.is_visible()
    time.sleep(10)
    assert page.LOCATOR_wrong_login_or_password.is_visible()

#15
def test_wrong_login_or_password(web_browser):
    """ регистрация нового пользователя с невалидным повторным паролем """
    page = RostelecomPage(web_browser)
    page.wait_page_loaded()
    page.LOCATOR_kc_register.is_visible()
    page.LOCATOR_kc_register.click()
    time.sleep(1)
    page.LOCATOR_firstName.send_keys('Сан')
    page.LOCATOR_lastName.send_keys('Саныч')
    page.LOCATOR_address.send_keys('123@mail.ru')
    page.LOCATOR_password.send_keys('Aa123456')
    page.LOCATOR_show_password.click()
    page.LOCATOR_password_confirm.send_keys('1234')
    page.LOCATOR_show_password_confirm.click()
    page.LOCATOR_register.click()
    time.sleep(5)
    assert page.LOCATOR_error_number_of_characters.is_visible()

#16
def test_wrong_2_password(web_browser):
    """ повторная регистрация ранее созданного пользователя """
    page = RostelecomPage(web_browser)
    page.wait_page_loaded()
    page.LOCATOR_kc_register.is_visible()
    page.LOCATOR_kc_register.click()
    time.sleep(1)
    page.LOCATOR_firstName.send_keys('Сан')
    page.LOCATOR_lastName.send_keys('Саныч')
    page.LOCATOR_address.send_keys('123@mail.ru')
    page.LOCATOR_password.send_keys('Aa123456')
    page.LOCATOR_show_password.click()
    page.LOCATOR_password_confirm.send_keys('Aa123456')
    page.LOCATOR_show_password_confirm.click()
    page.LOCATOR_register.click()
    time.sleep(2)
    assert page.LOCATOR_account_exist.is_visible()


