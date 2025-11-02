def transform_types(df):
    """
    Приведение типов колонок и добавление новой колонки Cost_per_Unit.
    """
    # Словарь колонок и типов
    types_dict = {
        "Year": int,
        "Country": str,
        "Feedstock_Yield": float,
        "Production_Capacity": float,
        "Processing_Tech_Efficiency": float,
        "Energy_Consumption": float,
        "Feedstock_Cost": float,
        "Transportation_Cost": float,
        "Distribution_Cost": float,
        "Carbon_Emissions": float,
        "Water_Usage": float,
        "Market_Demand": int,
        "Price_Per_Gallon": float,
        "Govt_Incentive": float,
        "Bioethanol_Growth": float,
    }

    # Преобразуем типы
    df = df.astype(types_dict)

    # Новая колонка
    df["Cost_per_Unit"] = df["Feedstock_Cost"] / df["Production_Capacity"]

    # Проверка пропусков
    missing = df.isna().sum().sum()
    if missing == 0:
        print("Пропусков нет.")
    else:
        print(f"Обнаружено {missing} пропусков. Рассмотрите заполнение или удаление.")

    print("Трансформации выполнены: типы приведены, новая колонка добавлена.")
    return df
