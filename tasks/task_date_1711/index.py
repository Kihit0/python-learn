class Learn1711:
    def number_of_occurrences(self, lst: list[int], k: int):
        print(lst.count(k))

    def nearest_number(self, lst: list[int], k: int) -> None:
        print(min(lst, key=lambda x: abs(x - k)))

    def scrabble(self, k: str) -> None:
        keys: dict = {
            "AEIOULNSTRАВЕИНОРСТ": 1,
            "DGДКЛМПУ": 2,
            "BCMPБГЁЬЯ": 3,
            "FHVWYЙЫ": 4,
            "KЖЗХЦЧ ": 5,
            "JXШЭЮ": 8,
            "QZФЩЪ": 10,
        }

        count: int = 0

        for char in k:
            for key in keys:
                isCharInList: int = list(key).count(char.upper())

                if isCharInList:
                    count += keys[key]
                    break

        print(count)


learn: Learn1711 = Learn1711()
# learn.number_of_occurrences(lst=[3, 3, 3, 3, 3], k=3)
# learn.nearest_number(lst=[1, 2, 3, 4, 5], k=6)
learn.scrabble(k="ноутбук")
