# 1) Дана строка в виде случайной последовательности чисел от 0 до 9.
# Требуется создать словарь, который в качестве ключей будет принимать данные числа (т. е. ключи будут типом int),
# а в качестве значений – количество этих чисел в имеющейся последовательности.

str1 = "124835737504846385650"
print(len(str1))

dic = {}
for i in str1:
    a =(str1.count(i))
    d = (dict.fromkeys(i,a))
    dic.update(d)
for i in str1:
    a = (str1.count(i))
    d = (dict.fromkeys(i,a))
    print(d)
print(dic)





# 2) Даны два списка чисел, которые могут содержать до 10000 чисел каждый.
# Выведите все числа, которые входят как в первый, так и во второй список в порядке возрастания.
_list1 = set([1, 2, 55, 89, 600])
_list2 = set([5, 1, 400, 55])
_sort = _list1 & _list2
print(_sort)

# 3) Имеется файл file.txt с текстом. Напишите программу,
# которая выводит следующую статистику по тексту:
# количество букв латинского алфавита;
# число строк.
import os
with open ('file.txt', 'r') as file:

    a = file.read().replace(" ","")

    _count = 0
    _num = 0
    for i in a:
        if i.isalpha():
         _count +=1;
        if i.isdigit():
            _num +=1
    quantity = len(open('file.txt').readlines())
    print(_count,_num, quantity)