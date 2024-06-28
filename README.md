# cachettl v1.0.3

An elegant LRU TTL Cache decorator that also works with asyncio. It has the cache_info(), cache_clear() methods and access to the remainingttl property.

More info about LRU (Last Recent Used) cache: https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_recently_used_(LRU)

```
What's new in v1.0.3 - 28/Jun/2024
- Added a decorator for asynchronous use: @async_cachettl

What's new in v1.0.1 - 27/Jun/2024
- The default value for the maxsize parameter is now set to None,
  so the cache can grow indefinitely and only obey the specified 
  TTL. If you want to impose a limit, simply enter the desired 
  value in the maxsize parameter.
```

## Installation
```bash
pip install cachettl
```

## @cachettl and @async_cachettl description
The **@cachettl** and **@async_cachettl** decorators allows you to add a time-limited (TTL) cache to a function, with options for controlling maximum size and typing. Additionally, it provides methods to view cache statistics and clear the cache. It is also possible to access the cache_info() properties, including the remaining TTL for the function.


```python
def cachettl(ttl=60, maxsize=None, typed=False):
def async_cachettl(ttl=60, maxsize=None, typed=False):
    """ 
    If *maxsize* is set to None, the LRU features are disabled and the cache
    can grow without bound.

    If *typed* is True, arguments of different types will be cached separately.
    For example, f(3.0) and f(3) will be treated as distinct calls with
    distinct results.

    Arguments to the cached function must be hashable.

    View the cache statistics named tuple (hits, misses, maxsize, currsize and remainingttl)
    with f.cache_info().  Clear the cache and statistics with f.cache_clear().

    Access the underlying function with f._wrapped.
    """
``` 
### Parameters

- **`ttl`** (int): Lifetime (in seconds) of items in the cache. Default is 60 seconds.

- **`maxsize`** (int or None): Maximum cache size. If None, the cache can grow indefinitely.

- **`typed`** (bool): If True, arguments of different types are stored separately in the cache.

### Methods

- **`cache_info()`**: Returns a tuple with cache statistics (hits, misses, maxsize, currsize, remainingttl).

- **`cache_clear()`**: Clears the cache and statistics.

### cache_info() Method Properties

- **`hits`**: The number of cache hits. This indicates how many times a request for a cached value was successful.

- **`misses`**: The number of cache misses. This indicates how many times a request for a value was not found in the cache.

- **`maxsize`**: The maximum size of the cache. This indicates the upper limit of the cache's capacity.

- **`currsize`**: The current size of the cache. This indicates the current number of entries stored in the cache.

- **`remainingttl`**: The remaining time-to-live for the oldest item in the cache. This indicates how much time is left before the oldest cached item expires.

### Examples of use

```python
@cachettl(ttl=10)
def print_datetime():
    return dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

print(print_datetime.cache_info()) # Displays cache statistics

print(print_datetime.cache_info().remainingttl) # Displays the remaining time-to-live 

print_datetime.cache_clear() # Clear the cache
``` 
<br>

___


## @cachettl_min and @async_cachettl_min description
The **@cachettl_min** and **@async_cachettl_min** decorators provides a simple TTL cache with no additional methods for cache information or clearing. **Does not support use with asyncio**.

```python
def cachettl_min(ttl=60, maxsize=None, typed=False):
def async_cachettl_min(ttl=60, maxsize=None, typed=False):
    """A minimal version of cachettl decorator without methods cache_info() and cache_clear()"""
```

### Parameters

- **`ttl`** (int): Lifetime (in seconds) of items in the cache. Default is 60 seconds.

- **`maxsize`** (int or None): Maximum cache size. If None, the cache can grow indefinitely.

- **`typed`** (bool): If True, arguments of different types are stored separately in the cache.

### Examples of use

```python
@cachettl_min(ttl=20)
def print_datetime():
    return dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
```
<br>

___

### - NonAsynchronous usage example:

```python
from cachettl import cachettl
import datetime as dt, time

@cachettl(ttl=4)
def print_datetime():
    return dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
if __name__ == '__main__':
    for I in range(15):
        print(f"{'%02d'%(I+1)}. {print_datetime()}")
        print(f"    CacheInfo: {print_datetime.cache_info()} - Only Remaining TTL: {print_datetime.cache_info().remainingttl}")
        time.sleep(0.5)
```

### - NonAsynchronous output:

