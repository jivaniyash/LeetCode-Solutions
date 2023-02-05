import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        f = ''
        for ch in string.punctuation:
            s = s.replace(ch,'')
        s = s.replace(' ','').lower()
        print(s)
        return s[::] == s[::-1]