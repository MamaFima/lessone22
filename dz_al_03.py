a = [0, 12, 15, 8, 9, 19, 99, -30, -7, 33, 14, -100]
n = len(a)

# Пузырьковая сортировка
for run in range(n-1):
    for i in range(n-1-run):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]

print(a)


# Быстрая сортировка
def quick_sort(a):
    if len(a) <= 1:
        return a

    element = a[0]
    left = list(filter(lambda i: i < element, a))
    center = [i for i in a if i == element]
    right = list(filter(lambda i: i > element, a))
    return quick_sort(left) + [center] + quick_sort(right)

print(quick_sort(a))


# Сортировка выбором
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

print(selection_sort(a))


# Сортировка вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

print(insertion_sort(a))
