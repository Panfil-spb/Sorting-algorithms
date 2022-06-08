def insertion_sort(mas: list):
    for i in range(1, len(mas)):
        j = i - 1
        value = mas.pop(i)
        while j >= 0 and mas[j] > value:
            j -= 1
        mas.insert(j + 1, value)
