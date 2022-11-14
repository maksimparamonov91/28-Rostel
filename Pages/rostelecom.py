import os
from Pages.base import WebPage
from Pages.elements import WebElement, ManyWebElements


class RostelecomPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = 'https://b2c.passport.rt.ru'
        super().__init__(web_driver, url)

# блок авторизации правая часть
    LOCATOR_page_right = WebElement(id='page-right')

# блок авторизации левая часть
    LOCATOR_BLOCK_page_left = WebElement(id='page-left')

# иконка забыл пароль
    LOCATOR_ICON_forgot_password = WebElement(id='forgot_password')

# локатор одноклассники
    LOCATOR_ok = WebElement(id='oidc_ok')

# локатор вконтакте
    LOCATOR_vk = WebElement(id='oidc_vk')

# локатор mail
    LOCATOR_mail = WebElement(id='oidc_mail')

# локатор google
    LOCATOR_google = WebElement(id='oidc_google')

# локатор ya
    LOCATOR_ya = WebElement(id='oidc_ya')

# Иконка Поддержка
    LOCATOR_ICON_widget_bar = WebElement(id='widget_bar')

# Иконка Отправить
    LOCATOR_ICON_widget_sendPrechat = WebElement(id='widget_sendPrechat')

# Иконка Отправить в вайбер
    LOCATOR_viber = WebElement(xpath='//*[@id="widget_bar"]/div[3]/a[1]')

# Иконка Отправить в телеграмм
    LOCATOR_telegarm = WebElement(xpath='//*[@id="widget_bar"]/div[3]/a[2]')

# локатор всплывающего окна сообщения
    LOCATOR_forgot_passwor = WebElement(xpath='//*[@id="full-name" and @id="phone" and @id="widget_sendPrechat"]')

# локатор запомнить меня
    LOCATOR_rememberMe = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[3]/label/span[1]/svg/path')

# локатор tel:88001000800//*[@id="page-right"]/div/div/div/form/div[3]/label/span[1]
    LOCATOR_88001000800 = WebElement(xpath='//*[@id="app-footer"]/div[2]/a')

# локатор checkbox
    LOCATOR_checkbox = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[3]/label/span[1]')

# локатор username
    LOCATOR_username = WebElement(id='username')

# локатор password
    LOCATOR_password = WebElement(id='password')

# локатор Войти
    LOCATOR_kc_login = WebElement(id='kc-login')

#Локатор Неверный логин или пароль
    LOCATOR_wrong_login_or_password = WebElement(xpath='//*[@id="page-right"]/div/div/p')

#Локатор Капча
    LOCATOR_captcha = WebElement(id='captcha')

# Локатор Зарегестрироваться
    LOCATOR_kc_register = WebElement(id='kc-register')

# Локатор Имя
    LOCATOR_firstName = WebElement(name='firstName')

# Локатор Фамилия
    LOCATOR_lastName = WebElement(name='lastName')

# Локатор E-mail
    LOCATOR_address = WebElement(id='address')

# Локатор Пароль
    LOCATOR_password = WebElement(id='password')

# Локатор Показать Пароль
    LOCATOR_show_password = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/div/div[2]')

# Локатор Подтверждение пароля
    LOCATOR_password_confirm = WebElement(id='password-confirm')

# Локатор Показать Подтверждение пароля
    LOCATOR_show_password_confirm = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/div/div[2]')

# Локатор Подтверждение пароля
    LOCATOR_register = WebElement(name='register')

# Локатор Длина пароля должна быть не менее 8 символов
    LOCATOR_error_number_of_characters = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span')

# Локатор Учётная запись уже существует
    LOCATOR_error_number_of_characters = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[1]/div/div/h2')



# Надпись Личный кабинет
    LOCATOR_SALE_LINC = WebElement(xpath='//*[@id="page-left"]/div/div[2]/h2')

# Лого Ростелеком
    LOCATOR_LOGO_ROSTELECOM = WebElement(xpath='//*[@id="app-header"]/div/div/svg')

# Пользовательское соглашение
    LOCATOR_account_exist = WebElement(xpath='//*[@id="rt-footer-agreement-link"]/span[2]')



