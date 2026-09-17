class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        row={
        1:"qwertyuiop",
        2:"asdfghjkl",
        3:"zxcvbnm"}
        ans=[]
        for word in words:
            r1,r2,r3=0,0,0
            for c in word.lower():
                print(c)
                if c in row[1]:
                    r1=1
                elif c in row[2]:
                    r2=2
                else:
                    r3=3
            print(r1,r2,r3)        
            if(r1==1 and r2==0 and r3==0) or (r1==0 and r2==2 and r3==0) or (r1==0 and r2==0 and r3==3):
                ans.append(word)
        return ans        
