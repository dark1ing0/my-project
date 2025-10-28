def transform_types(df):
    """
    Приводим типы колонок к нужным:
    - Year → int
    - Feedstock_Yield → float
    - Bioethanol_Growth → float
    итп
    """
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

    print("Типы колонок успешно приведены.")

    # Новая колонка
    df["Cost_per_Unit"] = df["Feedstock_Cost"] / df["Production_Capacity"]
    df["Cost_per_Unit"] = df["Cost_per_Unit"].astype(float)

    # Проверка пропусков
    missing = df.isna().sum().sum()
    if missing == 0:
        print("Пропусков нет.")
    else:
        print(f"Обнаружено {missing} пропусков. Рассмотрите заполнение или удаление.")

    print("Трансформации выполнены: типы приведены, новая колонка добавлена.")
    return df
