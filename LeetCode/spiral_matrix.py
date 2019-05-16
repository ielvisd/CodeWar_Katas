""" Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
	[1, 2, 3, 4],
	[5, 6, 7, 8],
	[9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7] """


class Solution:

		def spiralOrder(self, matrix: [[int]]) -> [int]:

				output = []

				number_of_rows = len(matrix)

				if number_of_rows == 0:
								return output

				number_of_columns = len(matrix[0])

				print(number_of_rows)
				print(number_of_columns)

				total_elements = number_of_rows * number_of_columns

				print(total_elements)

				current_row = 0
				current_column = 0

				move_down = False
				move_left = False
				move_up = False
				move_right = True

				remaining_rows = number_of_rows
				remaining_columns = number_of_columns

				while len(output) < total_elements:

						if current_row == 0 and current_column == 0:

								if number_of_columns == 1:
										for number in range(0, remaining_rows):
												print(f"number is {number}")
												output.append(matrix[current_row][current_column])
												current_row += 1
										return output

								move_right == True

						# If move-right is true, then move right along the current row from the current column to the end of the row, adding numbers to the output as you go along. ()
						if (move_right == True):

								if(remaining_rows == 1):
										for number in range(0, remaining_columns):
												print(f"number is {number}")
												output.append(matrix[current_row][current_column])
												current_column += 1
										return output
								else:
										for number in range(current_column, current_column + remaining_columns):
												output.append(matrix[current_row][current_column])
												current_column += 1
								current_column -= 1
								remaining_rows -= 1
								# Go down a row, set move_down to true and move_right to False
								move_down = True
								move_right = False
								print((output))

						# If move_down is true
						if (move_down == True):
								current_row += 1
								if(remaining_columns == 1):
										for number in range(0, remaining_rows):
												print(f"number is {number}")
												output.append(matrix[current_row][current_column])
												current_row += 1
										return output
								else: 									
									for number in range(current_row, current_row + remaining_rows):
											output.append(matrix[number][current_column])
											current_row += 1
								current_row -= 1
								remaining_columns -= 1
								move_left = True
								move_down = False
								print((output))

						# If move_left is true
						if (move_left == True):
								current_column -= 1


								if(remaining_rows == 1):
										for number in range(0, remaining_columns):
												print(f"number is {number}")
												output.append(matrix[current_row][current_column])
												current_column -= 1
										return output
								else:
										for number in range(current_column, current_column - remaining_columns, -1):
											output.append(matrix[current_row][number])
											current_column -= 1
								current_column += 1
								remaining_rows -= 1
								move_up = True
								move_left = False
								print((output))

						# If move_up is true
						if (move_up == True):
								current_row -= 1
								for number in range(current_row, current_row - remaining_rows, -1):
										output.append(matrix[number][current_column])
										current_row -= 1
								remaining_columns -= 1
								current_row += 1
								current_column += 1
								move_right = True
								move_up = False
								print((output))

				return output


solution = Solution()


# print(solution.spiralOrder([
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]))

# print(solution.spiralOrder([
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]))

# print(solution.spiralOrder([
#     [1], [4]]))

print(solution.spiralOrder([[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]))

