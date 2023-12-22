# is the number palindrome, meaning is it the same when read from left to right and
# when read from right to left like 121, 11 and 33 or not
# like 10 or -121 or 32
# the input should be an integer and the return should be a boolean value
class palindrome:
    def ispalindrome(self, x: int)-> bool:
        if x<0:
            return False
        div = 1
        while x >= 10 * div:
            div *= 10
        while x:
            # the loop will execute as long as the number remains non-zero.
            # If x becomes 0, the loop will cease, as 0 is considered a falsy value in Python.
            right = x % 10
            left = x // div # double slash is how we divide an integer in python
            if left != right: return False

            x = (x%div) // 10
            div = div/100
        return True

pal = palindrome()
result = pal.ispalindrome(10)
print(result)

# when implemented in leetcode this is the code i used
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool

         """
        if x < 0:
            return False
        div = 1
        while x >= 10 * div:
            div *= 10
        while x:

            right = x % 10
            left = x // div
            if left != right: return False

            x = (x % div) // 10
            div = div / 100
        return True

