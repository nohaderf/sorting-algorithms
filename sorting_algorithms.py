# Bubble Sort
def bubble_sort(arr):
    swap_happened = True

    while swap_happened:
        print ('Bubble sort status: ' + str(arr))
        swap_happened = False
        for num in range(len(arr) - 1):
            if arr[num] > arr[num + 1]:
                arr[num], arr[num + 1] = arr[num + 1], arr[num]
                swap_happened = True

arr = [ 4, 2, 7, 3, 9, 10, 1, 6, 5, 8]
bubble_sort(arr)

# Selection Sort
def selection_sort(arr):
    marker = 0
 
    while marker < len(arr):
        print ('Selection sort status: ' + str(arr))
        for num in range(marker, len(arr)):
            if arr[marker] > arr[num]:
                arr[marker], arr[num] = arr[num], arr[marker]
        marker += 1

arr = [ 4, 2, 7, 3, 9, 10, 1, 6, 5, 8]
selection_sort(arr)

# Insertion Sort
def insertion_sort(arr):
    for num in range(1, len(arr)):
        key = arr[num]

        while arr[num - 1] > key and num >= 0:
            print ('Insertion sort status: ' + str(arr))
            arr[num - 1], arr[num] = arr[num], arr[num - 1]
            num -= 1

arr = [ 4, 2, 7, 3, 9, 10, 1, 6, 5, 8]
insertion_sort(arr)

# Merge Sort
def merge_sort(arr1, arr2):
    sorted_arr = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        else:
            sorted_arr.appen(arr2[j])
            j += 1
    
    while i < len(arr1):
        sorted_arr.append(arr1[i])
        i += 1
    
    while j < len(arr2):
        sorted_arr.append(arr2[j])
        j += 1
    return sorted_arr

arr1 = [4, 2, 7, 3, 9]
arr2 = [10, 1, 6, 5, 8]
print("Merge sort complete: {}".format(merge_sort(arr1, arr2)))

# Quick Sort
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[-1]
        smaller, equal, larger = [], [], []
        for num in arr:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else: 
                larger.append(num)
        return quick_sort(smaller) + equal + quick_sort(larger)

l = [ 6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
print(quick_sort(l))