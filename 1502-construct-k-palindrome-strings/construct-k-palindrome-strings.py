class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # Step 1: Count the frequency of each character
        freq = {}
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        # Step 2: Count how many characters have an odd frequency
        odd_count = 0
        for count in freq.values():
            if count % 2 != 0:
                odd_count += 1

        # Step 3: Check if we can form exactly k palindromes
        # We need the number of odd characters to be less than or equal to k
        return odd_count <= k and k <= len(s)
