#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        The valid range for the index is from 0 to the length of the dataset
        minus 1 because in Python list indices start at 0, not 1.
        Here, because the range function excludes the end value we refer
        to total_items and not total_items - 1
        """
        total_items = len(self.dataset())
        assert index in range(0, total_items)
        data = []
        indexed_data = self.indexed_dataset()
        for key, value in indexed_data.items():
            if len(data) <= page_size:
                data.append(value)
            else:
                break
        next_index = index + len(data)

        return {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': data
        }
