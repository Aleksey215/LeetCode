from typing import List
from collections import defaultdict


def topKFrequent(nums: List[int], k: int) -> List[int]:
    res = list()
    tmp_dict = defaultdict(int)
    for num in nums:
        tmp_dict[num] += 1
    sorted_items = sorted(
        tmp_dict.items(), key=lambda item: item[1], reverse=True
    )
    for item in sorted_items[:k]:
        res.append(item[0])
    return res


nums = [1, 1, 1, 2, 2, 3]
k = 2
print(topKFrequent(nums=nums, k=k))

nums = [1]
k = 1
print(topKFrequent(nums=nums, k=k))
