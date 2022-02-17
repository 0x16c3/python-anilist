#!/usr/bin/env python3
# Copyright (C) 2021-2022 Amano Team <https://amanoteam.com/>
#
# SPDX-License-Identifier: MIT

from typing import Callable, Dict


class PageInfo:
    """Page object. Contains Pagination info."""

    def __init__(
        self,
        *,
        total_items: int,
        current: int,
        last: int,
    ):
        self.total_items = total_items
        self.current = current
        self.last = last

    def raw(self) -> Dict:
        return self.__dict__

    def __repr__(self) -> Callable:
        return self.__str__()

    def __str__(self) -> str:
        return str(self.raw())
