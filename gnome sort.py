def gnome_sort(mas: list):
    i, size = 1, len(mas)
    while i < size:
        if mas[i-1] <= mas[i]:
            i += 1
        else:
            mas[i-1], mas[i] = mas[i], mas[i-1]
            if i > 1:
                i -= 1
