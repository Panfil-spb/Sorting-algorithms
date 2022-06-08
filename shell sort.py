def shell_sort(mas: list):
    inc = len(mas) // 2
    while inc:
        for i, el in enumerate(mas):
            while i >= inc and mas[i - inc] > el:
                mas[i] = mas[i-inc]
                i -= inc
            mas[i] = el
        inc = 1 if inc == 2 else int(inc * 5 / 11)
