283. Move Zeroes

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = 0
        
        while left < len(nums):
            if nums[left] != 0:
                # Swap nums[left] and nums[right]
                nums[left], nums[right] = nums[right], nums[left]
                right += 1
            left += 1

# Example usage:
nums1 = [0, 1, 0, 3, 12]
sol = Solution()
sol.moveZeroes(nums1)
print(nums1)  # Output: [1, 3, 12, 0, 0]

nums2 = [0]
sol.moveZeroes(nums2)
print(nums2)  # Output: [0]
  
