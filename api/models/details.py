from typing import Optional

from sqlmodel import SQLModel, Field, Column, Enum

from api.enums import Categories


class Info(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    value: str = Field()
    category: Categories = Field(sa_column=Column(Enum(Categories)))
