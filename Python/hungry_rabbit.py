""" Hungry Rabbit
A very hungry rabbit is placed in the center of of a garden, represented by a rectangular N x M 2D matrix.

The values of the matrix will represent numbers of carrots available to the rabbit in each square of the garden. If the garden does not have an exact center, the rabbit should start in the square closest to the center with the highest carrot count.

On a given turn, the rabbit will eat the carrots available on the square that it is on, and then move up, down, left, or right, choosing the the square that has the most carrots. If there are no carrots left on any of the adjacent squares, the rabbit will go to sleep. You may assume that the rabbit will never have to choose between two squares with the same number of carrots.

Write a function which takes a garden matrix and returns the number of carrots the rabbit eats. You may assume the matrix is rectangular with at least 1 row and 1 column, and that it is populated with non-negative integers. For example,

[[5, 7, 8, 6, 3],
 [0, 0, 7, 0, 4],
 [4, 6, 3, 4, 9],
 [3, 1, 0, 5, 8]]
Should return

27
 """

import math

def hungry_rabbit(garden_matrix):

  # Assumptions
    # Shape of garden: N x M rectangular 2D matrix
    # Minimum size of garden: 1x1 matrix
    # Values of squares in garden represent # of carrots
    # Squares are non-negative integers

  # Algorithm

    # Initialize the number of carrots eaten
  carrots_eaten = 0

    # Place rabbit in initial square
      # Check if it's a square matrix (if N == M)

  number_of_rows = len(garden_matrix); 
  print(f'The number of rows are: ', number_of_rows)
  number_of_columns = len(garden_matrix[0])
  print(f'The number of columns are: ', number_of_columns)

  if (number_of_rows == number_of_columns):
    # Rabbit starts in the center
    rabbit_N_location = int(number_of_rows/2)
    print(f'Rabbits N Location is: ', rabbit_N_location)
    rabbit_M_location = int(number_of_columns/2)
    print(f'Rabbits N Location is: ', rabbit_M_location)

    # If garden has no center, rabbit starts at square closest to center with highest # of carrots
  else: 
    if (number_of_rows % 2 == 0):
      rabbit_N1_location = int(number_of_rows/2) - 1
      rabbit_N2_location = int(number_of_rows/2) 
      print(f'Rabbits N1 Location is: ', rabbit_N1_location)
      print(f'Rabbits N2 Location is: ', rabbit_N2_location)
      rows_even = False
    else:   
      rabbit_N_location = int(number_of_rows/2)
      rows_even = True
    if (number_of_columns % 2 == 0):
      columns_even = False
      rabbit_M1_location = int(number_of_columns/2)
      rabbit_M2_location = int(number_of_columns/2) + 1
      print(f'Rabbits M1 Location is: ', rabbit_M1_location)
      print(f'Rabbits M2 Location is: ', rabbit_M2_location)
    else:
      rabbit_M_location = int(number_of_rows/2)
      columns_even = True


    if (rows_even == False and columns_even == True): 
      # Test both squares and start at the one with most amount of carrots
      square_one_carrots = garden_matrix[rabbit_N1_location][rabbit_M_location]
      square_two_carrots = garden_matrix[rabbit_N2_location][rabbit_M_location]

      if (square_one_carrots >= square_two_carrots):
        rabbit_N_location = rabbit_N1_location
      else: 
        rabbit_N_location = rabbit_N2_location


    

  # While there is a carrot on the current square eat it and move to next square with highest # of carrots (if any, else sleep)
  while(garden_matrix[rabbit_N_location][rabbit_M_location] != 0):
    print("Eating a yummy carrot")
    carrots_eaten += garden_matrix[rabbit_N_location][rabbit_M_location]
    garden_matrix[rabbit_N_location][rabbit_M_location] = 0

    # Set the # of carrots in N, S, E & W directions

    north_carrots = 0
    south_carrots = 0
    west_carrots = 0
    east_carrots = 0

    # directions & carrots

    
  # check if locations in range otherwise don't move
    if rabbit_M_location + 1 < number_of_columns:
      north_location = rabbit_N_location - 1 
      if north_location < 0:
        north_location = 0
    else: 
      north_location = rabbit_N_location
    if rabbit_M_location - 1 > number_of_columns:
      south_location = rabbit_N_location + 1
    else: 
      south_location = rabbit_N_location 
    if rabbit_N_location + 1 < number_of_rows:
      east_location = rabbit_M_location + 1
    else: 
      east_location = rabbit_M_location
    if rabbit_N_location - 1 > number_of_rows:
      west_location = rabbit_M_location - 1
      if west_location < 0:
        north_location = 0
    else: 
      west_location = rabbit_N_location

    north_carrots = garden_matrix[north_location][rabbit_M_location]
    south_carrots = garden_matrix[south_location][rabbit_M_location]
    west_carrots = garden_matrix[rabbit_N_location][west_location]
    east_carrots = garden_matrix[rabbit_N_location][east_location]

    # available directions & carrots:
    directions_available = {
      north_carrots: north_location,
      south_carrots: south_location,
      west_carrots: west_location, 
      east_carrots: east_location
    }
  
    # If all directions are zero or None then sleep (exit)
    if (north_carrots == south_carrots == west_carrots == east_carrots == 0):
        return carrots_eaten

    # Otherwise move to the location with the highest carrot count
    else:
      direction = max(north_carrots, south_carrots, east_carrots, west_carrots)
      
      # If direction is North or South move rabbits M location
      if (direction == north_carrots or direction == south_carrots):
        rabbit_N_location = directions_available[direction]
      elif (direction == north_carrots or direction == south_carrots):
        rabbit_M_location = directions_available[direction]

      # If direction is East or West move the rabbits N location

# print(hungry_rabbit([[1]]))

print(hungry_rabbit([[5, 7, 8, 6, 3],
 [0, 0, 7, 0, 4],
 [4, 6, 3, 4, 9],
 [3, 1, 0, 5, 8]]))







