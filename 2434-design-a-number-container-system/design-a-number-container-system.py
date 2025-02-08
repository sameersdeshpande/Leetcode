class NumberContainers:

    def __init__(self):
        self.numbers = defaultdict(list)
        self.indexnumbers = {}

    def change(self, index: int, number: int) -> None:
        self.indexnumbers[index] = number
        heapq.heappush(self.numbers[number],index)
        

    def find(self, number: int) -> int:
        if not self.numbers[number]:
            return -1
        while self.numbers[number]:
            index = self.numbers[number][0]
            if self.indexnumbers.get(index)==number:
                return index
            heapq.heappop(self.numbers[number])
        return -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)