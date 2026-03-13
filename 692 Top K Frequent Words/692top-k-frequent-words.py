class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # count=Counter(words)
        # heap=[]
        # for w,f in count.items():
        #     heapq.heappush(heap,(-f,w))
         
        # res=[]
        # for w in range(k):
        #     res.append(heapq.heappop(heap)[1])
        # return res  
        

        table = defaultdict(int)
        for word in words:
            table[word] += 1

        heap_lst = []
        heapq.heapify(heap_lst)

        for key, value in table.items():
            heapq.heappush(heap_lst, (-value, key))

        res = []
        
        for i in range(k):
            _, key = heapq.heappop(heap_lst)
            res.append(key)

        return res
        
        