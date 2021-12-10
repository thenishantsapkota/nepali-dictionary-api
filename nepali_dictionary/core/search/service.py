import typing as ty

from nepali_dictionary.common.db import Dictionary
from sqlmodel import Session, select


class SearchService:

    def search(self, query: str, session: ty.Type[Session], engine) -> ty.Optional[dict]:
        with session(engine) as s:
            statement = select(Dictionary).where(Dictionary.word == query)
            result: ty.Any = s.execute(statement).fetchone()

            if result:
                return result[0].dict()
