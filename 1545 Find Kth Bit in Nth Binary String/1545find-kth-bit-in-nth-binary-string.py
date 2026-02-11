class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # lenght=2**n -1
        # def helper(lenght,k): 
        #     if lenght==1:
        #         return "0"
        #     half=lenght//2
        #     if k<=half:
        #         return helper(half,k)
        #     elif k> half+1:
        #        res= helper(half,1+lenght-k)

        #        return "0" if res=="1" else "1"
        #     else:
        #         return "1"    
        # return helper(lenght,k)   

        # lenght=2**n-1
        # inverted=False
        # while lenght>1:
        #     half=lenght//2
        #     if k<=half:
        #         lenght=half
        #     elif k>half+1:
        #         k=1+lenght-k
        #         lenght=half
        #         inverted= not inverted
        #     else:
        #         return "1" if not inverted else "0"   
        # return "0" if not inverted else "1"         

        length=2**n -1
        inverted=False
        def helper(length ,k ,inverted):
            if length==1:
                return "0" if not inverted else "1"
            half=length//2
            if k<=half:
                return helper(half,k,inverted)
            elif k>half+1:
                return helper(half,1+length-k,  not inverted)
            else:
                return "1" if not inverted else "0"
        return helper(length,k,False)                    
