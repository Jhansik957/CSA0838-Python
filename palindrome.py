def is_palindrome(s):
    s = s.lower()
    cleaned_s = ''.join(char for char in s if char.isalnum())
    return cleaned_s == cleaned_s[::-1]

print(is_palindrome("A man, a plan, a canal: Panama"))  
print(is_palindrome("race a car"))                      
                               
