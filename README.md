Тесты для проекта https://qa-scooter.praktikum-services.ru/
Структура
 - allure_results/ - Директория с отчетами о тестировании. Команда для просмотра отчета ```allure serve allure_results```, для формирования отчета ```pytest tests --alluredir=allure_results```

 - locators/ - Директория с локаторами
 - pages/ - Директория с методами
    - base_page
    - main_page
    - order_page
 -tests/ - Директория с тестами
 - conftest - Модуль фикстур проекта.
 - data - Модуль с данными
 - requirements - Модуль с внешними зависимостями для установки ```pip install -r requirements.txt```
