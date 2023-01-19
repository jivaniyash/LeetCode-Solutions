class Solution:
    def romanToInt(self, s: str) -> int:
        self.dict1 = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        self.dict2 = {'IV':4,'IX' : 9,'XL':40,'XC':90,'CD':400,'CM':900} 
        number = 0
        i = 0
        while i < len(s):
            if s[i:i+2] in self.dict2:
                #print(s[i:i+2],self.dict2[s[i:i+2]])
                number += self.dict2[s[i:i+2]]
                i += 2
            else:
                number += self.dict1[s[i]]
                #print(s[i],self.dict1[s[i]])
                i += 1 
        return number