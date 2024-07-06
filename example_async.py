#!/usr/bin/env python3
# encoding: utf-8
# -*- coding: utf-8 -*-
import asyncio, time
from cachettl import async_cachettl, async_cachettl_min

@async_cachettl(ttl=7)
async def print_my_data(param):
    print("Starting print_my_data() function...")
    await asyncio.sleep(1) # Just wait 1 second to simulate an asynchronous operation
    return f"- Data for {param}"

async def main():
    print("\nTesting with a TTL of 7 seconds\n")
    print(await print_my_data('Test 1'))
    print(f"  {print_my_data.cache_info()}")
    print(await print_my_data('Test 1'))
    print(f"  {print_my_data.cache_info()}")

    print("")

    print(await print_my_data('Test 2'))
    print(f"  {print_my_data.cache_info()}")
    print(await print_my_data('Test 2'))
    print(f"  {print_my_data.cache_info()}")
    
    print("")

    print(await print_my_data('Test 3'))
    print(f"  {print_my_data.cache_info()}")
    print(await print_my_data('Test 3'))
    print(f"  {print_my_data.cache_info()}")
    
    print("\ntime.sleep(1.5)...\n")
    time.sleep(1.5)
    
    print(await print_my_data('Test 1'))
    print(f"  {print_my_data.cache_info()}")

    print(await print_my_data('Test 2'))
    print(f"  {print_my_data.cache_info()}")

    print("\ntime.sleep(1.5)...\n")
    time.sleep(1.5)

    print(await print_my_data('Test 1'))
    print(f"  {print_my_data.cache_info()}")

    print(await print_my_data('Test 2'))
    print(f"  {print_my_data.cache_info()}")
    
    print("\ntime.sleep(5) to expire the time-to-live cache...\n")
    time.sleep(5)
    
    print(await print_my_data('Test 1'))
    print(f"  {print_my_data.cache_info()}")
    print(await print_my_data('Test 1'))
    print(f"  {print_my_data.cache_info()}")

    print("")

asyncio.run(main())

