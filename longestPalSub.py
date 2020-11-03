# longest palindomic substring


def helper(s, left, right):
    while (left >= 0 and right < len(s)) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1 : right]


def longPal(s):
    res = ""
    for i in range(len(s)):
        test = helper(s, i, i)
        if len(test) > len(res):
            res = test
        test = helper(s, i, i + 1)
        if len(test) > len(res):
            res = test
    return res if len(res) > 1 else "No pal"


string = "racecar"
string1 = "google"
string2 = "sam"

print(longPal(string))
print(longPal(string1))
print(longPal(string2))

