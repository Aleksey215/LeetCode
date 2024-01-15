from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    """
    Check array on duplicates
    Args:
        nums (List[int]): input array

    Returns:
        bool: result of checking
    """
    # if len(set(nums)) != len(nums):
    #     return True
    # else:
    #     return False
    # seen = set()

    # for i in range(len(nums)):
    #     if nums[i] in seen:
    #         return True
    #     seen.add(nums[i])

    # return False
    return len(nums) != len(set(nums))


print(
    contains_duplicate([1, 2, 3, 1])
)

print(
    contains_duplicate([1, 2, 3, 4])
)

print(
    contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
)
