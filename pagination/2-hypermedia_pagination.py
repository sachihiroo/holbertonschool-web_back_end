#!/usr/bin/env python3
"""1-simple_pagination.py"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """Return the tuple of start and end indices"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names"""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        retrieving a specific page of data from the dataset
        """
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        rus = self.dataset()
        start, end = index_range(page, page_size)
        if start >= len(rus):
            return []
        return rus[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        returns a dictionary containing the key-value pairs
        """
        res = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        prev_page = page - 1 if page > 1 else None
        next_page = page + 1 if page < total_pages else None

        dict_hyper = {
            "page_size": page_size,
            "page": page,
            "data": res,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
        return dict_hyper
