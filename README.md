## Тестирование интерфейса, для  https://b2c.passport.rt.ru 
#### Данный финальный проект создан в рамках учебного процесса.


#### 1 Правая часть блока аторизации видна на странице
#### 2 Левая часть блока аторизации видна на странице
#### 3 Переход по кнопке 'Забыл пароль' переводит на страницу 'Восстановление пароля'
#### 4 Переход по иконке 'OK' ведет на соответствующую страницу
#### 5 Переход по иконке 'VK' ведет на соответствующую страницу
#### 6 Переход по иконке 'mail' ведет на соответствующую страницу
#### 7 Переход по иконке 'google' ведет на соответствующую страницу
#### 8 Переход по иконке 'ya' ведет на соответствующую страницу
#### 9 Нажатие на "Отправить" во вкладке "Поддержка"
#### 10 Наведение на вкладку 'Чат', клик по иконке телеграмм и проверка перехода на соответствующую страницу
#### 11 Наведение на вкладку 'Чат', клик по иконке viber и проверка перехода на соответствующую страницу
#### 12 Кликабельность кнопки 88001000800
#### 13 Кликабельность кнопки checkbox (снятие галочки с контейнера 'Запомнить меня')
#### 14 Введение невалидного логина и пароля (кириллицей)
#### 15 Регистрация нового пользователя с введением невалидного повторного пароля)
#### 16 пПовторная регистрация ранее созданного пользователя


Команда для запуска тестов python -m pytest -v --driver chrome --driver-path chromedriver.exe tests/test_rostelecom.py