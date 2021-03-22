from math import sqrt

## SudokuTable represents an instance of a sudoku solver
#
class SudokuTable:
    def __init__(self, table: list, boxWidth: int = None, boxHeight: int = None) -> None:
        # if len(table) == 0: pass
        self._table = table.copy()
        self._width = len(self._table)
        self._height = len(self._table[0])

        if boxWidth == None:
            self._boxWidth = int(sqrt(self._width))

        if boxWidth == None:
            self._boxHeight = int(sqrt(self._height))


    def getTable(self) -> list:
        return self._table.copy()

    def validatePos(self, x: int, y: int) -> bool:
        # Ensure the point is on the table
        if x > self._width or y > self._height:
            return False

        point = self._table[y][x]

        # Check for duplicate numbers on the row of the point
        for i in range(len(self._table[y])):
            if i == x: continue # Ignore the original point

            # Invalidate if another point on the row has the same value
            if self._table[y][i] == point: return False

        # Check for duplicate numbers on the column of the point
        for i in range(len(self._table)):
            if i == y: continue # Ignore the original point

            # Invalidate if another point on the column has the same value
            if self._table[i][x] == point: return False

        # Check for duplicate numbers in box of the
        for i in range(self._boxWidth):
            for j in range(self._boxHeight):
                pass


        return True
