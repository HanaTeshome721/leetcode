class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        memo=[0]*len(questions)

        def dfs(i):
            if i>=len(questions):
                return 0
            if memo[i]:
                return memo[i]
            points,brainpower=questions[i]    
            memo[i]=max(dfs(i+1),
                       points + dfs(i+1+brainpower))  
            return memo[i]
        return dfs(0)