```bash
01. 28/06/2024 02:49:56
    CacheInfo: CacheInfo(hits=0, misses=1, maxsize=None, currsize=1, remainingttl=3.999953031539917) - Only Remaining TTL: 3.99992299079895
02. 28/06/2024 02:49:56
    CacheInfo: CacheInfo(hits=1, misses=1, maxsize=None, currsize=1, remainingttl=3.4994564056396484) - Only Remaining TTL: 3.4994266033172607
03. 28/06/2024 02:49:56
    CacheInfo: CacheInfo(hits=2, misses=1, maxsize=None, currsize=1, remainingttl=2.998894453048706) - Only Remaining TTL: 2.998859405517578
04. 28/06/2024 02:49:56
    CacheInfo: CacheInfo(hits=3, misses=1, maxsize=None, currsize=1, remainingttl=2.498380184173584) - Only Remaining TTL: 2.49833607673645
05. 28/06/2024 02:49:56
    CacheInfo: CacheInfo(hits=4, misses=1, maxsize=None, currsize=1, remainingttl=1.9978115558624268) - Only Remaining TTL: 1.9977762699127197
06. 28/06/2024 02:49:56
    CacheInfo: CacheInfo(hits=5, misses=1, maxsize=None, currsize=1, remainingttl=1.497302770614624) - Only Remaining TTL: 1.4972443580627441
07. 28/06/2024 02:49:56
    CacheInfo: CacheInfo(hits=6, misses=1, maxsize=None, currsize=1, remainingttl=0.9967324733734131) - Only Remaining TTL: 0.9966979026794434
08. 28/06/2024 02:49:56
    CacheInfo: CacheInfo(hits=7, misses=1, maxsize=None, currsize=1, remainingttl=0.4961709976196289) - Only Remaining TTL: 0.49613475799560547
09. 28/06/2024 02:50:00
    CacheInfo: CacheInfo(hits=7, misses=2, maxsize=None, currsize=2, remainingttl=3.999948740005493) - Only Remaining TTL: 3.999933958053589
10. 28/06/2024 02:50:00
    CacheInfo: CacheInfo(hits=8, misses=2, maxsize=None, currsize=2, remainingttl=3.499492883682251) - Only Remaining TTL: 3.4994630813598633
11. 28/06/2024 02:50:00
    CacheInfo: CacheInfo(hits=9, misses=2, maxsize=None, currsize=2, remainingttl=2.9988961219787598) - Only Remaining TTL: 2.9988625049591064
12. 28/06/2024 02:50:00
    CacheInfo: CacheInfo(hits=10, misses=2, maxsize=None, currsize=2, remainingttl=2.498270273208618) - Only Remaining TTL: 2.498141050338745
13. 28/06/2024 02:50:00
    CacheInfo: CacheInfo(hits=11, misses=2, maxsize=None, currsize=2, remainingttl=1.997661828994751) - Only Remaining TTL: 1.9975805282592773
14. 28/06/2024 02:50:00
    CacheInfo: CacheInfo(hits=12, misses=2, maxsize=None, currsize=2, remainingttl=1.4970712661743164) - Only Remaining TTL: 1.4970340728759766
15. 28/06/2024 02:50:00
    CacheInfo: CacheInfo(hits=13, misses=2, maxsize=None, currsize=2, remainingttl=0.9964652061462402) - Only Remaining TTL: 0.9964287281036377
    
```
<br>

___

### - Asynchronous usage example:

```python
import asyncio, time
from cachettl import *

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

```

### - Asynchronous output:

```bash
Testing with a TTL of 7 seconds

Starting print_my_data() function...
- Data for Test 1
  CacheInfo(hits=0, misses=1, maxsize=2, currsize=1, remainingttl=5.998431444168091)
- Data for Test 1
  CacheInfo(hits=1, misses=1, maxsize=2, currsize=1, remainingttl=5.998369216918945)

Starting print_my_data() function...
- Data for Test 2
  CacheInfo(hits=1, misses=2, maxsize=2, currsize=2, remainingttl=4.996579885482788)
- Data for Test 2
  CacheInfo(hits=2, misses=2, maxsize=2, currsize=2, remainingttl=4.996516942977905)

Starting print_my_data() function...
- Data for Test 3
  CacheInfo(hits=2, misses=3, maxsize=2, currsize=2, remainingttl=4.996507167816162)
Starting print_my_data() function...
- Data for Test 1
  CacheInfo(hits=2, misses=4, maxsize=2, currsize=2, remainingttl=4.9968273639678955)
- Data for Test 3
  CacheInfo(hits=3, misses=4, maxsize=2, currsize=2, remainingttl=4.996763467788696)

time.sleep(1.5)...

- Data for Test 1
  CacheInfo(hits=4, misses=4, maxsize=2, currsize=2, remainingttl=3.496213436126709)
Starting print_my_data() function...
- Data for Test 2
  CacheInfo(hits=4, misses=5, maxsize=2, currsize=2, remainingttl=3.496246814727783)

time.sleep(1.5)...

- Data for Test 1
  CacheInfo(hits=5, misses=5, maxsize=2, currsize=2, remainingttl=1.9956271648406982)
- Data for Test 2
  CacheInfo(hits=6, misses=5, maxsize=2, currsize=2, remainingttl=1.9953944683074951)

time.sleep(5) to expire the time-to-live cache...

Starting print_my_data() function...
- Data for Test 1
  CacheInfo(hits=0, misses=1, maxsize=2, currsize=1, remainingttl=5.998239278793335)
- Data for Test 1
  CacheInfo(hits=1, misses=1, maxsize=2, currsize=1, remainingttl=5.9981842041015625)
```

## Sugestions, feedbacks, bugs...
E-mail me: ricardoabuchaim at gmail.com

