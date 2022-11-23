seq = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = filter(lambda x: x % 2 != 0, seq)  # result contains odd numbers of the list
print(list(result))

result = filter(lambda x: x % 2 == 0, seq)  # result contains even numbers of the list
print(list(result))

# Below is the Output :
[1, 3, 5, 7, 9]
[0, 2, 4, 6, 8, 10]
