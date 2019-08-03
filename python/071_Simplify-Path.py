# 简化路径

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        # 使用栈来解决
        stack = []
        path = path.split('/')
        path = [p for p in path if p]
        for x in path:
            if x == '.':
                continue
            elif x == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(x)
        return '/'+'/'.join(stack)

# s = Solution()
# path = input("input: ")
# print(s.simplifyPath(path))