from helper_functions import timer


def letters_of_number(num: int) -> int:
    """
    Compute the total number of letters for a specific number.

    Note
    ----
    For example, 101 is referenced as "one hundred and one" due
    to british convention
    """
    # In case num < 10, return corresponding word length
    if (num < 20):
        return len(ONE_TO_NINETEEN[num])
    # In case num < 100, split number into 2 digits
    elif (num >= 20 and num < 100):
        dec = int(num/10)
        res = int(num % 10)
        ans = len(TENS[dec]) + len(ONE_TO_NINETEEN[res])
        return ans
    # In case num < 1000, split number accordingly
    elif (num < 1000):
        hun = int(num/100)
        res = int(num % 100)
        ans = len(ONE_TO_NINETEEN[hun]) + len(HUNDRED)
        if (res > 0 and res < 20):
            ans += len(AND) + len(ONE_TO_NINETEEN[res])
        elif (res >= 20):
            dec = int(res/10)
            un = int(res % 10)
            ans += len(AND) + len(TENS[dec]) + len(ONE_TO_NINETEEN[un])
        return ans
    elif (num == 1000):
        return len(THOUSAND)
    else:
        print("Not supported in this version")

    return 0


@timer
def count_number_letters(N: int) -> int:
    """
    Return the total letters for numbers starting from 
    1 to <N>
    """
    count = 0
    for number in range(1, N+1):
        count += letters_of_number(number)
    return count


if (__name__ == "__main__"):

    # Define global lists that contain alphanumeric values
    # of standard numbers
    ONE_TO_NINETEEN = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
                       "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
                       "eighteen", "nineteen"]
    TENS = ["", "", "twenty", "thirty", "forty", "fifty",
            "sixty", "seventy", "eighty", "ninety"]
    AND = "and"
    HUNDRED = "hundred"
    THOUSAND = "onethousand"

    N1, ANS1 = 5, 19
    N2, ANS2 = 1000, 21124
    assert(ANS1 == count_number_letters(N1))
    ans = count_number_letters(N2)
    assert(ANS2 == ans)

    print(f"Problem 17 answer is {ans}")
