class Solution:

    def isPalindrome(self, x: int) -> bool:
        """Check if given number is a palindrome"""
        """Computational complexity: O(log10(N)) since we only iterate the half of the digits"""
        """Space complexity: O(1) """
        # (0) special cases
        # (0-a) negative number
        if x < 0:
            return False
        # (0-b) last digit is 0, then it is false unless it's 0
        if x % 10 == 0 and x != 0:
            return False

        orig = x
        rev = 0

        # how do we know tht we've reache the half of the number?
        # Stop when the original number is less than the reversed number
        while orig > rev:
            # (1) pop a number from orig
            pop = orig % 10
            orig = orig // 10

            # (2) put into rev
            rev = rev * 10 + pop

        # when length is odd = we get rid of middle number by rev/10
        return orig == rev or orig == rev // 10