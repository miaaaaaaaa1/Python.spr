#category = ["React"[1 , 2 , 3 , 4 , 5]]
#print(type(category))
#courses = list(("Python","Java"))
#print(type(courses))
#print(category[-1][-1])
#print(courses[0])

#courseswithSymbol = [i + "*" for i in courses]
#print(courseswithSymbol)
#list1 = [i*i for i in range(6) if i % 2 == 0]
#print(list1)

#5 count
#6 disting не можна 
#n = int(input("Enter number of elements: "))
#numbers = []

#for i in range(n):
#    num = float(input(f"Enter element {1+1}: "))
#    numbers.append(num)

#total = sum(numbers)
#average = total / n

#print(f"List: {numbers}")
#print(f"Sum: {total}")
#print(f"Average: {average}")

#print("_______________________________________")

#numbers = list(map(int, input("Введіть цілі числа : ").split()))
#target = int(input("Введіть число для пошуку: "))
#count = numbers.count(target)
#print("Число", target, "зустрічається", count, "рази")

#print("_______________________________________")

#numbers = list(map(int, input("Введіть числа: ").split()))
#positive_sum = sum(n for n in numbers if n > 0)
#print("Сума додатних чисел:", positive_sum)

#print("_______________________________________")

#a = list(map(int, input("Введіть числа: ").split()))
#for i in range(len(a)):
#    if a[i] % 2 == 0:
#        print(i, end=' ')

#print("_______________________________________")

#t = input("Введи текст: ")
#s = t.split('. ')
#for i in range(len(s)):
#    s[i] = s[i].capitalize()
#a = '. '.join(s)
#b = 0
#for x in t:
#    if x.isdigit():
#        b += 1
#c = 0
#for x in t:
#    if x in ',.;:!?-':
#        c += 1
#d = 0
#for x in t:
#    if x == '!':
#        d += 1
#print("Текст:", a)
#print("Цифр:", b)
#print("Розділових знаків:", c)
#print("Знаків оклику:", d)

#nums = list(map(int, input("Введи числа: ").split()))
#uniq = []
#for n in nums:
#   if n not in uniq:
#        uniq.append(n)
#print("Унікальні числа:", *uniq)
