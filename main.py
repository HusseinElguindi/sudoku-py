# Hussein Elguindi
# 22 March 2021

from sudoku import SudokuTable
import math

def main():
    # Get table info
    width = int(input("Width of table: "))
    height = int(input("Height of table: "))

    boxWidth = input("Box width (ignore for squares): ")
    boxWidth = None if boxWidth == "" else int(boxWidth)

    boxHeight = input("Box height (ignore for squares): ")
    boxHeight = None if boxHeight == "" else int(boxHeight)

    # Prompt user for table
    table = []
    for _ in range(height):
        table.append([int(x) for x in input().split()[:width]])
    print(table)

    # Solve and display
    st = SudokuTable(table, boxWidth, boxHeight)
    st.prettyPrint()
    print()
    # print("Solved:", st.solve(), end="\n\n")
    print(st.solveVerbose())
    st.prettyPrint()

main()