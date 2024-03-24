import os

from sqlmodel import Session, select

from api.db import engine
from api.models import Info
from api.enums import Categories


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
    initial_dict = {e.name: [] for e in list(Categories)}

    with Session(engine) as session:
        query = select(Info.category, Info.value)
        results = session.exec(query)

        for info in results:
            initial_dict[Categories(info.category).name].append(info.value)

    data = dict(
        **default_fields,
        hobbies=initial_dict[Categories.HOBBY.name],
        interests=initial_dict[Categories.INTEREST.name],
        languages=initial_dict[Categories.LANGUAGE.name],
        programming_languages=initial_dict[Categories.PROGRAMMING_LANGUAGE.name],
    )

    return data
