m = int(input())    # Unuseful in Python implementation.
nums = [int(i) for i in input().split()]

# Guaranteed having two mismatches one after another.
for i, n in enumerate(nums):
    if n % 2 != nums[i - 1] % 2:
        first_mismath = i + 1
        break

# If first_mismatch occurs at the 0 index, two possibilities.
if first_mismath == 1:
    if nums[0] % 2 == nums[1] % 2:
        first_mismath = len(nums)

print(first_mismath)
