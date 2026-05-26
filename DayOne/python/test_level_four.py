from unittest import TestCase

from level_four import *



class Test_Level_Four(TestCase):


    def test_that_given_text_returns_number_of_vowels_and_consonants_in_array(self):
    
        text = "Hello - World"  
        
        expected =  [ ["vowels" , 3], ["consonants", 7] ]
        
        actual = check_count("Hello - World" )
        self.assertEqual(expected, actual)
        
    def test_that_given_text_returns_run_time_length(self):
    
        text = "aaabbc"  
        
        expected =  "a3b2c" 
        
        actual = get_run_length( text  )
        self.assertEqual(expected, actual)
    
        
