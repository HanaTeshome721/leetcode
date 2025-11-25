class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q = deque(range(len(tickets)))
        res = 0
        while True:
            i = q.popleft()
            tickets[i] -= 1
            res += 1

            if i == k and tickets[i] == 0:
                return res

            if tickets[i] > 0:
                q.append(i)
        

