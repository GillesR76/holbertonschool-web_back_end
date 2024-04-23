#!/usr/bin/env python3


"""Async Comprehensions"""


from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collecte 10 nombres aléatoires en utilisant une async
    comprehension sur async_generator.
    """
    return [i async for i in async_generator()]
