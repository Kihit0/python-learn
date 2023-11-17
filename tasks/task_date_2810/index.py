import math
class Learn2810:
    def sumThreeNumber(self, number: str) -> None:
        sum: int = 0
        for i in number:
            sum += int(i)
        print(sum)

    # ratios 1:1:4
    def paperCranes(self, number: int) -> None:
        correlationToOne: int = int(number / 6)
        print(correlationToOne, correlationToOne * 4, correlationToOne)

    def luckyTicket(self, number: str):
        long: int = int(len(number))
        leftNumber: str = number[0: int(long/2)]
        rightNumber: str = number[int(long/2): long]

        leftNumberSum: int = 0
        rightNumberSum: int = 0
        i: int = 0

        if len(leftNumber) != len(rightNumber):
            print("no")

        while i < int(long/2):
            leftNumberSum += int(leftNumber[i])
            rightNumberSum += int(rightNumber[i])
            i += 1

        if leftNumberSum == rightNumberSum:
            print("yes")
        else:
            print("no")

    def splittingChocolateBar(self, a: int, b: int, c: int) -> None:
        if(c > (a * b)):
            print("no")
        elif(c == 1 & ((a == 1) | (b == 1))):
            print("yes")
        elif (a != 1) & (b != 1) & (c != 1):
            if (a % c == 0) | (c % a == 0) | (b % c == 0) | (c % b == 0):
                print("yes")
        else:
            print("no")