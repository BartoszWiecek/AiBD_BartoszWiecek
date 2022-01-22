from typing import List


def bubble_sort(tab: List[int]) -> List[int]:
    if type(tab) is not list:
        raise TypeError('Given parameter is not list')

    tab_length: int = len(tab)

    if tab_length == 0:
        raise ValueError('Given list is empty')

    for elem in tab:
        if type(elem) is not int:
            raise TypeError('Given list contains non-int element')

    tab_copy: List[int] = tab[:]

    for i in range(tab_length - 1, 0, -1):
        for j in range(i):
            if tab_copy[j] > tab_copy[j + 1]:
                tab_copy[j], tab_copy[j + 1] = tab_copy[j + 1], tab_copy[j]

    return tab_copy
