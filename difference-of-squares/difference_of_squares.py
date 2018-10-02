def square_of_sum(count):
    sum_of_count = count * (count + 1) / 2
    return sum_of_count**2


def sum_of_squares(count):
    sum = 0
    for n in range(count):
        sum += (n+1)**2
    return sum


def difference(count):
    return square_of_sum(count) - sum_of_squares(count)
