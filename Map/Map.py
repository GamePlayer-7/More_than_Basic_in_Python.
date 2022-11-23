def square(n):
    return n*n
my_list = [2, 3, 4, 5, 6, 7, 8, 9]
updated_list = map(square, my_list)
print(updated_list)
print(list(updated_list))             # We have to iterate the output from map using a for-loop or using list() method to get the final output.

# Below is the Output :

<map object at 0x000000585B527940>
[4, 9, 16, 25, 36, 49, 64, 81]
