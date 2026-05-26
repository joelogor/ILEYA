from unittest import TestCase

from level_one import *


class LevelOneTest(TestCase):


    def test_that_array_passed_return_split_of_the_array_to_odd_and_even_arrays(self):
    
        array = [45,60,3,10,9,22]
        
        expected = [[45,3,9], [60,10,22]]
        
        actual = get_split_array([45,60,3,10,9,22])
        
        self.assertEqual(expected,actual )
        
    def test_that_list_of_array_is_palindromic(self):
    
        array = [45, 0, 8, 0, 45 ] 
        
        expected = True
        
        actual = check_is_palindromic([45, 0, 8, 0, 45 ])
        
        self.assertTrue(expected,actual  )
    
    def test_that_list_of_array_is_not_palindromic(self):
    
        array = [45, 0, 8, 0, 1 ] 
        
        expected = True
        
        actual = check_is_palindromic([45, 0, 8, 0, 45 ])
        
        self.assertTrue(expected,actual  )
        
        
    def test_that_i_pass_list_of_array_it_return_all_list_of_perfect_squares(self):
    
        array = [4, 7, 9, 10, 16, 18] 
        
        expected = [4, 9, 16]
        
        actual = check_perfect_square([4, 7, 9, 10, 16, 18] )
        
        self.assertEqual(expected,actual  )
                
               
    def test_that_i_pass_list_of_array_it_return_the_list_with_non_perfect_squares_as_negative_one(self):
    
        array = [4, 7, 9, 10, 49, 6] 
        
        expected =  [4, -1, 9, -1, 49 , -1]
        
        actual = replace_non_perfect_square( [4, 7, 9, 10, 49, 6])
        
        self.assertEqual(expected,actual)
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
           
