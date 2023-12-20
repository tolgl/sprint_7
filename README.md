# Автотесты API для сервиса [Яндекс Самокат](https://qa-scooter.praktikum-services.ru/)
*В проекте использовалась библиотека Requests и фреймворки Pytest, Allure*


1. Файл tests/conftest.py содержит фикстуры добавления/удаления курьера, генерации логина, пароля, имени курьера и фикстура создания заказа
1. Файл tests/test_creating_courier.py содержит автотесты добавления курьера:
   - __test_successful_creating_courier__ - проверяет успешное добавление курьера
   - __test_creating_courier_without_login__ - проверяет добавление курьера без логина
   - __test_creating_courier_without_password__ - проверяет добавление курьера без пароля
   - __test_creating_courier_with_same_login__ - проверяет добавление курьера с уже добавленным логином
1. Файл tests/test_login_courier.py содержит автотесты авторизации:
   - __test_successful_login_courier__ - проверяет успешную авторизацию курьера
   - __test_login_courier_without_password__ - проверяет авторизацию курьера без пароля
   - __test_login_courier_without_login__ - проверяет авторизацию курьера без логина
   - __test_login_courier_non_existent_login__ - проверяет авторизацию курьера с несуществующим логином
   - __test_login_courier_non_existent_password__ - проверяет авторизацию курьера с несуществующим паролем
1. Файл tests/test_creating_order.py содержит автотесты создания заказа:
   - __test_status_code_creating_order__ - проверяет статус код при успешном создании заказа
   - __test_response_creating_order__ - проверяет текст ответа при успешном создании заказа
1. Файл tests/test_delete_courier.py содержит автотесты удаления курьера:
   - __test_successful_delete_courier__ - проверяет текст ответа успешного удаления курьера
   - __test_delete_courier_without_id__ - проверяет удаление курьера без указания id
   - __test_delete_courier_non_existent_id__ - проверяет удаление курьера с несуществующим id
1. Файл tests/test_get_order.py содержит автотесты получения заказа:
   - __test_get_list_order_without_courier__ - проверяет что в теле ответа содержатся заказы
   - __test_get_order_by_track__ - проверяет получение заказа по номеру заказа
   - __test_get_order_without_track__ - проверяет получение заказа без номера заказа
   - __test_get_order_non_existent_track__ - проверяет получение заказа с несуществующим номером заказа
1. Файл tests/test_accept_order.py содержит автотесты создания заказа:
   - __test_successful_accept_order__ - проверяет успешное оформление заказа
   - __test_accept_order_without_id_courier__ - проверяет принятие заказа без указания id курьера
   - __test_accept_order_without_id_order__ - проверяет принятие заказа без указания id заказа
   - __test_accept_order_non_existent_id_courier__ - проверяет принятие заказа с несуществующим id курьера
   - __test_accept_order_non_existent_id_order__ - проверяет принятие заказа с несуществующим id заказа
1. Файл config.py содержит базовые переменные
1. Файл requirements.txt содержит используемые зависимости в проекте