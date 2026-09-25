class FrequencyTracker:

    def __init__(self):
            self.frq={}
            self.frqfq=defaultdict(int)        

    def add(self, number: int) -> None:
        if number in self.frq:
           old= self.frq[number]
           self.frq[number]+=1
           self.frqfq[old+1]+=1
           self.frqfq[old]-=1
        else:
            self.frq[number]=1
            self.frqfq[1]+=1   
    def deleteOne(self, number: int) -> None:
            if number not in self.frq:
                return
            cur=self.frq[number]
            if cur==1:
                self.frqfq[1]-=1
                del self.frq[number]
            else:
                self.frq[number]-=1
                self.frqfq[cur-1]+=1
                self.frqfq[cur]-=1        

    def hasFrequency(self, frequency: int) -> bool:
            return self.frqfq[frequency]>0        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)