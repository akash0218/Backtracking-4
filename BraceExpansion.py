# Time Complexity : O(k^(n/k)); k --> average length of the block.
# Space Complexity : O(n);
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
#
#
class Solution:
    def helper(self, groups, index, path):
        # base
        if len(path) == len(groups):
            self.result.append(''.join(path))
            return
        # logic
        for i in groups[index]:
            path.append(i)
            self.helper(groups, index+1, path)
            path.pop()

    def expand(self, s):
        self.result = []
        groups = []
        ptr = 0
        while ptr < len(s):
            if s[ptr] == '{':
                ptr += 1
                temp = []
                while s[ptr] != '}':
                    if s[ptr] != ',':
                        temp.append(s[ptr])
                    ptr += 1
            else:
                temp = [s[ptr]]
            ptr += 1
            temp.sort()
            groups.append(temp)
        self.helper(groups, 0, [])
        return self.result


print(Solution().expand('{b,a,c}de{f,g,h}'))
