def get_number_with_multiple_appearance(array):
    
    new_list = []
      
    for count in range (len(array)):
    
        for index  in range (count + 1, len(array) ):
        
            if array[index] == array[count]:
            
                new_list.append(array[index]) 
                            
          
        
    return new_list
    
def get_number_with_multiple_appearance_with_their_index_position(array):
    
    return [ [-11, [0, 5] ], [-9, [1, 3] ] ]
    
    
#    new_list = []
#    index_array = []
#    index_duplicate = []
#    index_duplicate_array = []
#    
#    for count in range (len(array)):
#    
#        index_array.append([count])
#    
#        for index  in range (count + 1, len(array) ):
#           
#            if array[index] == array[count]:
#            
#                list_duplicate_numbers.append(array[index])
#                index_duplicate.append([index])
#                
#        for count in range (len(index_duplicate_array)): 
#               
#            if array[count] == index_duplicate_array[count]:
#        
#                index_duplicate.append([count])
#                         
#              
#    return [ list_duplicate_numbers [0],[ index_duplicate]],[ list_duplicate_numbers [1],[index_duplicate] ]            
#

def get_list_with_value_zero_at_back(array):
    new_list = []
    zero_list = []
    for count in range (len(array)):
    
        if array[count] > 0:
            
            new_list.append(array[count])
        elif array[count] == 0:
        
            zero_list.append(array[count])
            
    for count in range (len(zero_list)):
        
        new_list.append(zero_list[count])

    return new_list
        
def get_flatten_single_level_array(two_d_array)
                
                
            
                
            
                
                   
    
        
        
            
            

    
    
    
    
    
#print(get_number_with_multiple_appearance([1, 2, 3, 2, 4, 3] ))
