class Logic:
    _data: list[str] = list()
    _path: str = ""

    def __init__(self, path: str) -> None:
        self._path = path
        phones = open(self._path, "r", encoding="utf8")
        self._data = list(phones)

    def printEntity(self, data: list[str] | None = None) -> None:
        if data != None:
            print(*data, sep="")
        elif len(self._data) == 0:
            print("Phones book is empty")
        else:
            print(*self._data, sep="")

    def searchEntity(self, payload: str) -> list[str]:
        if len(payload) == 1:
            while len(payload) <= 1:
                print("Слишком короткая строка для поиска")
                payload = input()

        searchPhones: list[str] = list()

        for item in self._data:
            if payload.lower() in item.lower():
                searchPhones.append(item)

        if len(searchPhones) == 0:
            print("Phones not found")
        else:
            self.printEntity(searchPhones)

        return searchPhones

    def writeEntity(self, payload: str | list[str]) -> None:
        fileWrite = open(self._path, "w", encoding="utf8")

        if len(self._data) == 0 and isinstance(payload, str):
            fileWrite.write(payload)
        elif isinstance(payload, list):
            fileWrite.write("".join(payload).strip())
        else:
            self._data.append(f"\n{payload}")
            fileWrite.write("".join(self._data))

        fileWrite.close()
        fileRead = open(self._path, "r", encoding="utf8")
        self._data = list(fileRead)
        fileRead.close()

    def _choiceEntity(self, payload: list[str]) -> str:
        if len(payload) == 0:
            print("Ничего не найдено. Введите новые значения")
            phones: list[str] = payload

            while len(phones) > 0:
                search: str = input()
                phones: list[str] = self.searchEntity(search)

            payload = phones

        print("Выберите из найденых")
        for index in range(0, len(payload)):
            print(f"{index} : {payload[index]}", end="")

        indexPayload: int = int(input())

        if 0 < indexPayload < len(payload):
            while 0 > indexPayload > len(payload):
                print("Такого индекса нет")
                indexPayload: int = int(input())

        return payload[indexPayload]

    def updateEntity(self, payload: list[str], update: str) -> None:
        choice: str = self._choiceEntity(payload)

        for item in self._data:
            if choice.lower() == item.lower():
                idx = self._data.index(item)
                self._data[idx] = f"{update}\n"
                self.writeEntity(self._data)
                print("Данные обновлены")
                break

    def deleteEntity(self, payload: list[str]) -> None:
        choice: str = self._choiceEntity(payload)
        self._data.remove(choice)
        print("Данные удалены")
        self.writeEntity(self._data)
