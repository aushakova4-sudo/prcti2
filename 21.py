move = input()
from_cell, to_cell = move.split('-')
start_x = ord(from_cell[0]) - 96
start_y = int(from_cell[1])
end_x = ord(to_cell[0]) - 96
end_y = int(to_cell[1])
diff_x = abs(start_x - end_x)
diff_y = abs(start_y - end_y)
if (diff_x == 2 and diff_y == 1) or (diff_x == 1 and diff_y == 2):
    print("верно")
else:
    print("ошибка")