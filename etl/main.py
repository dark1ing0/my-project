import argparse
import sqlite3
from etl.extract import load_csv, save_raw
from etl.transform import transform_types
from etl.load import load_to_db, save_parquet
from etl.validate import validate_df


def get_db_url():
    """
    Считывает учетные данные из creds.db и возвращает URL для SQLAlchemy.
    """
    conn = sqlite3.connect("creds.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM access")
    host, port, user, password = cursor.fetchone()
    conn.close()

    dbname = "homeworks"
    db_url = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}"
    return db_url


def main():
    parser = argparse.ArgumentParser(description="ETL pipeline for Bioethanol dataset")
    parser.add_argument(
        "--source", required=True, help="URL или путь к исходному CSV файлу"
    )
    parser.add_argument(
        "--table",
        default="revyakina",
        help="Название таблицы для записи в PostgreSQL",
    )
    parser.add_argument(
        "--parquet",
        default="data/processed/processed_data.parquet",
        help="Путь для сохранения parquet файла",
    )
    parser.add_argument(
        "--validate", action="store_true", help="Включить валидацию данных"
    )

    args = parser.parse_args()

    # Загрузка и сохранение raw данных
    df = load_csv(args.source)
    save_raw(df)

    # Трансформации
    df = transform_types(df)

    # Валидация (если указан флаг)
    if args.validate:
        validate_df(df)

    # Сохранение parquet
    save_parquet(df, args.parquet)

    # Запись в базу PostgreSQL
    db_url = get_db_url()
    load_to_db(df, table_name=args.table, db_url=db_url)

    print("ETL pipeline выполнен успешно!")


if __name__ == "__main__":
    main()
