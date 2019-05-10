""" Task
Write the processArray function, which takes an array and a callback function as parameters. The callback function can be, for example, a mathematical function that will be applied on each element of this array. Optionally, also write tests similar to the examples below.

Examples
1) Array [4, 8, 2, 7, 5] after processing with function

function(a): return a*2;
will be [ 8, 16, 4, 14, 10 ].

2) Array [7, 8, 9, 1, 2] after processing with function

function(a): return a+5;
will be [ 12, 13, 14, 6, 7 ]. """

def process_array(arr, callback):
    # initialize new array
    new_array = []
    # for every item in the passed in array, append that to the new array after it has been passed through the callback funcction
    for i in arr: 
      new_array.append(callback(i))
    return new_array

my_array = [4, 8, 2, 7, 5]
func = lambda val: val * 2
my_array = process_array(my_array, func)
print(my_array)
# test.assert_equals(my_array, [ 8, 16, 4, 14, 10 ], 'The result array is wrong.');

my_array = [7, 8, 9, 1, 2];
func = lambda val: val + 5
my_array = process_array(my_array, func)
print(my_array)
# test.assert_equals(my_array, [ 12, 13, 14, 6, 7 ], 'The result array is wrong.');

my_array = [-1, 1, 2, 3, 4, 5];
func = lambda val: val ** 3
my_array = process_array(my_array, func)
print(my_array)
# test.assert_equals(my_array, [ -1, 1, 8, 27, 64, 125 ], 'The result array is wrong.');

# Best Practice Solutions: 

# def process_array(arr, callback):
#     return map(callback, arr)

# def process_array(arr, callback):
#     new_arr = [callback(x) for x in arr]
#     return new_arr