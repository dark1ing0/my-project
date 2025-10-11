## Работа с API
API Open Food Facts API Example - https://publicapis.io/open-food-facts-api

Сначала надо активировать виртуальное окружение. 
Далее установить необходимые библиотеки: `pip install pandas requests`
# Создание скрипта api_reader.py
В скрипте я:
1. Отправляю GET-запрос к Open Food Facts API.
2. Получаю JSON с данными о продуктах.
3. Преобразую JSON в Pandas DataFrame.
4. Выбираю только **4 колонки для наглядности**: `product_name`, `brands`, `categories`, `nutriments`.
5. Вывожу **первые 10 строк** данных для проверки.
6. Вывожу типы колонок выбранных данных.

Результат:

После запуска скрипта появился DataFrame с 10 продуктами и 4 колонками:

```
 product_name                                brands                                         categories                                         nutriments
0                Sidi Ali                              Sidi Ali  Beverages and beverages preparations,Beverages...  {'carbohydrates': 42, 'carbohydrates_100g': '4...
1                   Perly                                Jaouda  Dairies,Fermented foods,Fermented milk product...  {'calcium': '0.25', 'calcium_100g': '0.25', 'c...
```

Типы данных колонок:

`product_name`, `brands`, `categories` — текстовые (object)

`nutriments` — объект (object), внутри словарь с числовыми данными о питательной ценности

Результат работы скрипта:
<img width="1915" height="1017" alt="image" src="https://github.com/user-attachments/assets/6b43b669-eed0-497d-a34b-b6ca9d25197b" />
