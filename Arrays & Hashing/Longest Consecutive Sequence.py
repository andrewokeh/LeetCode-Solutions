class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_seq = 0
        for num in nums:
            if num - 1 not in num_set:
                next_ = num + 1
                while next_ in num_set:
                    num_set.remove(next_)
                    next_ += 1
                max_seq = max(max_seq, next_ - num)
        return max_seq
