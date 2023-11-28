class Learn2711:
    def pow(self, a: int, b: int) -> int:
        if b == 1:
            return a

        return self.pow(a, b - 1) * a

    def sum(self, a: int, b: int) -> int:
        if b == 0: 
            return a
        return self.sum(a + 1, b - 1)

learn: Learn2711 = Learn2711()

print(learn.pow(2, 5))
print(learn.sum(16, 6))