def print_board(bo):
	for i in range(len(bo)):
		if i % 3 == 0 and i != 0:
			print('- - - - - - - - - - - ')

		for j in range(len(bo[0])):
			if j % 3 == 0 and j != 0:
				print("|", end =' ')

			if j == 8:
				print(bo[i][j])

			else:
				print(bo[i][j],'', end = '')

def find_empty(bo):
	for i, row in enumerate(bo):
		for j, val in enumerate(row):
			if val == 0:
				return (i, j) #(row, column)

	return None

def valid(bo, num, pos):
	#row
	for i in range(len(bo[0])):
		if bo[pos[0]][i] == num and pos[1] != i:
			return False

	#column
	for i in range(len(bo)):
		if bo[i][pos[1]] == num and pos[0] != i:
			return False

	#box
	box_row = pos[0]//3
	box_col = pos[1]//3
	
	for i in range(box_row * 3, box_row * 3 + 3):
		for j in range(box_col * 3, box_col * 3 + 3):
			if bo[i][j] == num and pos != (i, j):
				return False

	return True

def solve(bo):
	empty = find_empty(bo)
	if not empty:
		return True
	else:
		row, col = empty

	for i in range(1, 10):
		if valid(bo, i, (row, col)):
			bo[row][col] = i

			if solve(bo):
				return True

			bo[row][col] = 0

	return False

def main():
	print_board(board)
	print('\n\n')
	solve(board)
	print_board(board)

if __name__ == '__main__':
	board = [
		[5, 3, 0, 0, 7, 0, 0, 0, 0],
		[6, 0, 0, 1, 9, 5, 0, 0, 0],
		[0, 9, 8, 0, 0, 0, 0, 6, 0],
		[8, 0, 0, 0, 6, 0, 0, 0, 3],
		[4, 0, 0, 8, 0, 3, 0, 0, 1],
		[7, 0, 0, 0, 2, 0, 0, 0, 6],
		[0, 6, 0, 0, 0, 0, 2, 8, 0],
		[0, 0, 0, 4, 1, 9, 0, 0, 5],
		[0, 0, 0, 0, 8, 0, 0, 7, 9]
	]
	main()