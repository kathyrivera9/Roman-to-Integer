class Solution:
    def romanToInt(self, s: str) -> int:
        hash = {'I': 1, 'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        str = []
        sum = 0
        
        for char in s:
            str.append(char)
            
        i = 0
        while i < (len(str)):
            if(i+1 != len(str) and hash.get(str[i]) < hash.get(str[i+1])):
                sum = sum + (hash.get(str[i+1]) - hash.get(str[i]))
                i = i +2 
            else:
                sum = sum + hash.get(str[i])
                i+=1
        return sum
