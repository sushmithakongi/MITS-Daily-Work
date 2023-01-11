def anagram (str1, str2):
    if (sorted(str1) == sorted(str2)):  
      return True 
    else:  
      return False 
str1 = input ("Please enter String 1: ")
str2 = input ("Please enter String 2: ")
if anagram (str1, str2):
    print("Anagram")
else:
    print ("Not an anagram")
