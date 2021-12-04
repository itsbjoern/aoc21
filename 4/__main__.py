import re

lines = open(f'4/input.txt').read().split('\n\n')
draws = lines[0].split(',')
boards = lines[1:]

win_boards = {}
curr_boards = boards

for i in range(1, len(draws)+1):
    current_draw = draws[:i]
    left_boards = []

    for board in curr_boards:
        row_data = board.replace('\n ', '\n').split('\n')
        rows = []
        for row in row_data:
            rows.append(row.replace('  ', ' ').split(' '))
        cols = zip(*rows)

        found = False
        for row in rows:
            cnt = 0
            for cell in row:
                if cell in current_draw:
                    cnt += 1
            if cnt == 5:
                found = True
                win_boards.setdefault(i, [])
                win_boards[i].append(board)
                break
        if found:
            continue
        for col in cols:
            cnt = 0
            for cell in col:
                if cell in current_draw:
                    cnt += 1
            if cnt == 5:
                found = True
                win_boards.setdefault(i, [])
                win_boards[i].append(board)
                break
        if found:
            continue
        left_boards.append(board)
    curr_boards = left_boards

def board_nums(board):
    return board.replace('\n', ' ').replace('  ', ' ').split(' ')

min_index = min(win_boards.keys())
min_board = win_boards[min_index][0]
min_left = sum([int(num) for num in board_nums(min_board) if num not in draws[:min_index]])
print(min_left * int(draws[min_index-1]))

max_index = max(win_boards.keys())
max_board = win_boards[max_index][0]
max_left = sum([int(num) for num in board_nums(max_board) if num not in draws[:max_index]])
print(max_left * int(draws[max_index-1]))