def longestCommonPrefix(strs):
    minLen=min([len(s) for s in strs])
    for i in range(minLen,-1,-1):
        comm=[s[:i] for s in strs]
        if len(set(comm))==1:
            return comm[0]
        print(minLen)
        return ''
print(longestCommonPrefix(["flower","flow","flight"]))
