# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

# The test cases are generated so that the length of the output will never exceed 105.

 

# Example 1:

# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# Example 2:

# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# Example 3:

# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"

def decode_string(s):
    _map = {"]":"["}
    number_map = {
        "1":1,
        "2":2,
        "3":3,
        "4":4,
        "5":5,
        "6":6,
        "7":7,
        "8":8,
        "9":9,
        "0":0
    }
    stk = []
    for idx in range(len(s)):
        if s[idx] not in _map:
            stk.append(s[idx])
        else:
            sub_out = ''
            while stk and stk[-1] != _map[s[idx]]:
                sub_out = stk.pop() + sub_out
            ignored_open = stk.pop()
            number = ''
            while stk and stk[-1] in number_map:
                number = stk.pop() + number
            for idx in range(int(number)):
                stk.append(sub_out)
    return "".join(stk)


s = "2[Coding]"
#"2[abc]3[cd]ef"
#"3[a]2[bc]"#"3[a2[c]]"
#"3[a]2[bc]"

print(decode_string(s))