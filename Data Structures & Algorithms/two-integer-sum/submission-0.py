class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i, n in enumerate(nums):
            indices[n] = i

        for i, n in enumerate(nums):
            value = target - n
            if value in indices and indices[value] != i:
                return [i, indices[value]]