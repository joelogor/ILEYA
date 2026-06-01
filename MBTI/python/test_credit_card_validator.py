from unittest import TestCase

from credit_card_validator import *


class Credit_Card_Validator(TestCase):

    def test_that_credit_card_numbers_witht_length_between_thirteen_and_sixteen_digits_is_valid(self):
    
        is_valid = validate_card_number_length("5399831619698408")
        
        self.assertTrue(is_valid)
    
    def test_that_credit_card_numbers_witht_length_less_than_13_digits_is_invalid(self):
    
        is_invalid = validate_card_number_length("31619698408")
        
        self.assertTrue(is_invalid)
    
    def test_that_credit_card_numbers_witht_length_more_than_16_digits_is_invalid(self):
    
        is_invalid = validate_card_number_length("5388899831619698408")
        
        self.assertTrue(is_invalid)
        
            
    def test_that_credit_card_numbers_starts_with_4_is_visa_card(self):
        
        expected = "Visa Card"
        actual = validate_card_type("4399831619698408")
        
        self.assertEqual(actual,expected ) 
        
    def test_that_credit_card_numbers_starts_with_5_is_visa_card(self):
        
        expected = "Master Card"
        actual = validate_card_type("5399831619698408")
        
        self.assertEqual(actual,expected )
        
    def test_that_credit_card_numbers_starts_with_37_is_visa_card(self):
        
        expected = "American Express Card" 
        actual = validate_card_type("3799831619698408")
        
        self.assertEqual(actual,expected ) 
                         
    def test_that_credit_card_numbers_starts_with_6_is_visa_card(self):
        
        expected = "Discover Card"
        actual = validate_card_type("6399831619698408")
        
        self.assertEqual(actual,expected )
        
    def test_that_all_second_digits_from_left_are_each_doubled_and_all_summed_with_doubled_number_with_two_digit_added_to_make_one_digit(self):
    
        card_number = "4388576018402626"
        
        expected = "44823178"
        actual = luhn_check_step_one(card_number)
        
        self.assertEqual(expected, actual)
        
    def test_that_all_second_digits_from_left_are_each_doubled_and_all_summed_with_doubled_number_with_two_digit_added_to_make_one_digit_and_the_result_added(self):
    
        card_number = "4388576018402626"
        
        expected = 37
        actual = luhn_check_step_two(card_number)
        
        self.assertEqual(expected, actual)
                          
    def test_that_all_digits_in_odd_places_from_left_are_added(self):
    
        card_number = "4388576018402626"
        
        expected = 38
        actual = luhn_check_step_three(card_number)
        
        self.assertEqual(expected, actual)
               
    def test_that_result_from_step_2_and_step_3_are_added(self):
    
        card_number = "4388576018402626"
        
        expected = 75
        actual = luhn_check_step_four(card_number)
        
        self.assertEqual(expected, actual)

    def test_that_result_from_step_2_and_step_3_are_added_and_if_divisible_by_10_is_valid(self):
    
        card_number = "4388576018410707"
        
        expected = "Is Valid"
        actual = luhn_check_step_five(card_number)
        
        self.assertEqual(expected, actual)                
        
    def test_that_result_from_step_2_and_step_3_are_added_and_if_not_divisible_by_10_is_valid(self):
    
        card_number = "4388576018402626"
        
        expected = "Is Invalid"
        actual = luhn_check_step_five(card_number)
        
        self.assertEqual(expected, actual)          
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
         
         
       
