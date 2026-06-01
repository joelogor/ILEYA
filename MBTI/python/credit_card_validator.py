def validate_card_number_length(card_number):

    card_number = "5399831619698408"
    if len(card_number) >= 13 or len(card_number) <= 16 :
    
        return True

def  validate_card_type(card_number):

    number = "5399831619698408"
    
        
    if card_number[0] == "4":
        return "Visa Card" 
            
    elif card_number[0] ==  "5":
        
        return "Master Card"
        
    elif card_number[0] == "3" and card_number[1] == "7":
        
        return "American Express Card" 
            
    elif card_number[0] == "6":
        
        return "Discover Card"
        
        
def luhn_check_step_one(card_number):
    
    number =  [] 
        
    for count in range (1, len(card_number)-1, 1 ):
        
        digit = int(card_number[count])
        
        if count % 2 == 0:
            if digit*2 >= 0 and digit <= 9 :
            
                number.append(digit*2)
                    
            elif digit *2 > 9 :
                
                number.append(((digit*2) // 10 )+ ((digit*2 )% 10))
                    
    return number
                
                   
        
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
