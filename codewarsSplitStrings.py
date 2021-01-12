def solution(s):
    if s == "":
        return []
    
    substrings = []
    
    i = 0
    
    while i <= (len(s)-1):
        substrings.append(s[i:i+2])
        i += 2
    last_substring = substrings[-1]
    if len(last_substring) %2 != 0:
        substrings.pop()
        substrings.append(s[-1]+'_')
        
    return substrings