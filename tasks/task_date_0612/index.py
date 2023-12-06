import logics


class Interface(logics.Logic):
    _isEnd: bool = True
    _example: str = "Пример ввода данных: Иванов Иван Иванович 800000000"

    def __init__(self, path: str) -> None:
        super().__init__(path)

    def interface(self) -> None:
        while self._isEnd:
            print(
                "\nВыберете действие: \
                    \n 0 - Выйти \
                    \n 1 - Вывести все контакты \
                    \n 2 - Добавить контакт \
                    \n 3 - Поиск контакта \
                    \n 4 - Обновление контакта \
                    \n 5 - Удаление контакта \n"
            )

            command: int = int(input())
            print()
            match command:
                case 0:
                    self._isEnd = False
                case 1:
                    self.printEntity()
                case 2:
                    print(f"Введите данные. {self._example}")
                    writePhone: str = input()

                    st: set = set(map(lambda item: len(item) != 1, writePhone.split()))

                    if (
                        len(writePhone.split()) != 4
                        or len(st) != 1
                        or list(st)[0] == False
                    ):
                        while (
                            len(writePhone.split()) != 4
                            or len(st) != 1
                            or list(st)[0] != False
                        ):
                            print("Вы ввели некорректные данные")
                            writePhone: str = input()
                    else:
                        self.writeEntity(writePhone.strip().lstrip())
                case 3:
                    print(
                        f"Введите строку для поиска. Поиск может произведен по Фамилии, Имени, Отвечеству или Телефону. \
                        \nДля более узкого поиска можете ввести все данные. \n{self._example}"
                    )
                    search: str = input()

                    self.searchEntity(search)
                case 4:
                    print(f"Введите данные для поиска")
                    search: str = input()
                    print(f"Введите данные для изменения. {self._example}")
                    update: str = input()

                    if len(update.split()) != 4:
                        while len(update.split()) != 4:
                            print("Вы ввели недостаточно данных")
                            update: str = input()
                    else:
                        self.updateEntity(self.searchEntity(search), update)
                case 5:
                    print("Введите данные для поиска")
                    phone: str = input()
                    self.deleteEntity(self.searchEntity(phone))
                case _:
                    print("Неверная команда")


if __name__ == "__main__":
    path: str = "tasks/task_date_0612/phone.txt"
    workWithFile: Interface = Interface(path)
    workWithFile.interface()
