class Solution:
    def convertToBase7(self, num: int) -> str:
        # If the number is 0, return "0"
        if num == 0:
            return "0"
        
        # Determine if the number is negative
        negative = num < 0
        num = abs(num)
        
        # List to store the digits of the base 7 number
        digits = []
        
        # Convert the number to base 7 by dividing by 7 and storing remainders
        while num:
            digits.append(str(num % 7))
            num //= 7
        
        # If the number was negative, add the minus sign
        if negative:
            return '-' + ''.join(digits[::-1])
        
        # Join the digits to form the final base 7 number string
        return ''.join(digits[::-1])
