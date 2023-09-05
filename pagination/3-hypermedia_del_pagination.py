#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from math import ceil
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
        """Returns a dict containing the start index of the return page,
        the index of the first item after the last item on the current page,
        the current page size,
        the actual page of the dataset."""
        hyper_index = {}
        indexed_dataset = self.indexed_dataset()

        assert 0 <= index < len(indexed_dataset)

        hyper_index["index"] = index

        next_index = index + page_size
        data = []
        idx = index
        while idx < next_index:
            item = indexed_dataset.get(idx)
            if item:
                data.append(item)
            else:
                next_index += 1
            idx += 1
        hyper_index["data"] = data

        hyper_index["page_size"] = len(data)
        hyper_index["next_index"] = next_index

        return hyper_index
