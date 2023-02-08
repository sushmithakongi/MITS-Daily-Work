
def wordPattern(pattern, s):
    d={}
    s=s.split()
    for i in range(len(pattern)):
        if pattern[i] not in d:
            d[pattern[i]]=s[i]
            if s[i] not in d:
                d[s[i]]=pattern[i]
            else:
                return False
        elif d[pattern[i]]!=s[i]:
            return False
    return True
print(wordPattern("abba","happy bday bday happy"))
