def days_since_birthday(birthday):
    """
    Calculates how many days have passed since the given birthday,
    excluding the birth year and current year, while considering leap years.

    :param birthday: String in the format "DD-MM-YYYY"
    :return: Number of days that passed in full years
    """

    # Extract the birth year from the last 4 characters of the string
    birth_year = int(birthday[-4:])  # Convert to integer

    # Ask the user for the current year (since we can't import datetime)
    current_year = int(input("Enter the current year: "))

    # Calculate the number of full years that passed (excluding birth year and current year)
    full_years = current_year - birth_year - 1

    # Count the number of leap years in the full years range
    leap_years = 0
    for year in range(birth_year + 1, current_year):  # Exclude birth & current year
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):  # Leap year check
            leap_years += 1

    # Total days = (normal years * 365) + (leap years * 366)
    total_days = (full_years - leap_years) * 365 + (leap_years * 366)

    return total_days


# Example usage:
print(days_since_birthday("20-08-2003"))
