def lengthOfLongestSubstring(s):
    length = 0
    left = 0
    char_set = set()

    for right in range(len(s)):
        if s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        length = max(length, (right - left) + 1)

    return length


s = 'abcabcdbb'
n = lengthOfLongestSubstring(s)
print(n)