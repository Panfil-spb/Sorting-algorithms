def shaker_sort(mas: list):
    left = 0
    right = len(mas) - 1

    while left <= right:
        for i in range(left, right, 1):
            if mas[i] > mas[i+1]:
                mas[i], mas[i+1] = mas[i+1], mas[i]
        right -= 1

        for i in range(right, left, -1):
            if mas[i-1] > mas[i]:
                mas[i-1], mas[i] = mas[i], mas[i-1]
        left += 1
