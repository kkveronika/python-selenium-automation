# Compute the sum of digits in all numbers from 1 to n.
# When a function gets a number n, find the sum of digits in all numbers from 1 to n.
# Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15

def sum_numbers(n:int):
    sum = 0
    for i in range(n+1):
        sum += i
    return sum


i = 28
result = sum_numbers(i)
print(result)

# Find the max number from 3 values.
# Example: 124, 21, 32. Result = 124.

def find_max (m, n, k):
    if m > n and m > k:
        return m
    if n > m and n > k:
        return n
    return k


result = find_max(23, 45, 67)
print(result)


# Count odd and even numbers. Count odd and even digits of the whole number.
# Example: number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).

def count_odd_even(n:int):
    odd = 0
    even = 0

    while n != 0:
        digit = n % 10
        if digit % 2:
            odd +=1
        else:
            even +=1

    n = n//10

    print(f"odd: {odd}")
    print(f"even: {even}")


n = 5678
print(count_odd_even)

#soory Vitaly, I am submitting later based on your solution,
# that helps me much better to understand these difficult algorithms



