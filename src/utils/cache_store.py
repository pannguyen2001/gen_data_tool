from cachetools import TTLCache
from typing import Optional
import pandas as pd
import asyncio

# # ✅ Define a global or module-level cache
# df_cache = LRUCache(maxsize=100)

# Create in-memory TTL cache (max 100 entries, 600 sec lifetime)
ttl_cache = TTLCache(maxsize=100, ttl=600)

def cache_df(key: str, df: pd.DataFrame):
    ttl_cache[key] = df

def get_cached_df(key: str) -> Optional[pd.DataFrame]:
    return ttl_cache.get(key)

def invalidate_cache(key: str):
    ttl_cache.pop(key, None)

def clear_all_cache():
    ttl_cache.clear()
