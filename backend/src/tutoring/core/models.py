import uuid


class Person:
    def __init__(
        self, name: str, surname: str, identifier: uuid.UUID | None = None
    ) -> None:
        self.name = name
        self.surname = surname
        self.id = self._generate_id() if identifier is None else identifier

    @property
    def full_name(self) -> str:
        return f"{self.name} {self.surname}"

    @staticmethod
    def _generate_id() -> uuid.UUID:
        return uuid.uuid7()
