from bubble_sort import bubble_sort
import pytest


test_data_1 = [([5, 2, 6, 1], [1, 2, 5, 6]),
            ([1], [1]),
            ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
            ([1, 2, 3], [1, 2, 3])]


@pytest.mark.parametrize('sample, expected_output', test_data_1)
def test_bubble_sort(sample, expected_output):
    assert bubble_sort(sample) == expected_output


def test_bubble_sort_parameter_is_not_list():
    was_type_error: bool = False
    try:
        bubble_sort(1)
    except TypeError:
        was_type_error = True

    assert was_type_error


def test_bubble_sort_empty_list():
    was_value_error: bool = False
    try:
        bubble_sort([])
    except ValueError:
        was_value_error = True

    assert was_value_error


test_data_2 = [[5, 2, 'a', 1], [1, [2], 3], [5.7, 3], ['c']]


@pytest.mark.parametrize('sample', test_data_2)
def test_bubble_sort(sample):
    was_type_error: bool = False
    try:
        bubble_sort(sample)
    except TypeError:
        was_type_error = True

    assert was_type_error



