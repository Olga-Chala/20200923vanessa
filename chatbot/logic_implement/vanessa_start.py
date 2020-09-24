from .vanessa_talking import say
from .vanessa_listening import listening_key, listening_name,search_google


def start():
#     lang = locale.getdefaultlocale()[0]

    phr_purp = 'Что привело тебя к нам?'
    phr_offer = 'О, мне есть что вам предложить. Я предлагаю вам денежный расклад или финансовый расклад. Какой расклад вы хотите выбрать?'
    phr_propose = 'К сожалению, у нас пока нет разворотов по этой теме. Могу я предложить вам спреды по финансам?'
    phr_no_offer = 'Извините, мне пока нечего вам предложить. До свидания!'



    lang = 'ru'
    listening_name(lang)
    say(phr_purp)
    
    if listening_key('финансы', 6, lang):
        say(phr_offer)
        if listening_key('финансовый', 4, lang):
            search_google('финансовый')
        elif listening_key('денежный', 4, lang):
            search_google('денежный')
    else:        
        say(phr_propose)
        if listening_key('да', 4, lang):
            search_google('финансовый')
        else:
            say(phr_no_offer)