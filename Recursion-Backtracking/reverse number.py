# def reversenumber(n):
#     rev = 0
#     while n > 0:
#         remainder = n % 10
#         rev = rev * 10 + remainder
#         n = n // 10
#     return rev
#
#
# n = 1234
# print(reversenumber(n))


def reversenumber(n):
    ns = ""
    for i in range(len(n) -1,-1,-1):
        ns += n[i]
    return ns

n = "hello"
print(reversenumber(n))