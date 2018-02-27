'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

'''

def longest_substring(str):
    length = len(str)
    start_pos = 0
    result_interval = [0, 0]
    while (start_pos < length):
        old_pos = start_pos
        hash_table = [-1] * 256
        for ii in range(start_pos, length):
            if (hash_table[ord(str[ii])] >= 0):
                if ((result_interval[1] - result_interval[0]) < (ii - start_pos)):
                    result_interval[1] = ii
                    result_interval[0] = start_pos
                start_pos = hash_table[ord(str[ii])] + 1
                break
            else:
                hash_table[ord(str[ii])] = ii

        if (old_pos == start_pos):
            if ((result_interval[1] - result_interval[0]) < (length - start_pos)):
                result_interval[1] = length
                result_interval[0] = start_pos
            break
    return str[result_interval[0]:result_interval[1]]

def longest_substring_1(str):
    length = len(str)
    result_interval = [0, -1]
    hash_table = [0] * 256
    ii = 0
    jj = 0
    while (jj < length):
        ii = max(hash_table[ord(str[jj])], ii)
        if ((result_interval[1] - result_interval[0]) < (jj - ii)):
            result_interval[1] = jj
            result_interval[0] = ii
        hash_table[ord(str[jj])] =  jj + 1
        jj = jj + 1
    return str[result_interval[0]:result_interval[1] + 1]

print (longest_substring("pwwkew"))
print (longest_substring("bbbbb"))
print (longest_substring("abcabcbb"))
print (longest_substring("abcdefghi"))
print (longest_substring("abcabcdefghi"))

print (longest_substring_1("pwwkew"))
print (longest_substring_1("bbbbb"))
print (longest_substring_1("abcabcbb"))
print (longest_substring_1("abcdefghi"))
print (longest_substring_1("abcabcdefghi"))
