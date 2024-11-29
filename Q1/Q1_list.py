def flatten_list(nested):
    for i in nested:
        if isinstance(i, list):
            for value in flatten_list(i):  
                yield value
        else:
            yield i

original_list = [[5, 2], 1, [4, 3, 8, [9, 7]]]
flattened_list = list(flatten_list(original_list))
print(flattened_list)  
