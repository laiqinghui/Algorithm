import math


def partition(arr, left, right):

    pivot = math.floor((left + right)/2)
    print("Pivot for comparison: ", pivot)
    temp = arr[left]
    arr[left] = arr[pivot]
    arr[pivot] = temp
    lastSmall = left
    print("Initial): ", arr)
    print("range(left+1, right+1, 1)", range(left+1, right+1, 1))

    for i in range(left+1, right+1, 1):

        if arr[i] < arr[left]:
            temp = arr[i]
            lastSmall += 1
            arr[i] = arr[lastSmall]
            arr[lastSmall] = temp
            print("i: ", i, " Arr: ", arr)

    temp = arr[left]
    arr[left] = arr[lastSmall]
    arr[lastSmall] = temp

    print("Results of partition: ", arr)
    return lastSmall


def QuickSort(arr, left, right):

    if right <= left:
        return

    pivot = partition(arr, left, right)
    print("Pivot: ", pivot)
    QuickSort(arr, left, pivot-1)
    QuickSort(arr, pivot+1, right)


arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
QuickSort(arr, 0, (len(arr)-1))
print("Final: ", arr)


def partition2(arr, left, right):
    
    pivot = math.floor((left + right)/2)
    lastsmall = left
    temp = arr[left]
    arr[left] = arr[pivot]
    arr[pivot] = temp

    for i in range(left+1, right+1, 1):
        if arr[i] < arr[left]:
            temp = arr[i]
            lastsmall += 1
            arr[i] = arr[lastsmall]
            arr[lastsmall] = temp

    temp = arr[lastsmall]
    arr[lastsmall] = arr[left]
    arr[left] = temp

    return lastsmall