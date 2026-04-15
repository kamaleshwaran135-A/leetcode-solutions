import heapq

class MedianFinder(object):

    def __init__(self):
        self.small = []  # max heap (use negative values)
        self.large = []  # min heap

    def addNum(self, num):
        # add to max heap
        heapq.heappush(self.small, -num)
        
        # balance: move largest from small to large
        heapq.heappush(self.large, -heapq.heappop(self.small))
        
        # maintain size property
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self):
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        else:
            return (-self.small[0] + self.large[0]) / 2.0