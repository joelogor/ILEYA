from unittest import TestCase

from book_suggetion_app import *


class Test_Book_Suggetion_App(TestCase):

    def test_that_app_keep_suggesting_book_with_random_page_number_between_one_and_hundred(self):
    
      
        actual = suggest_random_page()
    
        self.assertTrue(actual >= 1)
        
        self.assertTrue(actual <= 100)
    
#    def test_that_suggestion_stop_when_user_decide_to_stop(self):
#    
#      
#        actual = suggest_random_page()
#    
#        self.assertTrue(actual >= 1)
#        
#        self.assertTrue(actual <= 100)
#          
    def test_that_User_can_add_a_new_book_to_the_list(self):
    
        book_list = ["The Hobbit", "The Mystery", "Brave kind"]
        new_book = "Animal Farm"
        
        expected =["The Hobbit", "The Mystery", "Brave kind", "Animal Farm"]
    
        actual = add_new_book(book_list,new_book  )
    
        self.assertEqual(expected, actual ) 
        
    def test_that_user_can_remove_a_book_from_the_list(self):
    
        book_list = ["The Hobbit", "The Mystery", "Brave kind"]
        book_to_remove = "The Mystery"
        expected = ["The Hobbit",  "Brave kind"]
    
        actual = remove_book(book_list, book_to_remove)
    
        self.assertEqual(expected, actual ) 
              
    def test_that_user_can_update_a_book_in_the_list(self):
    
        book_list = ["The Hobbit", "The Mystery", "Brave kind"]
        book_to_update = "The Mystery"
        new_book_title =  "Brave kingdom"
        
        expected = ["The Hobbit", "Brave kingdom", "Brave kind"]
    
        actual = update_book(book_list, book_to_update, new_book_title)
    
        self.assertEqual(expected, actual )
        
     
    def test_that_user_can_view_list_of_books_in_the_list(self):
    
        book_list = ["The Hobbit", "Brave kingdom", "Animal Farm", "Brave kind"]
        
        expected = "1. The Hobbit\n2. Brave kingdom\n3. Animal Farm\n4. Brave kind\n"  
    
        actual = view_list(book_list)
    
        self.assertEqual(expected, actual )
                      
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
                      
        
