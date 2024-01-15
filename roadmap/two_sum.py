from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    res = list()
    for idx, num in enumerate(nums):
        nums.remove(num)
        if target - num in nums:
            res.append(idx)
        nums.insert(idx, num)
    return res


nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums=nums, target=target))

nums = [3, 2, 4]
target = 6
print(twoSum(nums=nums, target=target))

nums = [3, 3]
target = 6
print(twoSum(nums=nums, target=target))

print()
l = [1, 2, 3]
for i in l:
    print(l[i::])
