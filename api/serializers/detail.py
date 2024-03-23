from pydantic import BaseModel
from typing import List


class DetailResponse(BaseModel):
    name: str
    email: str
    birth_date: str
    phone_number: str
    description: str
    interests: List[str]
    hobbies: List[str]
    languages: List[str]
    programming_languages: List[str]
