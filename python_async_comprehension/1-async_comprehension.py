#!/usr/bin/env python3
"""write a coroutine called async_comprehension that takes no arguments.
The coroutine will collect 10 random numbers using an async comprehensing
over async_generator, then return the 10 random numbers.
"""

import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    list_nbrs = []
    async for number in async_generator():
        list_nbrs.append(number)
    return list_nbrs
