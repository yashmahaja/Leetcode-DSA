def generateParenthesis(n: int):
    stk = []
    res = []

    def backtrack(openc, closec):
        if openc == closec == n:
            res.append("".join(stk))
            return

        if openc < n:
            stk.append("(")
            backtrack(openc + 1, closec)
            stk.pop()

        if closec < openc:
            stk.append(")")
            backtrack(openc, closec + 1)
            stk.pop()

    backtrack(0, 0)
    return res


n = 3
print(generateParenthesis(n))
