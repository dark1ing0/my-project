import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

URL = "https://ru.citaty.net/"  # URL

try:
    response = requests.get(
        URL, headers={"User-Agent": "Mozilla/5.0"}, timeout=10, allow_redirects=True
    )

    # Проверяем доступность сайта
    if response.status_code != 200:
        print(f"Ошибка: сайт недоступен ({response.status_code})")
        exit()
    response.raise_for_status()
except requests.RequestException as e:
    print("Ошибка при запросе:", e)
    raise SystemExit(1)

soup = BeautifulSoup(
    response.text, "html.parser"
)  # Создаём объект BeautifulSoup для разбора HTML

# Сбор данных с защитой от дублей
seen = set()  # здесь будем хранить уникальные ключи (quote, author)
products = []

for item in soup.find_all("div", class_="blockquote"):
    quote_elem = item.find("p", class_="blockquote-text")
    quote = (
        quote_elem.get_text(strip=True).replace("\xa0", " ") if quote_elem else "N/A"
    )
    author_elem = item.find("a", class_="link")
    author = author_elem.get_text(strip=True) if author_elem else "N/A"
    if quote != "N/A" and len(quote) > 10:
        products.append({"quote": quote, "author": author})

        # Приведение типов
        products.append({"quote": str(quote), "author": str(author)})

        # Проверяем, что данные найдены
if not products:
    print("Цитаты не найдены. Проверьте структуру сайта.")
    exit()

    # Преобразуем список словарей в DataFrame
df = pd.DataFrame(products)

# (опционально) на всякий случай можно ещё раз удалить дубликаты в DataFrame
df = df.drop_duplicates(subset=["quote", "author"]).reset_index(drop=True)

# Выводим результат
# Настройки pandas для полного отображения цитат
pd.set_option("display.max_colwidth", None)
# Красивый вывод первых 10 цитат
print("Парсинг завершён успешно!")
print(f"Найдено {len(df)} цитат.\n")
print("Первые 10 цитат:\n")
for i, row in df.head(10).iterrows():
    print(f"{i+1}. {row['quote']} — {row['author']}\n")

print("Типы колонок:")
print(df.dtypes)

# Сохраняем в Parquet
df.to_parquet("quotes.parquet", index=False)
