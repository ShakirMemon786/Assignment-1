def char_frequency(str):
    dict={}
    
    for n in str:
        
        if n in dict:
            dict[n] +=1
        else:
            dict[n] = 1
    return dict
print("Total number of character count in string: ",char_frequency('google.com'))    
