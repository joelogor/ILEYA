def get_flatten_single_level_array(two_d_array):
    
    single_array = []
    for count in  two_d_array:
    
        for number in count:
        
            single_array.append(number)
            
    return single_array

    
