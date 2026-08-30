def valid_palindrome(palindrome):
    refine_palindrome = []
    for ch in palindrome:
        if ch.isalnum():            
            refine_palindrome.append(ch.lower())
    left = 0
    right = len(refine_palindrome) - 1
    while left < right:
        if refine_palindrome[left] == refine_palindrome[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

print(valid_palindrome("A man, a plan, a canal: Panama"))  # True
print(valid_palindrome("race a car"))                       # False
print(valid_palindrome(" "))                                # True
print(valid_palindrome("a"))                                # True