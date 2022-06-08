import random

def shell_sort(mas: list):
    inc = len(mas) // 2
    while inc:
        for i, el in enumerate(mas):
            while i >= inc and mas[i - inc] > el:
                mas[i] = mas[i-inc]
                i -= inc
            mas[i] = el
        inc = 1 if inc == 2 else int(inc * 5 / 11)

mas = []
for i in range(random.randrange(1, 100)):
    mas.append(random.randrange(1, 100))
print(mas)
shell_sort(mas)
print(mas)