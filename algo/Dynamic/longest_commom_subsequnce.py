# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

 

# Example 1:

# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.
# Example 2:

# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
# Example 3:

# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.

def solve(text1, text2, i, j,mem):
    if i >= len(text1) or j >= len(text2):
        return 0
    if mem[i][j] != -1:
        return mem[i][j]
    if text1[i]==text2[j]:
        mem[i][j] = 1 + solve(text1, text2, 1+i, 1+j, mem)
        return mem[i][j]
    mem[i][j] = max(solve(text1, text2, i, 1+j, mem), solve(text1, text2, i+1, j, mem))
    return mem[i][j]

def longest_common_sunbsequence(text1, text2):
    mem = [[-1 for j in range(1001)] for i in range(1001)]
    return solve(text1, text2, 0, 0, mem)

text1 = "abcde"
text2 = "ace" 

print(longest_common_sunbsequence(text1, text2))