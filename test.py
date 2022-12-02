# def plus(x, y):
#     return x + y
# def minus(x, y):
#     return x - y
# def umnoj(x, y):
#     return x * y
# def delen(x, y):
#     return x / y
# while True:
#     try:
#         choice = input("Выберите метод '+, - , / , *': ")
#
#         if choice in ('+', '-', '/', '*'):
#
#             a = float(input("Первое число: "))
#             b = float(input("Второе число: "))
#             if choice == '+':
#                 print(a, "+", b, "=", plus(a, b))
#
#             elif choice == '-':
#                 print(a, "-", b, "=", minus(a, b))
#
#             elif choice == '*':
#                 print(a, "*", b, "=", umnoj(a, b))
#
#             elif choice == '/' and b != 0:
#                 print(a, "/", b, "=", delen(a, b))
#             else:
#                 print("Неправильный ввод")
#         else:
#             print("Неправильный ввод")
#     except:
#         ValueError

#
# games = 50
# dict_ = {
# 'points ': 561,
# 'threes ': 83,
# 'bloks ': 33,
# 'assists':  168,
# 'steals': 144,
# 'rebounds':  163,
# }
#
# for i , y in dict_:
#     b = y // games
#     print(i, y)
#

sample = {'Aus' , 'Ger' , 'Pediki' , 'Allah'}
print('hui')
for j in enumerate(sample):
    print(j)
    print('\n')
