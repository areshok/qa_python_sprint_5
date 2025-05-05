# Для ревьюера
---
На браузере Chrome не работает один тест `tests/test_registration.py/test_correct_registation_user`

Не работает функция field.clear() поле не очищается, причина не найдена, в учебном чате от наставника было только предложение field.send_keys(Keys.CONTROL, 'a') field.send_keys(Keys.DELETE)

которое тоже не работает, для браузера chrome нашел рабочий вариант с Keys.BACKSPACE, но это не панацея а какой то бред, причины почему поле не очищается ни field.clear() ни через control + a + delete непонятны, если есть идеи почему не работает и как сделать чтоб field.clear() работал напишите
к примеру

```
field.send_keys('test')
text_count = len(field.get_attribute('value'))
for _ in range(text_count):
	field.send_keys(Keys.BACKSPACE)
```
мне не нравиться этот способ, то как это выглядит и работает

в книге python разработка на основе tdd 2018 год, писалось что для selenium лучше явные ожидания чем неявные которые есть у selenium поэтому использовал time.sleep(1)

также на chrome не проходит тест `tests/test_transition_auth_user.py/test_1_transition_to_personal_account`

выходят когда получаешь url, и сравниваешь с фактом, почему то происходит не соответсвие, хотя firefox получает правильный url, и проблем с тестом нет
```
ite/account/profile
ite/account
```
Сделал в тесте не == , а in


# Тесты
В папке `tests` находятся фалы с тестами:
- `test_constructor.py`
- `test_registration.py`
- `test_transition_auth_user.py`
- `test_transition_log_in.py`

Список тестов
- test_constructor_selection
- test_correct_registation_user
- test_uncorrect_password_5_symbol_registration_user
- test_1_transition_to_personal_account
- test_2_transition_personal_account_to_constructor_button
- test_3_transition_personal_account_to_logo_button
- test_4_transition_personal_account_main_url
- test_5_exit_in_account
- test_redirect_log_in_on_home_page
- test_redirect_log_in_button_personal_account
- test_redirect_log_in_button_registration_form
- test_redirect_log_in_on_buttom_password_fogot
