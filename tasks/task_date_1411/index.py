import math


class Learn1411:
    def count_money(self, coins: list[int]) -> None:
        count: int = sum(coins)
        if count == len(coins):
            print(f"0")
        elif count > (math.floor(len(coins) / 2)):
            print(f"{len(coins) - count}")
        else:
            print(f"{count}")

    def xy(self, s: int, p: int) -> None:
        number: str = ""

        if s > 1000 | p > 1000:
            print("Numbers exceed the limit")

        for i in range(int(s / 2) + 1):
            for j in range(s + 1):
                if ((i * j == p) & (i + j == s)) & (i <= j):
                    number += f"{str(i)} {str(j)}"

        print(f"{number}")

    def sqrtTwo(self, n: int) -> None:
        for i in range(n):
            if (2**i) <= n:
                print(f"{2 ** i}")


learn: Learn1411 = Learn1411()

learn.count_money([0, 1, 1, 1, 1])
# learn.xy(s=12, p=27)
# learn.sqrtTwo(n=256)
