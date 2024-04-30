#!/usr/bin/env python3
"""Implement a get_hyper method that takes the same arguments (and defaults)
as get_page and returns a dictionary containing the following key-value pairs:
* page_size: the length of the returned dataset page
* page: the current page number
* data: the dataset page (equivalent to return from previous task)
* next_page: number of the next page, None if no next page
* prev_page: number of the previous page, None if no previous page
* total_pages: the total number of pages in the dataset as an integer
Make sure to reuse get_page in your implementation.
You can use the math module if necessary.
"""

from typing import List
import math
import csv
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Method that uses index_range to find the correct indexes to paginate
        the dataset correctly and return the appropriate page of the dataset
        Args:
            page (integer): the current page number
            page_size (integer): the number of items to display on
        each page
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        self.dataset()
        start_index, end_index = index_range(page, page_size)
        return self.__dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Method that takes two arguments and returns a dictionary
        containing key-value pairs
        Args:
            page (integer): the current page number
            page_size (integer): the number of items to display on
        each page
        """
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        # ceiling division: division that rounds up to the nearest integer
        total_pages = (total_items + page_size - 1) // page_size

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
