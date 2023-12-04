class Learn0112:
    def print_operation_table(self, operation, num_rows, num_columns) -> None:
        if num_rows < 2 or num_columns < 2:
            print("ОШИБКА! Размерности таблицы должны быть больше 2!")
        else:
            header = " ".join([str(i) for i in range(1, num_columns + 1)])
            print(header)
            for i in range(2, num_rows + 1):
                row = [str(i)] + [
                    str(operation(i, j)) for j in range(2, num_columns + 1)
                ]
                print(" ".join(row))

    def win_and_pooh(self, string: str) -> None:
        string: list = string.split()

        if len(string) == 1:
            print("none")
        else:
            lst: list[int] = []
            for word in string:
                sum_w = 0
                for i in word:
                    if i in "аеёиоуыэюя":
                        sum_w += 1
                lst.append(sum_w)
            if len(lst) == lst.count(lst[0]):
                print("Парам пам-пам")
            else:
                print("Пам парам")    


learn: Learn0112 = Learn0112()
# learn.print_operation_table(lambda x, y: x * y, 3, 3)
isParam = learn.win_and_pooh("за-гад-ка-ра-свет-ка-ра-газ-да-не-на-ма-ли-ва-ла")
