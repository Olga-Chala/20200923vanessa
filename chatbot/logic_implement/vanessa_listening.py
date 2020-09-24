import speech_recognition as sr
import numpy as np
import pandas as pd
import webbrowser as wb

from .vanessa_talking import say

rep_slow = 'Можешь, пожалуйста повторить?'


def listening_name(lang_val):
    '''
    possible values of langusages are:
        English - "en-GB" 
        Russian - "ru-RU"
        Ukrainian - "uk-UA"

        see more:https://stackoverflow.com/questions/14257598/what-are-language-codes-in-chromes-implementation-of-the-html5-speech-recogniti
    '''
    
    r2 = sr.Recognizer()
    count=0
    with sr.Microphone() as source:
        r2.dynamic_energy_threshold = True
        r2.adjust_for_ambient_noise(source, duration = 1)
    
        while count<4:
            count+=1
            if count == 1:
                say('Как мне к тебе обращаться?')   
            else:
                say(rep_slow)
                say('Как мне к тебе обращаться?')

                           
                # print('Как мне к тебе обращаться?')
                
            audio = r2.listen(source, phrase_time_limit = 2)
            try:
                name = r2.recognize_google(audio, language = lang_val)
                say('Здравствуй' + str(name))
                return name

            except sr.UnknownValueError:
                continue           
            except sr.RequestError as e:
                continue
            except sr.WaitTimeoutError:
                continue      
       


def listening_key(key_word, timeout_val, lang_val):
    '''
    
    '''    
    r2 = sr.Recognizer()
    with sr.Microphone() as source:
        r2.energy_threshold = 100
        r2.adjust_for_ambient_noise(source, duration = 1)
        count =1
        while count<=3:
            count+=1
            if count > 1:
                say(rep_slow)
            audio = r2.listen(source, phrase_time_limit = timeout_val)
            try:
                phrase = r2.recognize_google(audio, language = lang_val)
                return find_key(key_word, phrase)

            except sr.UnknownValueError:
                continue
            except sr.RequestError as e:
                print('failed'.format(e))
            except sr.WaitTimeoutError:
                continue



def find_key(keyword, phrase): 
    '''
    find if the key word appears in the phrase, which was told by user
    each word compares with the key and if it passes fixed threshod, the key in phrase
    keyword - our key
    phrase - where to search the key
    
    '''
    lili = pd.Series(levenshtein_ratio_and_distance(w, keyword.lower(), True) for w in phrase.lower().split())
#     print(lili)
    
    if lili.max() >= 0.8:
        return True
    else: return False

# find_key(var, sentence)


def levenshtein_ratio_and_distance(s, t, ratio_calc = True):
    """ levenshtein_ratio_and_distance:
        Calculates levenshtein distance between two strings.
        If ratio_calc = True, the function computes the
        levenshtein distance ratio of similarity between two strings
        For all i and j, distance[i,j] will contain the Levenshtein
        distance between the first i characters of s and the
        first j characters of t
    """
    # Initialize matrix of zeros
    rows = len(s)+1
    cols = len(t)+1
    distance = np.zeros((rows,cols),dtype = int)

    # Populate matrix of zeros with the indeces of each character of both strings
    for i in range(1, rows):
        for k in range(1,cols):
            distance[i][0] = i
            distance[0][k] = k

    # Iterate over the matrix to compute the cost of deletions,insertions and/or substitutions    
    for col in range(1, cols):
        for row in range(1, rows):
            if s[row-1] == t[col-1]:
                cost = 0 # If the characters are the same in the two strings in a given position [i,j] then the cost is 0
            else:
                # In order to align the results with those of the Python Levenshtein package, if we choose to calculate the ratio
                # the cost of a substitution is 2. If we calculate just distance, then the cost of a substitution is 1.
                if ratio_calc == True:
                    cost = 2
                else:
                    cost = 1
            distance[row][col] = min(distance[row-1][col] + 1,      # Cost of deletions
                                 distance[row][col-1] + 1,          # Cost of insertions
                                 distance[row-1][col-1] + cost)     # Cost of substitutions
    if ratio_calc == True:
        # Computation of the Levenshtein Distance Ratio
        Ratio = ((len(s)+len(t)) - distance[row][col]) / (len(s)+len(t))
        return Ratio
    else:
        # print(distance) # Uncomment if you want to see the matrix showing how the algorithm computes the cost of deletions,
        # insertions and/or substitutions
        # This is the minimum number of edits needed to convert string a to string b
        return "The strings are {} edits away".format(distance[row][col])


def search_google(search_val):
#     search_val = 'python'
    url = "https://www.google.com.tr/search?q={}".format(search_val)
    wb.open(url)        