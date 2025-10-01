import pandas as pd  # чтобы хранить данные в таблице
import requests  # для отправки запросов к API

# URL Open Food Facts API Example
url = "https://world.openfoodfacts.org/cgi/search.pl"

# Параметры запроса
params = {
    "search_simple": 1,  # простой поиск
    "action": "process",
    "json": 1,  # хотим JSON
    "page_size": 10,  # количество продуктов
}

# Отправка GET-запроса
response = requests.get(url, params=params)

# Проверяем успешность запроса
if response.status_code == 200:
    data = response.json()  # Получаем JSON
    products = data.get("products", [])  # список продуктов

    # Загружаем список словарей в DataFrame
    df = pd.DataFrame(products)  # превратили в таблицу

    # Выбираем колонки
    cols_to_show = ["product_name", "brands", "categories", "nutriments"]
    df_subset = df[cols_to_show]

    # Показываем первые 10 строк
    print("Первые 10 строк выбранных данных:")
    print(df_subset.head(10))  # показали первые 10 строк

    # Типы колонок
    print("\nТипы колонок:")
    print(df_subset.dtypes)
else:
    print("Ошибка запроса:", response.status_code)
