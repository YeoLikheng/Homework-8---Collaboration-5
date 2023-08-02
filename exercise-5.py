def reverse_ascending(numbers):
    if not numbers:  # if the list is empty
        return numbers
    # Initialize variables
    res, temp = [], [numbers[0]]
    # Iterate through the numbers
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i-1]:  # If the current number is greater than the previous one, it's part of an ascending subsequence
            temp.append(numbers[i])
        else:  # If it's not part of the same ascending subsequence, append the reversed subsequence to the result
            res += temp[::-1]
            temp = [numbers[i]]  # Start a new subsequence
    res += temp[::-1]  # Append the last subsequence
    

    return res
assert list(reverse_ascending([1, 2, 3, 4, 5])) == [5, 4, 3, 2, 1]
assert list(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])) == [10, 7, 5, 4, 8, 7, 2, 3, 1]
assert list(reverse_ascending([5, 4, 3, 2, 1])) == [5, 4, 3, 2, 1]
assert list(reverse_ascending([])) == []
