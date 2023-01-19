class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = min(strs,key = len)
        for index,letter in enumerate(prefix):
            for word in strs:
                if word[index] != letter:
                    return prefix[:index]
        return prefix

# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         prefix = strs[0]
#         for word in range(1,len(strs)):
#             if len(strs[word]) <= len(prefix) and prefix[:len(strs[word])] == strs[word]:
#                 prefix = prefix[:len(strs[word])]
#             for letter in range(min(len(prefix),len(strs[word]))):
#                 if len(strs[word]) == 1 and strs[word][letter] == prefix[letter]:
#                     prefix = prefix[:1]
#                 elif strs[word][letter] == prefix[letter]:
#                     pass
#                 else:
#                     prefix = prefix[:letter]
#                     break
#         return prefix

