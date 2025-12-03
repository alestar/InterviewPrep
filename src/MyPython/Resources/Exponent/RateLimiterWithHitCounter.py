"""
Build a hit counter that tracks the number of hits in the last 5 minutes, supporting multiple keys (e.g., “a”, “b”).
Then, use this counter to implement a simple rate limiter.

"""


import time
from collections import deque

class HitCounter:
    def __init__(self, window_seconds=300): # 5 minutes = 300 seconds
        self.window_seconds = window_seconds
        self.hits = {} # Stores {key: deque(timestamps)}

    def record_hit(self, key):
        current_time = int(time.time())
        if key not in self.hits:
            self.hits[key] = deque()
        self.hits[key].append(current_time)
        self._clean_old_hits(key)

    def get_hits(self, key):
        if key not in self.hits:
            return 0
        self._clean_old_hits(key)
        return len(self.hits[key])

    def _clean_old_hits(self, key):
        current_time = int(time.time())
        while self.hits[key] and self.hits[key][0] <= current_time - self.window_seconds:
            self.hits[key].popleft()


class RateLimiter:
    def __init__(self, hit_counter, max_hits_per_window):
        self.hit_counter = hit_counter
        self.max_hits_per_window = max_hits_per_window

    def allow_request(self, key):
        current_hits = self.hit_counter.get_hits(key)
        if current_hits < self.max_hits_per_window:
            self.hit_counter.record_hit(key)
            return True
        else:
            return False

if __name__ == "__main__":
    counter = HitCounter(window_seconds=10) # 10-second window for demonstration
    limiter_a = RateLimiter(counter, max_hits_per_window=3)
    limiter_b = RateLimiter(counter, max_hits_per_window=2)

    print("Testing key 'a' (max 3 hits in 10s):")
    for i in range(5):
        if limiter_a.allow_request("a"):
            print(f"Request 'a' allowed. Hits for 'a': {counter.get_hits('a')}")
        else:
            print(f"Request 'a' denied. Hits for 'a': {counter.get_hits('a')}")
        time.sleep(1) # Simulate requests over time

    print("\nTesting key 'b' (max 2 hits in 10s):")
    for i in range(4):
        if limiter_b.allow_request("b"):
            print(f"Request 'b' allowed. Hits for 'b': {counter.get_hits('b')}")
        else:
            print(f"Request 'b' denied. Hits for 'b': {counter.get_hits('b')}")
        time.sleep(1)

    time.sleep(5) # Wait for some hits to expire
    print(f"\nHits for 'a' after 5 seconds: {counter.get_hits('a')}")
    print(f"Hits for 'b' after 5 seconds: {counter.get_hits('b')}")