import argparse
import os
from etl.extract import load_csv, save_raw
from etl.transform import transform_types
from etl.load import load_to_db, save_parquet
from etl.validate import validate_df


def main():
    parser = argparse.ArgumentParser(description="ETL pipeline for Bioethanol dataset")
    parser.add_argument(
        "--source", required=True, help="URL или путь к исходному CSV файлу"
    )
    parser.add_argument(
        "--table", default="revyakina", help="Имя таблицы для PostgreSQL"
    )
    args = parser.parse_args()

    # Загрузка и сохранение raw данных
    df = load_csv(args.source)
    save_raw(df)

    # Трансформации
    df = transform_types(df)

    # Сохранение parquet
    save_parquet(df)

    # Валидация (опционально)
    validate_df(df)

    # Подключение к БД через переменные окружения
    user = os.environ.get("DB_USER")
    password = os.environ.get("DB_PASSWORD")
    host = os.environ.get("DB_HOST")
    port = os.environ.get("DB_PORT")
    dbname = os.environ.get("DB_NAME", "homeworks")  # default

    if not all([user, password, host, port, dbname]):
        raise ValueError("Не заданы все переменные окружения для подключения к БД!")

    db_url = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}"

    # Загрузка первых 100 строк в БД
    load_to_db(df, args.table, db_url)


if __name__ == "__main__":
    main()
