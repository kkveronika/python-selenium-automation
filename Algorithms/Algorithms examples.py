
#Given an array nums, write a function to move all zeroes to the end of it
#while maintaining the relative order of the non-zero elements.

def zeroes(nums):
    for i in nums:
        if 0 in nums:
            nums.remove(0)
            nums.append(0)

    return nums


array1 = [0,1,0,3,12]
array2 = [1,7,0,0,8,0,10,12,0,4]
# print(zeroes(array1))
# print(zeroes(array2))

#Write a function which will check if the string is a palindrome

def palindrome(string):
    result = string == string[::-1]
    return result



test_result = palindrome('house')

if test_result:
    print("Yeess it is")
else:
    print("Nooooo")



"""

def isPalindrome(s):
    return s == s[::-1]
    
s = "malayalam"
ans = isPalindrome(s)
if ans:
    print("Yes")
else:
    print("No")

"""
# Find the sum of 2 with the target
list = [1, 4, 6, 8]
target = 12

def sum_of_two(list):
    for i in list:
        if i + j







