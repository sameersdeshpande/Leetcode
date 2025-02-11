class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            part_index = s.find(part)
            s = s[:part_index] + s[part_index + len(part) :]
        return s


        