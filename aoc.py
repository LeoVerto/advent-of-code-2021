#!/usr/bin/env python3
from typing import Union

import requests

from config import SESSION_COOKIE


def get_inputs(day: int, to_int: bool = True) -> Union[list[int], list[str]]:
    year = 2021
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    cookies = {"session": SESSION_COOKIE}

    r = requests.get(url, cookies=cookies)
    lines = r.text.split("\n")[:-1]

    if to_int:
        return list(map(int, lines))
    else:
        return lines
