def remove_all_after(numbers, n):
    ...
    if n in numbers:
        index = numbers.index(n)
        numbers = numbers[:index + 1]
    return numbers


