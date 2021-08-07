from helper_functions import timer


def read_file(path: str) -> list:
    """Helper function that read and split names from 
    appropriate filepath.
    """
    with open(path) as f:
        data = f.read()

    names = data.split(",")
    return names


def alphabet_cost() -> dict:
    """Creates alphanum values. 
    """
    capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n_of_letters = len(capital_letters)
    alphabet = {capital_letters[i]: i+1 for i in range(n_of_letters)}
    alphabet['"'] = 0

    return alphabet


@timer
def count_names_score(names: list) -> int:
    """Compute the sum of alphabetical values for each name in <names> list by
    multiply aforementioned value with its alphabetical position in the list.
    """
    # Sort <names> list in respect to alphanumeric values
    # in ascending order
    names_sorted = sorted(names)
    ans = 0

    for i, capital_name in enumerate(names_sorted):
        letter_sum = sum(ALPHABET[letter] for letter in capital_name)
        ans += (i+1)*letter_sum

    return ans


if (__name__ == "__main__"):
    ALPHABET = alphabet_cost()
    ANS = 871198282
    FPATH = "Pr022_names.txt"

    names = read_file(FPATH)
    ans = count_names_score(names)
    print(f"Problem 22 answer is {ans}")
    assert(ans == ANS)
