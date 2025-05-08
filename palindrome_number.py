class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)  # Convert integer to string
        n = len(s)  # Get length of the string
        left = 0    # Initialize left pointer
        right = n - 1  # Initialize right pointer
        
        while left < right:
            if s[left] != s[right]:  # Compare characters
                return False  # Return False if not a palindrome
            left += 1  # Move left pointer to the right
            right -= 1  # Move right pointer to the left
        
        return True  