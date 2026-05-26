from unittest import TestCase

from level_two import *



class Test_Level_Two(TestCase):


    def test_that_given_array_return_list_with_vlaues_that_apper_more_than_once(self):
    
        array =  [1, 2, 3, 2, 4, 3] 
        
        expected = [2,3]
        
        actual = get_number_with_multiple_appearance([1, 2, 3, 2, 4, 3] )
       
        self.assertEqual(expected, actual )
        
    def test_that_given_array_return_list_with_vlaues_that_apper_more_than_once_and_where_they_appeared(self):
    
        array =  [-11, -9, 3, -9, 2, -11] 
        expected = [ [-11, [0, 5] ], [-9, [1, 3] ] ]
        
        actual = get_number_with_multiple_appearance_with_their_index_position([-11, -9, 3, -9, 2, -11] )
        
        self.assertEqual(expected, actual )
        
    def test_that_given_array_return_list_with_vlaues_equal_to_zero__at_end(self):
    
        array =  [5, 0 , 3, 0, 2, 0] 
        
        expected = [5, 3 , 2 , 0, 0 , 0]
        
        actual = get_list_with_value_zero_at_back([5, 0 , 3, 0, 2, 0]  )
       
        self.assertEqual(expected, actual )
        
    def test_that_given_two_dimension_array_return_a_single_level_array(self):
    
        array =  [[9, 0, 7], [3, 5, 1], [8, 1, 7], [9, 9, 6]] 
        
        expected = [9, 0, 7, 3, 5, 1, 8, 1, 7, 9, 9, 6]
        
        actual = get_flatten_single_level_array([[9, 0, 7], [3, 5, 1], [8, 1, 7], [9, 9, 6]] )
       
        self.assertEqual(expected, actual )
        
        
