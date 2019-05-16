# def IDsOfPackages(truckSpace, packagesSpace):

#     # Algorithm
#     original = packagesSpace.copy()
#     # Sort the packagesSpace list by size
#     packagesSpace.sort(reverse=True)

#     # target = 30 (for safety, per the proble spec)
#     target = truckSpace - 30

#     # length of packageSpace list
#     length_of_packagesSpace = len(packagesSpace)

#     # For every space in the list, check the remaining elements in the list for the first time you match the target
#     for item in range(0, length_of_packagesSpace):
#         for remaining_items in range(1, length_of_packagesSpace - 1):
#             # if the target's match, lookup the original index from the list and sort if necessary
#             if packagesSpace[item] + packagesSpace[remaining_items] == target:
#                 first_items_index = original.index(packagesSpace[item])
#                 second_item_index = original.index(packagesSpace[remaining_items])
#                 answer = ([first_items_index, second_item_index])
#                 answer.sort()
#                 return answer


# print(IDsOfPackages(110, [20, 70, 90, 30, 60, 100]))

# print(IDsOfPackages(250, [100, 180, 40, 120, 10]))

# print(IDsOfPackages(90, [1, 10, 25, 35, 60]))


def optimalUtilization(maxTravelDist, forwardRouteList, returnRouteList):

    # Assume I get at least one route in the forwardRouteList and one in the returnRouteList

    # initialize a dictionary of possible optimal routes

    #Example    
    # 
    # optimal_routes = {
    #  2 : 4
    #  3 : 2
    #}

    current_best_distance = 0


    optimal_routes_dictionary = {
    }

    # Will add arrays into this list when we are done from the optimal_routes dictionary
    optimal_routes_list = []

    max_travel_distance = maxTravelDist

    length_of_forwardRouteList = len(forwardRouteList)
    length_of_returnRouteList = len(returnRouteList)

    # First time through both lists just want to find the best distance
    # For every route in the forward list
    for forward_route in range(0, length_of_forwardRouteList):
      forward_distance = forwardRouteList[forward_route][1]
      # For every route in the return list
      for return_route in range(0, length_of_returnRouteList):
        return_distance = returnRouteList[return_route][1]
        total_distance = forward_distance + return_distance

        if (total_distance >= current_best_distance and total_distance <max_travel_distance):
          current_best_distance = total_distance

    # During the second pass I'll pull the best routes from the available options
    for forward_route in range(0, length_of_forwardRouteList):
      forward_distance = forwardRouteList[forward_route][1]
      # For every route in the return list
      for return_route in range(0, length_of_returnRouteList):
        return_distance = returnRouteList[return_route][1]
        total_distance = forward_distance + return_distance

        if (total_distance == current_best_distance):
          optimal_routes_dictionary[forwardRouteList[forward_route][0]] = returnRouteList[return_route][0]

    print(current_best_distance)

    # For key value pair in dictionary add to results list

    for key, value in optimal_routes_dictionary.items(): 
      optimal_routes_list.append([key,value])

    return optimal_routes_list

print(optimalUtilization(7000, [[1, 2000], [2, 4000], [3,6000]], [[1,2000]]))