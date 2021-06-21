from helper_functions import timer

@timer
def find_digit_sum_from_data(N: int, data: list) -> int:
    """ 
    
    Parameters
    ----------
    N : `int`
        Requested digits. 
    data : `list`
        Data with a number at each row.
        
    Returns
    -------
    n_digit_num : `int`
        <N> digit summary value of all existing numbers.
    """
    LIMIT = N + 1
    digit_sum = 0
    
    for dataline in data:
        digit_sum += int(dataline[:LIMIT])
    
    n_digit_num = str(digit_sum)[:N]
    return int(n_digit_num)
    
def read_file(path: str) -> list:
    """Helper function that reads file.
    """
    with open(path) as f:
        data = list(f.read().splitlines())
        
    return data

if (__name__ == "__main__"):
    PATH = "Pr013_numbers.txt"
    N, ANS = 10, 5537376230
    
    fData = read_file(PATH)
    ans = find_digit_sum_from_data(N,fData)
    assert(ans == ANS)
    print(f"Problem 13 answer is {ans}")
    