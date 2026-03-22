from collections import defaultdict


class TimeMap:
    def __init__(self):
        # Используем defaultdict, где значением будет список
        self._map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Добавляем пару в список для данного ключа
        self._map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key in self._map:
            value = ""
            # Бинарный поиск (поиск самого правого элемента, который <= timestamp)
            left, right = 0, len(self._map[key]) - 1
            while left <= right:
                mid = (left + right) // 2
                if self._map[key][mid][1] == timestamp:
                    return self._map[key][mid][0]
                elif self._map[key][mid][1] < timestamp:
                    value = self._map[key][mid][0]
                    left = mid + 1
                else:
                    right = mid - 1
            return value

        else:
            return ""
