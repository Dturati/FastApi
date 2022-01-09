from repository.people import PeopleRepository
from sqlalchemy.orm import Session
from models.People import PeopleModel
from fastapi import Depends
from dependency_injector.wiring import inject, Provide

@inject
class PeopleService:
    def __init__(self,
        people_repository: PeopleRepository,
        db: Session
    ) -> None:
        self._repository: PeopleRepository = people_repository
        self._db = db
    async def save(self, data: dict) -> dict:
        try:
            people = PeopleModel(name=data['name'], year=data['year'])
            self._db.add(people)
            self._db.commit()
            self._repository.save(data)
        except Exception as err:
            raise Exception('Erro ao salvar')
        return data