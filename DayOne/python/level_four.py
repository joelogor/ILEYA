def check_count(text):

    vowel_count = 0
    consonant_count = 0
    
    real_text = text.lower()
    vowel = "aeiou"
  
    for letter in real_text:
        
        if letter.isalpha():
        
            if letter in vowel:
            
                vowel_count += 1
                
            else:
            
                consonant_count += 1
                
    return  [ ["vowels" , vowel_count], ["consonants", consonant_count]]                
                
    
def get_run_length(text):
    
    for char in text:
    
        if      
    
          
       
