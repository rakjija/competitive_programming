import sys

score_board = (
    (12, 1600),
    (11, 894),
    (11, 1327),
    (10, 1311),
    (9, 1004),
    (9, 1178),
    (9, 1357),
    (8, 837),
    (7, 1055),
    (6, 556),
    (6, 773),
)

N = int(sys.stdin.readline())

print(*score_board[N - 1])
