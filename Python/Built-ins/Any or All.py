n,nums = input(),input().split()
print(any(list(map(lambda x: x == x[::-1] ,nums))) and all(list(map(lambda x: int(x)>=0 ,nums))))

# Alternative solution (by mpiele)
def is_palindrome(num):
    # Convert the number to a string and check if it's equal to its reverse
    return str(num) == str(num)[::-1]

def check_conditions(n, nums):
    # Check if all numbers are positive
    if all(num > 0 for num in nums):
        # Check if any number is a palindrome
        if any(is_palindrome(num) for num in nums):
            return True
    return False

# Read input values
n = int(input())
nums = list(map(int, input().split()))

# Check conditions and print the result
print(check_conditions(n, nums))
