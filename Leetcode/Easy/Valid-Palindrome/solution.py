#Built-in Function by using alnum()
class Solution(object):
    def isPalindrome(self, s):
        newStr = ""
        for i in s:
            if i.isalnum():
                newStr+=i.lower()
        return newStr == newStr[::-1]
    

#Create helper function to detect alphanumeric values
class Solution(object):
    def isPalindrom(self,s):
        l,r = 0,len(s)-1
        while l<r:
            while l<r and not self.isAlphaNum(s[l]):
                l+=1
            while r>l and not self.isAlphaNum(s[r]):
                r-=1
            if s[l].lower() != s[r].lower(r):
                return False
            l,r = l+1,r+1
        return True
    
    def isAlphaNum(self,c):
        return (ord("A")<=ord(c)<=ord("Z") or ord("a")<=ord(c)<=ord("z") or ord(0)<=ord(c)<=ord(9))