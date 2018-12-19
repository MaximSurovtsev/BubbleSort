def bubbleSort(a):
    for i in range(1, len(a)):
        swapped = False
        for j in range(len(a)-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        if not swapped:
            break
