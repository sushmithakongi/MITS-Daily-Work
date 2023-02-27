'''
A sentence is a string of single-space separated words where each word consists only of lowercase letters.
A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.
 '''

class Solution:
    def uncommonFromSentences(self,s1,s2):
        d={}
        a=[]
        str1=s1.split(" ")
        str2=s2.split(" ")
        for ch in str1:
            d[ch]=d.get(ch,0)+1
        for ch in str2:
            d[ch]=d.get(ch,0)+1
        for k,v in d.items():
            if v==1:
                a.append(k)

        return a
    

S=Solution()
print(S.uncommonFromSentences("this apple is sweet","this apple is sour"))
print(S.uncommonFromSentences("apple apple","banana"))
    
'''
    Input1:
    "this apple is sweet"
    "this apple is sour"
    Output1:
    ["sweet" "sour"]
    Input2:
    "apple apple"
    "banana"
    Output:
    ["banana"]
'''