from sqlmodel import Field, SQLModel 


class Dictionary(SQLModel, table=True):
    word: str = Field(primary_key=True)
    kind: str
    meaning: str
