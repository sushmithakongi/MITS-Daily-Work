"""Write a function in Python to check duplicate letters. It must accept a string, 
i.e., a sentence. The function should return True if the sentence has any word with
duplicate letters, else return False."""
def is_isogram(string):
    for i in string:
        if string.count(i) > 1:
            return True
    return False
string=input()
print(is_isogram(string))