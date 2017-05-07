rows = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}
columns = list(range(1, 9))

cell = input("Please enter cell (for example E2): ")
row = rows[cell[0]]
column = int(cell[1])

if (row + column) % 2 == 0:
    print("Black")
else:
    print("White")
