class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_set = {}
        for count, num1 in enumerate(nums):
            num2 = target - num1

            if num2 in num_set:
                return [num_set[num2], count]
                
            num_set[num1] = count
