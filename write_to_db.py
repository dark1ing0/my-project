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

# Приведение типов
df["Year"] = df["Year"].astype(int)
df["Country"] = df["Country"].astype(str)
df["Feedstock_Yield"] = df["Feedstock_Yield"].astype(float)
df["Production_Capacity"] = df["Production_Capacity"].astype(float)
df["Processing_Tech_Efficiency"] = df["Processing_Tech_Efficiency"].astype(float)
df["Energy_Consumption"] = df["Energy_Consumption"].astype(float)
df["Feedstock_Cost"] = df["Feedstock_Cost"].astype(float)
df["Transportation_Cost"] = df["Transportation_Cost"].astype(float)
df["Distribution_Cost"] = df["Distribution_Cost"].astype(float)
df["Carbon_Emissions"] = df["Carbon_Emissions"].astype(float)
df["Water_Usage"] = df["Water_Usage"].astype(float)
df["Market_Demand"] = df["Market_Demand"].astype(int)
df["Price_Per_Gallon"] = df["Price_Per_Gallon"].astype(float)
df["Govt_Incentive"] = df["Govt_Incentive"].astype(float)
df["Bioethanol_Growth"] = df["Bioethanol_Growth"].astype(float)

# Вывод
print("\nТипы данных перед записью:")
print(df.dtypes)

# Создание SQLAlchemy движка
engine = create_engine(
    f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}"
)

# Запись таблицы в PostgreSQL
df.to_sql(table_name, con=engine, schema="public", if_exists="replace", index=False)
print(f"Данные записаны в таблицу '{table_name}' базы '{dbname}'")
