from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()  # Sort the array
        closest_sum = float('inf')  # Initialize closest sum to infinity
        n = len(nums)

        for i in range(n - 2):  # First number
            left, right = i + 1, n - 1  # Two-pointer setup
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # Update closest sum if the current sum is closer to the target
                if abs(target - current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum
                
                # Move pointers based on the sum comparison
                if current_sum < target:
                    left += 1  # Increase sum by moving left forward
                elif current_sum > target:
                    right -= 1  # Decrease sum by moving right backward
                else:
                    return current_sum  # Exact match, return immediately
        
        return closest_sum
