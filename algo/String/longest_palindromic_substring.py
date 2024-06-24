def longestPalindromicSubstring(str_1):
    longest_palindrome = ""
    for idx in range(len(str_1)): 
        if idx == 0 :
            longest_palindrome = str_1[idx]
        else: 
            current_palindrome = str_1[idx]
            if len(current_palindrome) > len(longest_palindrome):
                longest_palindrome = current_palindrome    
            left_idx = idx-1
            right_idx = idx+1
            if right_idx == len(str_1):
                if str_1[idx] == str_1[idx-1]:
                    current_palindrome = str_1[idx-1:idx+1]
                    if len(current_palindrome) > len(longest_palindrome):
                        longest_palindrome = current_palindrome 
                break 
            while str_1[left_idx] == str_1[right_idx]:
                current_palindrome = str_1[left_idx:right_idx+1]
                left_idx -= 1
                right_idx += 1
                if left_idx == -1 or right_idx == len(str_1):
                    break
                pass
            if str_1[idx] == str_1[idx-1]:
               left_idx = idx-2
               right_idx = idx+1
               if left_idx != -1:
                    while str_1[left_idx] == str_1[right_idx]:
                        current_palindrome = str_1[left_idx:right_idx+1]
                        left_idx -= 1
                        right_idx += 1
                        if left_idx == -1 or right_idx == len(str_1):
                            break
                        pass  
            if len(current_palindrome) > len(longest_palindrome):
                longest_palindrome = current_palindrome    
        pass
    
    return longest_palindrome
str_1 =  "abcdefghfedcbaa"#"abcdefgfedcbazzzzzzzzzzzzzzzzzzzz"#"abaxyzzyxf"

print(longestPalindromicSubstring(str_1))