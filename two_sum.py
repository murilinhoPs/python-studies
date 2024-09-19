from typing import List


def two_sum(nums: List, target: int):
    hash_map = {}
    for index, value in enumerate(nums):
        if hash_map.get(value):
            return {"indexes": [hash_map.get(value), index],
                    "numbers": [nums[hash_map.get(value)], nums[index]]}
        hash_map[target - value] = index


print(two_sum([11, 15, 7, 2], 9))
