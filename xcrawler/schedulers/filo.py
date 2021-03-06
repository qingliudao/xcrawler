"""
    filo scheduler
    ~~~~~~~~~~~~~~
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

from collections import deque


class FILOScheduler(object):
    def __init__(self, maxsize=None):
        self._requests = deque(maxlen=maxsize)
        self.maxsize = maxsize

    def __repr__(self):
        return 'FILOScheduler()'

    def add(self, req):
        self._requests.append(req)

    def pop(self):
        try:
            return self._requests.pop()
        except IndexError:
            return None

    def clear(self):
        self._requests.clear()

    def is_full(self):
        return len(self) == self.maxsize

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self._requests)
