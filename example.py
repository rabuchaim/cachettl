#!/usr/bin/env python3
# encoding: utf-8
# -*- coding: utf-8 -*-
import datetime as dt, time
from cachettl import cachettl, cachettl_min

@cachettl(ttl=4)
def print_datetime():
    return dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
if __name__ == '__main__':
    for I in range(15):
        print(f"{'%02d'%(I+1)}. {print_datetime()}")
        print(f"    CacheInfo: {print_datetime.cache_info()} - Only Remaining TTL: {print_datetime.cache_info().remainingttl}")
        time.sleep(0.5)
    