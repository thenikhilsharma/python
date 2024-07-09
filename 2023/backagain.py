for _ in range(int(input('enter your test cases number: '))):
    word_dictionary = [['ummm, okay', 'hiding something','over_rude'],
                        ['haan haan thik h', 'teasing + cute', 'rude'],
                        ['hollow', 'enthusiam', 'cute_1'],
                        ['''hello babe,
                        u r the sweetest girl
                        i have ever met in my life,
                        i cant imagine myself without you''', 'super_lovely', 'love']]
    greet_list = [['hello', 'normal'],
                    ['hulu', 'cute_1'],
                    ['hillu', 'cute_2'],
                    ['helloi', 'cute_3'],
                    ['hi', 'normal'],
                    ['hn', 'rude'],
                    ['kya kaam hai', 'over_rude'],
                    ['hello babe', 'love']]
    wanna_learn = bool(input('wanna make this bot learn'))
    if wanna_learn == True:
        for x in range(_):
            word = input('Enter a word to learn: ')
            meaning = input('Enter its meaning: ')
            feeling_associated = input('Enter the Feeling associated with that word: ')
            word_dictionary.append([word, meaning, feeling_associated])
    #for iteration in word_dictionary:
    #    print(iteration)
    greet = input('Hello, Nick \n')
    reply = ''
    for greet_check in range(len(greet_list)):
        if greet == greet_list[greet_check][0]:
            x = greet_list[greet_check][1]
            for i in range(len(word_dictionary)):
                if x == word_dictionary[i][2]:
                    reply = word_dictionary[i][0]
    print(reply)