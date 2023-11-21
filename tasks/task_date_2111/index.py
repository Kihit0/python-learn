

class Learn2111:

    def ellerIntersection(self, st1: str, st2: str) -> None:
        lst: list = sorted(list(set(st1.split()) & set(st2.split())))
        print(" ".join(lst))

    def maxBerries(self, arr: list[int]) -> None: 
        maxCountBerries: int = 0
        index: int = -2

        for i in arr:
            sumBerries: int = arr[index] + arr[index + 1] + arr[index + 2]
            index += 1
            if sumBerries > maxCountBerries: 
                maxCountBerries = sumBerries

        print(maxCountBerries)         

learn: Learn2111 = Learn2111()
learn.ellerIntersection(st1='1 2 3', st2='1 2 3 4')
#learn.maxBerries(arr=[5, 8, 10, 4, 9, 2, 7, 3])

"""
var2 = '1 2 3'
var3 = '1 2 3 4'

var2 = '5 6 7 8' 
var3 = '6 7 8 9'

var2 = '1'
var3 = '3 4 5 6'

var2 = '10 20 30 40 50'
var3 = '10 20 30 40 50'

"""