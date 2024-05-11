def sumValue(a: float, b: float) -> float:
    if a % 2 == 0 or b % 2 == 0:
        return a + b
    return 0

def numberOperation(symbol: str):
    typeOperation = symbol

    if typeOperation == '+':
        def operation(a: float, b: float) -> float:
            return sumValue(a, b)
    elif typeOperation == '-':
        def operation(a: float, b: float) -> float:
            return a - b
    else:
        def operation(a: float, b: float) -> str:
            return f'operation \"{a} {typeOperation} {b}\" is not realized'

    return operation


sumNumbers = numberOperation('+')
result = sumNumbers(3, 5)
print(result)

subNumbers = numberOperation('-')
result2 = subNumbers(4, 5)
print(result2)