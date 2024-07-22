#!/usr/bin/env python3
"""second task simple_pagination
"""

import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """gets index range from given page and page size
    """

    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)


class Server:
    """popular baby names cached
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """dataset that is cached
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieves a page of data.
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]
