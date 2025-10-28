import pandas as pd
import numpy as np


def validate_df(df):
    """
    Проверка DataFrame:
    - пропуски
    - обязательные колонки
    - типы колонок
    """
    # Проверка пропусков
    if df.isna().sum().sum() == 0:
        print("Пропусков нет.")
    else:
        print(f"Обнаружено {df.isna().sum().sum()} пропусков!")

    # Проверка обязательных колонок
    required_cols = [
        "Year",
        "Country",
        "Feedstock_Yield",
        "Production_Capacity",
        "Processing_Tech_Efficiency",
        "Energy_Consumption",
        "Feedstock_Cost",
        "Transportation_Cost",
        "Distribution_Cost",
        "Carbon_Emissions",
        "Water_Usage",
        "Market_Demand",
        "Price_Per_Gallon",
        "Govt_Incentive",
        "Bioethanol_Growth",
        "Cost_per_Unit",
    ]
    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Отсутствуют обязательные колонки: {missing_cols}")

    # Проверка типов колонок
    expected_types = {
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
        "Cost_per_Unit": float,
    }

    for col, expected_type in expected_types.items():
        if not pd.api.types.is_dtype_equal(df[col].dtype, expected_type):
            print(
                f"Внимание: колонка '{col}' имеет тип {df[col].dtype}, ожидается {expected_type}."
            )

    print("Валидация завершена успешно.")
    return True
