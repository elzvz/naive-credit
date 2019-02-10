def is_creditable(age, salary):
    """
    >>> is_creditable(30, 40_000)
    True

    >>> is_creditable(20, 40_000)
    False

    >>> is_creditable(70, 40_000)
    False

    >>> is_creditable(30, 25_000)
    False

    :param age:
    :param salary:
    :return:
    """
    min_age = 21
    max_age = 60
    min_salary = 30_000

    if age < min_age:
        return False

    # если  был return, то до этой точки мы не дойдем
    if age > max_age:
        return False

    if salary < min_salary:
        return False

     # в этой точке все проверки пройдены
    return True



