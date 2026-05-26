def get_flatten_single_level_array(two_d_array):
    
    single_array = []
    for count in  two_d_array:
    
        for number in count:
        
            single_array.append(number)
            
    return single_array


def rotate_number_in_index(array, k):
    new_array = array
    
    if k == len(array):
        
        return array
        
    
    steps = k % len(new_array)
    
    for count in range(steps):

        last_item = new_array.pop()
        
        new_array.insert(0, last_item)
        
    return new_array
    
