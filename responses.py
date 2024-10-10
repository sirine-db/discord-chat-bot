from random import choice, randint




def get_response(user_input: str) -> str:
    lowered: str= user_input.lower()


    if lowered =='':
        return 'Well, you\'re awfully silent.... SPEAAAACK '
    elif 'hey' in lowered:
        return 'Hello there wssup👋!'
    elif 'hello' in lowered:
        return ("Oh hey! 👋 I was just hanging out here. How’s your day going? "
                "Any exciting plans today?")
    
    elif 'how are you' in lowered:
        return ("Ah, you know, just doing bot things... running code, hanging out in the digital world. "
                "What about you? Feeling good?")
    elif 'hru' in lowered:
        return 'better than u hehe!'
    elif 'bye' in lowered:
        return 'Wait, you \'re leaving already? 😢 Okay, but remember, I\'ll miss you even though I\'m just code :(( Take care!'
    elif 'count' in lowered:
        return '0,1,2,3,4,5,6,7,8,9,10 TADAAAAA!! ' " I could go on forever but I’ll spare you!"
    elif 'bot' in lowered:
        return 'yeah im the best bot!😎'
    elif 'best club' in lowered:
        return 'MC ofcc!'
    elif 'what\'s ur name?' in lowered:
        return 'idk ask my creator(meee)!'
    elif 'how old are u' in lowered:
        return 'count! I was born in oct-10-2024'
    elif 'do you have hobbies?' in lowered:
        return 'yeah talking with u hehe'
    elif 'ok' in lowered:
        return 'okie dokie'
    elif 'do you have any friends' in lowered:
        return 'yesss!! you ig'
    elif '123' in lowered:
        return 'vive l\'Algeriee weeeee'
    elif 'give me an advice' in lowered:
        return 'give up on your dreams and die!'
    elif 'another one' in lowered:
        return'TATAKEEEE'
    elif 'tell me more about yourself' in lowered:
        return 'sorry but nah! u\'are a stranger for me :))' 
    else:
        return choice (['Haaa!',
             'Are you chinese?',
             'nothing important',
             'what are u talking about'])
    
