from helper_functions import timer


def read_file(path: str) -> list:
    """Helper function that reads file.
    """
    data = []
    with open(path) as f:
        for line in f:
            temp_lst = [int(num) for num in line.split()]
            data.append(temp_lst)

    return data


@timer
def max_path_sum(data: list) -> int:
    """Compute the summary of maximun elements is a 
    horizontal neighboring path.

    Notes
    -----
    The `data` is represented in "triangle".

    Parameters
    ----------
    data : `list`

    Returns
    -------
    max_sum : `int`
        Summary of maximum horizontal neighboring elements.
    """
    bottom_triangle = len(data)-2

    # By using Dynamic Programming, starting from the bottom line,
    # compute the maximum value of neighboring values and add them
    # to the upper level value.
    for i in range(bottom_triangle, -1, -1):
        for j in range(i + 1):
            max_val = max(data[i+1][j], data[i+1][j+1])
            data[i][j] += max_val

    assert(len(data[0]) == 1)
    max_sum = int(data[0][0])

    return max_sum


if (__name__ == "__main__"):
    PATH = "Pr018_numbers.txt"
    ANS = 1074

    fData = read_file(PATH)
    ans = max_path_sum(fData)
    assert(ans == ANS)
    print(f"Problem 18 answer is {ans}")
