# for an array, calculate the sum of the series

def sum_of_series(s):

    subt = 0

    for i in s:
        subt += s[i]

    return subt


def diff_of_series(a, b):

    # sum_a = sum_of_series(a)
    # sum_b = sum_of_series(b)
    sum_a = sum(a)
    sum_b = sum(b)

    if sum_b >= sum_a:
        return sum_b - sum_a
    else:
        return sum_a - sum_b


def compare_series(a, b):

    # sum_a = sum_of_series(a)
    # sum_b = sum_of_series(b)
    sum_a = sum(a)
    sum_b = sum(b)

    return sum_a / sum_b


# test functions
def main():

    series_a = [6, 6, 6]
    series_b = [3, 3, 3]
    series_c = [8, 8, 8]
    series_e = [6.6, 6.6, 6.6]
    series_f = [3.3, 3.3, 3.3]

    print(f"Should be 9: {diff_of_series(series_a, series_b)}")
    print(f"Should be 6: {diff_of_series(series_a, series_c)}")
    print(f"Should be 9.9: {diff_of_series(series_e, series_f)}")
    print(f"Should be 2.0: {compare_series(series_a, series_b)}")
    print(f"Should be 0.5: {compare_series(series_b, series_a)}")
    print(f"Should be 2.0: {compare_series(series_e, series_f)}")
    print(f"Should be 0.5: {compare_series(series_f, series_e)}")


# stand alone test
if __name__ == '__main__':
    main()
