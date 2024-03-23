import os

from sqlmodel import Session, select

from api.db import engine
from api.models import Info


def get_default_fields():
    return dict(
        name=os.getenv('name'),
        email=os.getenv('email'),
        phone_number=os.getenv('phone_number'),
        birth_date=os.getenv('birth_date'),
        description=os.getenv('description'),
    )


def get_personal_data():
    default_fields = get_default_fields()

    query = select(Info)
    with Session(engine) as session:
        results = session.exec(query)

    print(list(results))
    hobbies = []
    interests = []
    languages = []
    programming_languages = []

    data = dict(
        **default_fields,
        hobbies=hobbies,
        interests=interests,
        languages=languages,
        programming_languages=programming_languages,
    )

    return data
