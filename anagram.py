def is_anagram(s1, t_dict):
    '''
        a string is an anagram of another if they contain the same letters
        quick way to check is to sort the two strings and compare them
        this function uses pythons in-built quick sort
        and returns True if the two strings are anagrams
    '''
    if len(s1) != len(t_dict):
        return False
    for i in s1:
        if i not in t_dict:
            return False
        else:
            t_dict[i] = t_dict[i] - 1
    
    if sum(t_dict.values()) == 0:
        return True
    return False

def question1(s,t):
    if s is None or t is None:
            return False
    if len(t) > len(s):
        return False
    if len(s) == 0 or len(t)==0:
        return False

    # loop over the input string and take slices of lenght = length(substring)
    # check if the two substrings match
    #sorted_t = sorted(s2.lower())
    t_dict = {}
    for j in t:
        if j not in t_dict:
            t_dict[j] = 1
        else :
            t_dict[j] = t_dict[j] + 1

    for i in range(len(s)-len(t)+ 1):
        segment = s[i:i+len(t)]
        if is_anagram(segment,t_dict):
            return True


##order((n-m-1)*mlog(m)
print("Question 1, Test 1")
print(question1("udacity", "ad"))
# output : True

print("Question 1, Test 2")
print question1("", "de")
#output : False

print("Question 1, Test 3")
print question1("udacity", "")
#output : False
    
    