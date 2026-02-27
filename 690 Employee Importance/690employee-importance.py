"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
       emp={emp.id:emp for emp in employees}
       def dfs(em):
         employ=emp[em]
         importance=employ.importance
         return importance + ( sum(dfs(nig) for nig in employ.subordinates))   
       return dfs(id) 


        # the_dict = dict()
        # for emp in employees: 
        #     the_dict[emp.id] = emp
    
        # def dfs(current_employee):
        #     if current_employee == None:
        #         return 0
                
        #     my_importance = current_employee.importance
        #     for sub in current_employee.subordinates:
        #         my_importance += dfs(the_dict[sub])
        #     return my_importance
        
        # return dfs(the_dict[id])
                

        # adj : Dict[int, 'Employee'] = {i.id: i for i in employees}
        # res = 0
        # q = deque([id])

        # while q:
        #     curr = q.popleft()
        #     employee = adj[curr]
        #     res += employee.importance
        #     # sum all employees importance on same level
        #     for subordinate_id in employee.subordinates:
        #         # add subordinates to be processed at next level
        #         q.append(subordinate_id)
        # return res        
            