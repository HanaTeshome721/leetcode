class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        # Initialize variables
        max_count = 0
        result = -1
        
        # Iterate through the list to find even numbers
        for i in nums:
            if i % 2 == 0:  # Check if the number is even
                count = 0
                
                # Count occurrences of the current number
                for j in nums:
                    if j == i:
                        count += 1
                
                # Update result if the current number has higher frequency
                # or if there's a tie, choose the smaller number
                if count > max_count or (count == max_count and i < result):
                    max_count = count
                    result = i
        
        return result
