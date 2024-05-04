from main import Teacher, polishko
from inspect import signature

# x: int
# x = 2
# print(type(x))
print(type(polishko))
attrs = dir(polishko)
# print(attrs)
#
# for attr in attrs:
#     if attr.startswith('__') is not True:
#         print(attr)

# for attr in attrs:
#     if attr.startswith('__') is not True:
#         print(f'{attr} :\t{getattr(polishko, attr)}')
#
# print(hasattr(polishko, 'age2'))

# for attr in attrs:
#     if attr.startswith('__') is not True:
#         print(type(getattr(polishko, attr)))


attrs2 = signature(Teacher)
for attr in attrs2.parameters:
    print(attr)

for attr in attrs2.parameters.values():
    print(attr)