class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # s = s.split()
        # return len(s[-1])
        c = 0
        for i in range(-1,-len(s)-1,-1):
            if s[i] == ' ' and c > 0:
                return c
            elif s[i] == ' ':
                pass
            else:
                c += 1
        return c