from helper_functions import timer


def read_file(file_path: str) -> list:
    """
    Helper function that reads an array-like file
    and returns it as a list of lists.
    """
    number_array = []
    # Read the lines of file.
    with open(file_path) as f:
        lines = f.readlines()

    # For each line, save the number contents.
    for l in lines:
        num_lst = [int(x) for x in l.split()]
        number_array.append(num_lst)

    return number_array


@timer
def find_adjacent_product(N: int, data: list) -> int:
    """
    Finds the greatest product of N adjacent numbers
    in the same direction (up, down, left, right, or diagonally)

    Parameters
    ----------
    N : `int`
      Number of adjacent elements
    data : `list`
      List of numbers

    Returns
    -------
    Maximum adjacent product 
    """
    # Define array limits and initial product value
    rows = len(data)
    columns = len(data[0])
    max_product = -1

    for row in range(rows):
        for col in range(columns):
            # Define flags about possible directions for specific element
            up_flag = (row-N > 0)
            down_flag = (row+N < rows+1)
            left_flag = (col-N > 0)
            right_flag = (col+N < columns+1)

            # Define possible routes (cross)
            dx, dy = 0, 0
            if up_flag:
                dx, dy = -1, 0
            if down_flag:
                dx, dy = 1, 0
            if left_flag:
                dx, dy = 0, -1
            if right_flag:
                dx, dy = 0, 1

            # Define possible routes (diagonal)
            if (down_flag and right_flag):
                dx, dy = 1, 1
            if (up_flag and left_flag):
                dx, dy = -1, -1
            if (up_flag and right_flag):
                dx, dy = -1, 1
            if (down_flag and left_flag):
                dx, dy = 1, -1

            # Compute the adjacent product and compare it with maximum
            product = 1
            for i in range(N):
                idx_x = row + i*dx
                idx_y = col + i*dy
                product *= data[idx_x][idx_y]

            max_product = max(product, max_product)

    return max_product


if (__name__ == "__main__"):
    FPATH = "Pr011_numbers.txt"
    N, ANS = 4, 70600674

    fData = read_file(FPATH)
    ans = find_adjacent_product(N, fData)
    print(f"Problem 11 answer is {ans}")
    assert(ans == ANS)
