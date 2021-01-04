nato = ['alfa', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india', 'juliett', 'kilo', 'lima', 'mike', 'november', 'oscar', 'papa', 'quebec', 'romeo', 'sierra', 'tango', 'uniform', 'victor', 'whiskey', 'x-ray', 'yankee', 'zulu']
telefoon = ['anton', 'bernard', 'cornelis', 'dirk', 'eduard', 'ferninand', 'gerard', 'hendrik', 'izak', 'johan', 'karel', 'lodewijk', 'marie', 'nico', 'otto', 'pieter', 'quotiënt', 'rudolf', 'simon', 'theodoor', 'utrecht', 'victor', 'willem', 'xantippe', 'ypsilon', 'zacharias']
numbers = ['0','1','2','3','4','5','6','7','8','9','$','&','+',',','/',':',';','=','?','@']

def anal_sentence(dictionary, sentence):
    answer = []
    for letter in sentence:
        if letter == ' ':
            answer.append('[space]')
        elif letter in numbers:
            answer.append(letter)
        else:
            for word in dictionary:
                if letter == word[0]:
                    answer.append(word)
    return answer

def contstruct_sentence(answer):
    stylized_sentence = ''
    for word in answer:
        stylized_sentence += (word.capitalize() + ' ')
    return stylized_sentence