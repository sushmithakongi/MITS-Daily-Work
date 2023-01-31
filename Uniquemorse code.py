"""Unique Morse Code Words
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:
'a' maps to ".-",
'b' maps to "-...",
'c' maps to "-.-.", and so on.
For convenience, the full table for the 26 letters of the English alphabet is given below:
[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.
For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-", and "-...". We will call such a concatenation the transformation of a word.
Return the number of different transformations among all words we have.
Example 1:
Input: words = ["gin","zen","gig","msg"]
Output: 2
Explanation: The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."
There are 2 different transformations: "--...-." and "--...--.".
Example 2:
Input: words = ["a"]
Output: 1"""
def uniqueMorseRepresentations(words):
    Morse_tab = [".-","-...","-.-.",
             "-..",".","..-.","--.","....",
             "..",".---","-.-",".-..","--",
             "-.","---",".--.","--.-",".-.",
             "...","-","..-","...-",".--",
             "-..-","-.--","--.."]
    if len(words) == 0:
        return 0
    ans_set = set()
    for word in words:
        morsed = ""
        for c in word:
            morsed += Morse_tab[ord(c) - ord('a')]
        ans_set.add(morsed)
    return len(ans_set)
words=["gin","zen","gig","msg"]
a=uniqueMorseRepresentations(words)
print(a)