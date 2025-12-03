class DataStream:

    def __init__(self, value: int, k: int):
        self.k=k
        self.value=value
        self.q=deque()
        self.cn=0
    def consec(self, num: int) -> bool:
        
        if len(self.q)==self.k:
            n=self.q.popleft()
            if n== self.value:
                self.cn-=1
        self.q.append(num)
        if num==self.value:
            self.cn+=1
        return self.cn==self.k        
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)