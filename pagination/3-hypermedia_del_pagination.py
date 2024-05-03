#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination

This script implements a deletion resilient hypermedia
pagination system for a database of popular baby names.
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initialize the Server object and set the cached
        dataset and indexed_dataset to None.
        """
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        Return the cached dataset or load it from the
        DATA_FILE if it is not yet cached.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Return the cached indexed_dataset or create
        it from the dataset if it is not yet cached.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))}

        return self.__indexed_dataset

def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
    """Return a hypermedia index of the dataset
    with the given index and page size.
    """
    if index is None:
        index = 0
    # Assert that the index is within a valid range
    assert 0 <= index < len(self.__indexed_dataset)

    # Calculate the next index based on the
    # current index and page size
    next_index = index + page_size
    data = []

    # Retrieve the data for the current page,
    # skipping over missing indices
    i = index
    while len(data) < page_size and i < next_index:
        if i in self.__indexed_dataset:
            data.append(self.__indexed_dataset[i])
        i += 1

    # Return the dictionary with the required information
    return {
        "index": index,
        "next_index": min(next_index, len(self.__indexed_dataset)),
        "page_size": page_size,
        "data": data,
    }
