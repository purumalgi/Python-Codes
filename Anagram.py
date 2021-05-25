def anagram(str1, str2):
    word1 = str1.lower()
    word2 = str2.lower()

    if len(str1) == len(str2):
        if sorted(word1) == sorted(word2):
            print(str1 + ' and ' + str2 + ' are anagram')
        else:
            print(str1 + ' and ' + str2 + ' are not anagram')
    else:
        print(str1 + ' and ' + str2 + ' are not anagram')
        
