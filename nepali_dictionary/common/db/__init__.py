from sqlmodel import create_engine, SQLModel

from nepali_dictionary.common.db.Dictionary import Dictionary


engine = create_engine(
    'postgresql://root:root@db:5432/db', echo=True)


def migrate():
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    migrate()

__all__ = ["Dictionary"]
