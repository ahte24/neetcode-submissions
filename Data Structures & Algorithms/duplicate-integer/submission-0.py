class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        frequency_dict = {}
        for item in nums:
            frequency_dict[item] = frequency_dict.get(item, 0) + 1
        for key, value in frequency_dict.items():
            if value > 1:
                return True
        return False

        