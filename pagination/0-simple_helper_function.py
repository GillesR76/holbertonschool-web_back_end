#!/usr/bin/env python3
"""Write a function named index_range that takes
two integer arguments page and page_size.
* The function should return a tuple of size two containing a start
index and an end index corresponding to the range of indexes to
return in a list for those particular pagination parameters.
* Page numbers are 1-indexed, i.e. the first page is page 1.
"""


def index_range(page, page_size):
    """Function that takes two integer arguments and returns a
    tuple of size two containing a start index and an end index
    Args:
        page (integer): the current page number
        page_size (integer): the number of items to display on
        each page
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
