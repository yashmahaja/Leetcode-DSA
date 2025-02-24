def isAnagram(s, t):
    hashmap_s = {}
    hashmap_t = {}

    if len(s) != len(t):
        return False
    for char, char_t in zip(s, t):
        hashmap_s[char] = 1 + hashmap_s.get(char, 0)
        hashmap_t[char_t] = 1 + hashmap_t.get(char_t, 0)

    for key, values in hashmap_s.items():
        # !! Check if value of the key are same, use .get(key, 0) to avoid key error
        # Assume key is not present in another hashmap we'll get 0 which is not equal
        # to hashmap_s[key] hence return false
        if hashmap_s[key] != hashmap_t.get(key, 0):
            return False
    return True