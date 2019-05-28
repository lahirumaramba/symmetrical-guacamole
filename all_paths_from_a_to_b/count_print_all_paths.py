mat = [ [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9] ]

rows = len(mat)
cols = len(mat[0])

#print(rows, cols)
#print(mat[rows-1][cols-1])

W = rows-1
O = cols-1

dp = [[0 for i in range(cols)] for j in range(rows)]

def isValid(row, col):
    return row >= 0 and row < rows and col >= 0 and col < cols

#Time O(N*M)
def find_paths_dp(row, col):
    for r in range(rows):
        for c in range(cols):
            if r == 0 or c == 0:
                dp[r][c] = 1
                continue
            dp[r][c] = dp[r-1][c] + dp[r][c-1]


find_paths_dp(0, 0)
for a in dp:
    print(a)

print("--------")

path = []

#Time (2^n) Exponential
def find_paths(row, col, row_dest, col_dest):
    if col == row_dest and row == col_dest:
        path.append(mat[row][col])
        print(path)
        path.pop(-1)
        return

    path.append(mat[row][col])

    if isValid(row+1, col): #down
        find_paths(row+1, col, row_dest, col_dest)

    if isValid(row, col+1): #right
        find_paths(row, col+1, row_dest, col_dest)

    path.pop(-1)

#find_paths(0, 0, rows-1, cols-1)

#Time (2^n) Exponential
def find_paths_to(row, col):
    if col == 0 and row == 0:
        path.append(mat[row][col])
        print(path)
        path.pop(-1)
        return

    path.append(mat[row][col])

    if isValid(row-1, col): #down
        find_paths_to(row-1, col)

    if isValid(row, col-1): #right
        find_paths_to(row, col-1)

    path.pop(-1)

#find_paths_to(rows-1, cols-1)

#DP print all paths
dp_path = [[[] for c in range(cols)] for r in range(rows)]

def print_paths_dp(row, col):
    for r in range(rows):
        for c in range(cols):
            if c == 0 and r == 0:
                dp_path[r][c] = [[mat[r][c]]]
                continue
            if c == 0 and r > 0:
                dp_path[r][c] = [dp_path[r-1][c][0] + [mat[r][c]]]
                continue
            if c > 0 and r == 0:
                dp_path[r][c] = [dp_path[r][c-1][0] + [mat[r][c]]]
                continue

            ps = []
            for p in dp_path[r][c-1]:
                ps += [p + [mat[r][c]]]
            dp_path[r][c] += ps

            ps = []
            for p in dp_path[r-1][c]:
                ps += [p + [mat[r][c]]]
            dp_path[r][c] += ps

print_paths_dp(0, 0)
#for a in dp_path:
#    print(a)

for path in dp_path[rows-1][cols-1]:
    print(path)
