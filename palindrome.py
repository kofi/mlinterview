import sys
def search_from_indices(s, i, j):
    left = i
    right = j
    while (left >=0 and right <= len(s)-1 and s[left].lower()==s[right].lower()):
        left = left -1 
        right = right + 1

    return s[left+1:right]

def question2(s):
    if len(s) == 0 or s is None:
        return ''
    palindrome = s[0:1]
    #print(palindrome)
    for i in range(len(s)-1):
        #print(i)
        curr_pal = search_from_indices(s,i,i)
        #print(curr_pal)
        if len(curr_pal) > len(palindrome):
            palindrome = curr_pal 
            #print(palindrome)
        curr_pal = search_from_indices(s,i,i+1)
        #print(curr_pal)
        if len(curr_pal) > len(palindrome):
            palindrome = curr_pal 
            #print(palindrome)

    return palindrome

##order(N^2)


def main():

    s = 'abracadabra'
    print('Question 2, Test 1')
    print(question2(s))
    # output : aca

    s = 'abrACaDaBRa'
    print('Question 2, Test 2')
    print(question2(s))
    # output: ACa 
    
    s = ''
    print('Question 2, Test 3')
    print(question2(s))
    # output : ''
    
    s='FourscoreandsevenyearsagoourfaathersbroughtforthonthiscontainentanewnationconceivedinzLibertyanddedicatedtothepropositionthatallmenarecreatedequalNowweareengagedinagreahtcivilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth'
    
    print('Question 2, Test 4')
    print(question2(s))
    # #output : ranynar


if __name__ == '__main__':
    main()






    


    