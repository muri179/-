def is_those_words_anagrams():
    word1= input("First word:")
    word2 = input("Second word:")
    dict_word1 = {}
    dict_word2={}
    for i in word1:
        if i in dict_word1:
            dict_word1[i] += 1
        else:
            dict_word1[i] = 1
    for i in word2:
        if i in dict_word2:
            dict_word2[i] += 1
        else:
            dict_word2[i] = 1

    if dict_word1 == dict_word2:
        print("Both words are anagrams")
    else:
        print("The words are not anagrams")
is_those_words_anagrams()
