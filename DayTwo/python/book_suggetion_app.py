import random

def suggest_random_page():

    return random.randint(1, 100)
    
def add_new_book(book_list, book_to_add):

    lists = ["The Hobbit", "The Mystery", "Brave kind"]
    to_add = "Animal Farm"
  
    lists.append(to_add)
    
    return lists   
def remove_book(book_list, book_to_remove):

    lists = ["The Hobbit", "The Mystery", "Brave kind"]
    to_remove = "The Mystery"
  
    lists.remove(to_remove)
    
    return lists
    

def update_book(book_list, book_to_update, new_book_title):

    lists = ["The Hobbit", "The Mystery", "Brave kind"]
    to_update = "The Mystery"
    new_book = "Brave kingdom"
    
    for count in range (len(lists)):
  
        if lists[count] ==  to_update:
        
            lists[count] = new_book
    
    return lists
    
    
def view_list(book_list):
    
    list_view = ""
    for count in range (len(book_list)):
    
        list_view += f"{count + 1}. {book_list[count]}\n" 
        
    return list_view 
    
    
    
    
    
    
    
                

        
