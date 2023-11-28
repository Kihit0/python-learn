class Learn2811:
    def betweenTwoNumber(
        self, lst: list[int], min_number: int, max_number: int
    ) -> list[int]:
        printLst: list[int] = list()
        for i in range(len(lst)):
            if lst[i] >= min_number and lst[i] <= max_number:
                printLst.append(i)

        return printLst

    def arithmeticProgression(self, a1: int, d: int, n: int) -> list[int]:
        arithmeticProgress: list[int] = list()

        for i in range(1, n + 1):
            arithmeticProgress.append(a1 + (i - 1) * d)

        return arithmeticProgress


lst: list[int] = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
learn: Learn2811 = Learn2811()
print(learn.betweenTwoNumber(lst, -10, -4))
print(learn.arithmeticProgression(2, 3, 4))
