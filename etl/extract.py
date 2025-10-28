import pandas as pd
import os

FILE_ID = "1odXw81javPy4RwmYhj4IZts80g-3rMOv"
file_url = f"https://drive.google.com/uc?id={FILE_ID}"


def load_csv(file_url):
    """
    Загружает CSV файл из URL или локального пути и проверяет, что он не пустой.
    file_url: URL или локальный путь к CSV
    return: pandas DataFrame
    """
    df = pd.read_csv(file_url)

    if df.empty:
        raise ValueError("Файл пустой!")

    print(f"Файл успешно загружен. Строк: {len(df)}")
    return df


def save_raw(
    df, bioethanol_growth_prediction="data/raw/bioethanol_growth_prediction.csv"
):
    """
    Сохраняет DataFrame в CSV в папку data/raw
    """
    os.makedirs(
        os.path.dirname(bioethanol_growth_prediction), exist_ok=True
    )  # создаём папку, если нет
    df.to_csv(bioethanol_growth_prediction, index=False)
    print(f"Данные сохранены в {bioethanol_growth_prediction}")
