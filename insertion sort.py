import random

def insertion_sort(mas: list):
    for i in range(1, len(mas)):
        j = i - 1
        value = mas.pop(i)
        while j >= 0 and mas[j] > value:
            j -= 1
        mas.insert(j + 1, value)


mas = []
for i in range(random.randrange(1, 100)):
    mas.append(random.randrange(1, 100))
print(mas)
insertion_sort(mas)
print(mas)