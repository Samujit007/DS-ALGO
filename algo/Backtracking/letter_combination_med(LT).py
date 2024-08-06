def solve(idx, s, temp, map_t, result):
    if idx >= len(s):#index out of bounds
        result.append(''.join(temp))
        return
    ch = map_t[s[idx]]
    for i in range(len(ch)):
        temp.append(ch[i])
        comb = solve(idx+1, s, temp, map_t, result)
        
        temp.pop()

def letter_comb(digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
             return []
        temp = []
        map_t = {
            "1":"000",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        result = []
        solve(0, digits, temp, map_t, result)
        return result

digits = ""
result = letter_comb(digits)
print(result)
#====================================================================

# map = {
#         "2": "abc",
#         "3": "def",
#         "4": "ghi",
#         "5": "jkl",
#         "6": "mno",
#         "7": "pqrs",
#         "8": "tuv",
#         "9": "wxyz"
#     }
# result = []
# def solve(idx, s, temp):
#     if idx >= len(s):#index out of bounds
#         result.append(''.join(temp))
#         return
#     ch = map[s[idx]]
#     for i in range(len(ch)):
#         temp.append(ch[i])
#         solve(idx+1, digits, temp)
#         temp.pop()


# def letter_comb(digits):
#     temp = []
#     solve(0, digits, temp)
#     pass


# digits = "234"
# letter_comb(digits)
# print(result)