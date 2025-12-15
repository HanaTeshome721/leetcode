class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # s[:]=s[::-1]

        # s.reverse()


        # l=0
        # r=len(s)-1
        # while r>l:
        #     s[r],s[l]=s[l],s[r]
        #     l+=1
        #     r-=1

        def rev(l,r):
            if l>r:
                return
            s[l],s[r]=s[r],s[l]
            return rev(l+1,r-1)
        rev(0,len(s)-1)             
        