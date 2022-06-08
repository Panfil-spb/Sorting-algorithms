def bubble_sort(mas: list):
    len_list = len(mas)
    for i in range(len_list - 1):
        for j in range(len_list - i - 1):
            if mas[j] > mas[j+1]:
                mas[j], mas[j+1] = mas[j+1], mas[j]
