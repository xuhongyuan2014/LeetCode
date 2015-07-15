class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        if n==0:
            return False
        while n%2==0:
            n=n/2
        if (n==1):
            return True
        else:
            return False
if __name__=='__main__':
    print(Solution().isPowerOfTwo(1))
