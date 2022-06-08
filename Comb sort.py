import random

def combo_sort(mas: list):
    k = 1.217
    step = len(mas) - 1
    swaps = True
    while step > 1 or swaps:
        step = max(1, int(step / k))
        swaps = False
        for i in range(len(mas) - step):
            if mas[i] > mas[i+step]:
                mas[i], mas[i+step] = mas[i+step], mas[i]
                swaps = True
