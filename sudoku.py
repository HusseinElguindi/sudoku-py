# Imports
from math import sqrt

# SudokuTable represents an instance of a sudoku solver
class SudokuTable:
    def __init__(self, table: list, boxWidth: int = None, boxHeight: int = None) -> None:
        if len(table) == 0:
            raise Exception("Invalid list of length 0")

        self._table = table.copy()
        self._width = len(self._table)
        self._height = len(self._table[0])

        # Calculate the box dimensions, if not passed
        if boxWidth == None:
            self._boxWidth = int(sqrt(self._width))
        if boxWidth == None:
            self._boxHeight = int(sqrt(self._height))


    # Return a copy of the internal table
    def getTable(self) -> list:
        return self._table.copy()


    # TODO: split checks into private functions
    # Validate a point value at a specific position
    def validatePos(self, pos: tuple, point: int) -> bool:
        # Destructure position
        row, col = pos

        # Ensure the point is on the table
        if col > self._width or row > self._height:
            return False

        # point = self._table[row][col]

        # Invalidate if another point on the row has the same value
        for i in range(len(self._table[row])):
            if self._table[row][i] == point and i != col:
                return False

        # Invalidate if another point on the column has the same value
        for i in range(len(self._table)):
            if self._table[i][col] == point and i != row:
                return False

        # Calculate the top left corner position for each "box"
        boxRow, boxCol = (row // self._boxHeight) * self._boxHeight, (col // self._boxWidth) * self._boxWidth

        # Check for duplicate numbers in a box
        for i in range(boxRow, boxRow + self._boxHeight):
            for j in range(boxCol, boxCol + self._boxWidth):
                if self._table[i][j] == point and (i, j) != pos:
                    return False

        # All checks passed
        return True

    # Solve the Sudoku table recursively, using backtracking
    def solve(self) -> bool:
        # Get the next empty position, or if none are left
        emptyPos = self._nextEmptyPos()
        if len(emptyPos) == 0: return True
        row, col = emptyPos

        # Loop through the range of possible numbers
        for i in range(1, self._width+1):
            # Validate the number at a position
            if self.validatePos(emptyPos, i):
                # Set the valid number to pos
                self._table[row][col] = i

                # If solved return true (base case)
                if self.solve(): return True

            # Back track
            self._table[row][col] = 0

        # None of the numbers in the range were valid
        return False


    # Find the next empty position
    def _nextEmptyPos(self) -> tuple: # (row, col)
        for i in range(self._height):
            for j in range(self._width):
                if self._table[i][j] == 0: return (i, j)

        return () # Did not find an empty position


    # Pretty print the table
    def prettyPrint(self) -> None:
        for i in range(len(self._table)):
            if i % self._boxHeight == 0 and i != 0:
                print("- " * (self._width + self._boxWidth - 1))

            for j in range(len(self._table[i])):
                if j % self._boxWidth == 0 and j != 0:
                    print("| ", end="")

                print(" " if self._table[i][j] == 0 else self._table[i][j], end=" ")

            print()