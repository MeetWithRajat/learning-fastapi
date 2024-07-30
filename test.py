import copy

original_object = {'key1': 'value1', 'key2': [1, 2, 3]}
shallow_copy_object = copy.copy(original_object)

# Modify the original object
original_object['key1'] = 'new_value'
original_object['key2'].append(4)
shallow_copy_object['key2'].append(5)

# Now you can compare the original object and the shallow copy
print("Original Object:", original_object)
print("Shallow Copy Object:", shallow_copy_object)


original_object2 = {'key1': 'value1', 'key2': [1, 2, 3]}
deep_copy_object2 = copy.deepcopy(original_object2)

# Modify the original object
original_object2['key1'] = 'new_value'
original_object2['key2'].append(4)
deep_copy_object2['key2'].append(5)

# Now you can compare the original object and the deep copy
print("\nOriginal Object:", original_object2)
print("Deep Copy Object:", deep_copy_object2)
