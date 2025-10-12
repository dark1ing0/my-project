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
