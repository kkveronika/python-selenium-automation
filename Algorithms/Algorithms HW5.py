# 1.Selection Sort
# Implement the selection sort algorithm that is sorting in descending order.

#need to know:
# Selection sort in Python
# time complexity O(n*n)
# sorting by finding min_index
def selection_sort(arr: list):
    for i in range (len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
             if arr[j] > arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# test_list = [22, 44, 56, 78, 11, 1]
# print(test_list)
# print(selection_sort(test_list))

# 2.Bubble Sort
# Implement the bubble sort algorithm that is sorting in descending order.

def bubble_sort (arr: list):
    for i in range (len(arr)):
        for j in range (len(arr) - 1 - i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


test_result = [89, 67, 12, 44, 0, 80]
print(test_result)
print(bubble_sort(test_result))


# 3.Insertion Sort
# Implement the insertion sort algorithm that is sorting in descending order.

# 4.Merge Sort
# Implement the merge sort algorithm that is sorting in descending order.


