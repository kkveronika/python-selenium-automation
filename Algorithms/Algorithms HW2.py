# Split in Half
# Given a string. Split it into two equal parts. Swap these parts and return the result.
# If the string has odd characters, the first part should be one character greater than the second part.
# Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’.


# 'abcdefg' -> 7
# 'abcd'
# 'efg'
#
# 'efgabcd'

def split_in_half(string):
    # count how many characters are inside the string
    # if the number of characters is odd, the first part of the string will be bigger than the second one
    # swap the parts and merge those variables together
    number_characters = len(string)

    if number_characters % 2 != 0:
        # if the string contains odd number of characters the program will enter here
        first_middle = string[:number_characters // 2 + 1]
        second_middle = string[number_characters // 2 + 1 :]
    else:
        # otherwise it will enter here
        first_middle = string[:number_characters // 2]
        second_middle = string[number_characters // 2:]

    first_middle, second_middle = second_middle, first_middle

    return first_middle + second_middle


# print(split_in_half('abcdefg'))
# print(split_in_half('aaaaaabbbbbbbbb'))




# Unique Characters in String
# Given a string, determine if it consists of all unique characters.
# For example, the string 'abcde' has all unique characters and should return True.
# The string 'aabcde' contains duplicate characters and should return False.

#
# 'abcdefgc'
# 'a' -> 1
# 'b' -> 1
# 'c' -> 2

def unique_char(s1):
    # iterate over the string and get each character
    # verify how many  times this character appear inside the string
    # if it appears more than once return false
    # otherwise when the loop finishes return true


    for character in s1:
        number_of_times_inside_str = s1.count(character)

        if number_of_times_inside_str > 1:
            return False

    return True


s1 = "abcdeaaaa"

result = unique_char(s1)
print(result)



