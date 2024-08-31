def roman_to_int(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(len(s)):
        if i > 0 and roman[s[i]] > roman[s[i - 1]]:
            result += roman[s[i]]-2
        else:
            result += roman[s[i]]
    return result

# Test Case 1
print(roman_to_int("IV"))

# Test Case 2
print(roman_to_int("IX"))  
