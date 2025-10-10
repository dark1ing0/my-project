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

try:
    response = requests.get(url, params=params, timeout=10)  # Отправка GET-запроса
    response.raise_for_status()  # проверка успешности запроса
except requests.RequestException as e:
    print("Ошибка запроса:", e)
    raise SystemExit(1)

# Получаем данные
data = response.json()
products = data.get("products", [])

if not products:
    print("Продукты не найдены. Проверьте API и параметры запроса.")
    raise SystemExit(1)

# Загружаем список словарей в DataFrame
df = pd.DataFrame(products)  # превратили в таблицу

# Выбираем колонки
cols_to_show = ["product_name", "brands", "categories", "nutriments"]
df_subset = df[cols_to_show]

# Приведение типов (все текстовые колонки в str, nutriments оставляем как объект)
for col in ["product_name", "brands", "categories"]:
    df_subset.loc[:, col] = df_subset[col].astype(str)

# Выводим на экран
print("Первые 10 строк выбранных данных:")
print(df_subset.head(10))
print("\nТипы колонок:")
print(df_subset.dtypes)

print(f"\nВсего записей: {len(df_subset)}")

# Сохраняем в Parquet
df_subset.to_parquet("open_food_facts.parquet", index=False)
