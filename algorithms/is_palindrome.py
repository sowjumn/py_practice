class CheckPalindrome:
    def isPalindrome(self, x: int) -> bool:
        num_str = str(x)
        if num_str == num_str[::-1]:
            return True
        else:
            return False
        
num = 12
sol = CheckPalindrome()
print(sol.isPalindrome(num))

num_2 = 141
print(sol.isPalindrome(num_2))