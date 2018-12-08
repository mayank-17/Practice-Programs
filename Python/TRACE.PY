def get_diagnols(grid, bltr = False):
    dim = len(grid)
    assert dim == len(grid[0])
    return_grid = [[] for total in range(2 * len(grid) - 1)]
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if bltr:
                return_grid[row + col].append(grid[col][row])
            else:
                return_grid[col - row + (dim - 1)].append(grid[row][col])
    return return_grid

test = int(input())
for i in range(test):
    mat_len = int(input())
    mat = []
    for j in range(mat_len):
        row = list(map(int,input().split()))
        mat.append(row)
    # print(mat)
    myList = get_diagnols(mat)
    for i in range(len(myList)):
        myList[i] = sum(myList[i])
    print(max(myList))