

class ContinuousWood:

    def __init__(self, wood) -> None:
        self.step = 3, 1
        self._wood = list(zip(*wood))  # Transpose
        self._width = len(self._wood)
        self._height = len(self._wood[0])
        self.print_wood()

    def __str__(self) -> str:
        return f'wood width: {self._width}, height: {self._height}'

    def _has_next(self):
        return self._current[1] + self.step[1] < self._height

    def __iter__(self):
        self._current = 0, 0
        return self

    def __next__(self):
        if not self._has_next():
            raise StopIteration
        next_x = (self._current[0] + self.step[0]) % self._width
        next_y = self._current[1] + self.step[1]
        self._current = (next_x, next_y)
        # print(f'wood{self._current} = {self._wood[self._current[0]][self._current[1]]}')
        return self._wood[next_x][next_y]

    def print_wood(self):
        for j in range(self._height):
            for i in range(self._width):
                print(self._wood[i][j], end='')
            print()

    @staticmethod
    def parse(filename):
        with open(filename) as f:
            return ContinuousWood([line.strip() for line in f.readlines() if len(line) > 0])
