import bisect

class TimeMap:

    def __init__(self):
        self.k_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.k_map:
            self.k_map[key] = {}
            self.k_map[key]["values"] = []
        self.k_map[key][timestamp] = value
        if "values" not in self.k_map[key]:
            self.k_map[key]["values"] = []
        bisect.insort(self.k_map[key]["values"], timestamp)

    def get(self, key: str, timestamp: int) -> str:
        t_stamp = self.b_search(key, timestamp)
        if t_stamp == -1:
            return ""
        return self.k_map[key][t_stamp]
    
    def b_search(self, key, timestamp) -> int:
        if key not in self.k_map:
            return -1

        if len(self.k_map[key]["values"]) == 0:
            return -1
        if self.k_map[key]["values"][-1] <= timestamp:
            return self.k_map[key]["values"][-1]
        
        left, right = 0, len(self.k_map[key]["values"]) - 1

        while right - left > 1:
            m = (right + left) // 2
            bef = self.is_before(m, timestamp, key)
            if bef == True:
                left = m
            else:
                right = m
        if self.k_map[key]["values"][left] <= timestamp:
            return self.k_map[key]["values"][left]
        return -1
    
    def is_before(self, m, target, key) -> bool:
        if self.k_map[key]["values"][m] <= target:
            return True
        return False

