class Solution(object):
    def subset(self,arr):
        result = []
        if not arr:
            result.append(arr)
        else:
            first = arr[0]
            second = arr[1:]
            for x in self.subset(second):
                result.append(x)
                c = [first] + x
                result.append(c)
        return result

sol = Solution()
print(sol.subset([1, 5, 11, 5]))
        