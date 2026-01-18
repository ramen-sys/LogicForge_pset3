

def check_palindrome(s):
    if s==s[::-1]:
        return True
    else:
        return False
def longest(s):
    if s[0]==s[-1]:
        if check_palindrome(s):
            return s
        else:
            return None


    else:
        left = longest(s[1:])
        right = longest(s[:-1])

        if len(left) > len(right):
            return (left)
        else:
            return (right)
s=input().lower()
print(longest(s))