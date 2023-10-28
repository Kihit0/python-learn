import math
class Learn:
    def sumThreeNumber(self, number: str):
        sum: int = 0
        for i in number:
            sum += int(i)
        print(sum)

    # соотношения 1:1:4
    def paperCranens(self, number: int):
        correlationToOne: int =  int(number / 6)
        print(correlationToOne, correlationToOne * 4, correlationToOne)

    def luckyTiket(self, number: str):
        long: int = int(len(number))
        leftNumber: str = number[0: int(long/2)]
        rightNumber: str = number[int(long/2): long]

        leftNumberSum: int = 0
        rightNumberSum: int = 0
        i: int = 0

        if(len(leftNumber) != len(rightNumber)):
            print("no")

        while i < int(long/2):
            leftNumberSum += int(leftNumber[i])
            rightNumberSum += int(rightNumber[i])
            i += 1

        if(leftNumberSum == rightNumberSum):
            print("yes")
        else:
            print("no")

    def splittingChocolateBar(self):


learn: Learn = Learn()
#learn.sumThreeNumber(number="123")
#learn.paperCranens(number=24)
#learn.luckyTiket("124123")
