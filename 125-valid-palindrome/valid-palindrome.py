class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = re.sub(r'[^A-Za-z0-9]+', '', s).lower()
        revStr = string[::-1]

        return string == revStr