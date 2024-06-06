# def add(*args):
#     sum = 0
#     for arg in args:
#         sum += arg
#     return sum
#
#
# func_sum = add(1, 5, 6, 10)
# print(func_sum)


def calculate(n, **kwargs):
    n += kwargs.get('add')
    n *= kwargs.get('multiply')
    print(n)


calculate(2, add=3, multiply=5)


