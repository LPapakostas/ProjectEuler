from helper_functions import timer


def read_file(path: str) -> list:
    """Helper function that returns data 
    from file.
    """
    newline = '\n'
    with open(path, "r") as f:
        data = list(f.read())
    while(newline in data):
        data.remove(newline)

    return data


@timer
def find_largest_series_product(N: int, data: list) -> int:
    """Find the largest product of adjucent one digit
    numbers.

    Parameters
    ----------
    N : `int`
        Adjucent numbers length.

    data : `list`
        Data that need to be processed. 

    Returns
    -------
    max_value : `int`
        Largest adjucent number product
    """
    # Find all values that obtained from
    # adjacent numbers.
    adj_values = []
    for i in range(0, len(data) - N):
        temp_value = 1
        temp_lst = data[i:i+N]
        for num in temp_lst:
            temp_value *= int(num)
        adj_values.append(temp_value)

    max_value = max(adj_values)
    return max_value


if (__name__ == "__main__"):
    N1, ANS1 = 4, 5832
    N2, ANS2 = 13, 23514624000

    fname = "Pr008_numbers.txt"
    data_pr8 = read_file(fname)

    assert(find_largest_series_product(N1, data_pr8) == ANS1)
    ans = find_largest_series_product(N2, data_pr8)
    print(f"Problem 8 answer is {ans}")
    assert(ans == ANS2)
