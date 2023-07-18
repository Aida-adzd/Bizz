
def main():
    try:
        # Read the number of rows and columns from the user
        row, column = input().split()
        row, column = int(row), int(column)
    except:
        quit()
        # raise ValueError("Invalid input")

    table = list()

    # Read the table data row by row
    for _ in range(row):
        row = [int(x) for x in input().split()]
        if len(row) == column:
            # Append valid rows to the table
            table.append(row)

    # Calculate and print the number of walls in the table
    print(count_walls(table))


def count_walls(table: list):
    # Get the dimensions of the table
    counter = 0
    n = len(table)
    m = len(table[0])

    '''
        For each cell, the function checks the neighboring cells (top, bottom, left, and right) to determine whether the current cell should be spanned or not. 
        Considers table boundaries to handle edge cases properly.
        For example, if it is the first row, there is no element above it to check, so up = table [i][j]
        If it is the last row, there is no element below it to check, so down = table [i][j]
        For each row, the first and last columns are also the same, and there are no elements on the left or right
    '''

    for i in range(n):
        for j in range(m):
            if table[i][j] == 1:
                # Check left cell
                if j > 0 and table[i][j - 1] == 0:
                    counter += 1
                # Check right cell
                if j < m - 1 and table[i][j + 1] == 0:
                    counter += 1
                # Check bottom cell
                if i < n - 1 and table[i + 1][j] == 0:
                    counter += 1
                # Check top cell
                if i > 0 and table[i - 1][j] == 0:
                    counter += 1
            '''
            If the current cell is a wall (table[i][j] == 1), i.e. none of the adjacent cells is a wall (top, bottom, left, or right is 0), the number of walls is incremented accordingly.
            '''

    return counter


if __name__ == '__main__':
    # This code won't run if this file is imported.
    main()
