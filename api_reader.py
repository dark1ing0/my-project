import pandas as pd  # чтобы хранить данные в таблице
import requests  # для отправки запросов к API
import os  # чтобы работать с путями

pd.set_option("display.max_columns", None)  # показывать все колонки
pd.set_option("display.max_colwidth", 40)  # показывать весь текст в колонках
pd.set_option("display.width", 200)  # ширина окна вывода

# URL Open Food Facts API Example
url = "https://world.openfoodfacts.org/cgi/search.pl"

# Параметры запроса
params = {
    "search_simple": 1,  # простой поиск
    "action": "process",
    "json": 1,  # хотим JSON
    "page_size": 10,  # количество продуктов
}

# Определяем путь к директории, где лежит сам скрипт
current_dir = os.path.dirname(os.path.abspath(__file__))

# Путь к папке api_example (от корня проекта)
api_dir = os.path.join(current_dir, "api_example")

# Путь к parquet-файлу в этой же директории
parquet_path = os.path.join(current_dir, "open_food_facts.parquet")

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
df_subset.to_parquet(parquet_path, index=False)
print(f"Данные сохранены в: {parquet_path}\n")
