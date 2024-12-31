class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        
        for s in strs:
            # Sort the string and use it as the key
            sorted_str = ''.join(sorted(s))
            
            # Check if the sorted string is already a key in the dictionary
            if sorted_str not in anagram_map:
                anagram_map[sorted_str] = []
            
            # Append the original string to the list corresponding to the sorted key
            anagram_map[sorted_str].append(s)
        
        # Return all the lists of anagrams as output
        return list(anagram_map.values())

# Example usage
solution = Solution()