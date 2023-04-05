#Below The Arithmetical Mean
#When given a list, the program should return
# a list of all the elements lesser than the arithmetical mean.
# The arithmetical mean is the sum of all elements divided by the number of elements.
#Example: [1, 3, 5, 6, 4, 10, 2, 3] (The arithmetical mean is 4.25), Return [1, 3, 4, 2, 3]

# Understand the problem
# - See what is the input they will give to you. Example: [1, 3, 5, 6, 4, 10, 2, 3]
# - identify what is the process:
# sum up all elements and divide by the number of elements, this is going to represent the arithmetical mean
# compare all numbers from the original list with the arithmetical mena
# Output will be all numbers lesser than the arithmetical mean

# Do the process on your mind with some examples
#  [1, 2, 3, 4] mean = 2.5  result [1, 2]


def ar_mean_comparation(input):
    sum_result = sum(input)
    number_of_elements = len(input)

    ar_mean = sum_result / number_of_elements
    # print("mean:", ar_mean)

    result = []
    for item in input:
        if item < ar_mean:
            result.append(item)

    # print("result: ", result)
    return result


input = [1, 2, 3, 4]
#print(ar_mean_comparation(input))

#Two Lowest Elements
#When given a list of elements, find the two lowest elements.
#They can be equal to each other or different.
#Example: [198, 3, 4, 9, 10, 9, 2], Return: [2, 3]

# input [5, 4, 7, 10, 2] output: [2]
# input [91, 95, 96, 97, 100] ouput: [91, 95]
#process: pick one element -> compare to another one, if less than first elemnt -> keep it,
#do the same with each element in the list
#output -> two the lowest numbers

# def two_smallest_elements(list):
    # list= [198, 3, 4, 9, 10, 9, 2]
    # new_list = []
    # first_min_element= min(list)
    # # print(first_min_element)
    # new_list.append(first_min_element)
    #
    # list.remove(first_min_element)
    #
    # second_min_element = min(list)
    # new_list.append(second_min_element)
    # # print(new_list)
    # return new_list


# def two_smallest_elements(list):
#     list.sort()
#     return list [:2]

def two_smallest_elements(list):
    new_list = []
    lowest = list[0]
    for item in list:
        if item < lowest:
            lowest = item

    # print(lowest)
    list.remove(lowest)

    second_lowest = list[0]
    for item in list:
        if item < second_lowest:
            second_lowest = item

    # print(second_lowest)
    new_list.append(lowest)
    new_list.append(second_lowest)

    return new_list


list= [198, 3, 4, 9, 10, 9, 2]
print(two_smallest_elements(list))

