class Calculation:
    typeOperation: str

    def __init__(self, typeOperation: str):
        self.typeOperation = typeOperation

    def sumValue(self, a: float, b: float) -> float:
        if a % 2 == 0 or b % 2 == 0:
            return a + b
        return 0

    def __call__(self, a: float, b: float):

        if self.typeOperation == '+':
            return self.sumValue(a, b)
        elif self.typeOperation == '-':
            return a - b
        else:
            return f'operation \"{a} {self.typeOperation} {b}\" is not realized'


sumValue = Calculation(typeOperation='%')
print(sumValue(a=4, b=5))
