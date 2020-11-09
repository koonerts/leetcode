import collections
from typing import List

class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.__queue = [0] * k
        self.__start: int = 0
        self.__end: int = 0
        self.__size: int = 0

    @property
    def size(self) -> int:
        return self.__size

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False

        if self.isEmpty():
            self.__queue[0] = value
            self.__start, self.__end = 0, 0

        elif self.__end == len(self.__queue) - 1:
            self.__queue[0] = value
            self.__end = 0

        else:
            self.__queue[self.__end + 1] = value
            self.__end += 1

        self.__size += 1
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False

        self.__queue[self.__start] = 0
        if self.__start == len(self.__queue) - 1:
            self.__start = 0
        else:
            self.__start += 1

        self.__size -= 1
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        else:
            return self.__queue[self.__start]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        else:
            return self.__queue[self.__end]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.__size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.__size == len(self.__queue)

class MovingAverage:
    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.__que = collections.deque(maxlen=size)


    def next(self, val: int) -> float:
        """
        Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
        Ex: MovingAverage m = new MovingAverage(3);
            m.next(1) = 1
            m.next(10) = (1 + 10) / 2
            m.next(3) = (1 + 10 + 3) / 3
            m.next(5) = (10 + 3 + 5) / 3
        """
        self.__que.append(val)
        return sum(self.__que)/len(self.__que)

class QueueEasy:
    ROOM = 2**31 - 1
    GATE = 0
    WALL = -1

    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        You are given a m x n 2D grid initialized with these three possible values.

        -1 - A wall or an obstacle.
        0 - A gate.
        INF - 2**31 - 1 = 2147483647

        Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.
        Example:

        Given the 2D grid:
        INF  -1  0  INF
        INF INF INF  -1
        INF  -1 INF  -1
          0  -1 INF INF

        After running your function, the 2D grid should be:
          3  -1   0   1
          2   2   1  -1
          1  -1   2  -1
          0  -1   3   4
        """
        if not rooms: return

        q = collections.deque()
        rows = len(rooms)
        cols = len(rooms[0])
        directions = [(-1, 0), (1,0), (0, -1), (0,1)]

        for row in range(rows):
            for col in range(cols):
                if rooms[row][col] == self.GATE:
                    q.append((row, col))

        while len(q) > 0:
            row, col = q.popleft()
            for x, y in directions:
                if row+x < 0 or row+x >= rows or col+y < 0 or col+y >= cols or rooms[row+x][col+y] != self.ROOM:
                    continue
                rooms[row+x][col+y] = rooms[row+x][col+y] + 1
                q.append((row+x, col+y))

    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.
        An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
        You may assume all four edges of the grid are all surrounded by water.

        Example 1:
        Input: grid = [
          ["1","1","1","1","0"],
          ["1","1","0","1","0"],
          ["1","1","0","0","0"],
          ["0","0","0","0","0"]
        ]
        Output: 1

        Example 2:
        Input: grid = [
          ["1","1","0","0","0"],
          ["1","1","0","0","0"],
          ["0","0","1","0","0"],
          ["0","0","0","1","1"]
        ]
        Output: 3
        """
        LAND = 1
        WATER = 0


print(QueueEasy.ROOM)