class Learn0112:
    def print_operation_table(self, operation, num_rows, num_columns):
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

    def win_and_pooh(self, string: str) -> bool:
        str: list = string.split()

        list_1 = []
        for word in str:
            sum_w = 0
            for i in word:
                if i in "аеёиоуыэюя":
                    sum_w += 1
            list_1.append(sum_w)

        return len(list_1) == list_1.count(list_1[0])


learn: Learn0112 = Learn0112()
# learn.print_operation_table(lambda x, y: x * y, 3, 3)
isParam = learn.win_and_pooh("за-гад-ка-ра-свет-ка-ра-газ-да-не-на-ма-ли-ва-ла")

if isParam:
    print("Парам пам-пам")
else:
    print("Пам парам")
