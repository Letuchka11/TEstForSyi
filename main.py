# l = ["h" , "C" , "e" ,3,"T" , "k" ,4, "e" , "e" , "g", True ]
# n = [ 3 , 1]
#
# # l.reverse()
# # l[1] = "G"
# # l[-2] = "c"
# # n.insert(1,2)
# # n.sort()
# # n = (i**2 for i in n)
# # print(l)
# # print(n)
#
# for i in l:
#     if type(i) == int:
#         print(i)
# print(l)
#
#
# dict_ = {I;1}
# b = help(index)
#
# print(b)

# number = range(10)
# a = []
# for i in number:
#     if i % 3 == 0:
#         a.append(i)
#     elif i % 5 == 0:
#         a.append(i)
#
# print(sum(a))

#
# bad_words = ["пидор", 'пидр ', 'уебан', "уебок", 'хуила', 'уебище', "уебан", "хуй", "хуя", "ху",
#              "Жалап", "Шлюха", "Пиздоеб", "Говноед", "Кусок хуя", 'сука', "Моча ослиная",
#              "Мохнатка", "Керим", "Чорт", "Пиздоглаз", "Долбоеб", "Хуеглот", 'Долбоящер',
#              "Пидрила", "Эмонали рахмон", "мал", "коток", "кот", "ам", "пидар", 'скейн',
#              "манда", 'мандавошка']
#
# a = 23.4
#
# print(type(a))
# print(len(bad_words))

# a = 3432
def solution(roman):
    answer= []
    context = {
        "I" : 1,
        "V" : 2,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }
    context["IV"] = 4
    context["IX"] = 9
    context["XL"] = 40
    context["XC"] = 90
    context["CD"] = 400
    context["CM"] = 900
    for i , j in context.items():
        if i in roman:
            answer.append(j)
    return answer

solution("I")