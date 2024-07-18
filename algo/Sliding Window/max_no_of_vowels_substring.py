# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

# Example 1:

# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.
# Example 2:

# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.
# Example 3:

# Input: s = "leetcode", k = 3
# Output: 2
# Explanation: "lee", "eet" and "ode" contain 2 vowels.

#sliding window
def max_no_of_vowels_substring(s, k):
    vowel_map = {
        'a': True,
        'e': True,
        'i': True,
        'o': True,
        'u': True 
    }
    
    i = 0
    j = 0
    max_vowel = 0
    vowel_count_window = 0
    while j < len(s):
        if j-i+1<=k:
            if s[j] in vowel_map:
                vowel_count_window += 1
            j += 1
        else:
            max_vowel = max(max_vowel, vowel_count_window)
            if s[i] in vowel_map:
                vowel_count_window -=1
            i += 1
    return max(vowel_count_window, max_vowel)


    


s = "weallloveyou"
k = 7
print(max_no_of_vowels_substring(s, k))