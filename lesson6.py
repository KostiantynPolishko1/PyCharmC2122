a = '5'
b = 2
values = [1, 2, 3, 4]
# result = a / b

# if not b == 0:
#     result = a / b
#     print(f'division = {result}')

try:
    result = a / b
except(BaseException) as e:
    print(e)
    result = -1
finally:
    print(f'{a} / {b} = {result}')
    values.append(result)

# except (ZeroDivisionError, TypeError) as error:
#     print(error)
# except (TypeError) as error:
#     print(error)

for value in values:
    print(value)
