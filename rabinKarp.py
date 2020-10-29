# pattern matching


def hashfn(x):
    xdict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
    x = list(x)
    val = 0
    for i in range(len(x)):
        val = val * 10
        val += xdict[x[i]]
    return val


# print(hashfn("abc"))


def sol(a, b):
    if not a or not b or len(a) < len(b):
        return -1
    x = hashfn(b)
    n = len(b)
    for i in range(len(a) - len(b) + 1):
        # print(a[i : i + n], b)
        if hashfn(a[i : i + n]) == x:
            if a[i : i + n] == b:
                return i
    return -1


x = "aaaaaabc"
p = "abc"
p2 = "cba"
print(sol(x, p))
print(sol(x, p2))
