class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        cn=0
        l=0
        r=len(people)-1
        while l<=r:
            sm=people[l]+people[r]
            if sm<=limit:
                r-=1
                l+=1
            else:
                r-=1
            cn+=1

        return cn
            