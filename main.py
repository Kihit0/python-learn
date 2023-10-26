class Project:
    _name: str
    _id: int

    def __init__(self, name, id) -> None:
        self._name = name
        self._id = id

    def __repr__(self) -> str:
        return f"id: {self._id} \n name: {self._name}"


p: Project = Project("Kihito", 1)
