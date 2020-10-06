#https://leetcode-cn.com/problems/fizz-buzz/

class Solution:
    def fizzBuzz(self, n: int) -> 'List[str]':
        result = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:#同时可以被3和5整除
                result.append('FizzBuzz')
            elif i % 3 == 0:
                result.append('Fizz')#只能被3整除
            elif i % 5 == 0:
                result.append('Buzz')#只能被5整除
            else:
                result.append(str(i))#既不能被3整除，也不能被5整除
        return result


if __name__ == '__main__':
    S = Solution()
    result = S.fizzBuzz(15)
    print(result)