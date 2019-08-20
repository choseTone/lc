__author__ = 'wangqc'


# https://leetcode.com/problems/time-based-key-value-store/


import bisect, collections

class TimeMap:
    def __init__(self):
        self.cache = collections.defaultdict(list)

    def set(self, key, value, ts):
        self.cache[key].append((ts, value))

    def get(self, key, ts):
        idx = bisect.bisect(self.cache[key], (ts+1,)) - 1
        return self.cache[key][idx][1] if idx >= 0 else ""


if __name__ == '__main__':
    obj = TimeMap()
    print(obj.set("foo", "bar", 1))
    print(obj.get("foo", 1))
    print(obj.get("foo", 3))
    print(obj.set("foo", "bar2", 4))
    print(obj.get("foo", 4))
    print(obj.get("foo", 5))
    print("---")
    obj = TimeMap()
    print(obj.set("love","high",10))
    print(obj.set("love","low",20))
    print(obj.get("love",5))
    print(obj.get("love",10))
    print(obj.get("love",15))
    print(obj.get("love",20))
    print(obj.get("love",25))