class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        if '*' not in p:
            return s == p
        
        psub = p.split('*')
        if len(psub) != 2:
            return False
        
        s1 = psub[0]
        s2 = psub[1]
        n1, n2 = len(s1), len(s2)
        
        i = 0
        while i <= len(s) - n1:
            x = s[i:i+n1]
            if x == s1:
                j = i + n1
                while j <= len(s) - n2:
                    y = s[j:j+n2]
                    if y == s2:
                        return True
                    j += 1
            i += 1
        return False