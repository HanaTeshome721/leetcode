class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
# cp
        result = "1"
        for _ in range(1, n):
            current = ""
            count = 1
            for j in range(1, len(result)):
                if result[j] == result[j - 1]:
                    count += 1
                else:
                    current += str(count) + result[j - 1]
                    count = 1
            current += str(count) + result[-1]
            result = current

        return result
