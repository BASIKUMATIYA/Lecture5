def even(numbers):
    evens = []
    for n in numbers:
        if n % 2 == 0:
            evens.append(n)
    return evens


nums = [10, 15, 22, 33, 40, 51]
print(nums)
print(even(nums))