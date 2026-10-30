import uuid
from dataclasses import dataclass
from decimal import Decimal
from enum import StrEnum

from tutoring.core.models import Person


class Stage(StrEnum):
    PRIMARY = "primary"
    SECONDARY = "secondary"  # ESO
    BACCALAUREATE = "baccalaureate"  # Bach
    VOCATIONAL = "vocational"  # FP
    UNIVERSITY = "university"
    OTHER = "other"


MAX_YEAR_BY_STAGE = {
    Stage.PRIMARY: 6,
    Stage.SECONDARY: 4,
    Stage.BACCALAUREATE: 2,
    Stage.VOCATIONAL: 2,
    Stage.UNIVERSITY: 6,
}


@dataclass(frozen=True)
class SchoolLevel:
    stage: Stage
    year: int

    def __post_init__(self) -> None:
        max_year = MAX_YEAR_BY_STAGE.get(self.stage)
        if max_year is None:  # OTHER: sin cursos que validar
            return
        if not 1 <= self.year <= max_year:
            raise ValueError(f"{self.stage} has years 1-{max_year}, got {self.year}")


class Student(Person):
    def __init__(
        self,
        name: str,
        surname: str,
        school_level: SchoolLevel,
        default_price: Decimal,
        identifier: uuid.UUID | None = None,
    ) -> None:
        super().__init__(name, surname, identifier)
        self.school_level = school_level
        self.default_price = default_price
