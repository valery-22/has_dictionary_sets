def repeating_elements(nums):
    seen, repeated = set(), set()
    for num in nums:
        if num in seen:
            repeated.add(num)
        else:
            seen.add(num)
    return sorted(list(repeated))

print(repeating_elements([9, 8, 7, 8, 7, 6, 5]))  # Expected output: [7, 8]
print(repeating_elements([-1, 2, 3, -1, 2, 3]))   # Expected output: [-1, 2, 3]
print(repeating_elements([1, 2, 3, 4, 5]))        # Expected output: []
