# my-project
Ссылка на датасет Bio Ethanol Production Dataset: https://drive.google.com/file/d/1odXw81javPy4RwmYhj4IZts80g-3rMOv/view?usp=sharing

---

## 1️⃣ Создание виртуального окружения
В папке с проектом создала виртуальное окружение:
powershell
`python -m venv venv`
Активировала окружение в PowerShell:
`.\venv\Scripts\Activate.ps1`
Установила необходимые библиотеки:
`pip install pandas`
Когда библиотеки были установлены, я зафиксировала их в файл requirements.txt. Это позволяет в будущем быстро установить такие же пакеты, если проект переносится на другой компьютер:
`pip freeze > requirements.txt`
Если другой человек захочет повторить мою работу, ему достаточно активировать окружение и установить все зависимости командой:
`pip install -r requirements.txt`

## 2️⃣ Загрузка датасета
Создала файл data_loader.py и вставила туда код:
`import pandas as pd`

`FILE_ID = "1odXw81javPy4RwmYhj4IZts80g-3rMOv"` # Google Drive file id

`file_url = f"https://drive.google.com/uc?id={FILE_ID}"`

`raw_data = pd.read_csv(file_url)` # Читаем CSV

Скрипт `data_loader.py` читает датасет и выводит первые 10 строк.
Результат работы скрипта:
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/821898de-e93b-49c8-86bd-a0b1efc4c3b7" />

## 3️⃣ Приведение типов колонок
В моем датасет 3 вида типа данных:
Тип данных | Примеры | Применение
--- | --- | ---
int | 2023, 5, -12 | Целые числа: сортировка, арифметика, подсчёт сумм
float | 3.14, 0.5, -12.7 | Дробные числа: усреднение, вычисления, графики
str | "USA", "Hello", "123" | Текст: фильтрация, группировка, поиск, замена

`print("\nТипы колонок после приведения:")`

`print(raw_data.dtypes)`

Пример приведения типов:
`raw_data["Year"] = raw_data["Year"].astype(int)`

Приведение типов должно выполняться после того, как данные уже загружены в raw_data. Если писать до `raw_data = pd.read_csv(...)`, переменной ещё нет, и Python выдаст ошибку. Получается: Загружаем данные из CSV (`raw_data = pd.read_csv(file_url)`) → Приводим колонки к нужным типам → Выводим проверку (`print(raw_data.head(10))`)

Результат работы скрипта:
<img width="1919" height="1074" alt="hw3" src="https://github.com/user-attachments/assets/5728ade9-6ee6-4ca0-9731-5ff6cfb57742" />

Далее создание clean_data.parquet: `raw_data.to_parquet("clean_data.parquet", index=False)` 

Далее надо установить дополнительную библиотеку: `pip install pyarrow`

После установки и запуска скрипта появился файл. В нём лежат все строки DataFrame с правильными типами.


## 4️⃣ Работа с API
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
<img width="1917" height="1016" alt="image" src="https://github.com/user-attachments/assets/1f76be71-9c08-4163-8c89-f41413643df4" />


## 5️⃣ Парсер цитат с сайта citaty.net

В этом примере я использую Python для парсинга сайта с цитатами и вывожу их в удобном виде.

Описание

Скрипт `data_parser.py` делает следующее:
1. Отправляет GET-запрос к сайту citaty.net.
2. Использует BeautifulSoup для разбора HTML страницы.
3. Извлекает блоки с цитатами и авторами.
4. Сохраняет цитаты в список словарей с ключами quote и author.
5. Выводит первые 10 цитат и общее количество найденных цитат.

# Установка зависимостей
Установите необходимые библиотеки: `python -m pip install requests beautifulsoup4` → Запуск скрипта

# Особенности кода
1. Добавлен заголовок User-Agent в requests.get, чтобы сайт разрешил запрос.
2. Используется проверка if quote != "N/A" and len(quote) > 10, чтобы исключить пустые или слишком короткие цитаты.
3. Прописана `replace("\xa0", " ")` так как неразрывный пробел ухудшает читабельность текста.
4. Цитаты и авторы сохраняются в список словарей для удобной работы и возможного дальнейшего экспорта в CSV/JSON.
5. Скрипт выводит первые 10 элементов для наглядности, но можно легко вывести все или сохранить в файл.

Результат работ скрипта:
<img width="1913" height="1015" alt="image" src="https://github.com/user-attachments/assets/eb6db3fc-fa51-4a6a-bc52-689ffc1a16f6" />

