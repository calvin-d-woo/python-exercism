def is_leap_year(year):
    if year < 0:
        raise Exception("Not a valid year. Make it positive!")
    else:
        if (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)):
            return True
        return False
