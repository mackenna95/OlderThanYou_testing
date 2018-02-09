# @vertikoff create sum function here
def return_sum(num_list):
    """

    takes the values passed in as num_list and returns their sum
    :param num_list: mixed list of ints and floats
    :returns sum: the sum of the ints and floats passed in num_list
    """
    sum = 0
    try:
        for num in num_list:
            sum += num
    except TypeError:
        return("\'" + str(num) + "\' is invalid type (expects int or float).")
    except ValueError:
        return("ValueError returned")

    return(sum)


# @jlongc12 create tuple min/max function here
def return_limits(num_list):
    limits = (min(num_list), max(num_list))
    return limits


# @mackenna95 create max difference function here
def list_max_adjacent(num_list):
    import numpy as np

    if len(num_list) == 0:
        max_diff = 0
    elif len(num_list) == 1:
        max_diff = 0
    else:
        diff = np.diff(num_list)
        abs_diff = np.absolute(diff)
        max_diff = np.max(abs_diff)

    return max_diff
