import pandas as pd

FILE_ID = "1odXw81javPy4RwmYhj4IZts80g-3rMOv"

file_url = f"https://drive.google.com/uc?id={FILE_ID}"

# Читаем CSV
raw_data = pd.read_csv(file_url)

# Приведение типов
raw_data["Year"] = raw_data["Year"].astype(int)
raw_data["Country"] = raw_data["Country"].astype(str)
raw_data["Feedstock_Yield"] = raw_data["Feedstock_Yield"].astype(float)
raw_data["Production_Capacity"] = raw_data["Production_Capacity"].astype(float)
raw_data["Processing_Tech_Efficiency"] = raw_data["Processing_Tech_Efficiency"].astype(float)
raw_data["Energy_Consumption"] = raw_data["Energy_Consumption"].astype(float)
raw_data["Feedstock_Cost"] = raw_data["Feedstock_Cost"].astype(float)
raw_data["Transportation_Cost"] = raw_data["Transportation_Cost"].astype(float)
raw_data["Distribution_Cost"] = raw_data["Distribution_Cost"].astype(float)
raw_data["Carbon_Emissions"] = raw_data["Carbon_Emissions"].astype(float)
raw_data["Water_Usage"] = raw_data["Water_Usage"].astype(float)
raw_data["Market_Demand"] = raw_data["Market_Demand"].astype(int)
raw_data["Price_Per_Gallon"] = raw_data["Price_Per_Gallon"].astype(float)
raw_data["Govt_Incentive"] = raw_data["Govt_Incentive"].astype(float)
raw_data["Bioethanol_Growth"] = raw_data["Bioethanol_Growth"].astype(float)

# Вывод первых 10 строк
print(raw_data.head(10))

# Выводим типы всех колонок
print("\nТипы колонок после приведения:")
print(raw_data.dtypes)

# Сохраняем DataFrame в Parquet
raw_data.to_parquet("clean_data.parquet", index=False)