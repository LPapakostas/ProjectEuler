from helper_functions import timer


def days_of_month(month: str, year: int) -> int:
    """
    Returns the number of days of a month for 
    specific year.
    """
    if (month in DAYS_31):
        return 31
    if (month in DAYS_30):
        return 30
    # If month == "February", need to check whether
    # the specific year is leap
    is_leap = (year % 400 == 0) and (year % 4 == 0)
    if is_leap:
        return 29

    return 28


@timer
def count_sundays(start_year: int, end_year: int) -> int:
    """
    Counts how many Sundays fell on the first of the month 
    during given start and end year.
    """
    # Initialize Helper variables
    sundays = 0
    week_days = 0
    YEARS = [year for year in range(start_year, end_year + 1)]

    for year in YEARS:
        for month in MONTHS:
            month_days = days_of_month(month, year)
            for day in range(1, month_days+1):
                # Obtain current day, in respect to week
                current_day = DAYS[week_days]
                # Check if it is the first Sunday of the month
                # and update the counter
                is_sunday = ((current_day == "Sunday") and (day == 1)
                             and (year != START_YEAR))
                if is_sunday:
                    sundays += 1
                week_days += 1
                # Reset days of week counter
                if (week_days == len(DAYS)):
                    week_days = 0

    return sundays


if (__name__ == "__main__"):
    # Define Global Helper identifiers
    DAYS = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']
    MONTHS = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    DAYS_31 = ['January', 'March', 'May',
               'July', 'August', 'October', 'December']
    DAYS_30 = ['April', 'June', 'September', 'November']

    START_YEAR = 1900
    END_YEAR = 2000
    ANS = 172

    ans = count_sundays(START_YEAR, END_YEAR)
    assert(ANS == ans)
    print(f"Problem 19 answer is {ans}")
