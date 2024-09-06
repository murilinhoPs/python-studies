from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    hash_map = {}

    for index, value in enumerate(nums):
        if hash_map.get(value) is not None:
            return [hash_map.get(value), index]
        hash_map[target-value] = index


print(two_sum([3, 2, 4], 6))
