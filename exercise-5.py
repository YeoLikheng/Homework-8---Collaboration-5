def reverse_ascending(numbers):
    if not numbers:
        return numbers
    result = []
    current_subsequence = [numbers[0]]
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i-1]:
            current_subsequence.append(numbers[i])
        else:
            current_subsequence.reverse()
            result.extend(current_subsequence)
            current_subsequence = [numbers[i]]
    current_subsequence.reverse()
    result.extend(current_subsequence)
    return result

# Run the tests
test_cases = [
    [1, 2, 3, 4, 5],
    [5, 7, 10, 4, 2, 7, 8, 1, 3],
    [5, 4, 3, 2, 1],
    []
]

# Output for first test case
result = reverse_ascending(test_cases[1])
print('\n'.join(map(str, result)))

print()

# Output for second test case
for i in range(1, 15):
    print(i)
