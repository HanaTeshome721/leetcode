class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #    count=Counter(nums)
    #    heap=[]
    #    for num,frq in count.items():
    #         heapq.heappush(heap,(-frq,num))
    #    res=[]
    #    for i in range(k):
    #         res.append(heapq.heappop(heap)[1])
    #    return res        


    #     count=Counter(nums)
    #     heap=[]
    #     for num,freq in count.items():
    #         heapq.heappush(heap,(freq,num))
    #         if len(heap)>k:
    #             heapq.heappop(heap)
    #     return [num for freq,num in heap]

      cnt=Counter(nums)
      n=len(nums)
      bucket=[[] for i in range(n+1)]

      for i, f in cnt.items():
        bucket[f].append(i)
      ans=[]
      for i in range(len(bucket)-1,-1,-1):
         for n in bucket[i]:
            ans.append(n)
            if len(ans)==k:
                return ans