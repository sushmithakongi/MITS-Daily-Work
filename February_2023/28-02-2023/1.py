# A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

# For example, "Hello World", "HELLO", "hello world hello world" are all sentences.
# Words consist of only uppercase and lowercase English letters. Uppercase and lowercase English letters are considered different.

# A sentence is circular if:

# The last character of a word is equal to the first character of the next word.
# The last character of the last word is equal to the first character of the first word.

class Solution:
    def isCircularSentence(self, sentence):
        print(sentence[0],sentence[-1])
        if sentence[0]!=sentence[-1]:
            return "false"
            
        else:
            li=sentence.split()
            if li[0][0]==li[0][-1] and len(li)==1:
                return "true"
            
            for i in range(len(li)-1):
                if ord(li[i][-1])==ord(li[i+1][0]):
                    return "true"
                else:
                    return "false"
                
S=Solution()
print(S.isCircularSentence("Leetcode is cool"))

#Input:"Leetcode is cool"
#Output:false