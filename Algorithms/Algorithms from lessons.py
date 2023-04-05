# 1.HW 4 Solutions
# Even First
# Your input is an array of integers, and you have to reorder its entries so that the even entries appear first.
# You are required to solve it without allocating additional storage (operate with the input array).
# Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]

# O(n)
# def even_odd(arr: list):
#     next_even = 0
#     next_odd = len(arr) - 1
#     while next_even < next_odd:
#         if arr[next_even] % 2 == 0:
#             next_even += 1
#         else:
#             arr[next_even], arr[next_odd] = arr[next_odd], arr[next_even]
#             next_odd -= 1
#     return arr
#
#
# test_list = [5, 3, 4, 6, 10, 9, 11]
# print(test_list)
# test_result_list = even_odd(test_list)
# print(test_result_list)  # [4, 6, 10, ....]
# print(test_list)

# Write a program that takes as input an array of digits encoding a nonnegative decimal integer D
# and updates the array to represent the integer D + 1.
# For example, if the input is [1, 2, 9] then you should update the array to [1, 3, 0].


# O(n)
def plus_one(arr: list):
    arr[-1] += 1
    for i in reversed(range(1, len(arr))):
        if arr[i] != 10:
            break
        arr[i] = 0
        arr[i - 1] += 1
    if arr[0] == 10:
        arr[0] = 1
        arr.append(0)

    return arr


test_digit1 = [1, 2, 3]  # => 1, 2, 4
test_digit2 = [1, 9, 9]  # => 2, 0, 0
test_digit3 = [9, 9, 9]  # => 1, 0, 0, 0
# print(plus_one(test_digit1))
# print(plus_one(test_digit2))
print(plus_one(test_digit3))


#2.Lesson sort
list_words = ['banana', 'strawberry', 'apple', 'orange', 'kiwi']
print(list_words)
result_list = sorted(list_words, key=len, reverse=True)
print(result_list)

#3. Recursion
def recursion(number: int):
    if number == 0:
        return
    print(number)
    number -= 1
    recursion(number)

recursion(10)


#4. Selection sort
# O(n^2)
def selection_sort(arr: list):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


test_list = [5, 3, 6, 1, 2, 9]
print(test_list)
print(selection_sort(test_list))


#5.# O(N * Log N)
def merge_sort(arr: list):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    return merge_arrays(merge_sort(arr[:middle]), merge_sort(arr[middle:]))


def merge_arrays(left_arr: list, right_arr: list):
    merged_list = []
    i = j = 0
    while i < len(left_arr) or j < len(right_arr):
        if i == len(left_arr):
            merged_list.append(right_arr[j])
            j += 1
            continue
        if j == len(right_arr):
            merged_list.append(left_arr[i])
            i += 1
            continue

        if left_arr[i] <= right_arr[j]:
            merged_list.append(left_arr[i])
            i += 1
        else:
            merged_list.append(right_arr[j])
            j += 1
    return merged_list


test_list = [9, 4, 3, 1, 6, 2, 5]
print(test_list)
print(merge_sort(test_list))


#6. Insertion sort
# O(n^2)
def insertion_sort(arr: list):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr

test_list = [6, 4, 2, 5, 1]
print(test_list)
print(insertion_sort(test_list))


#7. Bubble sort
# O(n^2)
def bubble_sort(arr: list):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


test_list = [5, 4, 7, 9, 1, 6]
print(test_list)
print(bubble_sort(test_list))


#https://www.geeksforgeeks.org/python-program-for-bubble-sort/?ref=lbp