from collections import deque

"""
On an 2 x 3 board, there are five tiles labeled from 1 to 5, and an empty square 
represented by 0. A move consists of choosing 0 and a 4-directionally adjacent 
number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given the puzzle board board, return the least number of moves required so 
that the state of the board is solved. If it is impossible for the state 
of the board to be solved, return -1.
"""
def SlidingPuzzle(board):
    adjacents = {
        0: [1,3],
        1: [0,2,4],
        2: [1,5],
        3: [0,4],
        4: [1,3,5],
        5: [2,4]
    }
    b = "".join([str(c) for row in board for c in row])
    # print(b)
    q = deque([(b.index("0"),b,0)])
    visit = set([b])
    while q:
        i,b,length =  q.popleft()
        print(b[i])

        if b == "123450":
            return length

        b_arr = list(b)
        for j in adjacents[i]:
            # print(j)
            new_b = b_arr.copy()
            new_b[i], new_b[j] = b_arr[j],b_arr[i]
            joined_b = "".join(new_b)
            if joined_b not in visit:
                # print(q)
                q.append((j,joined_b,length+1))
                visit.add(joined_b)
    return -1

board = [[1,2,3],[4,0,5]]
print(SlidingPuzzle(board))