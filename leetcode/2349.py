class NumberContainers:

    def __init__(self):
        self.map = {} # number, heap[index]
        self.index_to_number = {} # index, number

    def change(self, index: int, number: int) -> None:
        if number not in self.map:
            self.map[number] = []

        heapq.heappush(self.map[number], index)
        self.index_to_number[index] = number

    def find(self, number: int) -> int:
        if number not in self.map:
            return -1

        heap = self.map[number]
        while heap:
            index = heapq.heappop(heap)
            if self.index_to_number[index] == number:
                heapq.heappush(heap, index)
                return index
            
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)