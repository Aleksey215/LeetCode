from typing import List
from collections import defaultdict
from functools import reduce


def product_except_self(nums: List[int]) -> List[int]:
    res = list()
    for num in nums:
        tmp = nums[:]
        tmp.remove(num)
        res.append(reduce(lambda x, y: x*y, tmp))
    return res


# Example 1:
nums = [1, 2, 3, 4]
product_except_self(nums=nums)
# answer = [24, 12, 8, 6]

print()

# Example 2:
nums = [-1, 1, 0, -3, 3]
product_except_self(nums=nums)
# answer = [0, 0, 9, 0, 0]
