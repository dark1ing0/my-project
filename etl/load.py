from sqlalchemy import create_engine
import os


def load_to_db(df, table_name, db_url):
    """
    Сохраняем первые 100 строк DataFrame в базу PostgreSQL.
    df: DataFrame с данными
    table_name: имя таблицы в PostgreSQL
    db_url: URL для подключения через SQLAlchemy
    """
    engine = create_engine(db_url)
    df.head(100).to_sql(table_name, con=engine, if_exists="replace", index=False)
    print(f"Первые 100 строк записаны в таблицу '{table_name}'.")


def save_parquet(df, filename="data/processed/processed_data.parquet"):

    # Сохраняем весь DataFrame в parquet.
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    df.to_parquet(filename, index=False)
    print(f"Данные сохранены в {filename}.")
