class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
       
        # if not needle:
        #     return 0
        # return haystack.find(needle)

        # if needle=="":
        #     return 0
        # for i in range(len(haystack) + 1 -len(needle)):
        #     if haystack[i:i+len(needle)] ==needle:
        #         return i
        # return -1        


        
        MOD = 10**9 + 7
        base = 27

        # Convert character to number
        # a -> 1, b -> 2, ..., z -> 26
        def convert(char):
            return ord(char) - 96

        # Add character to the end of the rolling hash
        def add_last(Hash, char):
            return (Hash * base + convert(char)) % MOD

        # Remove the first character contribution
        def poll_first(Hash, char, base_power):
            return (Hash - convert(char) * base_power) % MOD

        N1, N2 = len(haystack), len(needle)

        # If needle is longer than haystack
        if N1 < N2:
            return -1

        # Precompute powers of base
        base_powers = [1] * (N2 + 1)

        for i in range(1, N2 + 1):
            base_powers[i] = (base_powers[i - 1] * base) % MOD

        target = 0
        window_hash = 0

        # Compute hash of needle
        for char in needle:
            target = add_last(target, char)

        # Compute hash of first window
        for i in range(N2):
            window_hash = add_last(window_hash, haystack[i])

        # Check first window
        if window_hash == target:
            if haystack[:N2] == needle:
                return 0

        # Slide the window
        for right in range(N2, N1):

            # Leftmost character index
            left = right - N2

            # Add new character
            window_hash = add_last(window_hash, haystack[right])

            # Remove old character
            window_hash = poll_first(
                window_hash,
                haystack[left],
                base_powers[N2]
            )

            # Compare hashes
            if window_hash == target:

                # Verify actual substring
                if haystack[left + 1:right + 1] == needle:
                    return right - N2 + 1

        return -1    
