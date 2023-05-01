testMatrix = [
  [0, 1, 0, 1, 0],
  [1, 0, 1, 0, 1],
  [0, 1, 1, 1, 0],
  [1, 0, 1, 0, 1]
]

directions = [
  [-1, 0], # up
  [0, 1],  # right
  [1, 0],  # down
  [0, -1]  # left
]

def dfs(matrix, current_row, current_col):
    # check boundary for row and col, less than zero and len(matrix)
    if current_row < 0 or current_row >= len(matrix) or \
    current_col < 0 or current_col >= len(matrix[0]):
        return
    
    if matrix[current_row][current_col] == 1:  # flip the cell so that it is not revisited
        matrix[current_row][current_col] = 0
        
        # check all four directions and then increment row and col
        for i in range(len(directions)):
            current_dir = directions[i]
            row = current_dir[0]
            col = current_dir[1]
            dfs(matrix, current_row + row, current_col + col)
            
def number_of_islands(matrix):
    if not len(matrix):   # matrix length is zero, then no islands
        return 0
    
    island_count = 0      # initialize
    for row in range(len(matrix)):          # loop through row of the matrix i.e. matrix
        for col in range(len(matrix[0])):   # loop through col of the matrix i.e. matrix[0]
            if matrix[row][col] == 1:       # when encountering the first instance of a cell with one
                island_count += 1           # increment island count
                dfs(matrix, row, col)       # do recursive dfs
        
    return island_count  # return the total

print(number_of_islands(testMatrix))