import pandas as pd
import sqlite3
from sqlalchemy import create_engine

# Подключение к локальной БД
conn = sqlite3.connect("creds.db")
cursor = conn.cursor()

# Просмотр
cursor.execute("SELECT * FROM access")
host, port, user, password = cursor.fetchone()
conn.close()

dbname = "homeworks"  # имя базы
table_name = "revyakina"  # фамилия на латинице в нижнем регистре

FILE_ID = "1odXw81javPy4RwmYhj4IZts80g-3rMOv"
file_url = f"https://drive.google.com/uc?id={FILE_ID}"
df = pd.read_csv(file_url)
df = df.head(100)

# Создание SQLAlchemy движка
engine = create_engine(
    f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}"
)

# Запись таблицы в PostgreSQL
df.to_sql(table_name, con=engine, schema="public", if_exists="replace", index=False)
print(f"Данные записаны в таблицу '{table_name}' базы '{dbname}'")
