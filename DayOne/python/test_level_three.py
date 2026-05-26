from unittest import TestCase

from level_three import *



class Test_Level_Three(TestCase):

    def test_that_given_two_dimension_array_return_a_single_level_array(self):
    
        array =  [[9, 0, 7], [3, 5, 1], [8, 1, 7], [9, 9, 6]] 
        
        expected = [9, 0, 7, 3, 5, 1, 8, 1, 7, 9, 9, 6]
        
        actual = get_flatten_single_level_array([[9, 0, 7], [3, 5, 1], [8, 1, 7], [9, 9, 6]] )
       
        self.assertEqual(expected, actual )
        
         
