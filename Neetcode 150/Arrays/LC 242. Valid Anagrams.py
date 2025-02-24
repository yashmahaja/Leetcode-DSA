def isAnagram(s,t):
    s_dict = {}
    t_dict = {}

    if len(s) != len(t):
        return False

# 1st approach sort both string and compare
# 2nd Approach use only one dictionary increment count by one looping on s and then
# decrement while looping on another string t, check if count != 0 return False

    for i in range(len(s)):
        # cant iterate directly on string need range
        s_dict[s[i]] = 1 + s_dict.get(s[i],0)
        t_dict[t[i]] = 1 + t_dict.get(t[i],0)

    return s_dict == t_dict


# s = "anagram"
# t = "nagaram"
s = "rat"
t = "car"
print(isAnagram(s,t))