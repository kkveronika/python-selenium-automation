#Even First
#Your input is a list of integers,
# and you have to reorder its entries so that the even entries appear first.
# You are required to solve it without allocating additional storage (operate with the input list).
#Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]

#input list
#ouput all even integers first then odd
#process take first element if even -> put at the beginning,
# if not -> at the end,
# then take second element..
# process of ordering elements by identifying even or odd

#process in my mind - if first element divide by 2 -> even, so put at the beginning,
# if result with the reminder -> place after even numbers

# for element in list:
#     if element % 2 == 0
# ist = [7, 3, 5, 6, 4, 10, 3, 2]

def even_odd_sort(arr):
    # start two index, one at the beginning of the list and another one in the final position
    left = 0
    right = len(arr) - 1

    while left < right:
        # We are going to repeat this process until the left index is lesser than the right index

        # We will move the left index until it reaches an even number
        while arr[left] % 2 == 0 and left < right:
            left += 1

        # We will move the right index until it reaches an odd number
        while arr[right] % 2 != 0 and left < right:
            right -= 1

        # Swap the numbers at the left and right index
        arr[left], arr[right] = arr[right], arr[left]

    return arr

arr = [1, 2, 3, 5, 4, 9]
print(even_odd_sort(arr))  # Output: [4, 2, 3, 5, 1, 9]

"""
input [1, 2, 3, 5, 4, 9]
left = 0
right = 4

[4, 2, 3, 5, 1, 9]
left = 2
right = 2


#Increment a Number
#Write a program that takes as input a list of digits
# encoding a nonnegative decimal integer D and updates the list to represent the integer D + 1.
#For example, if the input is [1, 2, 9] then you should update the array to [1, 3, 0].



