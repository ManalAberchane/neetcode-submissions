class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for ch in s:
            if ch.isalnum():
                clean += ch.lower()
        return clean == clean[::-1]
        # s = s.lower()
        # s = s.replace(" ", "")
        # for i in range(len(s) // 2):
        #     j = len(s) - 1 - i
        #     if (s[j].isalnum == False): 
        #         s = s[:j] + s[j+1:]
        #         j-=1
        #     if s[i] != s[j]:
        #         return False
        # return True
        