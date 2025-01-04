'''
return the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

strs = ["flower","flow","flight"]
Output: "fl"

strs = ["dog","racecar","car"]
Output: ""

'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        j, ans = 0, []
        while True:
            if j == len(strs[0]):
                return ''.join(ans)
            temp = strs[0][j]
            # print("while loop", temp)
            for i in range(1, len(strs)):
                # print("iter", i)
                if j >= len(strs[i]):
                    return ''.join(ans)
                if temp != strs[i][j]:
                    print(strs[i][j])
                    return ''.join(ans)
                # print("ans is ", ans)
            ans.append(temp)
            j += 1
        return ''.join(ans)