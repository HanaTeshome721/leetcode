class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
      count=Counter(nums)
      def customsort(n):
        return (count[n],-n)
      nums.sort(key=customsort)
      return nums  
      