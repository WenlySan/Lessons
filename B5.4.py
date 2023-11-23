# def D(a, b, c):
#     return b ** 2 - 4 * a * c
#
# def quadratic_solve(a, b, c):
#     if D(a, b, c) < 0:
#         return "Нет вещественных корней"
#     elif D(a, b, c) == 0:
#         return -b / (2 * a)
#     else:
#         return (-b - D(a,b,c) ** 0.5) / (2 * a), (-b + D(a, b, c) ** 0.5) / (2 * a)
#
# L = [1, 0, -1]
# M = {'a': 1,
#      'b': 0,
#      'c': -1}
#
# print(quadratic_solve(**M))
#
#
# print(*M)
#
#
# iter_obj = iter("Hello!")
#
# print(next(iter_obj))
#
#
# def e():
#     n = 1
#     e()
#     # while True:
#     #     yield (1 + 1 / n) ** n
#     #     n += 1
#
# e()

a = ["asd", "bbd", "ddfa", "mcsa"]
print(map(len,a))
print(list(map(len, a)))

print(list(map(str.upper, a)))