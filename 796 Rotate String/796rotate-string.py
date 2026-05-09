class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        double=s+s    
        return double.find(goal)!=-1

        # l=len(s)

        # for _ in range(l):
        #     s=s[1:] + s[0]
        #     if s==goal:
        #         return True
        # return False      


