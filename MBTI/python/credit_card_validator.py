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
    
    number_list =  [] 
        
    for count in range (0,len(card_number), 1 ):
        
        digit = int(card_number[count])
        
        if count % 2 == 0:
            if digit *2 > 9 :
                
                number_list.append((digit*2 // 10 )+ (digit*2 % 10))
                    
            elif digit*2 >= 0 and digit <= 9 :
            
                number_list.append(digit*2)
                    
    result = result = "".join(str(number) for number in number_list)[::-1]
    
    return result
    
def luhn_check_step_two(card_number):
    
    sum_ = 0
    
    digits_step_one = luhn_check_step_one(card_number)

    for count in range (len(digits_step_one)):
    
        sum_ += int(digits_step_one[count])
    
    return sum_
    
def luhn_check_step_three(card_number):

    number_list =  [] 
    
    sum_ = 0
        
    for count in range (0,len(card_number), 1 ):
        
        digit = int(card_number[count])
        
        if count % 2 == 1:
        
            sum_ += digit
    
    return sum_   
    
def luhn_check_step_four(card_number):

    step_two = luhn_check_step_two(card_number)
    
    step_three = luhn_check_step_three(card_number)                 
    
    return step_two + step_three
          

def luhn_check_step_five(card_number):

    result = luhn_check_step_four(card_number)
    
    if result % 10 == 0:
    
        return "Is Valid"
    
    else:
        
        return "Is Invalid"                
                   
        
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
