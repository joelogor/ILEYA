def get_split_array(array):

    list_even = []
    list_odd = []
    
    for count in range (len(array)):
        
        if array[count] %2 == 0:
        
            list_even.append(array[count])
        else:
            list_odd.append(array[count])
        

    return [list_odd, list_even]
    
def check_is_palindromic(array):
    
    for count in range (len(array)):
    
        for index in range (len(array), 1):
    
            if array[count] == array[index]:
                
            
                return True
                
    return False
    
def check_perfect_square(array):
    list_perfect_square = []
    for count in range (len(array)):
        
        if (array[count]**0.5) %1  == 0:
        
            list_perfect_square.append(array[count])
            
    return list_perfect_square
    
def replace_non_perfect_square(array):
    new_list = []
    for count in range (len(array)):
    
         if (array[count]**0.5) %1  != 0:
         
            new_list.append(-1)
            
         elif (array[count]**0.5) %1  == 0:
            
            new_list.append(array[count])
            

    return new_list
    
    
    
    
    
    
        
        
        
    
    
print(replace_non_perfect_square([4, 6, 9, 7, 45 ]))    
#print(get_split_array([45,60,3,10,9,22]))
