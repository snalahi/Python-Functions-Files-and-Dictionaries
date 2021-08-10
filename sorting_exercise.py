# Create a function called last_four that takes in an ID number and returns the last four digits. For example, the number 17573005 should return 3005. Then,
# use this function to sort the list of ids stored in the variable, ids, from lowest to highest. Save this sorted list in the variable, sorted_ids. Hint:
# Remember that only strings can be indexed, so conversions may be needed.

def last_four(x):
  return int(str(x)[-4])

ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]

sorted_ids = sorted(ids, key=last_four)

# Sort the list ids by the last four digits of each id. Do this using lambda and not using a defined function. Save this sorted list in the variable
# sorted_id.

ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
sorted_id = sorted(ids, key=lambda num: int(str(num)[-4]))

# Sort the following list by each element’s second letter a to z. Do so by using lambda. Assign the resulting value to the variable lambda_sort.

ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']
lambda_sort = sorted(ex_lst, key=lambda ex: ex[1])

