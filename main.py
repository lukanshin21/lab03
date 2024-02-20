def bubble_sort(n,k):
    arr = []
    for _ in range(n):
        num = int(input())
        arr.append(num)
    if k == 1:
        for i in range(len(arr) - 1):
            for j in range(0, len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
    elif k == 2:
        for i in range(len(arr) - 1):
            for j in range(0, len(arr) - i - 1):
                if arr[j] < arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print("Отсортированный список: ")
    for num in arr:
        print(num)

k = int(input("Введите 1, если по возрастанию, 2 - по убыванию: "))
n = int(input("Введите число элементов: "))
bubble_sort(n,k)
