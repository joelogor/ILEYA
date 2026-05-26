from unittest import TestCase

from level_three import *



class Test_Level_Three(TestCase):

    def test_that_given_two_dimension_array_return_a_single_level_array(self):
    
        array =  [[9, 0, 7], [3, 5, 1], [8, 1, 7], [9, 9, 6]] 
        
        expected = [9, 0, 7, 3, 5, 1, 8, 1, 7, 9, 9, 6]
        
        actual = get_flatten_single_level_array([[9, 0, 7], [3, 5, 1], [8, 1, 7], [9, 9, 6]] )
       
        self.assertEqual(expected, actual )


    def test_that_array_is_passed_it_rorate_number_in_given_index_at_back_of_same_index_from_back(self):
    
        array =  [1, -9, 3, 0, 8] 
        index = 2 
        
        expected = [0, 8, 1, -9, 3]
        
        actual = rotate_number_in_index(array, index )
       
        self.assertEqual(expected, actual )
        
                     
    def test_that_array_is_returned_if_k_equal_length_of_array(self):
    
        array =   [1, -9, 3, 0, 8] 
        index = 5
        
        expected =  [1, -9, 3, 0, 8]
        
        actual = rotate_number_in_index(array, index )
       
        self.assertEqual(expected, actual )
        
                 
