#!/usr/bin/env python3
"""Method get_hyper to return a dict of details on the
current pagination state"""

import csv
from math import ceil
from typing import List

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
        """
        Args:
            page (int, optional): Defaults to 1.
            page_size (int, optional): Defaults to 10.
        Returns:
            List[List]: Appropriate page of the dataset
        """
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0

        page_set: tuple = index_range(page, page_size)
        dataset: List = self.dataset()

        current_page_data = dataset[page_set[0]:page_set[1]]
        return current_page_data

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Returns a dict containing hypermedia info on the pagination"""
        hypermedia = {}
        current_page_data = self.get_page(page, page_size)
        hypermedia["page_size"] = len(current_page_data)

        hypermedia["page"] = page

        hypermedia["data"] = current_page_data

        next_page = None
        if self.get_page(page + 1) != []:
            next_page = page + 1
        hypermedia["next_page"] = next_page

        prev_page = None
        if page > 1:
            prev_page = page - 1
        hypermedia["prev_page"] = prev_page

        hypermedia["total_pages"] = ceil(len(self.dataset()) / page_size)

        return hypermedia
